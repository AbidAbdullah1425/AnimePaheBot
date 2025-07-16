
#..........This Bot Made By [RAHAT](https://t.me/r4h4t_69)..........#
#..........Anyone Can Modify This As He Likes..........#
#..........Just one requests do not remove my credit..........#

import requests
import re
from urllib.parse import unquote
from plugins.headers import session, pahewin_headers

def extract_kwik_link(pahe_url):
    """Extract Kwik.si link from pahe.win URL"""
    try:
        # Using headers from headers.py
        response = session.get(pahe_url, headers=pahewin_headers, timeout=10)
        response.raise_for_status()
        
        # Try multiple patterns to find the kwik link
        patterns = [
            r'https://kwik\.si/f/[a-zA-Z0-9]+(?=["\'])',
            r'href="(https://kwik\.si/f/[^"]+)"',
            r"https://kwik\.si/f/\w+"
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, response.text)
            if matches:
                return matches[0]
        
        raise Exception("Kwik link not found in the page")
        
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error extracting kwik link: {str(e)}")
    except Exception as e:
        raise Exception(f"Unexpected error: {str(e)}")












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

