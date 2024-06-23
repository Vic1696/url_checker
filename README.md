# URL Status Checker

This Python script checks the HTTP status of a list of URLs and saves the results in a CSV file. The script uses the `requests` library to perform the HTTP requests and the `concurrent.futures` library to handle multiple requests in parallel. The results are saved in a timestamped CSV file for future reference.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. **Install Python:**
   - Download and install Python from the [official website](https://www.python.org/downloads/). Make sure to check the box that says "Add Python to PATH" during installation.

2. **Install Required Library:**
   - Open a command prompt or terminal and run the following command to install the `requests` library:
     ```sh
     pip install requests
     ```

## Usage

1. **Prepare the URLs File:**
   - Create a file named `urls.txt` in the same directory as the script. Add the URLs you want to check, one per line. For example:
     ```
     https://www.google.com
     https://www.example.com
     https://nonexistent.website
     ```

2. **Run the Script:**
   - Save the script as `check_urls.py`:

   - Open a command prompt or terminal, navigate to the directory where `check_urls.py` is saved, and run the script:
     ```sh
     python check_urls.py
     ```

3. **Check the Results:**
   - The script will generate a CSV file with a name like `urls_status_20240623_101530.csv`, where the numbers represent the current date and time. This file will contain the URLs and their corresponding status codes.


