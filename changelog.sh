#!/bin/bash
git log --pretty=format:"%cd%n- %h %s (%an)%n" --date=short | awk 'BEGIN { FS="\n"; OFS="\n" } { if ($1 != p) { if (title != "") print entries; title=$1; entries=""title"\n"; first_commit=1 }; p=$1; $1="## "; if (!first_commit) entries=entries"\n"; entries=entries""$0; first_commit=0 } END { if (title != "") print entries }' | awk '!a[$0]++' >> CHANGELOG.md




