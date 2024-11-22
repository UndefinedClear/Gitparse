# -*- coding: utf-8 -*-
from requests import get
from bs4 import BeautifulSoup
from random import randint

class Git():
    def __init__(self, git_repo_author:str, git_repo_name:str):
        self.main_raw = f'https://raw.githubusercontent.com/{git_repo_author}/{git_repo_name}/refs/heads/main/'

    def getProxies(self, protocol:str = 'http'):

        """Return the proxy dict for requests

        :param protocol:
          - Protocol for dict of proxies, http or https
        """

        original = self.main_raw

        self.main_raw = f'https://raw.githubusercontent.com/proxify/free-proxy-list/refs/heads/main/'


        if protocol == 'http':
              # Path to file
              http_path = 'proxies/protocols/http/data.txt'
              #https_path = 'proxies/protocols/https/data.txt'

              # Getting the content of the file
              http = self.parse(http_path)
              #https = git.parse(https_path)

              proxies = {
                  'http': http
              }

              self.main_raw = original

              return proxies

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