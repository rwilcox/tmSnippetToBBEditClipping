#!/usr/bin/env python

import plistlib
import os, sys

for potential_file in os.listdir( sys.argv[1] ):
	if potential_file.endswith(".tmSnippet"):
	    res = plistlib.readPlist(  open( os.path.join(sys.argv[1], potential_file) )  )
	    name_without_ext, junk = os.path.splitext(potential_file)
	    with open( os.path.join(sys.argv[1], name_without_ext), "w" ) as f:
	        f.write( res["content"] )

