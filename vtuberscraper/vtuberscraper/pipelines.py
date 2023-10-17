# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2
import os

class VtuberscraperPipeline:
    def process_item(self, item, spider):
        return item

class saveTopostgresPipeline:

    def __init__(self):
        self.conn = psycopg2.connect(
            host=os.environ["GACHIKOI_GG_DB_HOST"],
            dbname="gachikoi",
            user="matt",
            password="Atarashii5040!($)"
        )

        self.cur = self.conn.cursor()
