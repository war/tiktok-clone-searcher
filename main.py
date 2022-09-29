from lib.TiktokChecker import TiktokChecker
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

if __name__ == "__main__":
    usernames   = ["xp", "bf", "eak", "bozo"]

    chrome_options = Options()
    chrome_options.add_argument("--log-level=3")

    driver      = webdriver.Chrome(options=chrome_options)
    checker     = TiktokChecker(driver)
    res         = checker.check_usernames(usernames)

    driver.close()

    print("Results:")

    for key, item in res.items():
        print("{} \t\t({}): {}".format(key, len(item)-1, ", ".join(item)))

    print("<username>\t(<number of clones>): list, of, taken, usernames")