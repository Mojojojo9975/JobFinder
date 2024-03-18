import scrapy
from ..items import ScrapperItem


class LinkedinjobsSpider(scrapy.Spider):
    name = "linkedinJobs"
    api_url = 'https://pk.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/jobs-in-pakistan?start=' 

    def start_requests(self):
            first_job_on_page = 0
            first_url = self.api_url + str(first_job_on_page)
            yield scrapy.Request(url=first_url, callback=self.parse_job, meta={'first_job_on_page': first_job_on_page})

    def parse_job(self, response):
        items=ScrapperItem()
       
        first_job_on_page = response.meta['first_job_on_page']

        
        jobs = response.css("li")

        num_jobs_returned = len(jobs)
        print("******* Num Jobs Returned *******")
        print(num_jobs_returned)
        print('*****')
        
        for job in jobs:
            
            items['jtitle'] = job.css("h3::text").get().strip()
            items['jdescription'] = job.css('h4 a::attr(href)').get()
            items['jcompany'] = job.css('h4 a::text').get().strip()
            items['jsalary'] = job.css('h4 a::text').get().strip()
            items['jpublish'] = job.css('time::text').get().strip()
            items['jlocation'] = job.css('.job-search-card__location::text').get().strip()
            items['jurl'] = job.css(".base-card__full-link::attr(href)").get().strip()
            yield items
        

        if num_jobs_returned > 0:
            first_job_on_page = int(first_job_on_page) + 25
            next_url = self.api_url + str(first_job_on_page)
            yield scrapy.Request(url=next_url, callback=self.parse_job, meta={'first_job_on_page': first_job_on_page})

''' 

    job_id = models.BigAutoField(primary_key=True)
    job_title=models.CharField(max_length=70)
    job_description=models.TextField()
    company=models.CharField(max_length=50)
    salary=models.DecimalField(max_digits=8, decimal_places=2)
    publish_date=models.DateField()
    location=models.CharField(max_length=50)
    url=models.CharField( max_length=50)

    '''
