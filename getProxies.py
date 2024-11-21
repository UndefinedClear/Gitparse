from gitparse import Git, get

# Path to file
http_path = 'proxies/protocols/https/data.txt'
https_path = 'proxies/protocols/https/data.txt'

# Initializing Git class
git = Git('proxifly', 'free-proxy-list')

# Getting the content of the file
http = git.parse(http_path)
https = git.parse(https_path)

proxies = {
    'http': http,
    'https': https,
}

#check
get('https://google.com', proxies=proxies)

# Return proxies
print(f'''
All free proxies from https://github.com/proxifly/free-proxy-list/blob/main/proxies/protocols/https/data.txt
      
Proxies:

HTTP:
{http}
------------------
HTTPS:
{https}
''')

# # Creating file with downloaded content
# with open(path, 'w') as parsed_file:
#     parsed_file.write(text)