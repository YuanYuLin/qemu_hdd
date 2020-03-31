import os
import sys

def help():
    print 'gen_storage.py <output_image>'

if __name__ == '__main__':
    if len(sys.argv) < 3:
        help()
        sys.exit()

    out_img = sys.argv[1]

    img_size = 64 * 1024 * 1024

    data = bytearray('\0' * img_size)
    fp = open(out_img, 'wb')
    fp.write(data)
    fp.close()

