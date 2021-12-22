# webscraper

## A python tool for Webscraping

Webscaper is a python tool for scraping websites. It recursively visits all domain level links, and prints each link visible on every domain level page.

The tool can be run via CLI or can be imported as a module.

## Installation

Please see requirements.txt for all packages used for this tool.

`pip install -r requirements.txt`

## Usage

### CLI

To run this tool via CLI, use either of the following:

`python webscraper.py --url <url>`

For example:

`python webscraper.py --url "https://www.vk.com"`

You can also run the package directly without the additional flag:

`python webscraper.py`

You will then be prompted to enter a valid URL to scrape.

**Note**: All URLS provided must contain the full protocol i.e `https://`.

### Package Import

To run this tool as a module, import the following:

`from webscraper import scrape_url`

Within your code, you can call the function as follows:

`returned_set = scrape_url("https://<website>")`

The function will return a set of all unique domain level links within the website.

### Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


This is a test comment. 