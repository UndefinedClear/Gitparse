from gitparse import Git, get

# Path to file
http_path = 'proxies/protocols/http/data.txt'
# https_path = 'proxies/protocols/https/data.txt'

# Initializing Git class
git = Git('proxifly', 'free-proxy-list')

# Getting the content of the file
http = git.parse(http_path)
proxies_http = http.split('\n')
# https = git.parse(https_path)

proxies = {
    'http': http,
    # 'https': https,
}

working_proxies:str = ''
not_working_proxies:str = ''


#check
for proxy in proxies_http:
    resp = get('https://google.com', proxies=proxies)

    if resp.status_code == 200:
        working_proxies += f'{proxy}\n'

        print(proxy + ' | SUCCESS')
    else:
        not_working_proxies += f'{proxy}\n'
        print(proxy + ' | FAIL')


print(f'\n\nWorking:\n{working_proxies}')
print(f'\n\nNot Working:\n{not_working_proxies}')

# Creating file with downloaded content
with open('examples/proxies.txt', 'w') as f:
    f.write(f'\n\nWorking:\n{working_proxies}')