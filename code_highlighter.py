# Name: code_highlighter.py
#
# Author: Erik Solis
#
# Created: 2024-01-25

import sys
from pygments import highlight
from pygments.lexers import guess_lexer_for_filename
from pygments.formatters import TerminalFormatter



def main():
    if len(sys.argv) != 2:
        print("Usage: python syntaxcolor.py <source_code_file>")
        sys.exit(1)

    source_code_file = sys.argv[1]
    try:
        with open(source_code_file, 'r') as file:
            code = file.read()

        lexer = guess_lexer_for_filename(source_code_file, code)
        highlighted_code = highlight(code, lexer, TerminalFormatter())
        print(highlighted_code)

    except FileNotFoundError:
        print(f"Error: File '{source_code_file}' not found.")
    
    return

    
if __name__ == "__main__":
    main()