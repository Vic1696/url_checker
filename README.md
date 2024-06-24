# URL Status Checker

This project is a Flask-based web application that allows you to upload a file containing URLs, checks the status of each URL, and generates a CSV file with the results. The results file is dynamically named based on the original file name and the current timestamp.

## Features

- Upload a file containing URLs.
- Check the status of each URL.
- Generate a CSV file with the status results.
- Dynamically name the results file based on the original file name.
- Styled web interface using Tailwind CSS with a dark theme.

## Requirements

- Python 3.x
- Flask
- Requests

## Setup Instructions

1. **Clone the Repository**: 
   ```sh
   git clone git@github.com:Vic1696/url_checker.git
   cd url-status-checker

2. **Install Dependencies**:
   ```sh
   pip install flask requests

3. **Run the Application**:
   ```sh
   python3 check_urls.py

4. **Open the Web Interface**:
   Open a web browser and go to http://127.0.0.1:5000.

## Usage
- __Upload a File__: Use the web interface to upload a file containing URLs (one URL per line).
- __Check Status__: Click the "Check Status" button to process the URLs.
- __Download Results__: The application will generate a CSV file with the status of each URL. The file name will be based on the original file name and the current timestamp.

## Notes
- This application is intended for development and testing purposes. For production deployment, use a production WSGI server.
- Ensure that the uploaded file is properly formatted (one URL per line) for accurate results.