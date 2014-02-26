#!/usr/bin/python
import os
import os.path
import subprocess

if __name__ == '__main__':
    i = 1
    while True:
        fname = "fig%d.png" % i
        if not os.path.exists(fname):
            break
        p = subprocess.check_output(['convert', fname, '-print', '%w,%h', '/dev/null'])
        width, height = p.strip().split(',')
        width, height = int(width), int(height)
        sideways = ''
        if width > 1300 and height * (1.35) < width:
            sideways = 's'
            scale = min(575.0/height, 800.0/width, 1)
        else:
            scale = min(575.0/width, 800.0/height, 1)
        print "%s: %0.2f%s" % (fname, scale, sideways)
        i += 1
