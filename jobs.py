import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'particular-job-portal-website-url'

page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')

job_title = []
company_nam = []
location = []
jobexperience = []

jobs = soup.find_all('li', class_='search_listing')

for job in jobs:
	job_title.append(job.find('li', class_="cls_jobtitle").text.strip())
	company_nam.append(job.find('li', class_="cls_jobcompany").text.strip())
	location.append(job.find('li', class_="jobList-year-loc").find('em', class_="snp_loc").text.strip())
	jobexperience.append(job.find('li', class_="jobList-year-loc").find('span', class_="cls_jobexperience").text.strip())

 
data = pd.DataFrame({'Job Title': job_title,'Company Name': company_nam, 'Location' : location, 'Experience': jobexperience})
data.to_csv('jobs.csv', index=False, encoding='utf-8')

	# print(product, end='\n'*2)