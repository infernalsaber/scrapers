## Scraping

<p>
This "project" is meant to house some of the scrapers I've built, for testing, for learning and similar purposes. <br>
Not really designed for scale/regular use, but I will add READMEs for understanding. <br>
Not recommeneded to use without checking every site's TOS.
</p>

The focus, at the moment, will be on basic Pythonic scraping and a bit less, on parsing.

## Directory

### Scraping Course

Challenges from https://www.scrapingcourse.com shall be housed here. <br>
In my opinion, this looks like a very good sandbox to learn/polish scraping skills.

Another such sandbox is https://toscrape.com/ which is, not as challenging; I might attempt it sometime but have no such inclination atm.

### Aniscrapers

Broadly, intended to house any scrapers related to anime/manga etc. sites I have created.

### E-commerce

E-commerce data is one of the biggest practical use cases for web scraping. As such, I have made many scrapers for them of varying granularity. <br>

Those shall be housed here.

### Misc.

TBA

## Environment

This project will broadly use curl-cffi for client requests, camoufox for browsers and bs4 for parsing.
Reasoning:
- curl-cffi has a largely requests-compatible API, with added measures for TLS fingerprinting
- camoufox is largely playwright-compatible API, with advanced options to avoid bot detection
- bs4 (with lxml) is fairly easy to use, and with lxml it becomes much faster

Recommended use: [uv](https://docs.astral.sh/uv/getting-started/installation/#pypi) for package management

```
uv venv --python 3.12
source .venv/bin/activate
uv pip install -r requirements.txt
```

## License

MIT