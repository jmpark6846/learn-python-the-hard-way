import argparse
parser = argparse.ArgumentParser()
parser.add_argument('files', nargs='*', type=argparse.FileType('r'),)
args = parser.parse_args()

for file in args.files:
    print(file.read(),end='')

