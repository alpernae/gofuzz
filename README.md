# DirScout - Fuzzing Tool

DirScout is a simple Python-based tool that scans directories of websites.

## Download and Installation

1. Clone this repository to your local machine or download it as a ZIP file.

    ```
    git clone https://github.com/alpernae/dirscout.git
    ```

2. Install Python (if not already installed): [Python Download Page](https://www.python.org/downloads/)

3. Install the required dependencies by running the following command:

    ```
    pip install -r requirements.txt
    ```

## Usage

You can use DirScout as follows:

```
python dirscout.py -u <target_url> -w <wordlist_file> -t <timeout> -l <log_name>
```

Parameters:

- `-u` or `--url`: URL of the target website to scan.
- `-w` or `--wordlist`: Path to the wordlist file to be used by the scanner.
- `-t` or `--timeout`: Timeout duration for requests (default is 5 seconds).
- `-l`: Name of the log name where scan results will be saved (default is "logs").

Example:

```
python dirscout.py -u https://example.com -w wordlist.txt -t 10 -l my_log.txt
```

## Contributions

Contributions are welcome. Please report issues or make pull requests!

## License

This project is licensed under the MIT License. For more information, see the [LICENSE](LICENSE) file.
