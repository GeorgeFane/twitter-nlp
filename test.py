from snscrape.modules.twitter import TwitterHashtagScraper as scrape

gen = scrape('gme').get_items()
next(gen)