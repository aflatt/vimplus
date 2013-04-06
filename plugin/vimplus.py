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

def gotoStart():
	"""Moves the cursor to the start of the current buffer"""
	vim.command("normal gg")
