# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.files import FilesPipeline
from scrapy import Request
import os

class PdbscrapePipeline(FilesPipeline):

    # def get_media_requests(self, item, info):
    #     urls = ItemAdapter(item).get(self.files_urls_field, [])
    #     return [Request(urls)]
    #
    # def file_path(self, request, response=None, info=None):
    #     media_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()
    #     media_ext = os.path.splitext(request.url)[1]
    #     # Handles empty and wild extensions by trying to guess the
    #     # mime type then extension or default to empty string otherwise
    #     if media_ext not in mimetypes.types_map:
    #         media_ext = ''
    #         media_type = mimetypes.guess_type(request.url)[0]
    #         if media_type:
    #             media_ext = mimetypes.guess_extension(media_type)
    #     return 'full/%s%s' % (media_guid, media_ext)

    def process_item(self, item, spider):
        #print("Pipeline " + item['file_urls'])
        return item


