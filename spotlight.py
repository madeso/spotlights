import unicodedata
import argparse
import subprocess

parser = argparse.ArgumentParser(description="Create a new spotlight")
parser.add_argument("name", help="The name of the spotlight")
args = parser.parse_args()
name = args.name

# https://stackoverflow.com/questions/3194516/replace-special-characters-with-ascii-equivalent
name = unicodedata.normalize('NFD', name).encode('ascii', 'ignore').decode()
# https://stackoverflow.com/questions/7406102/create-sane-safe-filename-from-any-unsafe-string
name = "".join(c for c in name if c.isalpha() or c.isdigit() or c==' ').strip().replace(' ', '_').lower()

file = f'spotlight/{name}/index.md'
# print(file)

subprocess.run(["hugo", "new", "content", file])

subprocess.run(["code.cmd", f'content/{file}'])
