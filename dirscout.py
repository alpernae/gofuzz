#!/usr/bin/env python

import argparse
import requests
from termcolor import colored
import warnings


# Tüm uyarıları kapat
warnings.filterwarnings("ignore")

def scan_folders(base_url, wordlist_file, timeout, log_file, example_codes):
    with open(wordlist_file, 'r') as f:
        wordlist = f.read().splitlines()

    try:
        with open(log_file, 'w') as log:
            print("\n\nScanning Started!\n")  # Tarama başladığında mesajı ekrana yazdır
            for folder in wordlist:
                target_url = f"{base_url + folder}"
                try:
                    response = requests.get(target_url, timeout=timeout)
                    status_code = response.status_code
                except requests.Timeout:
                    status_code = "Timeout"

                if should_show_status(status_code, example_codes):
                    print_status(target_url, status_code)
                    log_status(log, target_url, status_code)

    except KeyboardInterrupt:
        pass  # KeyboardInterrupt hatasını yakala ve sessizce çık

def should_show_status(status_code, example_codes):
    return not example_codes or status_code in example_codes

def print_status(url, status_code):
    status_color = 'green' if status_code == 200 else 'yellow' if status_code != "Timeout" else 'red'
    status_text = "Timeout" if status_code == "Timeout" else str(status_code)
    result = f"{colored('[STATUS CODE]', 'red')} [{colored(status_text, status_color)}] - {colored(url, 'cyan')}"
    print(result)

def log_status(log, url, status_code):
    status_text = "Timeout" if status_code == "Timeout" else str(status_code)
    result = f"[STATUS CODE] [{status_text}] - {url}\n"
    log.write(result)

def main():
    parser = argparse.ArgumentParser(description="Web folder scanning tool")
    parser.add_argument("-u", "--url", required=True, help="Base URL to scan")
    parser.add_argument("-w", "--wordlist", default="wordlist/dirsearch.txt", help="Path to the wordlist file")
    parser.add_argument("-t", "--timeout", type=float, default=1, help="Request timeout in seconds")
    parser.add_argument("-l", "--log", default="log.txt", help="Output Log file name")
    parser.add_argument("-mc", "--code", nargs='+', type=int, help="Shows status codes")

    args = parser.parse_args()

    scan_folders(args.url, args.wordlist, args.timeout, args.log, args.code)

if __name__ == "__main__":
    main()
