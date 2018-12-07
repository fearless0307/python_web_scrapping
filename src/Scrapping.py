'''
    Web Scrapping
    It's print the table which is in the link
    "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India".
    It use Urllib library for fetch the html content from URL.
    It use BeautifulScup library for find out the content of table.
    It use PrettyTable library for show the content from url in tabular format.
'''

import urllib.request
from bs4 import BeautifulSoup
import json
from prettytable import PrettyTable

# specify the url
wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

# Query the website and return the html to the variable 'page'
page = urllib.request.urlopen(wiki)

# Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(page, 'html.parser')

right_table = soup.find('table', {"class": 'wikitable'})

# Generate lists
A = []
B = []
C = []
D = []
E = []
F = []
G = []
for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    states = row.findAll('th')  # To store second column data
    if len(cells) == 5:  # Only extract table body not heading
        A.append(str(states[0].find(text=True)).replace("\n", ""))
        B.append(str(states[1].find(text=True)).replace("\n", ""))
        C.append(str(cells[0].find(text=True)).replace("\n", ""))
        D.append(str(cells[1].find(text=True)).replace("\n", ""))
        E.append(str(cells[2].find(text=True)).replace("\n", ""))
        F.append(str(cells[3].find(text=True)).replace("\n", ""))
        G.append(str(cells[4].find(text=True)).replace("\n", ""))

x = {"Num": "", "State": "", "Administrative": "", "Legislative": "", "Judiciary": "", "Year": "", "Former": ""}
y = []
with open('list.json', 'w') as File:
    for index in range(len(A)):
        x["Num"] = A[index]
        x["State"] = B[index]
        x["Administrative"] = C[index]
        x["Legislative"] = D[index]
        x["Judiciary"] = E[index]
        x["Year"] = str(F[index])
        x["Former"] = G[index]
        y.append(x.copy())
    json.dump(y, File)

# Open the file for reading
with open('list.json', 'r') as File:
    z = json.load(File)

# Close the file
File.close()

# create table
table = PrettyTable()

table.field_names = ["S.no.", "State or Union", "Administrative", "Legislative", "Judiciary", "Year", "Former"]
for index_t in range(len(z)):
    table.add_row([z[index_t]["Num"], z[index_t]["State"], z[index_t]["Administrative"], z[index_t]["Legislative"],
                   z[index_t]["Judiciary"], z[index_t]["Year"], z[index_t]["Former"]])

print(table.get_string())
