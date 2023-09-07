#!/usr/bin/env python

import argparse
import requests
from termcolor import colored
import warnings
import datetime
import sys
import signal
import os

# Tüm uyarıları kapat
warnings.filterwarnings("ignore")

# Global değişkenler
stop_scan = False

def scan_folders(base_url, wordlist_file, timeout, log_file, example_codes, cookies):
    global stop_scan
    
    with open(wordlist_file, 'r') as f:
        wordlist = f.read().splitlines()
    
    total_urls = len(wordlist)
    
    try:
        with open(log_file, 'w') as log:
            print("""\n\n

░██████╗░░█████╗░███████╗██╗░░░██╗███████╗███████╗
██╔════╝░██╔══██╗██╔════╝██║░░░██║╚════██║╚════██║
██║░░██╗░██║░░██║█████╗░░██║░░░██║░░███╔═╝░░███╔═╝
██║░░╚██╗██║░░██║██╔══╝░░██║░░░██║██╔══╝░░██╔══╝░░
╚██████╔╝╚█████╔╝██║░░ v.1.0.0#stable ░░░╚██████╔╝███████╗███████╗
░╚═════╝░░╚════╝░╚═╝░░░░░░╚═════╝░╚══════╝╚══════╝

Developer: @alpernae
Web: https://github.com/alpernae/gofuzz\n""")
            print( "\n" + colored("[!]", 'yellow') + " Scanning Started!\n")
            for index, fuzz in enumerate(wordlist, start=1):
                target_url = f"{base_url}/{fuzz}"

                try:
                    headers = {'Cookie': cookies} if cookies else {}
                    response = requests.get(target_url, timeout=timeout, headers=headers)
                    status_code = response.status_code
                    response_text = response.text
                except requests.Timeout:
                    status_code = "Timeout"
                    response_text = ""

                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                if should_show_status(status_code, example_codes, response_text):
                    print_status(timestamp, target_url, status_code)
                    log_status(log, timestamp, target_url, status_code)
                
                # Tarama sürecinin ilerlemesini ve çubuğu göster
                progress_percentage = (index / total_urls) * 100
                remaining_percentage = 100 - progress_percentage
                print_progress_bar(progress_percentage)
                
                if stop_scan:
                    print("\n\nScan Stopped.")
                    break
                
    except KeyboardInterrupt:
        print("\n\nScan Stopped.")
        sys.exit(0)

def should_show_status(status_code, example_codes, response_text):
    return (not example_codes or status_code in example_codes) and ("404 Not Found" not in response_text)

def print_status(timestamp, url, status_code):
    status_color = 'green' if status_code == 200 else 'yellow' if status_code != "Timeout" else 'red'
    status_text = "Timeout" if status_code == "Timeout" else str(status_code)
    result = f" [{colored(timestamp, 'green')}] - {colored('[STATUS CODE]', 'white')} [{colored(status_text, status_color)}] - {colored(url, 'cyan')}"
    print(result)

def log_status(log, timestamp, url, status_code):
    status_text = "Timeout" if status_code == "Timeout" else str(status_code)
    result = f"{url}\n"
    log.write(result)

def print_progress_bar(progress):
    sys.stdout.write("\r")
    sys.stdout.write(f"[{progress:.2f}%]")
    sys.stdout.flush()

def stop_scan_prompt():
    global stop_scan
    stop_scan = True
    print("\n\nScanning is being stopped. To completely terminate the scan, press 'q'.")
    while True:
        choice = input("To continue, press 'c'. To exit the scan, press 'q': ").strip().lower()
        if choice == 'q':
            print("\nScan terminated.")
            sys.exit(0)
        elif choice == 'c':
            print("\nScan is continuing...")
            stop_scan = False
            return
        else:
            print("Invalid choice. Please select 'c' to continue or 'q' to exit.")

def signal_handler(sig, frame):
    global stop_scan
    if stop_scan:
        print("\nScan successfully terminated.")
        sys.exit(0)
    else:
        print(colored("\n\nScan is being stopped. To completely terminate the scan, press 'q'. To continue, press 'c'.", 'red'))
        choice = input().strip().lower()
        if choice == 'q':
            print("\nScan terminated.")
            sys.exit(0)
        elif choice == 'c':
            print("\nScan is continuing...")
            stop_scan = False

def sigtstp_handler(sig, frame):
    print("\nScan terminated by Ctrl + Z.")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTSTP, sigtstp_handler)

def main():
    global stop_scan
    parser = argparse.ArgumentParser(description=
"""
GoFuzz -  Fuzzing Tool

"""
)
    parser.add_argument("-u", "--url", required=True, help="Base URL to scan")
    parser.add_argument("-w", "--wordlist", default="wordlist/default.txt", help="Path to the wordlist file")
    parser.add_argument("-t", "--timeout", type=float, default=1, help="Request timeout in seconds")
    parser.add_argument("-l", "--log", default="log.txt", help="Output Log file name")
    parser.add_argument("-c", "--cookies", default="", help="Custom cookies to include in requests")
    parser.add_argument("-mc", "--code", default="", help="Example status codes to show (e.g., 200,404)")

    args = parser.parse_args()

    if args.code:
        example_codes = args.code.split(',')
    else:
        example_codes = []

    scan_folders(args.url, args.wordlist, args.timeout, args.log, example_codes, args.cookies)

    if not stop_scan:
        stop_scan_prompt()

if __name__ == "__main__":
    main()
