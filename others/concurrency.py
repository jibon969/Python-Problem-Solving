
import requests
from typing import List

def check_website_status(url:str) -> None:
    response = requests.get(url=url)
    if response.status_code == 200:
        print(f"{url} --> status __ {response.status_code}")

def main(site_urls: List) -> None:
    for url  in site_urls:
        check_website_status(url=url)
    



if __name__ == "__main__":
    website_urls = [
    "https://www.google.com",
    "https://www.facebook.com",
    "https://www.twitter.com",
    "https://www.linkedin.com",
    "https://www.instagram.com",
    "https://www.youtube.com",
    "https://www.reddit.com",
    "https://www.wikipedia.org",
    "https://www.github.com",
    "https://www.stackoverflow.com",
]
    main(site_url=website_urls)