The Shell
=========

One of the most important aspects of the Linux system is the shell. When
you open a Terminal, you are gaining access to a shell session. The shell determines how
you enter and re-enter commands and handles
the execution of the commands themselves. One of the great features about Linux is there are
different shells that you can choose from. While each shell has the same set of general features, all have different  capabilities that may be useful depending
on your situation.

In order to find out which shell you are using, you can use the command::

  >> echo $SHELL

Note that capitalization matters on most Linux systems.
``echo`` is a command that tells Linux to display information about a variable. It is similar to *print* in python. In this case we pass 1 argument to *echo*: the variable named SHELL.
The $ character is Linux’s way of differentiating between a word and
a variable (something that stores information).

The system’s response to the echo call above will be to display the full path to your shell;
/bin/bash. You are using the bash shell because that is what was specified when your account was created.
By the way, bash stands for Bourne Again Shell, an extension of the original unix shell, sh.
Typically, the shell you start learning with becomes the one you stick with.

You can see which shells are available to you if you type::

  >> cat /etc/shells

and if you would like, you can change your shell with the ``chsh`` command.

Common features
---------------

There are a few features that are extremely convenient and available in most shells.

Tab completion
^^^^^^^^^^^^^^

cd into your home directory and type (but don’t hit enter)::

  >> cd Desk

Now, hit the tab key.
Most shells have a feature which will automatically complete the word you are typing
when the tab key is pressed. In this case, the shell should have auto-completed the rest
of Desktop/ . By default, this will only work if there is only one possible match. If there
is more than one possible match, the shell will beep at you and wait for you to type in
enough letters to distinguish the two (or more) files.
You can use tab completion to complete commands, directory names, filenames, and
pretty much anything else you might enter into the command line that is sufficiently
unambiguous.

It you enter some text into the shell and hit tab to autocomplete, but there are more than
one possible entries that fit the text that you’ve entered, there is a way to have the shell
return a list of possible completions instead of beep at you annoyingly. Ask me how to
do this later (it involves modifying a configuration file. Don’t worry, it’s easy).

Viewing session history
^^^^^^^^^^^^^^^^^^^^^^^

Most shells will save a history of the most recent commands that you have entered. Use
your shell for a little while, changing directories, listing files, redirecting output, etc.
After you have entered several commands press the **up arrow** once. You should see the
last command that you typed. You can continue to press up or down to cycle through
your most recent commands, and when you find the a command you wish to re-enter,
simply press enter.

As you cycle through the commands, you are able to modify any of the lines simply by
using the left and right arrows.
Next, use this ``history`` command::

  >> history

You will get a list of the most recent commands and what time you entered them.
You can re-execute any command by referencing the number in the history list::

  >> !10

would re-enter the command that corresponds to the 10th entry in your history.

Scripting
^^^^^^^^^

All shells make it possible to combine one or more commands
in a file for repeat execution. These files are
called shell scripts and are extremely useful for
expediting tasks that would otherwise take a long time,
such as performing batch actions on many files at once,
reorganizing a part of your filesystem, or handling
routine computer maintenance tasks.

With in a shell script, it is possible to do
all of the typical programming actions, including using
loops, conditional and comparison statements, and logic.
However, each shell has it's own syntax so if you become
proficient at making bash scripts, you will still have
to review syntax if you want to make tcsh scripts.

We wont address scripting specifically in this class
as it's beyond the scope, but know that if you find yourself
repeating the same tasks over and over when using Terminal,
it might make sense to package those commands in a
file and create a script.
