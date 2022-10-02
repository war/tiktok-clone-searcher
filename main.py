from lib.TiktokChecker import TiktokChecker
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lib.Utils import Util

if __name__ == "__main__":

    args        = Util.get_args()
    usernames   = Util.get_usernames(args)

    chrome_options = Options()
    chrome_options.add_argument("--log-level=3")

    if not args["show_browser"]:
        chrome_options.add_argument("--headless")

    if not usernames:
        print("No usernames.")
        exit(1)

    driver      = webdriver.Chrome(options=chrome_options)
    checker     = TiktokChecker(driver)
    res         = checker.check_usernames(usernames)

    driver.close()

    print("Results:")
    print("<username>\t(<number of clones>): list, of, taken, usernames")

    for key, item in res.items():
        print("{} \t\t({}): {}".format(key, len(item)-1, ", ".join(item)))
        
    print("\nAll results will contain the original username which does")
    print("not count towards the cloned counter.")