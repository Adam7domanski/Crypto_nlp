# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import codecs



# class JsonWithEncodingPipeline(object):

    # def __init__(self):
    #     self.file = codecs.open('Scraped_data.json', 'w', encoding='utf-8')
    #     self.file.write("\n")


    # def process_item(self, item, spider):
    #     line = json.dumps(dict(item), ensure_ascii=False) + "\n"
    #     # line = json.dumps(ItemAdapter(item).asdict(), ensure_ascii=False) + "\n"
    #     self.file.write(line)
    #     return item

    # def spider_closed(self, spider):
    #     self.file.close()


# class ScraperPipeline:
#     def process_item(self, item, spider):
#         return item