+++
date = '2024-02-10T11:02:38+09:00'
draft = false
title = '【WordPress】ショートコードで投稿IDやスラッグから記事の内部リンクを作成する'
categories = ["wordpress"] 
thumbnail = "images/shared/screenshot-1.webp"
+++

![](/images/shared/blackcat.webp)

## 投稿記事へのリンクを設置したい

記事にタイトルのリンクを追加するショートコードを作成するサンプルです。

ワードプレスでブログをやっていると別の投稿ページへのリンクを設置したいときがありますよね？

そんなときどうすれば簡単にリンクを設置する事ができるのか調べてみました！

最近はブロックエディターを使って記事を書くと思いますので、ブロックエディターを前提としてやる方法をまとめてみました。

- ワードプレスで管理画面から新規投稿を追加
- タイトルを追加
- 記事を書く
- ブロックを追加をクリック
- すべてを表示
- ショートコードを追加
- 記事の後ろにショートコードを入力
- 記事を公開する

という順番でできます。

その前に管理画面のツールからテーマエディターを選んで、function.phpの末尾にコードを追加しておきます。

    function linkpage_func ( $atts ) {
        extract( shortcode_atts( array(
            'id' => '', //投稿ID
            'slug' => '', //ページスラッグ
        ), $atts ) );
        $my_url = home_url( '/' );
        if($slug){ //スラッグを指定したときに投稿IDを取得する
            $id = url_to_postid($my_url. $slug);
        }
        $link = get_permalink($id);
        $title = get_the_title($id); //投稿IDで指定した投稿のレコードをデータベースから取得
        return '<a href="'. $link .'"' .'>'. $title. '</a>';
    }
    add_shortcode('pagelink', 'linkpage_func');

ワードプレスで投稿記事の管理をするのに投稿スラッグを使っていると思います

ショートコードに

    [pagelink slug="投稿スラッグ"]

というショートコードを入れると該当記事のタイトルを取得してリンクを設置できます
