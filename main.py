import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

params = {
    "Accept-Language" : "en-US,en;q=0.9",
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

response = requests.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6", headers=params)
soup = BeautifulSoup(response.content, "lxml")
price = soup.find(class_="a-offscreen").getText()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
#print(price_as_float)
if price_as_float < 100:
    message = f"Your product is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login("elsabecrous@gmail.com", "apgs qzya zjlj xkls")
        connection.sendmail(
            from_addr="elsabecrous@gmail.com",
            to_addrs="76248usa@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}".encode("utf-8")
        )





