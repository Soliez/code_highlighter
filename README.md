# code_highlighter
A simple script that accepts a path to a source code file as an argument and prints the contents of the file with syntax highlighting to the screen

#### Usage
```bash
$ python  code_higlighter.py /path/to/file.py
```
#### Example output printed to the screen with syntax highlighting

```python
$ python  code_higlighter.py /path/to/file.py
import requests

r = requests.get("https://jsonplaceholder.typicode.com/users")

print(r.json())
```
