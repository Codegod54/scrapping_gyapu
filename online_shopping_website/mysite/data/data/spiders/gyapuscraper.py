import scrapy


class GyapuscraperSpider(scrapy.Spider):
    name = "gyapuscraper"
    allowed_domains = ["gyapu.com"]
    start_urls = ["https://www.gyapu.com/category/laptops1"]

   
    def parse(self, response):

        products = response.css('div.categoryRightTop flex flex-wrap')
        for product in products:
            image_url = product.css('div.fslink relative::attr(href)').get()
            product_name = product.css('div.fsdet_title text-secondary text-md sm:text-sm text-center hover:text-primary line-clamp::text').get()
            product_price = product.css('div.price text__price text-center text-lg  font-bold::text').get() 

            yield {
                'product_name': product_name,
                'product_price': product_price,
                'image_url': image_url,

            }

        