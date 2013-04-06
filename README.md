Vimplus
=========

Vimplus is a python module for scripting vim.

Vim includes a python module called "vim", which facilitates scripting vim in python.
Unfortunately this module provides very limited interaction with vim.

Vimplus aims to provide a more comprehensive vim api. The ultimate goal of vimplus is that writing plugins for vim should be easier.

LICENSE
---------

Vimplus is currently published under the MIT license


USE
---------

I highly recommend using the excellent vim plugin pathogen in conjunction with vimplus.
To use vimplus simply:

1. Clone the git repo into your pathogen bundle directory.
2. Restart vim

You can test that vimplus is installed by running the following command directly from vim:

    :py import vimplus

If the command executes without any errors, than you're all set!


To get started using vimplus in a vim script you can use this simple template (note that you MUST NOT! indent this code):

    python << EOF
    import vim
    import vimplus
    print("Hello from vimplus")
    EOF

With the above file (i.e. the template) open in vim, you can run the script by sourcing the file:

    so %

REQUIREMENTS
----------

Right now vimplus requires vim built with python support. It currently only works with python 2, but I plan to eventually add support for python3 as well.
In the meantime if you are using python3, you can support python3 by changing any line that contains:

    python << EOF
to

    python3 << EOF
