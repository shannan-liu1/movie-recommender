# to run
# scrapy crawl imdb_spider -o movies.csv

import scrapy

class ImdbSpider(scrapy.Spider):
    name = 'imdb_spider'

    start_urls = ['https://www.imdb.com/title/tt0816692/']

    def parse(self,response):
        """
        assumes we start on a movie page, then
        navigates to "All Cast & Crew" page
        """
        next_page = f"{response.url}fullcredits/"
        #print(next_page)
        #next_page = response.urljoin(next_page)
        yield scrapy.Request(next_page, callback=self.parse_full_credits)

    def parse_full_credits(self, response):
        # get links for each actor's imdb page
        links = [a.attrib["href"] for a in response.css("td.primary_photo a")]

        # go through each actor's link and run the function "parse_actor_page"
        for link in links:
            yield scrapy.Request(f'https://www.imdb.com/{link}',
                                callback = self.parse_actor_page)

    def parse_actor_page(self, response):
        """yield the actor's name and all the movies or TV shows they've done"""

        # get actor's name
        actor = response.css("td h1.header span.itemprop::text").get()
        # get all the movies and tv shows they've worked on
        movies_and_shows = response.css("div.filmo-row b a::text").getall()

        # create a dictionary for each of the movies
        # and shows that actors have worked on
        for i in movies_and_shows:
            yield {"actor" : actor,
            "movie_or_TV_name" : i}
