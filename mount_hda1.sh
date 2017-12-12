#!/bin/bash
if [ $# -gt 3 ]; then

LINUX_IMAGE="$1"
ROOTFS_IMAGE="$2"
IMAGE_HDA="$3"
IMAGE_MNT="/tmp/mnt"
IMAGE_LOOP="/dev/loop7"
OFFSET=`fdisk $IMAGE_HDA -l | grep "hda.img1" | awk '{ print  $3 }'`

echo "OFFSET=$OFFSET"
echo "losetup -o $(($OFFSET*512)) $IMAGE_LOOP $IMAGE_HDA "
losetup -o $(($OFFSET*512)) $IMAGE_LOOP $IMAGE_HDA 
mkfs -t vfat $IMAGE_LOOP
mount $IMAGE_LOOP $IMAGE_MNT

cp $LINUX_IMAGE $IMAGE_MNT
cp $ROOTFS_IMAGE $IMAGE_MNT

umount $IMAGE_MNT
losetup -d $IMAGE_LOOP

else
echo "mount.sh <kernel> <rootfs> <hdd_img>"
fi
