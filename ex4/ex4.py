import argparse
parser = argparse.ArgumentParser()
parser.add_argument('echo', help="반복할 텍스트")
parser.add_argument('-t', '--times', help="반복", type=int)
parser.add_argument('-u', '--upper', help="대문자로 변경", action="store_true")
parser.add_argument('-l', '--lower', help="소문자로 변경", action="store_true")

args = parser.parse_args()

text: str = args.echo

if args.times:
    text = f"{text}\n"*args.times

if args.upper:
    text = text.upper()

if args.lower:
    text = text.lower()

print(text)
