Introduction
==========================

This is a tool - or a seed of a tool - that converts `.tmSnippet` files into BBEdit Clipping syntax.

The TextMate community created a great wealth of snippets, and these are stored in Apple's `plist` XML format. Which is great - easy extraction one by one!

Except when you're working on converting a whole TextMate bundle - then you need an automated tool.

What it does right now
========================

Call it on the command line with a folder of `.tmSnippet` files (probably a TextMate bundle's `Snippets` folder) and it will extract the contents of the snippet.

Example
========================


    $ ls Snippets
    function_start.tmSnippet
    function_with_parameters.tmSnippet
    enum.tmSnippet
    
    $ python tmSnippetToBBEdit.py Snippets
    
    $ ls Snippets
    function_start.tmSnippet
    function_start
    function_with_parameters.tmSnippet
    function_with_parameters
    enum.tmSnippet
    enum
    
The files without extensions were created by this script

Plea for help
========================

This is not the best example of my Python scripting ability -- I hacked it together to accomplish one thing, but I know it can be better.

I sincerely hope you can help make it better with me.

TODOs
========================

This script was hacked together in about an hour, so it needs some enhancements:

1. Turn TextMate clipping-isms into BBEDit ones
----------------------------

Right now this tool makes no attempt to convert TextMate Snippet syntax into BBEdit Clipping syntax. TextMate has a *much* richer clipping syntax than BBEdit, but we can convert what we can and do something with what we can't.

For example, `$0` can be converted to `<#?#>`, and other `$` number placeholders can be converted to `<##>` -- unless they we have seen these placeholders before, in which case we need to do something.


2. Warn about transformations
----------------------

Perhaps warn about transformations and/or placeholder mirroring that BBEdit's clipping syntax can't emulate??



License
=======================

LICENSE:

(The MIT License)

Copyright (c) 2012 Ryan Wilcox

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the ‘Software’), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED ‘AS IS’, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


    
