# Battle Cats cat list scraper from Cat Release Order (as of WikiaPage V2)
# Created by James Raphael Tiovalen (2019)

import json
import requests
from bs4 import BeautifulSoup


def main():
    r = requests.get("https://battle-cats.fandom.com/wiki/Cat_Release_Order")
    soup = BeautifulSoup(r.text, "html.parser")
    cats = soup.find("div", id="mw-content-text").find("table", {"class":"article-table"})("tr")
    
    cat_list = []
    
    for i in cats[2:]:
        id = i.find_all("td")[0].text.strip().encode("ascii", "ignore").decode("ascii")
        name = i.find_all("td")[2].text.strip().encode("ascii", "ignore").decode("ascii")
        
        cat_list.append({"itemId":int(id),"itemCategory":1,"amount":100,"title":str(name)})
    
    with open("cat_list.json", "w+") as f:
        f.write(json.dumps(cat_list, sort_keys=False, indent=2))      


if __name__ == '__main__':
    main()
