#!/usr/bin/env python
from pandocfilters import walk, toJSONFilter

"""
Does annotation stuff. For use with edNotes.sty.
"""

def removeLemma(x)
    are_we_there_yet = false
    def go(key, val, fmt, meta):
        if are_we_there_yet:
            return val
        else
            if key == 'Str':
                if val == '::':
                    are_we_there_yet = true
    return walk(x, go, "", {})

def parse(key, val, fmt, meta):
    if fmt == 'latex':
        if key == 'BlockQuote':
            return [latex('\\begin{linenumbers}')] + val + [latex('\\end{linenumbers}')]
        elif key == 'Note':
            contents = stringify(val).partition('::')
            if contents[0][0] == '>':
                lemma = contents[0][1:].strip()
                note = removeLemma(val)
                return [latex('\\Anote{' + lemma + '}{')] + note + [latex('}')]

if __name__ == "__main__":
  toJSONFilter(parse)
