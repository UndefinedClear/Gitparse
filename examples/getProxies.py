from gitparse import Git

# Path to file
path = 'proxies/protocols/https/data.txt'

# Initializing Git class
git = Git('proxifly', 'free-proxy-list')

# Getting the content of the file
text = git.parse(path)

print(f'''
All free proxies from https://github.com/proxifly/free-proxy-list/blob/main/proxies/protocols/https/data.txt
      
Proxies:
    {text}
''')

# # Creating file with downloaded content
# with open(path, 'w') as parsed_file:
#     parsed_file.write(text)