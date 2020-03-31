#!/bin/bash
if [ $# -gt 0 ]; then
TGTDEV=$1
echo $#
sed -e 's/\s*\([\+0-9a-zA-Z]*\).*/\1/' << EOF | sudo fdisk ${TGTDEV}
o
n
p
1
 #enter
+1M
n
p
2
 #enter
 #enter
a
1
p
w
q
EOF
else
echo " usage: parted.sh hd[x].img"
fi
