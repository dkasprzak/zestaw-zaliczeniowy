import threading
import requests

countries = ["Poland", "Germany", "Italy", "France", "Spain", "Switzerland", "Austria", "Belgium",
             "Canada", "India", "China", "San Marino", "Japan", "Australia", "United Kingdom"]

universities_by_country = {}

def fetch_universities(country):
    response = requests.get(f"http://universities.hipolabs.com/search?country={country}")
    if response.status_code == 200:
        data = response.json()
        universities = [university['name'] for university in data]
        universities_by_country[country] = universities
    else:
        universities_by_country[country] = []

threads = []

for country in countries:
    thread = threading.Thread(target=fetch_universities, args=(country,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(universities_by_country)