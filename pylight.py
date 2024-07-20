import os
import sys
from pygments import highlight
from pygments.lexers import guess_lexer
from pygments.formatters import TerminalFormatter



def main():

    FLAGS = ['-f', '-c', '-i', '-']

    lines = [
        f"Usage: pylight {FLAGS} [Path|Code|None]",
        "\t -f  Read input from a file",
        "\t -c  Read input from the second command line argument (argv[2]) (treat as code)",
        "\t -i  Read input from an interactive prompt",
        "\t -   Read input from standard-in (stdin) via pipe"
    ]
    USAGE = '\n'.join(lines)


    def read_source_file(path: str) -> str | None:
        source_file = os.path.abspath(path)
        if not os.path.exists(source_file):
            return None
        
        try:
            with open(path,'r') as f:
                code = f.read()
                return code
        except UnicodeDecodeError or IOError:
            print("Error: Target appears to be binary ...")
            return None


    def get_code() -> str:
        '''
        Dynamically get the code from the appropriate input source
        '''
        
        code = None

        if len(sys.argv) >= 1:
            flag = sys.argv[1]

            if flag not in FLAGS:
                print(f"Invalid flag option: {flag}")
                sys.exit(1)

            try:
                path_or_code = sys.argv[2]
                if flag == '-f':
                    code = read_source_file(path_or_code)
                elif flag == "-c":
                    code = sys.argv[2]
                else:
                    print(USAGE)
                    sys.exit(1)
            except IndexError:
                if flag == '-i':
                    code = input('Enter some code: ')
                elif flag == '-':
                    if not sys.stdin.isatty():
                        code = sys.stdin.read()
                    else:
                        print(USAGE)
                        sys.exit(1)
                else:
                    print(USAGE)
                    sys.exit(1)
        else:
            print(USAGE)
            sys.exit(1)
        return code


    def add_syntax_coloring(source: str):
        lexer = guess_lexer(source)
        highlighted_code = highlight(source, lexer, TerminalFormatter())
        return highlighted_code


    code = get_code()

    if not code or len(code) == 0:
        print("No valid input provided. Exiting.")
        sys.exit(1)
    else:
        highlight_code = add_syntax_coloring(code)
        print(highlight_code)


if __name__ == "__main__":
    main()