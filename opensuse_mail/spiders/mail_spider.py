import scrapy
from bs4 import BeautifulSoup
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exporters import CsvItemExporter
from opensuse_mail.items import MailItem

datadir= '/opt/scrapyd/datadir/'
year = '2019'

class BugsSpider(CrawlSpider):
    name = 'bugs'
    allowed_domains = ['lists.opensuse.org']
    start_urls = [
        'https://lists.opensuse.org/opensuse-bugs/'+year+'-01/all.html',
        'https://lists.opensuse.org/opensuse-bugs/'+year+'-02/all.html',
        'https://lists.opensuse.org/opensuse-bugs/'+year+'-03/all.html',
        'https://lists.opensuse.org/opensuse-bugs/'+year+'-04/all.html',
        'https://lists.opensuse.org/opensuse-bugs/'+year+'-05/all.html',
        'https://lists.opensuse.org/opensuse-bugs/'+year+'-06/all.html',
        'https://lists.opensuse.org/opensuse-bugs/'+year+'-07/all.html',
        'https://lists.opensuse.org/opensuse-bugs/'+year+'-08/all.html',
        'https://lists.opensuse.org/opensuse-bugs/'+year+'-09/all.html',
        'https://lists.opensuse.org/opensuse-bugs/'+year+'-10/all.html',
        'https://lists.opensuse.org/opensuse-bugs/'+year+'-11/all.html',
        'https://lists.opensuse.org/opensuse-bugs/'+year+'-12/all.html'
    ]
    custom_settings = {
        'FEED_URI': 'file://'+datadir+'opensuse-bugs/opensuse-bugs-'+year+'.json',
        'JOBDIR': datadir+'opensuse-bugs/jobs/'
    }
    rules = (
        #Defining rules for the crawler, if the link match the regex defined in 'allow' section, then the link will be opened and followed
        #Rule(LinkExtractor(allow=('opensuse\-bugs/2018\-\d{2}', ), deny=('msg\d{5}\.html', ), unique=False)),
        #Rule(LinkExtractor(allow=('opensuse\-bugs/2019\-\d{2}', ), deny=('msg\d{5}\.html', ), unique=False), follow=True),
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

class AnnounceSpider(CrawlSpider):
    name = 'announce'
    allowed_domains = ['lists.opensuse.org']
    start_urls = [
        'https://lists.opensuse.org/opensuse-announce/'+year+'-01/all.html',
        'https://lists.opensuse.org/opensuse-announce/'+year+'-02/all.html',
        'https://lists.opensuse.org/opensuse-announce/'+year+'-03/all.html',
        'https://lists.opensuse.org/opensuse-announce/'+year+'-04/all.html',
        'https://lists.opensuse.org/opensuse-announce/'+year+'-05/all.html',
        'https://lists.opensuse.org/opensuse-announce/'+year+'-06/all.html',
        'https://lists.opensuse.org/opensuse-announce/'+year+'-07/all.html',
        'https://lists.opensuse.org/opensuse-announce/'+year+'-08/all.html',
        'https://lists.opensuse.org/opensuse-announce/'+year+'-09/all.html',
        'https://lists.opensuse.org/opensuse-announce/'+year+'-10/all.html',
        'https://lists.opensuse.org/opensuse-announce/'+year+'-11/all.html',
        'https://lists.opensuse.org/opensuse-announce/'+year+'-12/all.html'
    ]    
    custom_settings = {
        'FEED_URI': 'file://'+datadir+'opensuse-announce/opensuse-announce-'+year+'.json',
        'JOBDIR': datadir+'opensuse-announce/jobs/'
    }
    rules = (
        #Defining rules for the crawler, if the link match the regex defined in 'allow' section, then the link will be opened and followed
        #Rule(LinkExtractor(allow=('opensuse\-announce\/2018\-\d{2}', ), deny=('msg\d{5}\.html', ), unique=False)),
        #Rule(LinkExtractor(allow=('opensuse\-announce/2019\-\d{2}', ), deny=('msg\d{5}\.html', ), unique=False)),
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

class UpdatesSpider(CrawlSpider):
    name = 'updates'
    allowed_domains = ['lists.opensuse.org']
    start_urls = [
        'https://lists.opensuse.org/opensuse-updates/'+year+'-01/all.html',
        'https://lists.opensuse.org/opensuse-updates/'+year+'-02/all.html',
        'https://lists.opensuse.org/opensuse-updates/'+year+'-03/all.html',
        'https://lists.opensuse.org/opensuse-updates/'+year+'-04/all.html',
        'https://lists.opensuse.org/opensuse-updates/'+year+'-05/all.html',
        'https://lists.opensuse.org/opensuse-updates/'+year+'-06/all.html',
        'https://lists.opensuse.org/opensuse-updates/'+year+'-07/all.html',
        'https://lists.opensuse.org/opensuse-updates/'+year+'-08/all.html',
        'https://lists.opensuse.org/opensuse-updates/'+year+'-09/all.html',
        'https://lists.opensuse.org/opensuse-updates/'+year+'-10/all.html',
        'https://lists.opensuse.org/opensuse-updates/'+year+'-11/all.html',
        'https://lists.opensuse.org/opensuse-updates/'+year+'-12/all.html'
    ]    
    custom_settings = {
        'FEED_URI': 'file://'+datadir+'opensuse-updates/opensuse-updates-'+year+'.json',
        'JOBDIR': datadir+'opensuse-updates/jobs/'
    }
    rules = (
        #Defining rules for the crawler, if the link match the regex defined in 'allow' section, then the link will be opened and followed
        #Rule(LinkExtractor(allow=('opensuse\-updates/2018\-\d{2}', ), deny=('msg\d{5}\.html', ), unique=False)),
        #Rule(LinkExtractor(allow=('opensuse\-updates/2019\-\d{2}', ), deny=('msg\d{5}\.html', ), unique=False)),
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

class SecuritySpider(CrawlSpider):
    name = 'security'
    allowed_domains = ['lists.opensuse.org']
    start_urls = [
        'https://lists.opensuse.org/opensuse-security-announce/'+year+'-01/all.html',
        'https://lists.opensuse.org/opensuse-security-announce/'+year+'-02/all.html',
        'https://lists.opensuse.org/opensuse-security-announce/'+year+'-03/all.html',
        'https://lists.opensuse.org/opensuse-security-announce/'+year+'-04/all.html',
        'https://lists.opensuse.org/opensuse-security-announce/'+year+'-05/all.html',
        'https://lists.opensuse.org/opensuse-security-announce/'+year+'-06/all.html',
        'https://lists.opensuse.org/opensuse-security-announce/'+year+'-07/all.html',
        'https://lists.opensuse.org/opensuse-security-announce/'+year+'-08/all.html',
        'https://lists.opensuse.org/opensuse-security-announce/'+year+'-09/all.html',
        'https://lists.opensuse.org/opensuse-security-announce/'+year+'-10/all.html',
        'https://lists.opensuse.org/opensuse-security-announce/'+year+'-11/all.html',
        'https://lists.opensuse.org/opensuse-security-announce/'+year+'-12/all.html'
    ]    
    custom_settings = {
        'FEED_URI': 'file://'+datadir+'opensuse-security/opensuse-security-'+year+'.json',
        'JOBDIR': datadir+'opensuse-security/jobs/'
    }
    rules = (
        #Defining rules for the crawler, if the link match the regex defined in 'allow' section, then the link will be opened and followed
        #Rule(LinkExtractor(allow=('opensuse\-security\-announce/2018\-\d{2}', ), deny=('msg\d{5}\.html', ), unique=False)),
        #Rule(LinkExtractor(allow=('opensuse\-security\-announce/2019\-\d{2}', ), deny=('msg\d{5}\.html', ), unique=False)),
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