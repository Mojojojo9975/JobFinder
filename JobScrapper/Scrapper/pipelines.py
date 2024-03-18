# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from itemadapter import ItemAdapter

import mysql.connector

class ScrapperPipeline(object):


    def __init__(self):
        self.create_connection()
        self.truncate_table()
        

    def create_connection(self):
        self.conn=mysql.connector.connect(host= 'localhost', user = 'root', passwd = '',database = 'jobfinder')
        self.curr=self.conn.cursor()


    def truncate_table(self):
        try:
            # Truncate the table if it exists
            self.curr.execute('TRUNCATE TABLE main_jobs')
            self.conn.commit()
            print('Table truncated successfully.')
        except mysql.connector.Error as e:
            print('Error truncating table:', e) 
    


    def process_item(self,item,spider):
        self.store_db(item)
        return item

    

    
    def store_db(self,item):
        self.curr.execute('''INSERT INTO main_jobs (job_title, job_description, company, salary, publish_date, location, url)
                     VALUES (%s, %s, %s, %s, %s, %s, %s)''',
                   (item['jtitle'], item['jdescription'], item['jcompany'],
                    item['jsalary'], item['jpublish'], item['jlocation'], item['jurl']))
        self.conn.commit()
        




