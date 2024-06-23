import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import csv
from datetime import datetime

# Check the status of single URL
def check_url(url):
    try:
        response = requests.get(url, timeout=10)
        return url, response.status_code
    except requests.RequestException as e:
        return url, None
    
# Check multiple urls using ThreadPoolExecutor
def check_urls(urls, max_workers=10):
    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_url = {executor.submit(check_url, url): url for url in urls}
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                result = future.result()
            except Exception as exc:
                result = (url,None)
            results.append(result)
    return results

# Read URLS from a file (one URL/line)
with open('urls.txt','r') as file:
    urls = [line.strip() for line in file]

#Check the status of URLs
results = check_urls(urls, max_workers=20)

#Get date and time for the CSV filename
now = datetime.now()
timestamp = now.strftime("%Y%m%d_%H%M%S")

#Save results to a csv file
csv_filename = f"urls_status_{timestamp}.csv"
with open(csv_filename, 'w', newline='') as csvfile:
    fieldnames = ['URL', 'Status']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for url, status in results:
        writer.writerow({'URL': url, "Status": status})

print(f"Results saved to {csv_filename}")