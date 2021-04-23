from requests_html import HTMLSession
from bs4 import BeautifulSoup
from lxml import html
from requests_html import HTMLSession
import json
import re

import unittest


class AdaptioTest(unittest.TestCase):
    page = None

    def get_comany_index_Class():
        url = "https://www.adapt.io/directory/industry/telecommunications/A-1/"
        r = session.get(url)

    def get_comany_profiles_Class():
        url = "https://www.adapt.io/directory/industry/telecommunications/A-1/"
        r = session.get(url)

    def test_companyNameText(self):
        company = AdaptioTest.bs.find("h1").get_text()
        self.assertEqual("Python", pageTitle)

    def test_contentExists(self):
        content = AdaptioTest.bs.find("div", {"id": "mw-content-text"})
        self.assertIsNotNone(content)


if __name__ == "__main__":
    unittest.main()
