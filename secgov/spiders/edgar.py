# -*- coding: utf-8 -*-
import scrapy


class EdgarSpider(scrapy.Spider):
    name = 'edgar'
    allowed_domains = ['www.sec.gov/Archives/edgar/data/1750/000104746918004978/0001047469-18-004978.txt']
    start_urls = ['http://www.sec.gov/Archives/edgar/data/1750/000104746918004978/0001047469-18-004978.txt']

    def parse(self, response):
        text = response.xpath("string(.)")
        accession_number = text.re_first(r"ACCESSION NUMBER:\t+([\d-]+)")
        conformed_submission_type = text.re_first(r"CONFORMED SUBMISSION TYPE:\t+([\w-]+)")
        public_document_count = text.re_first(r"PUBLIC DOCUMENT COUNT:\t+(\d+)")
        conformed_document_of_report = text.re_first(r"CONFORMED PERIOD OF REPORT:\t+(\d+)")
        filed_as_date = text.re_first(r"FILED AS OF DATE:\t+(\d+)")
        date_of_change = text.re_first(r"DATE AS OF CHANGE:\t+(\d+)")
        street_1 = text.re_first(r"BUSINESS ADDRESS:\s+STREET 1:\t+([\w -_]+)")
        city = text.re_first(r"BUSINESS ADDRESS:[\s\w :]+CITY:\t+([\w -_]+)")
        state = text.re_first(r"BUSINESS ADDRESS:[\s\w :]+STATE:\t+([\w -_]+)")
        zip_code = text.re_first(r"BUSINESS ADDRESS:[\s\w :]+ZIP:\t+([\w -_]+)")
        phone = text.re_first(r"BUSINESS ADDRESS:[\s\w :]+BUSINESS PHONE:\t+([\w -_]+)")


        return {
            'accession_number': accession_number,
            'conformed_submission_type': conformed_submission_type,
            'public_document_count': public_document_count,
            'conformed_document_of_report': conformed_document_of_report,
            'filed_as_date': filed_as_date,
            'date_of_change': date_of_change,
            'street_1': street_1,
            'city': city,
            'state': state,
            'zip_code': zip_code,
            'phone': phone
        }


