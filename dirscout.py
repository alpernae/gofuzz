import argparse
import requests
from termcolor import colored

def scan_folders(base_url, wordlist_file, timeout, log_file):
    with open(wordlist_file, 'r') as f:
        wordlist = f.read().splitlines()

    try:
        with open(log_file, 'w') as log:
            print("\n\nScanning Started!\n")  # Tarama başladığında mesajı ekrana yazdır
            for folder in wordlist:
                target_url = f"{base_url}/{folder}"
                try:
                    response = requests.get(target_url, timeout=timeout)
                    status_code = response.status_code
                except requests.Timeout:
                    status_code = "Timeout"

                result = f"[{colored(status_code, 'green' if status_code == 200 else 'red')}] - {folder}\n"
                log.write(result)
                print(result.strip())
    except KeyboardInterrupt:
        pass  # KeyboardInterrupt hatasını yakala ve sessizce çık

def main():
    parser = argparse.ArgumentParser(description="Web folder scanning tool")
    parser.add_argument("-u", "--url", required=True, help="Base URL to scan")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to the wordlist file")
    parser.add_argument("-t", "--timeout", type=float, default=5, help="Request timeout in seconds")
    parser.add_argument("-l", "--log", default="log.txt", help="Log file name")

    args = parser.parse_args()

    scan_folders(args.url, args.wordlist, args.timeout, args.log)

if __name__ == "__main__":
    main()
