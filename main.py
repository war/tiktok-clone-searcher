import re
from lib.TiktokChecker import TiktokChecker
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lib.Utils import Util
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed

def check_username_multi_thread(usernames):
    driver      = webdriver.Chrome(options=chrome_options)
    checker     = TiktokChecker(driver)
    res         = checker.check_usernames(usernames)
    return res

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

    threads = int(args["threads"])

    usernames_per_thread_count = len(usernames) / threads
    print(usernames_per_thread_count)

    usernames_per_thread = []
    thread_size = 2

    for u in range(0, len(usernames)-1):
        start = u * thread_size
        end = start + thread_size
        tmp = usernames[start: end]
        
        if tmp:
            usernames_per_thread.append(tmp)

    res = {}
    
    print(usernames_per_thread)

    with ThreadPoolExecutor(threads) as executor:
        futures = [executor.submit(check_username_multi_thread, i) for i in usernames_per_thread]
        
        for future in as_completed(futures):
            print(future.result())
            res.update(future.result())

    print("Results:")
    print("<username>\t(<number of clones>): list, of, taken, usernames")

    for key, item in res.items():
        print("{} \t\t({}): {}".format(key, len(item)-1, ", ".join(item)))
        
    print("\nAll results will contain the original username which does")
    print("not count towards the cloned counter.")