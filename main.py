from flask import Flask,render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)


def scrape_website1():
    url = 'https://careers.dana-farber.org/jobs/clinical-research/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    job_titles = soup.select('#job-list-section li a h3')
    job_links = soup.select('#job-list-section li a')
    job_location = soup.select('li dl div:nth-of-type(2) dd')
    job_description = soup.select('#job-list-section li dl p')
    BASE_URL = 'https://careers.dana-farber.org/'

    links = []
    titles = []
    location = []
    jobs = []

    for link in job_links:
        job_title = link.text
        job_url = link['href']
        

        if job_url.startswith('/'):
            job_url = BASE_URL + job_url
        
        for linkk in job_location:
            job_description = linkk.text

        job_data = {
            'title': job_title,
            'url': job_url,
            'location': job_description
        }

        jobs.append(job_data)
    
    return jobs


def scrape_website2():
    url = 'https://www.flexjobs.com/remote-jobs/clinical'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    id_titles = soup.select('a.kKkQRC')
    id_desc = soup.select('p.caAWyW')
    id_loc = soup.select('span.allowed-location')
    BASE_URL = 'https://careers.dana-farber.org/'

    jobs_indeed = []

    for link in id_titles:
        jobid_title = link.text

    for linkk in id_desc:
        jobid_desc = linkk.text

    for linkkk in id_loc:
        jobid_loc = linkkk.text

        jobid_data = {
            'title': jobid_title,
            'desc': jobid_desc,
            'loc': jobid_loc
        }

        jobs_indeed.append(jobid_data)

    return jobs_indeed

# def scrape_test_2():
#     indeed_jobs = scrape_website2()
#     print("Test Indeed Data")
#     for job in indeed_jobs:
#         print(job)

# scrape_test_2()

@app.route('/')
def display_jobs():
    jobs_website = scrape_website1()
    jobs_website_2 = scrape_website2()
    return render_template('jobs.html', jobs=jobs_website, jobs_indeed=jobs_website_2)



# @app.route('/indeed-route')
# def display_indeed():
#     indeed_jobs = scrape_website2()
#     return render_template('jobs.html', jobs_indeed=indeed_jobs)


if __name__ == "__main__":
    app.run(host='0.0.0', port=8000, debug=True)

