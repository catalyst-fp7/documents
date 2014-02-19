#!/usr/bin/python
import sys
import re
import os

begin_expr = re.compile(r'<pre><code class="(\w+)( [0-9\.]+)?">')
end_expr = re.compile(r'</code></pre>')
insert_expr = re.compile(r'\\include{(.*)}')
digraph_start_expr = re.compile(r'\s*(strict\s+)?digraph\s+\{')


if __name__ == '__main__':
    state = None
    num = 1
    for line in sys.stdin:
        if not state and begin_expr.match(line):
            m = begin_expr.match(line)
            state = m.group(1)
            if state == 'graphviz':
                print '<img src="fig%d.png" />' % (num)
                num += 1
                continue
            else:
                print m.group(0),
                line = line[m.end():]
        if insert_expr.search(line):
            m = insert_expr.search(line)
            fname = m.group(1)
            if not os.path.exists(fname):
                sys.stderr.write('Missing: %s\n' % fname)
                exit(1)
            with open(fname) as f:
                data = f.read()
                print data
            line = line[m.end():]
        elif state and end_expr.match(line):
            if state != 'graphviz':
                print line,
            state = None
        elif state != 'graphviz':
            print line,
