import vim

def runCmd(cmd):
	"""Runs a command using vim's !"""
	vim.command("!"+cmd)

def runSystemCmd(cmd, fileOutput=None):
	"""Runs the command using vim's system mechanism.
		fileOutput - specifies the file on disk to save the output of the cmd to
					if null doesn't save anything
		returns the results of the command"""
	vim.command("let cmdOutput = system('{0}')".format(cmd))
	output = vim.eval("cmdOutput")
	if fileOutput != None:
		file = open(fileOutput, "w")
		file.write(output)
		file.close()
	return output

def input(message):
	"""Prompt the user for input with. Supply the message as a prompt
		returns the input from the user"""
	vim.command("let inputText = input('{0}')".format(message))
	text = vim.eval("inputText")
	return text

def inputSecret(message):
	"""Prompt the user for hidden input. Supplies the message as a prompt
		returns the input from the user"""
	vim.command("let inputText = inputsecret('{0}')".format(message))
	text = vim.eval("inputText")
	return text

def splitWindowLeft(size, fileName=None):
	"""Split the vim window vertically with the new window appearing on the west
	of the screen
		size is the horizontal screen size the window should take
		fileName is an optional name of a file to open in the new window
		returns the newly created buffer"""
	if fileName is None:
		vim.command("aboveleft {0}vsplit {1}".format(size, fileName))
	else:
		vim.command("aboveleft {0}vnew".format(size))
	gotoStart()
	return vim.current.buffer

def splitWindodwRight(size, fileName=None):
	"""Split the vim window vertically with the new window appearing on the east
	of the screen
		size is the horizontal screen size the window should take
		fileName is an optional name of a file to open in the new window
		returns the newly created buffer"""
	if fileName is None:
		vim.command("botright {0}vsplit {1}".format(size, fileName))
	else:
		vim.command("botright {0}vnew".format(size))
	gotoStart()
	return vim.current.buffer

def splitWindowBottom(size, fileName=None):
	"""Split the vim window horizontally with the new window appearing on the south
	of the screen
		size is the vertical screen size (in lines) that the window should use
		fileName is an optional name of a file to open in the new window
		returns the newly created buffer"""
	if fileName is None:
		vim.command("belowright {0}split {1}".format(size, fileName))
	else:
		vim.command("belowright {0}new".format(size))
	gotoStart()
	return vim.current.buffer

def splitWindowTop(size, fileName=None):
	"""Split the vim window horizontally with the new window appearing on the north
	of the screen
		size is the vertical screen size (in lines) that the window should use
		fileName is an optional name of a file to open in the new window
		returns the newly created buffer"""
	if fileName is None:
		vim.command("{0}split {1}".format(size, fileName))
	else:
		vim.command("belowright {0}new".format(size))
	gotoStart()
	return vim.current.buffer

def setBufferTypeScratch():
	"""Make the current buffer a scratch buffer (i.e. where a temporary buffer that can be discarded)
	at any time"""
	vim.command("setlocal buftype=nofile")
	vim.command("setlocal bufhidden=hide")
	vim.command("setlocal noswapfile")

def gotoStart():
	"""Moves the cursor to the start of the current buffer"""
	vim.command("normal gg")

def setupCompletion(onKeys, completionMethod):
	"""The vimplus complete method, which display a list of available autocompletions
	can only be called from insert mode. This method sets up the appropriate key bindings
	that will trigger calling the method
		onKeys - the keys that will trigger the method
		completionMethod - the completion method to call"""
	pass

def complete(words):
	"""Shows the vim autocompletion menu"""
	vim.command("call complete(col('.'), {0})".format(words))

def onEvent(event, action):
	"""Registers a call back that will be invoked when a vim event occurs
		event is the name of the vim event to register (use event<name> members of vimplus)
		action is the python method to call when the event occurs"""
	pyMethodName = action.__name__
	vimFuncName = pyMethodName
	vimFuncName = pyMethodName[0].upper() + pyMethodName[1:]
	vim.command("autocmd {event} * call {functionName}()".format(event=event, functionName=vimFuncName))	
	vim.command("""fun! {functionName}()
py {pyMethodName}()
endf""".format(functionName=vimFuncName, pyMethodName=pyMethodName))

eventBuferWrite = "BuferWrite"
eventCursorMoved = "CursorMoved"
