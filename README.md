Utility Scripts
===============

Assorted scripts I want in my path.

For most pandoc stuff, see dfaligertwood/pandoc-filters

### dtom

Simple script to merge "draft" branch into master with a message passed on the 
command-line. It then renames draft to something else, and creates an empty 
draft branch. Used in conjunction with my .vimrc which autocommits on a draft 
branch.

### zotero-csljson-postprocess

jq-based script to convert Zotero’s CSL-JSON output into something that can be 
used by pandoc (which doesn’t like number-only CSL keys, for some reason) and 
are human-readable. Only changes the id of each entry.

### marked_processor

Fucking OS X paths. Also it’s easier to edit this stuff in vim than in the tiny 
box in marked…
