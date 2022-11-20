import scrapy
import re
import json


class TestFetchdataSpider(scrapy.Spider):
    name = 'test_fetchdata'
    start_urls = ["https://www.olx.co.id/jawa-tengah_g2000010/properti_c88"]
    
'''
bfs / dfs?
scrapernya harus gini:
1. ambil data berbentuk json yg isinya cuma interval waktu yang ditentuin (e.g: 1 hari), dari url kategori yang disediain. dump ke file json di cloud storage
TODOS:
- list url yang mau diambil
- ambil response yg berisi json
- fetch setiap elemen dari response tsb, jadiin file dict dict_response
- ambil bagian single_property = states[items][elements]
- siapin dict_baru = dict_response
- for setiap x di single_property:
	date = states[items][elements][display_date].jadiin_datetime
	if date < start_interval_date atau > end_interval_date:
		pass
	else:
		
- file dict jadiin json
- json diupload ke cloud storage by stream

2. transformation script, ambil json dari GCS, ambil bagian elements doang (informasi setiap page), dump ke file json di GCS
- set interval tanggal (start_interval dan end_interval)
- download file json di cloud storage

3. 



1. Open website (https://www.olx.co.id/jawa-tengah_g2000010/properti_c88)
2. ambil json di /script textnya window.__APP (spider)
3. cari karakter2 ngga penting lewat regex, buang 
4. panggil get_values() untuk (using regex) assign yg dibutuhin by regex. 
5. for semua elemen di get_values(id):

2. fetch informasi dasar setiap elemen LEWAT window.__APP di setiap halaman kategori
3. cari yg rangenya hari ini (dikasih start_interval etc) by info di window.__ app5. 
	- kalo nemu hasilnya, mark as true. 
	- temuin semua url setiap items lewat elemen "._1DNjI.a" utk ID yg marknya true tsb. append ke items
	- kalo ngga nemu, skip. next elemen 
4. Kalo ngga nemu, paginationnya ditambahin lagi, balik ke awa
5. Kalo udh ketemu semua per interval ini, dump semua yang marknya TRUE as json

fetch data per hari ini
kasih time range (kalo realtime pake hari ini ampe kemaren, kalo backfill pake date lawas)
kalo masuk range:
	x = si hasil fetch dalam bentuk json
	return x dalam bentuk json stream
'''

    def parse(self, response):
        #encode().decode('unicode_escape')
        datas = response.xpath("//script[contains(., 'window.__APP')]/text()").get().replace('window.__APP = ','\"window.__APP\":')
        print(type(datas))
        # jsons = json.loads(jsonified)
        # # jsons = re.sub('\n', '', datas)
        yield dict(content="test")
    
