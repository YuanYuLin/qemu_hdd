import os
import sys

def help():
    print 'gen_storage.py <output_image>'

if __name__ == '__main__':
    print len(sys.argv)
    if len(sys.argv) < 2:
        help()

    out_img = sys.argv[1]

    img_size = 128 * 1024 * 1024

    data = bytearray('\0' * img_size)
    fp = open(out_img, 'wb')
    fp.write(data)
    fp.close()

