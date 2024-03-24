# This program analyses python files and diplays the number of lines hte file has
import sys
#this program check the lines of codes your python file has
def count_lines(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    count = 0
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        count += 1
    return count

#Enter your file name and the file name you want to analyse
if __name__ == '__main__':
    if len(sys.argv) != 2:
        if len(sys.argv) > 2:
            print('Too many command-line arguments')
        else:
            print('No command-line argument')
        sys.exit(1)
    filename = sys.argv[1]
    if not filename.endswith('.py'):
        print('Not a Python file')
        sys.exit(1)
    try:
        count = count_lines(filename)
        print(f'{filename} has {count} lines of code')
    except FileNotFoundError:
        print(f'{filename}File does not exist')
        sys.exit(1)
# this is how to run
# start with your file name 
# example python file.py example.py
# ensure  it is a python file
# ensure it is in the same directory
