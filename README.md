# tiktok-clone-searcher
There used to be a bug in TikTok where you could "dupe" your username. (not sure if this is properly fixed actually).

This will search for username/s you want and tell you if that username has been duped or not.

This requires chromedriver.

# QuickStart Guide
```
git clone https://github.com/war/tiktok-clone-searcher.git

cd tiktok-clone-searcher

pip install -r requirements.txt

python main.py -m user1,user2,user3
```

# Arguments
```
-u --user:
- Use this when you want to want to check a single user (can be used multiple times)

E.g.
python main.py -u user1
python main.py -u user1 -u user2 -u user3
```
```
-m --multiuser:
- Use this when you want to want to check a multiple users (less effort than -u <> -u <> -u <>)

E.g.
python main.py -m user1,user2,user3
```
```
-e --env:
- Get a list of usernames from the .env file

.env:
USERNAMES="user1,user2,user3"

E.g.
python main.py -e
```
```
-i --input:
- Get usernames from input inside the program.

E.g.
python main.py -i
```
```
-s --show_browser:
- Show the browser that checks over the accounts

E.g.
python main.py -s
```