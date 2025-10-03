# Chapter 13 - Web Scraping
# (Practice Program) - Image Site Downloader
# Had a tough time finding an image site to scrape due to scrape blockers so I scraped a practice website


import os
import requests
from socket import gaierror
from bs4 import BeautifulSoup
from urllib3.exceptions import NameResolutionError
import validators


def verify_links(base_url, url):
    # Send a GET request to fetch the raw HTML content
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all <a> tags within the page
    links = soup.find_all("a")
    # Loop through each <a> tag
    for link in links:
        # Extract the 'href' attribute (link)
        href = link.get("href")
        if href:
            if not (str(href).startswith("http://") or str(href).startswith("https://")):
                href = base_url + href

            try:
                if validators.url(href):
                    print("Fetching " + href + " ...... ", end='')
                    response = requests.get(url=href)
                    if response.status_code != 200:
                        print(" failed, status_code:" + str(response.status_code))
                    else:
                        print(" ok")
                else:
                    print("Invalid url: " + href)

            except:
                print("Invalid url raised exception: " + href)


def main():
    base_url = "https://blog.miguelgrinberg.com"
    url = "https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xvii-deployment-on-linux"
    verify_links(base_url=base_url, url=url)


if __name__ == "__main__":
    main()