import requests
from bs4 import BeautifulSoup

base_url = "https://congenial-pancake-q7qx9g7qwqp5c4q66-8000.app.github.dev"

response = requests.get(f"{base_url}/gigs")
soup = BeautifulSoup(response.text, "html.parser")


def parse_data_from_table(table):
    headers = []
    for header in table.find_all("th"):
        headers.append(header.text.strip())

    results_dict = {header: [] for header in headers}
    for row in table.find_all("tr"):
        cells = row.find_all("td")
        for index, cell in enumerate(cells):
            results_dict[headers[index]].append(cell.text)

    return results_dict


table = soup.find("table")

table_data = parse_data_from_table(table)
print(table_data)

response = requests.get(f"{base_url}/filter_gigs?filter=past")
soup = BeautifulSoup(response.text, "html.parser")
table = soup.find("table")

table_data = parse_data_from_table(table)
print(table_data)
