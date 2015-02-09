# Twitter

## アプリの作成

1. Twitterのアカウントを作り、ログインする。
1. [Twitter Apps](https://apps.twitter.com/)でアプリを作成する。Websiteは`http://example.net/`でよい。

## OAuth認証

ここでは、自分だけアクセスできればよい。他人もアクセスできるようにする方法は割愛。

1. 「Access」タブでアクセスタイプを「Read and Write」にする。
1. 「Keys and Access Tokens」タブのConsumer KeyとConsumer Secretをメモする。
1. 「Create my access token」をクリックして、Access TokenとAccess Token Secretをメモする。

## ライブラリ

PythonからTwitterを利用するためのライブラリを導入する（ライブラリには長所・短所がある）。

```bash
sudo apt-get update
sudo pip install twitter
```

`tweet.py`

```python
from twitter import *

t = Twitter(
    auth=OAuth("Access Token", "Access Token Secret", "Consumer Key", "Consumer Secret"))

t.statuses.update(status="hello, world")
EOF
```
