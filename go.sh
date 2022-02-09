#!/usr/bin/env bash
content_name=`git status|grep content|awk -F '/' '{print $2}'`
git add content
git commit -m "add content $content_name"
git push origin master

make publish
cd ..
git clone git@github.com:xuanmingyi/xuanmingyi.github.io.git
cp -r blog/output/* xuanmingyi.github.io
cd xuanmingyi.github.io
git add .
git commit -m "auto push at `date`"
git push origin master
cd ..
rm -rf xuanmingyi.github.io
