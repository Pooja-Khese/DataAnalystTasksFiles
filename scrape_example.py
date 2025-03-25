# Import necessary libraries
from bs4 import BeautifulSoup
import requests

# Step 1: Send a GET request to the website
url = 'https://example.com'  # Replace with the website you want to scrape
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("Successfully connected to the website!")
else:
    print(f"Failed to retrieve the website. Status code: {response.status_code}")
    exit()

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Extract specific data
# Example: Find all 'h2' tags (usually article titles)
titles = soup.find_all('h2')

# Step 4: Display the extracted data
print("Article Titles:")
for title in titles:
    print(title.text.strip())

# Save the data to a file (optional)
with open('scraped_data.txt', 'w') as file:
    for title in titles:
        file.write(title.text.strip() + '\n')

print("\nData has been saved to scraped_data.txt")
