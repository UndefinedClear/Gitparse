<h1 align="center">Gitparse 😎</h1>
<h2 align="left"> This is a python library for parsing github files!</h2>

> [!NOTE]
> Maybe i will add proxy parsing in lib

<br>

> [!IMPORTANT]
> Download the required libraries (Windows)
> ```bash
> pip install lxml requests bs4
> ```

> [!IMPORTANT]
> For download required libs on termux run (Termux)
> ```bash
> bash termux.sh
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
> Parsing proxies with Gitparse! | [link](/getProxies.py) <br>
> Support authors of free proxies: [Proxies from here](https://github.com/proxifly/free-proxy-list)
