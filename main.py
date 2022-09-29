from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import itertools

class TiktokChecker:
    def __init__(self, driver) -> None:
        self.driver = driver

    def test_variant(self, base_url: str, username: str, variant: str) -> bool:
        self.driver.get(base_url + variant)
        
        content = driver.page_source
        soup = BeautifulSoup(content, "html.parser")

        # Tiktok has dynamic ids and the only consistant thing you can grab 
        # is this data-e2e attribute
        elem = soup.findAll("h2", attrs={"data-e2e": 'user-title'})

        if len(elem) > 0:
            return elem[0].getText().lower().strip() == username
        return False

    def check_username(self, username: str) -> list:
        clones      = []
        base_url    = "https://www.tiktok.com/@"

        upper       = username.upper()
        lower       = username.lower()
        tmp         = itertools.product(*zip(upper, lower))
        variants    = list(map(''.join, tmp))

        for x in variants:
            if self.test_variant(base_url, username, x):
                clones.append(x)

            # Sometimes it'll iterate quicker than the page can load
            sleep(2)

        return clones

    def check_usernames(self, usernames: list) -> dict:
        msg = ", ".join(usernames)
        print("Processing: {}".format(msg))

        res = {}

        for user in usernames:
            print("Searching for: {}...".format(user))

            tmp = self.check_username(user)
            clone_count = len(tmp)-1
            msg = "#### CLONES FOUND: {}".format(str(clone_count))

            res[user] = tmp

            print(msg, end="\n\n")
            
        return res

if __name__ == "__main__":
    from selenium.webdriver.chrome.options import Options

    chrome_options = Options()
    chrome_options.add_argument("--log-level=3")

    driver      = webdriver.Chrome(options=chrome_options)

    checker     = TiktokChecker(driver)

    usernames   = ["xp", "bf", "eak", "bozo"]
    res         = checker.check_usernames(usernames)

    driver.close()

    print("Results:")
    for key, item in res.items():
        print("{} \t({}): {}".format(key, len(item)-1, ", ".join(item)))
    print("<username> (<number of clones>): list, of, taken, usernames")