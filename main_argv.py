import calendar
import datetime
import locale
import os
import sys

import bs4


def set_month():
    mese = int(sys.argv[1])

    return mese


def get_time():
    locale.setlocale(locale.LC_ALL, 'it_IT')

    now = str(datetime.date.today().strftime('%d-%m-%Y'))
    data = now.split("-")
    data = list(map(int, data))

    data[1] = set_month()

    if data[1] == 7 or data[1] == 8 or data[1] == 9:
        exit()

    if data[1] == 0:
        data[1] = 12

    if data[1] < 10 and data[1] > 0:
        data[1] = "0" + str(data[1])

    return data


def login():
    os.system("wget -q --save-cookies cookies.txt --keep-session-cookies --post-data "
              "'login=USER&password=PWD&Submit=Accedi' --delete-after "
              "https://www.studiosep.com:51/doc/iar/include/login-exec.php")


def download(link):
    os.system("wget -q --load-cookies cookies.txt -O /home/nico/condivisa/Elena/Lavoro/Cedolini/" + str(get_time()[2]) + "/" + str(get_time()[2]) + get_time()[1] + "_cedolino.pdf " + link)
    time.sleep(15)
    os.remove("cookies.txt")
    os.remove("index.html")


def scraping():
    mese = calendar.month_name[int(get_time()[1])].capitalize()
    link = "https://www.studiosep.com:51/doc/iar/view.php?dir=Anno_" + str(get_time()[2]) + "/" + mese + "_" + str(get_time()[2])

    os.system("wget -q --load-cookies cookies.txt -O index.html " + link)

    with open("index.html", "r") as f:
        parser = bs4.BeautifulSoup(f, "html.parser")

    cedolino = parser.select('a[href*="download.php"]')
    cedolino = cedolino[0]["href"]

    link = "https://www.studiosep.com:51/doc/iar/" + str(cedolino)

    return link


if __name__ == "__main__":
    login()
    download(scraping())