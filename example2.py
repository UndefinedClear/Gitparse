from gitparse import *

# http
http_proxy = getProxy('http', True)
print(http_proxy)

# https
https_proxy = getProxy('https', True)
print(https_proxy)

# socks4
http_proxy = getProxy('socks4', True)
print(http_proxy)

# socks5
https_proxy = getProxy('socks5', True)
print(https_proxy)