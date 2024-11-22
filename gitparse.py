# -*- coding: utf-8 -*-
from requests import get
from bs4 import BeautifulSoup
from random import randint

class Git():
    def __init__(self, git_repo_author:str, git_repo_name:str):
        self.main_raw = f'https://raw.githubusercontent.com/{git_repo_author}/{git_repo_name}/refs/heads/main/'

    def parse(self, path:str) -> str:
        """Return the content of the file

        :param path:
          - Path to the file on repository from inits of Git()
        """
        st_accept = "text/html" # tell web,
        # imatate web connecting
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36/537.36'
            'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36/537.36'
            'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
            'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
            'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15'
        ]
        # formatting header
        headers = {
            "Accept": st_accept,
            "User-Agent": user_agents[randint(0, len(user_agents) - 1)]
        }

        self.main_raw = self.main_raw + path

        try:
            html = BeautifulSoup(get(self.main_raw, headers=headers).text, 'lxml')
        except Exception as e:
            print('ERROR: ' + str(e))
            return 'File does not exists!'
        else:
            return html.p.text
        
def testProxy(proxies, proxies_end_final):
    try:
        # Make a request to check the proxy
        resp = get('https://api.ipify.org/', proxies=proxies, timeout=10)

        #if response is successful
        if resp.status_code == 200:
            print(f"Proxy working: {proxies_end_final}")
            print(f"Your public IP address: {resp.text}")
        else:
            print(f"Failed to connect using the proxy: {proxies_end_final}")
            print(f"Status code: {resp.status_code}")
            # Handle failure (optional retry logic or fallback to another proxy)

    except Exception as e:
        print(f"Error occurred while trying to use the proxy: {proxies_end_final}")
        print(f"Exception: {e}")
        #Handle proxy failure (could try another proxy here)

def getProxy(protocol: str = 'http', test_proxy:bool = False):
    """Return the proxy dict for requests (with one random proxy)

    # Protocols:
    * http
    * https
    * socks4
    * socks5

    :param protocol:
      - Protocol for dict of proxies, http or https
    """

    # Path to file
    proxy_path = f'proxies/protocols/{protocol}/data.txt'

    # Initializing Git class
    git = Git('proxifly', 'free-proxy-list')

    # Getting the content of the file
    http = git.parse(proxy_path)
    proxies_http = http.split('\n')

    proxies_end: list[str] = []

    for proxy in proxies_http:
        proxies_end.append(proxy)

    proxies_end_final: str = proxies_end[randint(0, len(proxies_end) - 1)]

    # Dictionary for the library "requests"
    proxies = {
        f'{protocol}': proxies_end_final
    }
    
    if test_proxy:
        testProxy(proxies, proxies_end_final)

    # Return dictionary for the library "requests"
    return proxies