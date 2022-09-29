from lib.TiktokChecker import TiktokChecker
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Tiktok clone checker')
    parser.add_argument('-u','--user', action='append', help='User to check', required=False)
    parser.add_argument('-m','--multiuser', help='Users to check', required=False)
    parser.add_argument('--headless', action='store_true', help='Run in headless mode', required=False)
    args = vars(parser.parse_args())
    return args

if __name__ == "__main__":
    #usernames   = ["xp", "bf", "eak", "bozo"]
    args        = get_args()

    usernames = []

    if args["user"]:
        usernames = args["user"]
    
    if args["multiuser"]:
        for user in args["multiuser"].split(","):
            usernames.append(user)

    chrome_options = Options()
    chrome_options.add_argument("--log-level=3")

    if args["headless"]:
        chrome_options.add_argument("--headless")

    print(usernames)

    driver      = webdriver.Chrome(options=chrome_options)
    checker     = TiktokChecker(driver)
    res         = checker.check_usernames(usernames)

    driver.close()

    print("Results:")

    for key, item in res.items():
        print("{} \t\t({}): {}".format(key, len(item)-1, ", ".join(item)))

    print("<username>\t(<number of clones>): list, of, taken, usernames")