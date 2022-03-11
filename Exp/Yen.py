import requests
from lxml import etree

xml_response = etree.fromstring(requests.get("http://www.cbr.ru/scripts/XML_daily.asp").text.encode("1251"))

kurs = xml_response.find("Valute[@ID='R01820']/Value").text

print(f"Курс Японских иен равен {kurs} рублей")
