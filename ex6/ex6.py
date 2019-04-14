import argparse
import os
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('path')
parser.add_argument('-name')
parser.add_argument('-type')
parser.add_argument('-print', action="store_true")
parser.add_argument('-exec')

args = parser.parse_args()

def run_command(entry, _print=None, exec=None):
    print(entry, _print, exec)
    if _print:
        print(entry.name)

    if exec:
        subprocess.run([exec, ])

def find_files_in_dir(path, name=None, type=None, _print=None, exec=None):
    with os.scandir(path=path) as it:
        for entry in it:
            if name:
                if name in entry.path.split('/')[-1]:
                    run_command(entry, _print=_print, exec=exec)
            else:
                run_command(entry, _print=_print, exec=exec)

            if entry.is_dir():
                find_files_in_dir(entry.path, name)


find_files_in_dir(args.path, args.name, args.type, args.print, args.exec)
