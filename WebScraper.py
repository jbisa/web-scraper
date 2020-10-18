from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

# Create a csv file to write results
fileName = "results/ProductData.csv"
f = open(fileName, "w")
headers = "Brand, ProductName, ShippingPrice\n"
f.write(headers)

# Now hit the desired URL and extract the data you need
pageNumber = 1
while(pageNumber < 101):
    url = "https://www.newegg.com/p/pl?d=graphics+cards&page=" + str(pageNumber)

    # Open HTTP client and grab page
    uClient = urlopen(url)
    htmlPage = uClient.read()

    # Close HTTP client
    uClient.close()

    # Parse HTML
    soupPage = soup(htmlPage, "html.parser")

    # Get all relevant info from web page
    cells = soupPage.findAll("div", { "class": "item-cell" })

    # Loop through info and only keep track of data points we care about
    for cell in cells:
        if cell.div["class"] == ['item-container']:
            try:
                brand = cell.div.div.a.img["title"].replace(",", "")
            except:
                brand = "N/A"

            productName = cell.findAll("a", { "class": "item-title" })[0].text.replace(",", "|") or "N/A"
            
            shippingPrice = cell.findAll("li", { "class" : "price-ship"})[0].text.strip() or "N/A"
            
            print("\n-----------------------------------------")
            print("Brand: " + brand)
            print("Product Name: " + productName)
            print("Shipping Price: " + shippingPrice)
            print("-----------------------------------------\n")
            
            f.write(brand + "," + productName + "," + shippingPrice + "\n")

    pageNumber += 1

f.close()