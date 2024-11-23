import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
import argparse
import json
import os

BANNER = """
   
  _____ _                 _ ______     _______  
 / ____| |               | |  _ \ \   / /  __ \ 
| |    | | ___  _   _  __| | |_) \ \_/ /| |__) |
| |    | |/ _ \| | | |/ _` |  _ < \   / |  ___/ 
| |____| | (_) | |_| | (_| | |_) | | |  | |     
 \_____|_|\___/ \__,_|\__,_|____/  |_|  |_|     
                                                
                CloudBYP - Cloudflare Bypass
		Version: 1.1
		Author: G4UR4V007
A tool to find the origin IP of a Cloudflare-protected website using Censys.
"""

CONFIG_FILE = "config.json"

def load_config():
    """
    Load API credentials from the config file.
    Returns:
        tuple: (api_id, api_secret) if found, otherwise (None, None).
    """
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                config = json.load(f)
                return config.get("api_id"), config.get("api_secret")
        except Exception as e:
            print(f"Error reading config file: {e}")
    return None, None

def get_cloudflare_exposed_ips(domain, api_id, api_secret):
    url = "https://search.censys.io/api/v2/hosts/search"
    headers = {
        "Accept": "application/json"
    }
    params = {
        "q": f"{domain}",
        "per_page": 100
    }

    ip_addresses = []
    page = 1

    while True:
        response = requests.get(url, headers=headers, params=params, auth=HTTPBasicAuth(api_id, api_secret))

        if response.status_code != 200:
            print(f"Error: Received status code {response.status_code}")
            print("Response:", response.text)
            break

        data = response.json()

        if "result" in data and "hits" in data["result"]:
            hits = data["result"]["hits"]
            if not hits:
                print("No IP addresses found.")
                break

            for hit in hits:
                if "ip" in hit:
                    ip = hit["ip"]
                    formatted_ip = f"http://{ip}/"
                    title = fetch_site_title(ip)
                    ip_addresses.append(f"{formatted_ip} - {title}")

            if page >= data["result"]["total"] // 100 + 1:
                break

            page += 1
            params["page"] = page
        else:
            print("Error: 'hits' key not found in the response.")
            print("Response:", json.dumps(data, indent=2))
            break

    return ip_addresses

def fetch_site_title(ip):
    try:
        response = requests.get(f"http://{ip}")
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            title_tag = soup.find('title')
            if title_tag:
                return title_tag.get_text(strip=True)
    except Exception as e:
        print(f"Error fetching title from {ip}: {e}")
    
    return "No title found"

def main():
    print(BANNER)
    
    parser = argparse.ArgumentParser(description="Extract Cloudflare-exposed IP addresses and site titles for a domain.")
    parser.add_argument("domain", help="The domain to search for.")
    parser.add_argument("--api-id", help="Censys API ID.")
    parser.add_argument("--api-secret", help="Censys API secret.")
    parser.add_argument("--output", help="Output file.", default=None)
    args = parser.parse_args()

    # Load API credentials from config file
    config_api_id, config_api_secret = load_config()

    # Use CLI arguments if provided, otherwise fallback to config file
    api_id = args.api_id if args.api_id else config_api_id
    api_secret = args.api_secret if args.api_secret else config_api_secret

    if not api_id or not api_secret:
        print("Error: API ID and API Secret are required. Please provide them via arguments or a config file.")
        return

    ip_addresses = get_cloudflare_exposed_ips(args.domain, api_id, api_secret)

    if ip_addresses:
        if args.output:
            with open(args.output, "w") as f:
                for entry in ip_addresses:
                    f.write(entry + "\n")
            print(f"IP addresses and titles saved to {args.output}")
        else:
            print("IP addresses and titles:")
            for entry in ip_addresses:
                print(entry)
    else:
        print("No IP addresses found.")

if __name__ == "__main__":
    main()
