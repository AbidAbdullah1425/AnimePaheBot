#..........This Bot Made By [RAHAT](https://t.me/r4h4t_69)..........#
#..........Anyone Can Modify This As He Likes..........#
#..........Just one requests do not remove my credit..........#

#..........This Bot Made By [RAHAT](https://t.me/r4h4t_69)..........#
#..........Anyone Can Modify This As He Likes..........#
#..........Just one requests do not remove my credit..........#

import requests
import re
from bs4 import BeautifulSoup
from plugins.headers import session, pahewin_headers

def extract_kwik_link(pahe_url):
    """Extract Kwik.si link from pahe.win URL"""
    try:
        # Use session and headers from headers.py
        response = session.get(pahe_url, headers=pahewin_headers, timeout=10)
        response.raise_for_status()

        # Parse with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Look for the specific anchor tag with class 'redirect'
        redirect_link = soup.find('a', {'class': 'redirect', 'rel': 'nofollow'})
        
        if redirect_link and 'href' in redirect_link.attrs:
            kwik_url = redirect_link['href']
            if kwik_url.startswith('https://kwik.si/f/'):
                return kwik_url

        # Fallback: try regex if BeautifulSoup fails
        pattern = r'href="(https://kwik\.si/f/[^"]+)"[^>]*class="[^"]*redirect[^"]*"'
        match = re.search(pattern, response.text)
        if match:
            return match.group(1)

        raise Exception("Kwik link not found in the page")

    except requests.exceptions.RequestException as e:
        raise Exception(f"Error accessing pahe.win: {str(e)}")
    except Exception as e:
        raise Exception(f"Error extracting kwik link: {str(e)}")

def get_dl_link(kwik_url):
    """Extract direct download link from kwik.si"""
    try:
        # Use the same session but with referer set to pahe.win
        session.headers.update({'Referer': 'https://pahe.win/'})
        response = session.get(kwik_url, timeout=10)
        response.raise_for_status()

        # Parse with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Look for video source
        video_source = soup.find('source')
        if video_source and 'src' in video_source.attrs:
            return video_source['src']

        # Fallback: try regex
        pattern = r'source\s+src="([^"]+)"'
        match = re.search(pattern, response.text)
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

