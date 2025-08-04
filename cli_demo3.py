# multi_tool.py

import argparse

def greet(args):
    print(f"Hello, {args.name}!")

def add(args):
    print(f"Sum: {args.a + args.b}")

def main():
    parser = argparse.ArgumentParser(description="Multi-tool CLI")
    subparsers = parser.add_subparsers()

    # Greet command
    greet_parser = subparsers.add_parser('greet', help='Say hello')
    greet_parser.add_argument('name', type=str)
    greet_parser.set_defaults(func=greet)

    # Add command
    add_parser = subparsers.add_parser('add', help='Add numbers')
    add_parser.add_argument('a', type=int)
    add_parser.add_argument('b', type=int)
    add_parser.set_defaults(func=add)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
# for run the program in terminal
# python cli_demo3.py greet Deepak
# o/p-->Hello, Deepak!
# python cli_demo3.py add 2398 432
# o/p-->Sum: 2830