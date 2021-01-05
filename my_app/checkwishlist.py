import requests
import re
from bs4 import BeautifulSoup
"""
URL1 = 'https://www.nike.com/t/air-force-1-07-mens-shoe-5QFp5Z/CW2288-111'
URL2 = 'https://www.nike.com/t/react-infinity-run-flyknit-mens-running-shoe-zX42Nc/CD4371-401' # let users input this
URLs = [URL1,URL2]
expectedPriceList = [80,140]
"""
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

def get_symbol(price):
    pattern =  r'(\D*)[\d\,\.]+(\D*)'
    g = re.match(pattern, price.strip()).groups()
    return (g[0] or g[1]).strip()

def check_price(URL,expectedPrice):
    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, features='html.parser')

    if (soup.find(id="pdp_product_title") is None):
        print("  Can\'t find the item you are looking for!")
        return  

    title = soup.find(id="pdp_product_title").get_text()

    originalPrice = 0.0
    discountPrice = 0.0
    
    discountPriceList = soup.findAll("div", {"data-test": "product-price-reduced"})
    if discountPriceList != []:
        discountPriceWithSymbol = discountPriceList[0].get_text()
        price = discountPriceWithSymbol.replace(get_symbol(discountPriceWithSymbol),'')
        discountPrice = float(price)

    originalPriceList = soup.findAll("div", {"data-test": "product-price"})
    if originalPriceList != []:
        OriginalPriceWithSymbol = originalPriceList[0].get_text()        
        price = OriginalPriceWithSymbol.replace(get_symbol(OriginalPriceWithSymbol),'')
        originalPrice = float(price)
    
    print(" ",title.strip())
    if discountPrice != 0:
        print("  Discount Price -", discountPrice)
    else:
        print("  This item has no discount price!")

    if originalPrice != 0:   
        print("  Original Price -", originalPrice)
    else:
        print("  Original price cannot be found!")
    
    if((discountPrice != 0 and discountPrice <= expectedPrice) or (originalPrice != 0 and originalPrice <= expectedPrice)): #let users input the price that they want it to be less than or equal
        send_email()
    else:
        print("  The price is still more than your expected price -", str(expectedPrice) + "!")

def send_email():
    print("  Email has been sent!")

"""
#check_price("")
for i in range(len(URLs)):
    print("Item", (i+1))
    check_price(URLs[i],expectedPriceList[i])
"""