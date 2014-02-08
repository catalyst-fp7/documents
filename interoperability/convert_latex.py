#!/usr/bin/python
import sys
import re

begin_expr = re.compile(r'\\begin{lstlisting}\[language=(\w+)\]')
end_expr = re.compile(r'\\end{lstlisting}')

if __name__ == '__main__':
    state = None
    for line in sys.stdin:
        if not state and begin_expr.match(line):
            m = begin_expr.match(line)
            state = m.group(1)
            if state == 'graphviz':
                print '\\begin{dot2tex}'
            else:
                print '\\begin{minted}{%s}' % (state,)
        elif state and end_expr.match(line):
            if state == 'graphviz':
                print '\\end{dot2tex}'
            else:
                print '\\end{minted}'
            state = None
        else:
            print line,
