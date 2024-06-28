import sys
import re
from os import startfile

if __name__ == '__main__':
    if len(sys.argv) not in [2, 3]:
        print('''Usage: python parse_zybooks_headers.py <input .txt file name>
              OR  python parse_zybooks_headers.py <input .txt file name> <output .txt file name>''')
        sys.exit(1)

    infile_name = sys.argv[1] + '.txt'
    outfile_name = sys.argv[2] + '.txt' if len(sys.argv) == 3 else 'parsed_headers.txt'

    print(f'Will read from {infile_name} and write to file: {outfile_name}')
    
    with open(infile_name, 'r') as infile:
        with open(outfile_name, 'w') as outfile:
            for line in infile:
                line = line.strip()
                if (re.search("^\d+%$", line)) or line in ['No activities', 'Print chapter', 'Optional', '']:
                    print(f'Junk line found: {line}')
                else:
                    print(f'Non-junk line found: {line}')
                    outfile.write(f'{line}\n')

    print(f'Opening output file: {outfile_name}')
    startfile(outfile_name)

            