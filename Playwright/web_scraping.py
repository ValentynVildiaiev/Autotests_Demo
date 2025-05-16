import requests
from bs4 import BeautifulSoup

base_url = "https://congenial-pancake-q7qx9g7qwqp5c4q66-8000.app.github.dev"

response = requests.get(f"{base_url}/venues")

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
parsed_data = parse_data_from_table(table)

for key,items in parsed_data.items():
    seen = set()
    for value in items:
        if value in seen:
            print(f"Found possible duplicate at: {key}. It contains value: {value}")
        seen.add(value)
print(parsed_data)