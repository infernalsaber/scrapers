from curl_cffi import requests

def login(session: requests.Session, username: str, password: str):
    

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'origin': 'https://www.scrapingcourse.com',
        'pragma': 'no-cache',
        'referer': 'https://www.scrapingcourse.com/login',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    }

    data = {
        'email': username,
        'password': password,
    }

    response = session.post('https://www.scrapingcourse.com/login', headers=headers, data=data)
    response.raise_for_status()
    return response.status_code, response.text


def scrape_page(session: requests.Session):

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    }

    response = session.get('https://www.scrapingcourse.com/dashboard', headers=headers)
    response.raise_for_status()
    return response.status_code, response.text

if __name__ == '__main__':
    session = requests.Session()
    login(session,'admin@example.com', 'password')
    status_code, content = scrape_page(session)
    import ipdb; ipdb.set_trace()