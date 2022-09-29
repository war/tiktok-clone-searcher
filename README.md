# tiktok-clone-searcher
There used to be a bug in TikTok where you could "dupe" your username. (not sure if this is properly fixed actually)

This will search for username/s you want and tell you if that username has been duped or not.

This requires chromedriver.

# QuickStart Guide
```
git clone https://github.com/war/tiktok-clone-searcher.git

cd tiktok-clone-searcher

pip install -r requirements.txt

python main.py -u bozo
```

# python main.py options
```
python main.py
python main.py -u bozo
python main.py -u bozo -u bozo1 -u bozo2 -u bozo3
python main.py -m bozo,bozo1,bozo2,bozo3
```

Using only "python main.py" will prompt the user to input usernames.

# arguments
```
-u - Use this when you want to want to check a single user (can be used multiple times)
-u user

python main.py -u user1
python main.py -u user1 -u user2 -u user3
```
```
-m - Use this when you want to want to check a multiple users (less effort than -u <> -u <> -u <>)
-m user1,user2,user3

python main.py -m user1,user2,user3
```
```
--headless - hide the browser that checks over the accounts
--headless

python main.py -m user1,user2,user3 --headless
```

Using only "python main.py" will prompt the user to input usernames.