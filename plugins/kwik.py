#..........This Bot Made By [RAHAT](https://t.me/r4h4t_69)..........#
#..........Anyone Can Modify This As He Likes..........#
#..........Just one requests do not remove my credit..........#

import requests
import re
import time
from urllib.parse import unquote
from plugins.headers import session, pahewin_headers
import cloudscraper

def extract_kwik_link(pahe_url):
    """Extract Kwik.si link from pahe.win URL"""
    try:
        # Create a cloudscraper session to bypass protection
        scraper = cloudscraper.create_scraper(
            browser={
                'browser': 'chrome',
                'platform': 'windows',
                'mobile': False
            }
        )
        
        # Copy headers to scraper
        scraper.headers.update(pahewin_headers)
        
        # Try multiple times with delay
        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = scraper.get(pahe_url, timeout=10)
                response.raise_for_status()
                
                # Try multiple patterns to find the kwik link
                patterns = [
                    r'https://kwik\.si/f/[a-zA-Z0-9]+',
                    r'href="(https://kwik\.si/f/[^"]+)"',
                    r'"(https://kwik\.si/f/[^"]+)"'
                ]
                
                for pattern in patterns:
                    matches = re.findall(pattern, response.text)
                    if matches:
                        # Return the first match, stripped of any quotes
                        kwik_url = matches[0]
                        if isinstance(kwik_url, tuple):
                            kwik_url = kwik_url[0]
                        return kwik_url.strip('"')
                
                # If we get here and haven't found a link, try parsing JavaScript
                script_pattern = r'muzixagosi.*?href.*?\"(https://kwik\.si/f/[^\"]+)\"'
                script_match = re.search(script_pattern, response.text, re.DOTALL)
                if script_match:
                    return script_match.group(1)
                
                # If no link found, wait before retry
                if attempt < max_retries - 1:
                    time.sleep(6)
                    continue
                    
            except requests.exceptions.RequestException:
                if attempt < max_retries - 1:
                    time.sleep(6)
                    continue
                raise
        
        raise Exception("Kwik link not found in the page")
        
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error accessing pahe.win: {str(e)}")
    except Exception as e:
        raise Exception(f"Error extracting kwik link: {str(e)}")

def get_dl_link(kwik_url):
    """Extract direct download link from kwik.si"""
    try:
        scraper = cloudscraper.create_scraper(
            browser={
                'browser': 'chrome',
                'platform': 'windows',
                'mobile': False
            }
        )
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Referer': 'https://pahe.win/',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
        }
        
        scraper.headers.update(headers)
        
        # Get the kwik.si page
        response = scraper.get(kwik_url)
        response.raise_for_status()
        
        # Try to find the direct download link
        # This pattern might need adjustment based on kwik.si's current structure
        dl_pattern = r'source src="([^"]+)"'
        match = re.search(dl_pattern, response.text)
        
        if match:
            return match.group(1)
        
        raise Exception("Direct download link not found")
        
    except Exception as e:
        raise Exception(f"Error getting download link: {str(e)}")












'''import requests
from bs4 import BeautifulSoup
import re

# Function to extract kwik link
def extract_kwik_link(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Ensure we got a valid response

        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all <script> tags
        script_tags = soup.find_all('script', type="text/javascript")
        for script in script_tags:            
            match = re.search(r'https://kwik\.si/f/[\w\d]+', script.text)
            if match:
                return match.group(0)
        
        return "No kwik.si link found in the page."
    
    except Exception as e:
        return f"Error extracting kwik link: {str(e)}"'''

