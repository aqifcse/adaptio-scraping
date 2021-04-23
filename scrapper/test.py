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
        session = HTMLSession()
        url = "https://www.adapt.io/directory/industry/telecommunications/A-1/"
        r = session.get(url)

        bs = BeautifulSoup(r.text, "lxml")

        return bs

    bs = get_comany_index_Class()

    def get_comany_profiles_Class():
        session = HTMLSession()
        url = "https://www.adapt.io/company/a-a-technology-group"
        r = session.get(url)

    def test_companyNameText(self):
        company = AdaptioTest.bs.find("h1").get_text()
        self.assertEqual("Industry Directory - Telecommunications - A - 1", company)


if __name__ == "__main__":
    unittest.main()
