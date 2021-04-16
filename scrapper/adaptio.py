# -*- coding: utf-8 -*-
import string

from lxml import html
from requests_html import HTMLSession
from collections import OrderedDict
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json


def get_page(url):
    session = HTMLSession()
    resp = session.get(url)
    soup = BeautifulSoup(resp.text, "lxml")
    return soup


def parse_company_index(url):

    print("Scraping compnay index page url: %s" % url)
    company_index_list = []

    page = get_page(url)

    all_companies = page.find_all(
        "div", attrs={"class": "DirectoryList_linkItemWrapper__3F2UE"}
    )

    for company in all_companies:
        company_name = company.find("a").getText()
        source_url = company.find("a").get("href")

        company_index_data = {
            "company_name": company_name,
            "source_url": source_url,
        }

        print(company_index_data)

        company_index_list.append(company_index_data)

    return company_index_list


def parse_company_profiles(valid_source_url):

    page = get_page(valid_source_url)

    company_name = page.find("h1", attrs={"itemprop": "name"})
    if company_name is not None:
        company_name = company_name.getText()  # .replace('\n', '')
    else:
        company_name = ""

    company_location = page.find("span", attrs={"itemprop": "address"})
    if company_location is not None:
        company_location = company_location.getText()  # .replace('\n', '')
    else:
        company_location = ""

    company_website = page.find(
        "div", attrs={"class": "CompanyTopInfo_websiteUrl__13kpn"}
    )
    if company_website is not None:
        company_website = company_website.getText()  # .replace('\n', '')
    else:
        company_website = ""

    company_webdomain = page.find(
        "div", attrs={"class": "CompanyTopInfo_websiteUrl__13kpn"}
    )
    if company_webdomain is not None:
        company_webdomain = company_webdomain.getText().replace(
            "http://www.", ""
        )  # .replace('\n', '')
    else:
        company_webdomain = ""

    company_industry = (
        page.find_all("div", attrs={"class": "CompanyTopInfo_infoItem__2Ufq5"})[2]
        .find("div", attrs={"class": "CompanyTopInfo_contentWrapper__2Jkic"})
        .find("span", attrs={"class": "CompanyTopInfo_infoValue__27_Yo"})
    )
    if company_industry is not None:
        company_industry = company_industry.getText()  # .replace('\n', '')
    else:
        company_industry = ""

    company_employee_size = (
        page.find_all("div", attrs={"class": "CompanyTopInfo_infoItem__2Ufq5"})[1]
        .find("div", attrs={"class": "CompanyTopInfo_contentWrapper__2Jkic"})
        .find("span", attrs={"class": "CompanyTopInfo_infoValue__27_Yo"})
    )
    if company_employee_size is not None:
        company_employee_size = company_employee_size.getText()  # .replace('\n', '')
    else:
        company_employee_size = ""

    company_revenue = (
        page.find_all("div", attrs={"class": "CompanyTopInfo_infoItem__2Ufq5"})[0]
        .find("div", attrs={"class": "CompanyTopInfo_contentWrapper__2Jkic"})
        .find("span", attrs={"class": "CompanyTopInfo_infoValue__27_Yo"})
    )
    if company_revenue is not None:
        company_revenue = company_revenue.getText()  # .replace('\n', '')
    else:
        company_revenue = ""

    contact_details = []

    contact_detail = {
        "contact_name": "",
        "contact_jobtitle": "",
        "contact_email_domain": "",
        "contact_department": "",
    }

    contacts = page.find_all("div", attrs={"itemprop": "employee"})

    for contact in contacts:

        contact_name = contact.find("div").find("a")
        if contact_name is not None:
            contact_name = contact_name.getText()  # .replace('\n', '')
        else:
            contact_name = ""

        contact_jobtitle = contact.find("p", attrs={"itemprop": "jobTitle"})
        if contact_jobtitle is not None:
            contact_jobtitle = contact_jobtitle.getText()  # .replace('\n', '')
        else:
            contact_jobtitle = ""

        contact_email_domain = contact.find("button", attrs={"itemprop": "email"})
        if contact_email_domain is not None:
            contact_email_domain = contact_email_domain.getText()  # .replace('\n', '')
        else:
            contact_email_domain = ""

        contact_detail = {
            "contact_name": contact_name,
            "contact_jobtitle": contact_jobtitle,
            "contact_email_domain": contact_email_domain,
        }

        contact_details.append(contact_detail)

    company_profiles_data = {
        "company_name": company_name,
        "company_location": company_location,
        "company_website": company_website,
        "company_webdomain": company_webdomain,
        "company_industry": company_industry,
        "company_employee_size": company_employee_size,
        "company_revenue": company_revenue,
        "contact_details": contact_details,
    }

    return company_profiles_data


if __name__ == "__main__":

    page_url_list = []
    for character in string.ascii_uppercase:
        for i in range(1, 10):
            page_url_list.append(
                "https://www.adapt.io/directory/industry/telecommunications/%s-%s/"
                % (character, str(i))
            )

    company_index = []
    for url in page_url_list:
        page = get_page(url)
        data = page.find_all(
            "div", attrs={"class": "DirectoryList_linkItemWrapper__3F2UE"}
        )
        if data == []:
            print("Url: %s has no content. So, skipped!!!!!" % url)
            continue
        else:
            company_index.extend(parse_company_index(url))

    print("Dumping company indexed to JSON>>>>>>")

    file = open("company_index.json", "w", encoding="utf-8")
    json.dump(company_index, file, ensure_ascii=False)

    print(
        "Company index written successfully !!!!!! Check out the company_index.json in the same directory where adaptio.py file exist"
    )

    company_profiles = []

    for x in company_index:
        page = get_page(x["source_url"])
        data = page.find("h1", attrs={"itemprop": "name"})
        if data == "":
            print("Source Url: %s has no content. So, skipped!!!!!" % source_url)
            continue
        else:
            company_profiles.append(parse_company_profiles(x["source_url"]))

    print("Dumping company profiles to JSON>>>>>>")

    file = open("company_profiles.json", "w", encoding="utf-8")
    json.dump(company_profiles, file, ensure_ascii=False)

    print(
        "Company profiles written successfully !!!!!! Check out the company_profiles.json in the same directory where adaptio.py file exist"
    )
