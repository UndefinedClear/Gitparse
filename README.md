<h1 align="center">Gitparse 😎</h1>

> [!NOTE]
> This is a python library for parsing github files!
<!-- <h2 align="left">Download libraries</p> -->


> [!IMPORTANT]
> Download the required libraries
> ```bash
> pip install lxml requests bs4
> ```

> [!TIP]
> This is an example! [link](/example.py)
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
