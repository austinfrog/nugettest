import requests
import json

# Number of packages to fetch
number_of_packages = 800

# NuGet API endpoint for searching packages
api_url = f'https://api-v2v3search-0.nuget.org/query?q=&skip=0&take={number_of_packages}&prerelease=false&semVerLevel=2.0.0'

def fetch_package_names(url):
    response = requests.get(url)
    if response.status_code == 200:
        packages = response.json()["data"]
        return [pkg["id"] for pkg in packages]
    else:
        print("Failed to fetch data")
        return []

def save_to_file(packages, filename='packages.txt'):
    with open(filename, 'w') as file:
        for pkg in packages:
            file.write(f"{pkg}\n")

packages = fetch_package_names(api_url)
save_to_file(packages)

