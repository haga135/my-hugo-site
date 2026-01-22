+++
date = '2026-01-20T13:59:19+09:00'
draft = true
title = 'My First Post'
+++

{{< highlight go-html-template >}}
{{ range .Pages }}

  <h2><a href="{{ .RelPermalink }}">{{ .LinkTitle }}</a></h2>
{{ end }}
{{< /highlight >}}

## Introduction

This is **bold** text, and this is _emphasized_ text.

Visit the [Hugo](https://gohugo.io) website!
