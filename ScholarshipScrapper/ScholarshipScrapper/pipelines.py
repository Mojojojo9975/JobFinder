# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector

class ScholarshipscrapperPipeline:
    
    def __init__(self):
        self.create_connection()
        
        

    def create_connection(self):
        self.conn=mysql.connector.connect(host= 'localhost', user = 'root', passwd = '',database = 'jobfinder')
        self.curr=self.conn.cursor()




    def process_item(self,item,spider):
        self.store_db(item)
        return item

    

    
    def store_db(self,item):
        self.curr.execute('''INSERT INTO main_scholarships (university,scholarship_title,deadline,country,degree,course_start,url)
                     VALUES (%s, %s, %s, %s, %s, %s, %s)''',
                   (item['suni'], item['stitle'], item['sdeadline'],
                    item['scountry'], item['sdegree'], item['scoursestart'], item['surl']))
        self.conn.commit()
        

        '''
        stitle=scrapy.Field()
    suni=scrapy.Field()
    sdeadline=scrapy.Field()
    scountry=scrapy.Field()
    sdegree=scrapy.Field()
    scoursestart=scrapy.Field()
    surl=scrapy.Field()
        '''




