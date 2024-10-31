import os
im
from bs4 import BeautifulSoup
import requests
from google.oauth2.credentials import Credentials
from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime


class WebScraperToSheets:
    def __init__(self, credentials_file):
        """
        Initialize the scraper with Google Sheets credentials
        """
        self.SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        self.credentials = service_account.Credentials.from_service_account_file(
            credentials_file, scopes=self.SCOPES)
        self.sheets_service = build('sheets', 'v4', credentials=self.credentials)

    def extract_page_info(self, url):
        """
        Extract title and featured image from a webpage
        """
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Get title
            title = soup.title.string if soup.title else ''
            
            # Try different methods to find featured image
            featured_image = ''
            
            # Method 1: Open Graph image
            og_image = soup.find('meta', property='og:image')
            if og_image:
                featured_image = og_image.get('content', '')
            
            # Method 2: Article featured image
            if not featured_image:
                img = soup.find('img', class_=['featured', 'wp-post-image', 'attachment-featured'])
                if img:
                    featured_image = img.get('src', '')
            
            # Method 3: First significant image
            if not featured_image:
                images = soup.find_all('img')
                for img in images:
                    src = img.get('src', '')
                    if src and not src.endswith(('.gif', '.ico')) and 'logo' not in src.lower():
                        featured_image = src
                        break
            
            return {
                'url': url,
                'title': title.strip() if title else '',
                'featured_image': featured_image,
                'date_extracted': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            
        except Exception as e:
            print(f"Error extracting data from {url}: {str(e)}")
            return {
                'url': url,
                'title': 'ERROR',
                'featured_image': str(e),
                'date_extracted': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }

    def update_sheet(self, spreadsheet_id, range_name, data):
        """
        Update Google Sheet with extracted data
        """
        try:
            values = [[
                data['url'],
                data['title'],
                data['featured_image'],
                data['date_extracted']
            ]]
            
            body = {
                'values': values
            }
            
            result = self.sheets_service.spreadsheets().values().append(
                spreadsheetId=spreadsheet_id,
                range=range_name,
                valueInputOption='RAW',
                insertDataOption='INSERT_ROWS',
                body=body
            ).execute()
            
            return result
            
        except Exception as e:
            print(f"Error updating sheet: {str(e)}")
            return None

def main():
    # Configuration
    CREDENTIALS_FILE = '../google.json'  # Google Sheets API credentials
    SPREADSHEET_ID = '191239RoyhDxHCpQMj7woXZx5DDbpAWbtlyW6Sc2xYxE'  # Get this from the Google Sheets URL
    RANGE_NAME = 'Sheet1!A:D'  # Adjust according to your sheet name and desired range
    
    # Initialize scraper
    scraper = WebScraperToSheets(CREDENTIALS_FILE)
    
    # Example URLs to scrape
    urls = [
        'https://example.com/page1',
        'https://example.com/page2',
        # Add more URLs as needed
    ]
    
    # Process each URL
    for url in urls:
        print(f"Processing {url}...")
        data = scraper.extract_page_info(url)
        result = scraper.update_sheet(SPREADSHEET_ID, RANGE_NAME, data)
        
        if result:
            print(f"Successfully updated sheet with data from {url}")
        else:
            print(f"Failed to update sheet with data from {url}")

if __name__ == "__main__":
    