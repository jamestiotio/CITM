# Battle Cats cat list scraper from Cat Release Order (as of WikiaPage V2)
# Created by James Raphael Tiovalen (2019)

import json
import requests
from bs4 import BeautifulSoup


def main():
    r = requests.get("https://battle-cats.fandom.com/wiki/Cat_Release_Order")
    soup = BeautifulSoup(r.text, "html.parser")
    cats = soup.find("div", id="mw-content-text").find(
        "table", {"class": "article-table"}
    )("tr")

    cat_list = []

    for cat_id, val in enumerate(cats[2:]):
        # Ignore, delete/remove and omit non-ASCII characters since they could/might potentially cause some trouble (kind of)
        name = (
            val.find_all("td")[2].text.strip().encode("ascii", "ignore").decode("ascii")
        )

        cat_list.append(
            {
                "itemId": int(cat_id),
                "itemCategory": 1,
                "amount": 100,
                "title": str(name),
            }
        )

    with open("cat_list.json", "w+") as f:
        f.write(json.dumps(cat_list, sort_keys=False, indent=2))


if __name__ == "__main__":
    main()
