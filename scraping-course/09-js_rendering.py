from curl_cffi import requests


def scrape_page():
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.7',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://www.scrapingcourse.com/javascript-rendering',
        'sec-fetch-mode': 'cors',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
     }

    response = requests.get('https://www.scrapingcourse.com/ajax/products/json', headers=headers)
    response.raise_for_status()
    return response.status_code, response.text

if __name__ == '__main__':
    status_code, content = scrape_page()
    print(status_code)
    import ipdb; ipdb.set_trace()
