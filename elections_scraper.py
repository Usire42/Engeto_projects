
def main(URL,PATHWAY):
    inf_URL_to_csv(URL, PATHWAY)

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv



def obce_z_okresu(URL) -> list:
    '''extracts url adress and codes of municipalities'''
    URL_part = 'https://volby.cz/pls/ps2017nss/'
    r = requests.get(URL)
    html = r.text

    soup = BeautifulSoup(html, 'html.parser')

    urls = []
    code = []
    for link in soup.find_all('td', class_ = 'cislo'):
        for in_link in link.find_all('a'):
            urls.append(urljoin(URL_part, in_link.get('href')))
            code.append(int(in_link.get_text()))
    return urls, code

def str_to_int(list_of_lists) -> list:
    '''transfer data in list to int
    return list'''
    new_list = []
    for list in list_of_lists:
            new_row = list[:2]
            for value in list[2:]:
                    if '\xa0' in value:
                            value = value.replace('\xa0','')
                    new_row.append(int(value))
            new_list.append(new_row)
    return new_list

def inf_URL_to_csv(URL, PATHWAY) -> csv:
    '''get together results abou election in specific district - url '''
    obce_z_okresu(URL)
    urls = obce_z_okresu(URL)[0]
    codes = obce_z_okresu(URL)[1]

    r = requests.get(urls[0])
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')



    header = ['code', 'location', 'registered', 'envelopes', 'valid']
    x = 1
    while soup.find_all('td', headers=f't{x}sb2'):
        for strany in soup.find_all('td', headers=f't{x}sb2'):
                header.append((strany.get_text()))
        x += 1

    rows = []
    for code, url in zip(codes, urls):
            r_for = requests.get(url)
            html_for = r_for.text
            soup_for = BeautifulSoup(html_for, 'html.parser')

            obec = soup_for.find(text=lambda text: text and 'Obec:' in text).split('Obec: ')[1].replace('\n', '')
            volici = soup_for.find('td', headers = 'sa2').get_text()
            obalky_v = soup_for.find('td', headers = 'sa3').get_text()
            platne_hlasy = soup_for.find('td', headers = 'sa6').get_text()

            row = [code, obec, volici, obalky_v, platne_hlasy]

            y = 1
            while soup_for.find_all('td', headers=f't{y}sb3'):
                for hlasy in soup_for.find_all('td', headers=f't{y}sb3'):
                        row.append(hlasy.get_text())
                y += 1
            rows.append(row)

    int_rows = str_to_int(rows)
    okres = soup.find(text=lambda text: text and 'Okres:' in text).split('Okres: ')[1].replace('\n', '')
    file = PATHWAY + okres + '.csv'
    f = open(file, 'w', newline= '')
    f_writer = csv.writer(f)
    f_writer.writerow(header)
    f_writer.writerows(int_rows)
    f.close()


if __name__ == '__main__':
    URL = 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2111'
    PATHWAY = 'C:/Users/User/PycharmProjects/projects/'  '''wtire pathvay example:  
                                                            "'C:/Users/User/PycharmProjects/projects/" '''
    main(URL, PATHWAY)
