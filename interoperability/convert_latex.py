#!/usr/bin/python
import sys
import re

begin_expr = re.compile(r'\\begin{lstlisting}\[language=(\w+)\]')
end_expr = re.compile(r'\\end{lstlisting}')

if __name__ == '__main__':
    state = None
    num = 1
    for line in sys.stdin:
        if not state and begin_expr.match(line):
            m = begin_expr.match(line)
            state = m.group(1)
            if state == 'graphviz':
                print '\\digraph[scale=0.5]{fig%d}{' % num
                num += 1
            else:
                print '\\begin{minted}{%s}' % (state,)
        elif state == 'graphviz':
            # skip first line, the digraph declaration.
            state = 'graphviz1'
        elif state and end_expr.match(line):
            if state == 'graphviz1':
                print ''
            else:
                print '\\end{minted}'
            state = None
        else:
            print line,
