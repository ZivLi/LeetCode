awk -F' ' '{for(i=1;i<=NF;i=i+1){print $i}}' ./words.txt |
sort|uniq -c|sort -nr|awk -F' ' '{printf("%s %s\n",$2,$1)}'
