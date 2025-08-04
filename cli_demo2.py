import argparse
import os

def get_file_size(path):
    print(f"Checking path: {path}")  # Debug print
    if os.path.isfile(path):
        size = os.path.getsize(path)
        print(f"{path} size: {size} bytes")
    else:
        print("Invalid file path.")

def main():
    parser = argparse.ArgumentParser(description="Check file size")
    parser.add_argument('filepath', help="Path to the file")

    args = parser.parse_args()
    get_file_size(args.filepath)

if __name__ == "__main__":
    main()
