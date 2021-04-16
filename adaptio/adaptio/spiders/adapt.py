import scrapy
import string
from lxml import html
from requests_html import HTMLSession
from collections import OrderedDict
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json


class AdaptSpider(scrapy.Spider):
    name = "adapt"
    allowed_domains = ["adapt.io"]

    start_urls = [
        "https://www.adapt.io/directory/industry/telecommunications/%s-1/" % character
        for character in string.ascii_uppercase
    ]

    def parse(self, response):
        print("Response Url!!!!!!!!!!!!!!!!!!!!!! =>>>>>>>>>>>>>%s" % response.url)

    # all_companies = response.xpath(
    #     '//div[@class="DirectoryList_linkItemWrapper__3F2UE"]'
    # ).extract()

    # print(all_companies)

    #     for company in all_companies:
    #         company_name = company.xpath(".//a/text()").extract_first()
    #         source_url = company.xpath(".//a/@href").extract_first()

    #         company_index_data = {
    #             "company_name": company_name,
    #             "source_url": source_url,
    #         }
    #         print("company_index_data=>>>>>>" + "\n" + company_index_data)

    #         # file = open("company_index.json", "w", encoding="utf-8")
    #         # json.dump(company_index_data, file, ensure_ascii=False)

    #         yield scrapy.Request(
    #             url=response.urljoin(source_url), callback=self.parse_company_info
    #         )

    #     next_page_partial_url = response.xpath(
    #         '//div[@class="DirectoryList_actionBtnLink__Seqhh undefined"]/a/@href'
    #     ).extract_first()
    #     if next_page_partial_url:
    #         next_page_url = response.urljoin(next_page_partial_url)

    #         yield scrapy.Request(url=next_page_url, callback=self.parse)

    #     else:
    #         print(
    #             "I am Done!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    #         )

    # def parse_company_info(self, response):

    #     company_name = response.xpath('//h1[@itemprop="name"]/text()').extract_first()
    #     company_location = response.xpath(
    #         '//span[@itemprop="address"]/text()'
    #     ).extract_first()
    #     company_website = response.xpath(
    #         '//div[@itemprop="url"]/text()'
    #     ).extract_first()
    #     company_webdomain = (
    #         response.xpath('//div[@itemprop="url"]/text()')
    #         .replace("http://www.", "")
    #         .extract_first()
    #     )
    #     company_industry = response.xpath(
    #         '/div[@class="CompanyTopInfo_infoItem__2Ufq5"][0]/div[@class="CompanyTopInfo_infoItem__2Ufq5"]/div[@class="CompanyTopInfo_contentWrapper__2Jkic"]/span[@class="CompanyTopInfo_infoValue__27_Yo"]/text()'
    #     ).extract_first()
    #     company_employee_size = response.xpath(
    #         '//div[@class="CompanyTopInfo_infoItem__2Ufq5"][1]/div[@class="CompanyTopInfo_infoItem__2Ufq5"]/div[@class="CompanyTopInfo_contentWrapper__2Jkic"]/span[@class="CompanyTopInfo_infoValue__27_Yo"]/text()'
    #     ).extract_first()

    #     company_revenue = response.xpath(
    #         '//div[@class="CompanyTopInfo_infoItem__2Ufq5"][0]/div[@class="CompanyTopInfo_infoItem__2Ufq5"]/div[@class="CompanyTopInfo_contentWrapper__2Jkic"]/span[@class="CompanyTopInfo_infoValue__27_Yo"]/text()'
    #     ).extract_first()

    #     contact_details = []

    #     contact_detail = {
    #         "contact_name": "",
    #         "contact_jobtitle": "",
    #         "contact_email_domain": "",
    #         "contact_department": "",
    #     }

    #     contacts = response.xpath('//div[@itemprop="employee"]')

    #     for contact in contacts:
    #         contact_name = (contact.xpath("//div/a/text()").extract_first(),)
    #         contact_jobtitle = (
    #             contact.xpath('//p[@itemprop="jobTitle"]/text()').extract_first(),
    #         )
    #         contact_email_domain = (
    #             contact.xpath('//button[@itemprop="email"]/text()').extract_first(),
    #         )

    #     contact_detail = {
    #         "contact_name": contact_name,
    #         "contact_jobtitle": contact_jobtitle,
    #         "contact_email_domain": contact_email_domain,
    #     }

    #     contact_details.append(contact_detail)

    #     company_profiles_data = {
    #         "company_name": company_name,
    #         "company_location": company_location,
    #         "company_website": company_website,
    #         "company_webdomain": company_webdomain,
    #         "company_industry": company_industry,
    #         "company_employee_size": company_employee_size,
    #         "company_revenue": company_revenue,
    #         "contact_details": contact_details,
    #     }

    #     print("company_profiles_data=>>>>>>" + "\n" + company_profiles_data)

    #     # file = open("company_profiles.json", "w", encoding="utf-8")
    #     # json.dump(company_profiles_data, file, ensure_ascii=False)
