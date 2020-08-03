import scrapy
from ..items import PdbscrapeItem

proteins = ["6XC2", "6XC3", "6XC4", "6XC7", "6XHM", "6XKM", "6XKF", "6XKH", "6XMK", "6ZFO", "6XCM", "6XCN", "6XE1",
            "6Z97", "6ZDH", "6ZGE", "6ZGG", "6ZGH", "6ZGI", "7C2L", "6XHU", "6XIP", "6ZCO", "6XFN", "6XG2", "7C8U",
            "6XG3", "6ZCT", "6ZCZ", "6ZER", "7C8W", "7C8V", "7CAN", "6XDG", "6X2G", "6XB0", "6XB1", "6XB2", "6XA4",
            "6XAA", "6XA9", "6XCH", "6XBG", "6XBH", "6XBI", "6XDC", "6XDH", "6Z2E", "6Z4U", "6M5I", "7BQ7", "7C8R",
            "7C8T", "6X6P", "7BYR", "5RHB", "5RHC", "5RHD", "5RHE", "5RHF", "6X4I", "6YZ5", "6YZ7", "6Z2M", "6Z43",
            "6M1V", "7BWJ", "7BZF", "7C2K", "6WPS", "6WPT", "6X29", "6X2A", "6X2B", "6X2C", "6WZO", "6WZQ", "6X1B",
            "7BW4", "7C2I", "7C2J", "7C01", "6WZU", "5RGT", "5RGU", "5RGV", "5RGW", "5RGX", "5RGY", "5RGZ", "5RH0",
            "5RH1", "5RH2", "5RH3", "5RH4", "5RH5", "5RH6", "5RH7", "5RH8", "5RH9", "5RHA", "6Y2G", "6Y2F", "6Y2E",
            "6W02", "6W01", "6Y84", "6W41", "6W4H", "6VSB", "6W4B", "6W61", "6W63", "6W75", "6VW1", "6W6Y", "6VXS",
            "6VWW", "6VYO", "6VYB", "6VXX", "6YB7", "5R84", "5R83", "5R7Y", "5R80", "5R82", "5R81", "5R7Z", "5REA",
            "5REC", "5REB", "5REE", "5RED", "5REG", "5REF", "5RE9", "5RE8", "5RE5", "5RE4", "5RE7", "5RE6", "5RFB",
            "5RFA", "5RFD", "5RFC", "5RFF", "5RFE", "5RFH", "5RFG", "5REY", "5REX", "5RF9", "5REZ", "5RF2", "5REP",
            "5RF1", "5RES", "5RF4", "5RER", "5RF3", "5REU", "5RF6", "5RET", "5RF5", "5REW", "5RF8", "5REV", "5RF7",
            "5REI", "5REH", "5REK", "5REJ", "5REM", "5REL", "5REO", "5RF0", "5REN", "5RFZ", "5RFY", "5RFR", "5RFQ",
            "5RFT", "5RFS", "5RFV", "5RFU", "5RFX", "5RFW", "5RFJ", "5RFI", "5RFL", "5RFK", "5RFN", "5RFM", "5RFP",
            "5RFO", "5RG0", "6M03", "6M17", "6M0J", "6M3M", "6LU7", "6LVN", "6LXT", "6LZG", "6W9C", "5R8T", "6M71",
            "6W9Q", "6YI3", "7BTF", "6WEN", "6WCF", "5RG1", "5RG2", "5RG3", "5RGG", "5RGH", "5RGI", "5RGJ", "5RGK",
            "5RGL", "5RGM", "5RGN", "5RGO", "5RGP", "5RGQ", "5RGR", "5RGS", "6M2N", "6M2Q", "6YLA", "6WIQ", "6WJI",
            "6WJT", "7BQY", "7BV2", "7BV1", "6LZE", "6M0K", "7BUY", "6W37", "6WEY", "6WKP", "6WKQ", "6WLC", "6YHU",
            "6YM0", "6YNQ", "6YOR", "6WKS", "6WNP", "6WOJ", "6WQF", "6WQ3", "6WQD", "6WRH", "6YT8", "6YWK", "6YWL",
            "6YWM", "6WRZ", "6WTC", "6WVN", "6YVA", "6YYT", "6YZ1", "7BRO", "7BRP", "7BRR", "7BZ5", "6WTJ", "6WTK",
            "6WTM", "6WTT", "6YVF", "6YZ6", "6WUU", "6WX4", "6WXC", "6WXD", "6YUN", "7C22"]



class PdbSpider(scrapy.Spider):
    name = 'PDB'
    start_urls = ["https://www.rcsb.org/"]

    def parse(self, response):

       #Code loops through every protein of interest
       #for i in range(0, len(proteins)):
       for i in range(0, 2):
            link = "https://www.rcsb.org/structure/" + proteins[i]
            yield scrapy.Request(link, callback = self.parse2)

    def parse2(self, response):

        download = PdbscrapeItem()
        link =  response.xpath("//*[@id='DownloadFilesButton']/ul/li[3]/a").extract()

        url = ['https:'+(link[0])[9 : 43]]
        name = [(link[0])[35 : 43]]

        download['file_urls'] = url
        download['file_name'] = name
        #yield {"Read.ME" : download['file_urls']}
        #yield {"Read.ME": download['file_name']}
        yield download

    pass




    # def parse(self, response):
    #
    #     download = PdbscrapeItem()
    #
    #     link =  response.xpath("//*[@id='DownloadFilesButton']/ul/li[3]/a").extract()
    #
    #     url = ['https:'+(link[0])[9 : 43]]
    #
    #     download['file_urls'] = url
    #     #yield {"Read.ME" : download['file_urls']}
    #     yield download
    #
    #
    #
    # pass

#        Code loops through every protein of interest
#        for i in range(0, len(proteins)):
#             link = "https://www.rcsb.org/structure/" + proteins[i]
#             yield scrapy.Request(link, callback = self.sub_parse)