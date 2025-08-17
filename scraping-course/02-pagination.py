from curl_cffi import requests



def scrape_page(page_num: int = 1):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'en-US,en;q=0.7',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'referer': 'https://www.scrapingcourse.com/pagination',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    }

    response = requests.get(f'https://www.scrapingcourse.com/pagination/{page_num}', headers=headers)    
    response.raise_for_status() 
    return response.status_code, response.text

if __name__ == '__main__':
    page_num = 1
    status_code, content = scrape_page(page_num)
    # Some parsing logic maybe (future)