Shell Scripting
===============

At this point, you’ve been introduced to a several Linux commands and while they are
useful on their own, what if you needed to execute a series of commands over and over again? It
would be really annoying if you had to type each one of them every time you needed
to use them, and not much better if you used the history feature of Linux. As it turns
out, there is an easy way to handle repetitive tasks. Create a script! A script is
a small program that executes one or more Linux commands automatically. Since we are creating scrips using
shell commands, we call these shell scripts.
Being able to create shell scripts
quickly can be a really useful tool that makes doing routine tasks that may take a long
time if done using only the command line very quick.

A first script
--------------

Let’s start off by making a script that prints a message to the screen. Open up a file in
emacs called first.sh. The .sh suffix doesn’t really mean anything, other than it would be
an indication that this file is a shell script.
Add the folllowing lines to the file::

  #!/bin/bash
  #This is a comment!
  echo "Hello World"

The first line of the script tells Linux the shell that should be used to interpret the script.
In this case, we are telling Linux to use /bin/bash, or the Bourne Again shell. This is the shell that you
use normally in the command line, but including this
line tells the kernel which shell to use even if you
aren't using bash.

The second line of that script begins with a special symbol: #. This marks the line as a
comment, and is ignored by the shell. The only exception is when the very first line of
the file starts with #!, like ours. Then Linux knows to interpret it as described above.
The third line runs a command: echo, with one argument, the string “Hello World”.

Now we are ready to run the script. To do this, we need
to exit out of emacs and work in the command line. But,
before using C-x C-c to exit emacs, we can use another
Linux shortcut.

Background/foreground
---------------------

Instead, type::

  Control-z

This keystroke is Linux for "put this process in the background". This is analogous to setting emacs off to the
side while you work on something else. The nice thing about
putting a process in the background is that you
can come back to it later and it will be in the
exact same state that you left it in. This is called
putting a process in the foreground. To do that,
in the command line type::

  fg

and press return. Now, you should have your emacs window back. One more thing, it is possible to put
multiple processes in the background at a time. ``fg``
will bring the last process that you put in the background to
the foreground. So, if you have multiple processes in the
background and want to bring a different one up, you
need to use is's job number. Put emacs in the background again and type::

  jobs

in the command line. This command tells you about the
processes, or jobs, that you have running in your current shell session. If you only have the 1 emacs session running,
you will see it has an id of 1. If there were more jobs,
they would be listed here, each with a unique job number.
You can use the job number to bring a job to the foreground
like so::

  fg %n

where "n" is the job number. With your one processes, ``fg %1`` should bring emacs back to the foreground.

Running your script
-------------------

Ok, with emacs in the background, we are close to being
able to run your script. Try to execute it like you would
any command, by typing the command name::

  % ./first.sh

The “./” tells Linux to search the current directory for the command.
Upon entering this command, you should get an error. The reason is that Linux doesn’t know that this is an executable
file. Before you can execute this command you need to change the **permissions** of the file to be executable.

So back to our example. Give yourself permission to execute the file and then try to run
it again. You should see that the shell outputs the words “Hello World” on the next line
after the call to the script.
That’s a pretty simple script, but it does something. If you haven’t created one before,
congrats- that’s your first program. Now, let’s play around with scripting a little.

Create a
new file called first2.sh::

  #!/bin/bash
  # This is a comment!
  echo "Hello World" # This is a comment, too!
  echo "Hello World"
  echo "Hello * World"
  echo Hello * World
  echo Hello World
  echo "Hello" World
  echo Hello " " World
  echo "Hello "* " World"
  echo 'hello' world
  echo `hello` world

The last line uses the backtick charater which is below the
escape key (not the single quote).

Change the permissions and run it. It’s ok if you get an error or two. Try to make some
sense of whats going on with each line, and if you can’t figure out every line, that’s ok,
we’ll cover all the differences eventually.

Variables
---------

Pretty much every programming language out there uses the concept of variables: a
symbolic name for a chunk of memory to which we can assign, read, and manipulate its
contents. Scripting with the shell is the same. You may be familiar with a few variables
already, such as ``user``.
Lets play with the ability of Linux to be able to handle variables. Open up another file,
call it var.sh or something, and enter the following::

  #!/bin/bash
  my_message="Hello World"
  echo $my_message

This assigns the string “Hello World” to the variable
my_message, then echos the value
of the variable. The shell does not care about the type of variable used. It can store
strings, integers, real numbers, etc.

.. Note:: The shell is picky about spaces. This won’t
  work if you put spaces around the equals sign.

Note how the shell refers to variables. The third line of the above script includes the
$ character. If you remove this, then the echo command won’t know that my_message
is, in fact, a variable, and will simply write the word “my_message” in the terminal.
Requiring a special character to signify that a certain word is a variable is not typical of
most programming languages any longer, but it is the case when using the shell.
It is possible to interactively set variable names using the read command::

  #!/bin/bash
  echo What is your name?
  read my_name
  echo "Hello $my_name! I hope things are going well."

Certain programming languages, like C and Fortran require you to declare variables and
their type before you use them. This is not the case in most shells. What this means is
that if you try to reference a variable that has not been set, you will get an empty string,
and not an error. For example try running this::

  #!/bin/bash
  my_variable=500
  echo $my_var
  echo $mv_vra

You should see that the second echo doesn’t actually do anything, since the variable
name is misspelled. This can be a tricky source of bugs in your code, because in most programming languages, trying to print a variable that hasn’t been set would give you an
error.

Scope
-----

If you were to set a variable in the command line and then try to use it in a program it
wouldn’t work. Try it. First create a simple script, myvar2.sh::

  #!/bin/bash
  echo "my_var is: $my_var"
  my_var="hi there!"
  echo "my_var is: $my_var"

Once you’ve done that, go back to the command line and run the script. You will see
that the first echo gives you nothing, and the second spits out the string “hi there’!”
Now, try setting the variable in the command line (not in the script)::

  % my_var=”hello”

and test that it is set using echo in the command line.
Next run the code::

  % ./myvar2.sh

The output should be the same! The reason is that when you set a variable, as we have
been doing, the variable by default is local to the current shell. When a command is
executed, Linux actually spawns a separate shell to run the command. If we want to make
the variable available to all sub-processes started by the current shell, we want to change
the **scope** of the variable. This is done in bash using the ``export`` command. So, execute this in the command line::

  % setenv my_var hello
  % ./myvar2.sh

Now you should see the variable is set already when we call our script.

The concepts covered here are just the basics of shell
scripting and enough to get you started. Of course, we
can do a lot more with scripts, including looping, logic, etc. We'll save that stuff for another lesson.
