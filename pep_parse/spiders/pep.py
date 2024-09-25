from re import search

import scrapy

from ..items import PepParseItem

class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        for row in response.xpath(
            '//*[@id="numerical-index"]/table/tbody/tr'
        ):
            yield response.follow(
                row.xpath(
                    './td/a[@class="pep reference internal"]/@href'
                ).get(),
                callback=self.parse_pep,
            )

    def parse_pep(self, response):
        number_and_name_pep = search(
            r'(?P<number>\d{1,4})\W+(?P<name>.+)',
            response.xpath('//h1[@class="page-title"]/text()').get(),
        )
        yield PepParseItem({
            'number': number_and_name_pep.group('number'),
            'name': number_and_name_pep.group('name'),
            'status': response.xpath(
                '//dt[contains(.,"Status")]/following-sibling::dd/abbr/text()|'
                '//dd[contains(.,"Status")]/following-sibling::dt/abbr/text()'
            ).get(),
        })
