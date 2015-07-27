from tumblr.items import Post

import scrapy

class TumblrSpider(scrapy.Spider):
    name = "tumblr"
    start_urls = ['http://soyeahdjango.com/']

    def parse(self, response):
        """Finds links to each individual post"""
        for href in response.xpath("//h2/a/@href"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, self.parse_post_content)

        # Check for a next page
        next_page_links = response.xpath("//a[@class='right']/@href")
        if len(next_page_links) > 0:
            next_url = response.urljoin(next_page_links[0].extract())
            yield scrapy.Request(next_url, self.parse)

    def parse_post_content(self, response):
        """Extracts content from an individual post"""
        post = Post()
        post['title'] = response.xpath('//h2/a/text()')[0].extract()
        post['image_url'] = response.xpath("//div[@class='cont group']//img/@src")[0].extract()
        yield post
