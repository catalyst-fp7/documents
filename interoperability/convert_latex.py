#!/usr/bin/python
import sys
import re
import os

begin_expr = re.compile(r'\\begin{lstlisting}\[language=(\w+)( [0-9\.]+s?)?(.*)\]')
end_expr = re.compile(r'\\end{lstlisting}')
insert_expr = re.compile(r'\\include{(.*)}')
digraph_start_expr = re.compile(r'\s*(strict\s+)?digraph\s+\{')


if __name__ == '__main__':
    state = None
    num = 1
    for line in sys.stdin:
        if insert_expr.match(line):
            fname = insert_expr.match(line).group(1)
            if not os.path.exists(fname):
                sys.stderr.write('Missing: %s\n' % fname)
                exit(1)
            with open(fname) as f:
                data = f.read()
                if state == 'graphviz':
                    match = digraph_start_expr.match(data)
                    assert match
                    data = data[len(match.group(0)):]
                    state = 'graphviz1'
                print data
        elif not state and begin_expr.match(line):
            m = begin_expr.match(line)
            state = m.group(1)
            if state == 'graphviz':
                scale = m.group(2) or '0.5'
                scale = scale.strip()
                caption = m.group(3).strip()
                if scale[-1] == 's':
                    scale = scale[:-1] + ',angle=90,origin=c'
                print '\\begin{figure}[hbtp]'
                print '\\digraph[scale=%s]{fig%d}{' % (scale.strip(), num)
                num += 1
            else:
                print '\\begin{minted}{%s}' % (state,)
        elif state == 'graphviz':
            # skip first line, the digraph declaration.
            state = 'graphviz1'
        elif state and end_expr.match(line):
            if state == 'graphviz1':
                if caption:
                    print '\\caption{%s}' % (caption,)
                print '\\end{figure}'
            else:
                print '\\end{minted}'
            state = None
        else:
            print line,
