<h1 align="center">Gitparse 😎</h1>
<h2 align="left"> This is a python library for parsing github files!</h2>

> [!NOTE]
> Maybe i will add proxy parsing in lib

<br>

> [!IMPORTANT]
> Download the required libraries
> ```bash
> pip install lxml requests bs4
> ```

<br>

> [!WARNING]
> I don't test it with .exe files. Be careful!

<br>

> [!TIP]
> This is an example! | [link](/example.py)
> ```python
> from gitparse import Git
> 
> # Path to file
> path = 'examples/example.txt'
>
> # Initializing Git class
> git = Git('avirt1274', 'Gitparse')
>
> # Getting the content of the file
> text = git.parse(path)
>
> # Creating file with downloaded content
> with open(path, 'w') as parsed_file:
>     parsed_file.write(text)
> ```

<br>

> [!TIP]
> Parsing proxies with Gitparse! | [link](/getProxies.py)
> ```python
> from gitparse import Git, get
> 
> # Path to file
> http_path = 'proxies/protocols/http/data.txt'
> # https_path = 'proxies/protocols/https/data.txt'
> 
> # Initializing Git class
> git = Git('proxifly', 'free-proxy-list')
> 
> # Getting the content of the file
> http = git.parse(http_path)
> # https = git.parse(https_path)
> 
> proxies = {
>     'http': http,
>     # 'https': https,
> }
> 
> #check
> resp = get('https://google.com', proxies=proxies)
> print(resp.status_code)
> 
> # Return proxies
> print(f'''
> All free proxies from https://github.com/proxifly/free-proxy-list/blob/main/proxies/protocols/https/data.txt
>       
> Proxies:
> 
> HTTP:
> {http}
> ''')
> ```
> Support authors of free proxies: [Proxies from here](https://github.com/proxifly/free-proxy-list)
