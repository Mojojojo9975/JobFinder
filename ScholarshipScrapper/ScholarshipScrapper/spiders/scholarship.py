import scrapy
from ..items import ScholarshipItem


class ScholarshipSpider(scrapy.Spider):
    name = "scholarship"
    pgnum = 1


    def start_requests(self):
        url = f'https://www.scholars4dev.com/tag/scholarships-for-pakistans/page/{self.pgnum}/'
            
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        items=ScholarshipItem()

        scholarships=response.css("div.entry")

        for scholarship in scholarships:

            wholP=scholarship.css("p::text").extract()
            degree = wholP[0].strip()
            deadline = wholP[2].strip()
            country = wholP[3].strip()

            if len(wholP) >= 5:
                start_date = wholP[4].strip()
            else:
                start_date = "-"
            


           
            items["stitle"]=scholarship.css("a::text").get(default='not-found').strip()
            items["suni"]=scholarship.css("em::text").get(default='not-found').strip()
            items["sdeadline"]=deadline
            items["scountry"]=country
            items["sdegree"]=degree

            
            items["scoursestart"]=start_date
            items["surl"]=scholarship.css("a::attr(href)").get(default='not-found').strip()

            yield items

        self.pgnum += 1
        next_page = f'https://www.scholars4dev.com/tag/scholarships-for-pakistans/page/{self.pgnum}/'

        if self.pgnum <= 16:
            yield response.follow(next_page, callback=self.parse)

       
