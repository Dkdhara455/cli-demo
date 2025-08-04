# cli_tool.py

import argparse

def main():
    parser = argparse.ArgumentParser(description="Simple CLI Utility")

    # Add arguments
    parser.add_argument('--name', type=str, required=True, help='Your name')
    parser.add_argument('--count', type=int, default=1, help='How many times to greet')

    args = parser.parse_args()

    for _ in range(args.count):
        print(f"Hello, {args.name}!")

if __name__ == '__main__':
    main()
