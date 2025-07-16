#..........This Bot Made By [RAHAT](https://t.me/r4h4t_69)..........#
#..........Anyone Can Modify This As He Likes..........#
#..........Just one requests do not remove my credit..........#

from plugins.headers import session  # Use your session with headers!
from bs4 import BeautifulSoup

def extract_kwik_link(url):
    try:
        resp = session.get(url)
        resp.raise_for_status()

        soup = BeautifulSoup(resp.text, 'html.parser')
        button = soup.find("a", class_="btn btn-secondary btn-block redirect")
        if button and button.has_attr("href"):
            return button["href"]
        return "No kwik.si link found in the page."
    except Exception as e:
        return f"Error extracting kwik link: {str(e)}"




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

