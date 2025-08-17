from curl_cffi import requests

def scrape_page(page_num: int = 1):
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.7',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://www.scrapingcourse.com/button-click',
        'sec-fetch-mode': 'cors',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    }

    offset = (page_num - 1) * 10
    params = {
        'offset': str(offset),
    }

    response = requests.get(
        'https://www.scrapingcourse.com/ajax/products',
        params=params,
        headers=headers
    )
    response.raise_for_status()
    return response.status_code, response.text

if __name__ == '__main__':
    page_num = 1
    status_code, content = scrape_page(page_num)
    import ipdb; ipdb.set_trace()
    # Some parsing logic maybe (future)