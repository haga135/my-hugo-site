+++
date = '2024-02-24T20:58:16+09:00'
draft = false
title = 'このブログを始めるきっかけについてその2'
eyecatch = "https://snakewoman.blog/wp-content/uploads/2024/01/screenshot-1.png"
+++

![](https://snakewoman.blog/wp-content/uploads/2024/02/illust1129_thumb.gif)

## プロキシサーバーをインストール、設定

サーバに正常にwebアクセスできるようになったので、プロキシサーバをインストールします。squidという有名なプロキシサーバー用のソフトウエアです。squidの設定ファイルを自身の環境に合わせて設定します。ネットの情報を元に設定していきました。最終行に追記するだけで良かったようですが、該当箇所をコメントアウトして直後に追記しました。

このソフトはキャッシュサーバの機能もあるのですがあえて設定しない方が良いみたいです。

プロキシサーバーの存在を隠す設定

    request_header_access X-Forwarded-For deny all
    request_header_access Via deny all
    request_header_access Cache-Control deny all
    reply_header_access X-Forwarded-For deny all
    reply_header_access Via deny all
    reply_header_access Cache-Control deny all

を追記。デフォルトのポート番号3128は使わないのでコメントアウトして

    http_port ○○○○　（各自の設定）

を追記。認証方式はbasic認証を設定しました。

あと、Windowsのchromeなどでプロクシーの設定が手動だったので自動にするために、ドメインのdns設定が必要でした。wpadという自動認証の設定でドメインの別名（cname)　にwpadを設定してドメイン名を設定しておくと、wpadが追加されたurlにアクセスされたらプロクシサーバに接続されるように設定しました。社内のwebサーバに設定などと書かれていたけどそんなものはないのでvpsのwebサーバに設定しておいた。この辺の設定は少し忘れてしまいました。

それからはWordpressのサイトのテーマやフォントなどを考えていきました。最初はブロック・テーマをカスタマイズしていたのですがごちゃごちゃしてしまったのでtwenty-seventeenの子テーマを作ってブログの雛形からサイトを作ってみました。このテーマはブロック・テーマではないのですが、初心者なのでこれでしばらく運用してみようと思っています。

\>>Amazonおすすめ

[

![](https://snakewoman.blog/wp-content/uploads/2024/03/71UG725llL._AC_SX569_.jpg)  
クレバー プロテインバー \[高プロテイン／低糖質\] いちご味 12本

**Amazonで見る**

](https://amzn.to/3IhL4Jg)
