Utility Scripts
===============

Assorted scripts I want in my path.

Mostly pandoc filters and other stuff I use for academic writing.

Rundown:

### pandoc-ednotes, pandoc-musicnotes

Both these packages work with the LaTeX package edNotes.sty to create editorial 
notes with the following syntax:

pandoc-ednotes, level A footnote:

```
^[| lemma : comment]
```

pandoc-musicnotes, level B footnote:

```
^[& lemma : comment]
```

### pandoc-lineno

Required for pandoc-ednotes and pandoc-musicnotes. Replaces the 'blockquote' 
feature of pandoc with a line-numbered environment.

### pandoc-sidenotes, pandoc-offsidenotes

Also add features to the pandoc footnote feature. Sidenotes in LaTeX with the 
marginnotes.sty package. Uses the following syntax:

```
sidenote: ^[\> sidenote]
other sidenote: ^[~ off side note]
```

### dtom

Simple script to merge "draft" branch into master with a message passed on the 
command-line. It then renames draft to something else, and creates an empty 
draft branch. Used in conjunction with my .vimrc which autocommits on a draft 
branch.

