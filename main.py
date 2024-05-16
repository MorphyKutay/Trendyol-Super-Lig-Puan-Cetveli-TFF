import requests
from bs4 import BeautifulSoup
import csv

# CSV dosyasını açmak için bir kez kullanıyoruz
with open('veriler.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)

    # 1. haftadan 38. haftaya kadar olan verileri alıyoruz
    for i in range(1, 39):
        url = 'https://www.tff.org/Default.aspx?pageId=198&hafta=' + str(i)
        print(url)

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        data = []

        for row in soup.find_all('tbody'):
            row_data = []
            cells = row.find_all('td')
            for cell in cells:
                cell_text = cell.get_text(strip=True)
                cell_parts = cell_text.split('\n')
                for part in cell_parts:
                    row_data.append(part)
                    if len(row_data) == 9:  
                        data.append(row_data)
                        row_data = [] 
            data.append(row_data)

        # Her bir haftanın verilerini CSV dosyasına yazıyoruz
        for row in data:
            writer.writerow(row)

print("Veriler başarıyla 'veriler.csv' dosyasına yazıldı.")
