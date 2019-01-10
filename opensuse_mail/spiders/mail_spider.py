import scrapy
from bs4 import BeautifulSoup
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from opensuse_mail.items import MailItem

class OpensuseMailCrawler(CrawlSpider):
    name = 'mail_spider'

    def __init__(self, category=None, date=None, *args, **kwargs):
        super(OpensuseMailCrawler, self).__init__(*args, **kwargs)
        self.start_urls = ['https://lists.opensuse.org/'+ category +'/'+ date +'/all.html']

    allowed_domains = ['lists.opensuse.org']
    custom_settings = {
        'JOBDIR': '/opt/scrapyd/jobs/opensuse-mails/'
    }
    rules = (
        #Defining rules for the crawler, if the link match the regex defined in 'allow' section, then the link will be opened and thrown to the callback function
        Rule(LinkExtractor(allow=('msg\d{5}\.html', )), callback='parse_item', follow=False),
    )
    
    def parse_item(self, response):
        # item getter
        item = MailItem()
        # Mail parser
        headraw = response.css('div.header')
        bodyraw = response.css('div.body')
        bodysoup = BeautifulSoup(bodyraw.extract_first())
        item['subject'] = headraw.css('.subject::text').extract_first()
        item['origin'] = headraw.css('li::text')[0].extract().replace(': \n ', '')
        item['date'] = headraw.css('li::text')[1].extract().replace(': \n ', '')
        item['src_link'] = response.url
        item['reference_link'] = bodyraw.css('a::text').extract()
        item['msg_body'] = bodysoup.get_text()
        return item
