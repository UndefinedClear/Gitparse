from gitparse import Git

# Path to file
path = 'examples/example.txt'

# Initializing Git class
git = Git('avirt1274', 'Gitparse')

# Getting the content of the file
text = git.parse(path)

# Creating file with downloaded content
with open(path, 'w') as parsed_file:
    parsed_file.write(text)