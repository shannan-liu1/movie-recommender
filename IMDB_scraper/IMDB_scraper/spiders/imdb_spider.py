# to run
# scrapy crawl imdb_spider -o movies.csv

import scrapy

class ImdbSpider(scrapy.Spider):
    name = 'imdb_spider'

    start_urls = ['https://www.imdb.com/title/tt0816692/?ref_=fn_al_tt_1']

    def parse(self,response):
        
        pass

    def parse_full_credits(self, response):
        pass

    def parse_actor_page(self, response):
        yield({"actor" : actor_name, "movie_or_TV_name" : movie_or_TV_name})
