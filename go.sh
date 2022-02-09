#!/usr/bin/env bash
content_name=`git status|grep content|awk -F '/' '{print $2}'`
git add content
git commit -m "add content $content_name"
git push origin master

mv .git git
make publish
git clone https://github.com/xuanmingyi/xuanmingyi.github.io.git xuanmingyi.github.io
cp -r output/* xuanmingyi.github.io
cd xuanmingyi.github.io
git add .
git commit -m "auto push at `date`"
git push origin master
cd ..
rm -rf xuanmingyi.github.io
mv git .git
