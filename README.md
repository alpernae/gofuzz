# GoFuzz - Fuzzing Tool

GoFuzz is a lightweight Python-based web directory scanning tool designed to help security professionals and web administrators identify potential vulnerabilities in websites. By systematically testing different directory paths and filenames, GoFuzz assists in the discovery of hidden or unprotected content that could pose security risks. With its simplicity and versatility, GoFuzz is a valuable addition to any web security toolkit, aiding in the enhancement of web application security by pinpointing areas that may require additional protection.

## Download and Installation

1. Clone this repository to your local machine or download it as a ZIP file.

    ```
    git clone https://github.com/alpernae/gofuzz.git
    ```

2. Install Python (if not already installed): [Python Download Page](https://www.python.org/downloads/)

3. Install the required dependencies by running the following command:

    ```
    pip install -r requirements.txt
    ```

## Usage

You can use GoFuzz as follows:

`python gofuzz.py -u <target_url> -w <wordlist_file> -t <timeout> -l <log_name>`


Parameters:

- `-u` or `--url`: URL of the target website to scan.
- `-w` or `--wordlist`: Path to the wordlist file to be used by the scanner.
- `-t` or `--timeout`: Timeout duration for requests (default is 5 seconds).
- `-l` or `--log`: Specifies the name of a log file to save scan results (default: log.txt).
- `-c` or `--cookies`: Specifies custom cookies to include in requests.
- `-mc` or `--code`: Specifies example response codes to display (e.g., "200,404").

Example:

`python gofuzz.py -u https://example.com -w wordlist.txt -t 10 -l my_log.txt`


## Contributions

Contributions are welcome. Please report issues or make pull requests!

## License

This project is licensed under the MIT License. For more information, see the [LICENSE](LICENSE) file.
