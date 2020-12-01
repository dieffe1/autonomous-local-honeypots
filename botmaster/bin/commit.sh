#!/usr/bin/env bash

cd resources/localhoneypot.github.io
git add * > /dev/null
#git rm $(git ls-files --deleted) > /dev/null
git commit -m "`date`" > /dev/null
git push origin master  > /dev/null
