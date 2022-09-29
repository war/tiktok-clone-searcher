# tiktok-clone-searcher
There used to be a bug in Tiktok where you could "dupe" your username.

This will search for username/s you want and tell you if that username has been duped or not.

This requires chromedriver.

# Quickstart guide
```
git clone https://github.com/war/tiktok-clone-searcher.git

cd tiktok-clone-searcher

pip install -r requirements.txt

python main.py -u bozo
```

# python main.py options
```
python main.py -u bozo
python main.py -u bozo -u bozo1 -u bozo2 -u bozo3
python main.py -m bozo,bozo1,bozo2,bozo3
```