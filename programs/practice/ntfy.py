# Chapter 20 - Sending Emails, Texts and Push notifications
# (Practice Program) - Ntfy based computer control

import os
import sys
import subprocess
import requests
import json
import argparse
import time
from dotenv import load_dotenv


class ArgumentParserWithHelp(argparse.ArgumentParser):
    def error(self, message):
        """Override default error handling to show help text on invalid args."""
        self.print_help(sys.stderr)
        self.exit(2, f"\nError: {message}\n\n")


def send_ntfy(message: str, title="Torrent Download Request", tags="arrow_down,download"):
    """
    Send a notification to your ntfy server.
    """
    print(f"Sending notification: {message}")

    resp = requests.post(
        url=torr_url,
        data=message.encode("utf-8"),
        headers={
            "Title": title,
            "Tags": tags
        }    
    )
    print(resp.status_code, resp.reason)


def download_torrent(link: str):
    """
    Download a torrent file via qbittorrent or aria2c as a background process.
    Send ntfy notification on success/failure.
    """
    try:
        print(f"Received new torrent link: {link}")
        start = time.time()
        # Launch the downloader (aria2c recommended in WSL2)
        process = subprocess.Popen(
            ["aria2c", "--seed-time=0", "-d", download_dir, link],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        stdout, stderr = process.communicate()  # Wait for completion

        end = time.time()

        if process.returncode == 0:
            msg = f"Download completed in {end - start}.3f seconds"
            send_ntfy(message=msg, title="Torrent Download Complete", tags="white_check_mark")
            print("Download succeeded")
        else:
            msg = f"code {process.returncode}):\n{link}\nError: {stderr.decode()}"
            send_ntfy(message=msg, title="Torrent Download Failed", tags="x")
            print("Download failed")

    except Exception as e:
        msg = f"Exception: {e}"
        send_ntfy(message=msg, title="Python Exception", tags="lady_beetle")
        print(f"Exception occurred: {e}")


def listen():
    """Poll ntfy every 30s for new messages."""
    poll_url = f"{torr_url}/json?poll=1&since=30s"

    while True:
        print(f"Polling {poll_url}")
        try:
            resp = requests.get(poll_url)
            if resp.status_code == 200 and resp.text.strip():
                line = resp.text.splitlines()[-1]
                notification = json.loads(line)
                title = notification.get("title", 0)
                if title == "Torrent Download Request":
                    download_torrent(notification.get("message"))
            else:
                print(f"No new notifications. (Status {resp.status_code})")
        except Exception as e:
            print(f"Error while polling: {e}")

        time.sleep(30)  # wait before next poll



def main():
    load_dotenv()

    global download_dir, auth, torr_url
    download_dir = os.path.expanduser("~/torr_downloads/")
    torr_url = os.getenv('TORR_URL')

    parser = ArgumentParserWithHelp(description="Torrent sender/listener utility")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # --- send subcommand ---
    send_parser = subparsers.add_parser("send", help="Send a torrent link to the server")
    send_parser.add_argument("link", type=str, help="Torrent or magnet link to send")

    # --- listen subcommand ---
    subparsers.add_parser("listen", help="Run server that listens for torrent links")

    args = parser.parse_args()

    # --- handle subcommands ---
    if args.command == "send":
        send_ntfy(message=args.link)
    elif args.command == "listen":
        listen()


if __name__ == "__main__":
    main()