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
        p = subprocess.check_output(['convert', fname, '-print', '%w', '/dev/null'])
        width = int(p.strip())
        print "%s: %0.2f" % (fname, 468.0/width)
        i += 1
