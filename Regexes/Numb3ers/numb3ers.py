import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # matches = re.search(r"^(25[0-5]|2[0-4]\d|[01]?\d\d?)\.(25[0-5]|2[0-4]\d|[01]?\d\d?)\.(25[0-5]|2[0-4]\d|[01]?\d\d?)\.(25[0-5]|2[0-4]\d|[01]?\d\d?)$", ip)

    pattern = r"^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$"
    return re.search(pattern, ip) is not None

if __name__ == "__main__":
    main()

