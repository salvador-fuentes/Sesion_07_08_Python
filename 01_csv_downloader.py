#Download a CVS data set from an URL using requests
import requests

base_url = 'https://galileoguzman.com/data/articles_data_homeproject.csv'

response = requests.get(base_url)
response.raise_for_status()

response_content = response.content
filename = 'datasets/articles_data_homeproject.csv'

with open(filename, 'wb') as csv_file:
    csv_file.write(response_content)

print('file downloaded =)')
