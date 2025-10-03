# Chapter 13 - Web Scraping
# (Practice Program) - Image Site Downloader
# Had a tough time finding an image site to scrape due to scrape blockers so I scraped a practice website


import os
import requests
from bs4 import BeautifulSoup


def main():
    # Base URL of the Health category
    base_url = "https://books.toscrape.com/catalogue/category/books/health_47/index.html"

    # Create a directory to save the images
    os.makedirs("book_images", exist_ok=True)

    # Construct the URL for the current page

    # Send a GET request to fetch the raw HTML content
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all image tags within the page
    images = soup.find_all("img")
    # Loop through each image tag
    for img in images[:50]:
        # Extract the 'src' attribute (image source URL)
        img_url = img.get("src")
        if img_url:
            print(img_url)
            # Construct the full image URL
            img_url = "https://books.toscrape.com/" + img_url.strip("../../")

            # Extract the image name from the URL
            img_name = os.path.basename(img_url)

            # Define the path to save the image
            img_path = os.path.join("book_images", img_name)

            # Download and save the image
            with open(img_path, "wb") as f:
                img_data = requests.get(img_url).content
                f.write(img_data)
                print(f"Downloaded {img_name}")

    print("All images have been downloaded.")


if __name__ == "__main__":
    main()