# Pylight
Command line utility for viewing code snippets and source code files with syntax-highlighting

## Installation
> Before you get started, ensure you have Python 3.8 or later installed

#### **Step 1:** Clone this repository
```bash
git clone https://github.com/Soliez/pylight.git
```

#### **Step 2:** Run the install script
```bash
python3 pylight/install.py
```

### Alternative Installations

Pylight is also available as a compiled binary. See the [Releases](https://github.com/Soliez/pylight/releases) page for more details.

---

## Usage

> All of the following example usages are valid


### Reading input from a file

Invoking pylight with the `-f` flag instructs pylight to treat the second argument as a file path

```bash
pylight -f <path-to-source-code-file>
```

---

### Reading input from a command line argument

Invoking pylight with the `-c` flag instructs pylight to treat the second argument as code

```bash
pylight -c "import requests; r = requests.get('https://jsonplaceholder.typicode.com/users'); print(r.json())"
```

--- 

### Reading input from an interactive prompt

Invoking pylight with the `-i` flag instructs pylight to read the input from the user with an interactive prompt at runtime

```bash
pylight -i
```
---

### Reading input from standard-in

Invoking pylight with the `-` flag instructs pylight to read the input from `stdin`

```bash
echo "import requests; r = requests.get('https://jsonplaceholder.typicode.com/users'); print(r.json())" | pylight -
```
---

### Example Output

```bash
$ pylight -f example.py
```
```python3
import requests

r = requests.get("https://jsonplaceholder.typicode.com/users")

print(r.json())
```
