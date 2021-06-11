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


# starting URL
starting_url = "https://www.vk.com/"


def webpage_to_soup(url):
    """
    Convert a URL to a Soup Object
    """
    webpage = requests.get(url)
    soup_object = BeautifulSoup(webpage.content, features='html.parser')
    return soup_object


def scrape_url(url, domain=None, visited_webpages={*()}, iteration=0):
    """
    - Identify all A tags on page
    - Print all tags
    - Find all domain tags
    - Check if next domain tag is in set
    - If not, add it, and call self with new tag    
    """

    print(iteration)

    # If first iteration of loop, initialise set and domain
    if iteration == 0:
        # Re-define specified url for page specific definition
        domain = requests.get(url).request.url

    # Create a new soup object from the current url
    new_webpage = webpage_to_soup(url)

    # Obtain all "a" links on page
    all_links = new_webpage.findAll("a", href=True)

    print(f"Current Page: {url}")
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

                    # Call function again
                    scrape_url(raw_link, domain, visited_webpages, iteration)

                # else:
                    # Confirm URL already visited
                    # DEBUG
                    # print("URL already visited!")

    return visited_webpages


if __name__ == "__main__":
    visited_webpages = scrape_url(starting_url)
    print(f"Unique Domain Level URLs: {visited_webpages}")
    exit(1)
