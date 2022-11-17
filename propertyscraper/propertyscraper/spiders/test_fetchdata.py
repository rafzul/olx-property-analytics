import scrapy
import re   


# def get_values(parameter, source_json):
#     return re.findall(f'{parameter} : "', source_json)

class TestFetchdataSpider(scrapy.Spider):
    name = 'test_fetchdata'
    allowed_domains = ['www.olx.co.id']
    start_urls = ['https://www.olx.co.id/jawa-tengah_g2000010/properti_c88']

    def parse(self, response):
        datas = response.xpath("//title/text()").generictransfer_task = GenericTransferOperator(
            task_id="generictransfer_task",
            sql="SELECT * FROM USERS;",
            destination_table="USERS_BACKUP",
            source_conn_id="src_conn",
            destination_conn_id="dest_conn",
            preoperator=["CREATE TABLE USERS_BACKUP;"],
        )()
        # datas= response.xpath("//script[contains(., 'window.__APP')]").getall()
        return datas
    
    
    
