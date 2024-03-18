import scrapy
from ..items import ScholarshipItem

class ScholarshipsSpider(scrapy.Spider):
    name = "scholarships"
    url = 'https://www.scholars4dev.com/tag/scholarships-for-pakistans/' 



    def start_requests(self):
        surl=self.url
            
        yield scrapy.Request(url=surl, callback=self.parse)

    def parse(self, response):
        items=ScholarshipItem()

        scholarships=response.css("div.entry")

        for scholarship in scholarships:

            wholP=scholarship.css("p::text").extract()
            degree = wholP[0].strip()
            deadline = wholP[2].strip()
            country = wholP[3].strip()
            start_date = wholP[4].split('Course starts ')[1].strip()


           
            #items["stitle"]=scholarship.css("a::text").get(default='not-found').strip()
            #items["suni"]=scholarship.css("em::text").get(default='not-found').strip()
            #items["sdeadline"]=deadline
            #items["scountry"]=country
            #items["sdegree"]=degree
            #items["scoursestart"]=start_date
            #items["surl"]=scholarship.css("a::attr(href)").get(default='not-found').strip()

            yield items

           

