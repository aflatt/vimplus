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

def inputPassword(message):
	"""Prompt the user for hidden input. Supplies the message as a prompt
		returns the input from the user"""
	vim.command("let inputText = inputsecret('{0}')".format(message))
	text = vim.eval("inputText")
	return text

def splitWindowLeft(size, fileName):
	vim.command("aboveleft {0}vsplit {1}".format(size, fileName))
	vim.command("normal gg")

def splitWindodwRight(size, fileName):
	vim.command("botright {0}vsplit {1}".format(size, fileName))
	vim.command("normal gg")

def splitWindowBottom(size, fileName):
	vim.command("belowright {0}split {1}".format(size, fileName))
	vim.command("normal gg")

def splitWindowTop(size, fileName):
	vim.command("{0}split {1}".format(size, fileName))
	vim.command("normal gg")

def getTempFile(fileName=None):
	if fileName is None:
		pass
	return vim.eval("$TEMP") + "/" + fileName
