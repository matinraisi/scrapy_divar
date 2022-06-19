import scrapy
# https://api.divar.ir/v5/posts/gYuapJnR/contact/

url =  'https://divar.ir/v/{token}'

token_file = open("\scrapy project\scrapy_divar\divar/token.txt",'r',encoding='utf8')

tokens = token_file.read().split(',')
token_file.close()


Headers = {
    "Authorization":"Basic eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiMDkxNTYzMDgyMzAiLCJpc3MiOiJhdXRoIiwiaWF0IjoxNjU1NTQxNTIxLCJleHAiOjE2NTY4Mzc1MjEsInZlcmlmaWVkX3RpbWUiOjE2NTU1NDE1MjEsInVzZXItdHlwZSI6InBlcnNvbmFsIiwidXNlci10eXBlLWZhIjoiXHUwNjdlXHUwNjQ2XHUwNjQ0IFx1MDYzNFx1MDYyZVx1MDYzNVx1MDZjYyIsInNpZCI6IjE4MTRlNmRmLTFkNjAtNDg5Ni1iMTNmLTVjZTIwM2U2MTMwOCJ9.2E-8p03TQMgBODX7V4Ks0x3BSyxtlc6mJ8NmJSww1wY"
}


class DivarSpider(scrapy.Spider):
    name = 'divar'
    start_urls = [url.format(token=token,headers=Headers) for token in tokens ]


    def parse(self,response):
        informations = response.css('div span.kt-group-row-item__value::text')
        
        function = int(informations[0].extract())
        year = int(informations[1].extract())
      

        yield{
             'Fanction': function,
             'Year' : year,
        }








        # karkard = int(informations[0].extract)
        # year = int(informations[1].extract)
        # color = informations[2].extract()
        
        # number = response.css('div div.copy-row__content , .kt-group-row-item__value::text').extract()


        # yield{
        #     'Karkard':karkard,
        #     'Year':year,
        #     'Color':color,
        #     'Number':number
        # }