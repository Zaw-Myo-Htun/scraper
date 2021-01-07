import requests,re,smtplib
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
    pattern = r'(\D*)[\d\,\.]+(\D*)'
    g = re.match(pattern, price.strip()).groups()
    return (g[0] or g[1]).strip()

def check_price(url, expectedPrice, messageBody):
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, features='html.parser')

    if (soup.find(id="pdp_product_title") is None):
        print("  Can\'t find the item you are looking for!")
        return

    title = soup.find(id="pdp_product_title").get_text()
    messageBody += title.strip() + "\n"

    originalPrice = 0.0
    discountPrice = 0.0

    discountPriceList = soup.findAll(
        "div", {"data-test": "product-price-reduced"})
    if discountPriceList != []:
        discountPriceWithSymbol = discountPriceList[0].get_text()
        price = discountPriceWithSymbol.replace(
            get_symbol(discountPriceWithSymbol), '')
        discountPrice = float(price)

    originalPriceList = soup.findAll("div", {"data-test": "product-price"})
    if originalPriceList != []:
        OriginalPriceWithSymbol = originalPriceList[0].get_text()
        price = OriginalPriceWithSymbol.replace(
            get_symbol(OriginalPriceWithSymbol), '')
        originalPrice = float(price)

    print(" ", title.strip())
    if discountPrice != 0:
        messageBody += "  Discount Price - " + str(discountPrice) + "\n"
        print("  Discount Price -", discountPrice)
    else:
        messageBody += "  This item has no discount price!" + "\n"
        print("  This item has no discount price!")

    if originalPrice != 0:
        messageBody += "  Original Price - " + str(originalPrice) + "\n"
        print("  Original Price -", originalPrice)
    else:
        messageBody += "  Original price cannot be found!" + "\n"
        print("  Original price cannot be found!")

    messageBody += "  Expected Price - " + str(expectedPrice) + "\n"
    # let users input the price that they want it to be less than or equal
    if((discountPrice != 0 and discountPrice <= expectedPrice) or (originalPrice != 0 and originalPrice <= expectedPrice)):
        messageBody += "  Check the link " + url + "\n\n"
        #send_email(title, discountPrice, originalPrice, expectedPrice, url)
    else:
        messageBody += "  The price is still more than your expected price - " + str(expectedPrice) + "!" + "\n\n"
        print("  The price is still more than your expected price -",
              str(expectedPrice) + "!")
    return messageBody
"""
def send_email(title, discountPrice, originalPrice, expectedPrice, url):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("scrapertestingapp@gmail.com", "uk7ySFTf4HL4E9n")

    subject = 'CHECK THE PRICE!!!!'
    body = title.strip() + "\n" + " Discount Price - " + str(discountPrice) + "\n" + " Original Price - " + str(originalPrice) + \
        "\n" + " Expected Price - " + \
        str(expectedPrice) + "\n" + "Check the link " + url

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'scrapertestingapp@gmail.com',
        'jzhtun@gmail.com',
        msg
    )
    server.quit()
"""
def send_email(messageBody):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("scrapertestingapp@gmail.com", "uk7ySFTf4HL4E9n")
    
    subject = 'CHECK THE PRICE!!!!'
    body = messageBody

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'scrapertestingapp@gmail.com',
        'jzhtun@gmail.com',
        msg
    )
    server.quit()

"""
#check_price("")
for i in range(len(URLs)):
    print("Item", (i+1))
    check_price(URLs[i],expectedPriceList[i])
"""