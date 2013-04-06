py << EOF
import vim
import sys
import os
vim.command("let s:current_file=expand('<sfile>')")
currentFile = vim.eval("s:current_file")
scriptDir = os.path.dirname(currentFile)
#add the path of the script to the python path, so we can load the vimplus module
sys.path.insert(0, os.path.realpath(scriptDir))
import vimplus
EOF
