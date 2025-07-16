#..........This Bot Made By [RAHAT](https://t.me/r4h4t_69)..........#
#..........Anyone Can Modify This As He Likes..........#
#..........Just one requests do not remove my credit..........#

import requests
import re
import time
from urllib.parse import unquote
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from plugins.headers import session, pahewin_headers

class KwikExtractor:
    def __init__(self):
        self.session = self._create_session_with_retries()
        
    def _create_session_with_retries(self):
        session = requests.Session()
        retries = Retry(
            total=3,
            backoff_factor=0.1,
            status_forcelist=[500, 502, 503, 504, 403],
        )
        session.mount('http://', HTTPAdapter(max_retries=retries))
        session.mount('https://', HTTPAdapter(max_retries=retries))
        return session

    def _handle_rate_limit(self, response):
        if response.status_code == 403:
            time.sleep(5)
            return True
        return False

    def extract_kwik_link(self, pahe_url):
        """Extract Kwik.si link from pahe.win URL"""
        try:
            # Using headers from headers.py
            response = self.session.get(pahe_url, headers=pahewin_headers, timeout=10)
            
            if self._handle_rate_limit(response):
                response = self.session.get(pahe_url, headers=pahewin_headers, timeout=10)
            
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

    def get_pahe_url(self, anime_id, episode):
        """Get pahe.win URL for a specific anime episode"""
        try:
            api_url = f"https://animepahe.ru/api?m=release&id={anime_id}&sort=episode_asc&page=1"
            response = self.session.get(api_url, headers=session.headers)
            
            if self._handle_rate_limit(response):
                response = self.session.get(api_url, headers=session.headers)
            
            data = response.json()
            
            for ep in data.get('data', []):
                if str(ep.get('episode')) == str(episode):
                    return f"https://pahe.win/{ep.get('session')}"
            
            raise Exception(f"Episode {episode} not found")
            
        except Exception as e:
            raise Exception(f"Error getting pahe URL: {str(e)}")

    async def process_anime_request(self, anime_id, episode):
        """Main function to process anime request and return kwik link"""
        try:
            # Get pahe.win URL
            pahe_url = self.get_pahe_url(anime_id, episode)
            
            # Extract kwik link
            kwik_url = self.extract_kwik_link(pahe_url)
            
            return kwik_url
            
        except Exception as e:
            raise Exception(f"Error processing anime request: {str(e)}")

# Create a single instance to be used by the bot
kwik_extractor = KwikExtractor()












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

