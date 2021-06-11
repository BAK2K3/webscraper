"""
Webscraper
===================================================

Webscraper is a python utility designed to visit
all internal links within a given doman, and return a 
list of all links found within each page visited.

See https://github.com/BAK2K3/webscraper/blob/main/README.md
for complete documentation.

Created by Benjamin Kavanagh (BAK2K3) 2021.
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


# starting URL
starting_url = "www.vk.com"


def webpage_to_soup(url):
    """
    Convert a URL to a Soup Object

    Attributes
    ----------
    url : str
        The url to convert into a Soup object
    """
    webpage = requests.get(url)
    soup_object = BeautifulSoup(webpage.content, features='html.parser')
    return soup_object


def scrape_url(url, domain=None, visited_webpages={*()}, iteration=0):
    """
    - Identifies/Prints all <A> tag Hrefs on a given page
    - Finds all internal domain <A> tag Hrefs
    - Check if domain Href has been visited previously
    - If not, add it to set, and recursively call with current href

    Attributes
    ----------
    url : str
        The URL to be scraped
    domain: str
        The domain of the URL (Default=None)
    visitied_webpages: set
        Set of unique web addresses visited (Default = Empty Set)
    iteration: int 
        Function's current iteration (Default = 0)
    """

    # Check that a valid iteration has been provided
    if not isinstance(iteration, int):
        raise ValueError("Instance variable must be an integer.")

    # If first iteration of loop initialise domain
    if iteration == 0:

        # Prepares URL provided if required
        if "http" not in url:
            url = "https://" + url
        # Check that a valid URL has been provided
        if not urlparse(url).netloc:
            raise ValueError("Invalid URL provided.")
        # Check that visited_webpages is a set
        if not isinstance(visited_webpages, set):
            raise TypeError("visited_webpages must be a set")

        # Re-define specified url for page specific definition
        domain = requests.get(url).request.url
        print(f"Starting URL: {domain}")

    # Create a new soup object from the current url
    new_webpage = webpage_to_soup(url)

    # Obtain all <a> links on page
    all_links = new_webpage.findAll("a", href=True)

    # Print all links on current page
    print("All links on current page:-")
    for link in all_links:
        print(f"\t{link['href']}")

    # For each link in page
    for link in all_links:

        # Obtain the Href for the A tag
        raw_link = link['href']

        # Check there is content to the link
        if raw_link != "#":

            # Check to see whether there is no domain
            if "http" not in raw_link:
                raw_link = domain[:-1] + raw_link

            #  Check to see whether it is a parameter based URL
            if "?" in raw_link:
                raw_link = raw_link.split('?')[0]

            # If the domain is within the link
            if domain in raw_link:

                # Check to see whether the page has already been visited
                if raw_link not in visited_webpages:

                    # Increment iteration
                    iteration += 1
                    # Append website to set
                    visited_webpages.add(raw_link)
                    print(f"Visiting Unique URL: {raw_link}")
                    # Recursive function call
                    scrape_url(raw_link, domain, visited_webpages, iteration)

    # Return set of unique internal domain refs
    return visited_webpages


if __name__ == "__main__":
    visited_webpages = scrape_url(starting_url)
    print(f"Unique Domain Level URLs: {visited_webpages}")
    exit(1)
