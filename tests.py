import unittest
from webscraper import scrape_url


class WebscraperTests(unittest.TestCase):
    """
    Unit Testing for Webscraper functions.
    """

    def test_incorrect_url(self):
        """
        Tests handling of incorrect URL format.
        """

        self.assertRaises(ValueError, scrape_url, "this is not a website")

    def test_incorrect_increment(self):
        """
        Tests handling of incorrect increment value.
        """

        self.assertRaises(TypeError, scrape_url, url="https://www.google.com",
                          iteration="hello")

    def test_incorrect_visited_webpages(self):
        """
        Tests handling of incorrect visited_webpages variable.
        """

        self.assertRaises(TypeError, scrape_url, url="https://www.google.com",
                          visited_webpages="This is not a set")

    def test_valid_url(self):
        """
        Tests handling of valid URL.
        """

        self.assertTrue(isinstance(scrape_url("https://www.vk.com")))


if __name__ == '__main__':
    unittest.main()
