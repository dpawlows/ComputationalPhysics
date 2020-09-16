Basic Linux Commands 2
======================

You should be logged into a linux computer, such as
serenity, to follow along with the examples in this
lesson.

Now that we have a basic understanding of
the Linux filesystem and know how to create and remove files and directories, it’s time to add more commands to your tool belt so that you can start
doing something useful.

more
^^^^

You’ve learned how to quickly display the contents of a file using cat. But what if the
file is huge? For example, try::

  >> cat /var/log/system.log

You should get a lot of text printed to the screen. Now you could use the mouse wheel
(if that even works) to scroll up through the text, or an alternative is to use *more*::

  >> more /var/log/system.log

Now you should see the first “page” of text, and you can advance through it using the
space bar or the page up/page down keys. Pressing *q* will allow you to exit without
needing to go all the way to the bottom.

head/tail
^^^^^^^^^

Maybe you don’t need to see the whole text, but you just want to see the first or last few
lines. Then you’ll want to use the head or tail commands::

  >> more /var/log/system.log

will show you the first 10 lines of the linuxsystem.tex file, while
::

  >> tail /var/log/system.log

will show you the last 10 lines. Adding the *-n M* flag will show M number of lines
instead of the default 10.

Pipes
^^^^^

Recall that we can use *>* to redirect the output of one command into a file. Similarly, Linux offers us the
ability to take the output of one command
and **pipe** it into another command using the " | "
character.
For example::

  >> ls /usr/bin | more

Here, we list the contents of ls, but instead of
printing all of the files to the screen in one go, we are piping the output into the more command. This causes the output to be printed page-by-page as above.

Piping is an extremely powerful feature of Linux, and this simple example doesn’t do
the command justice. Piping can be used to do
simple tasks like viewing output easier and to do some more
complex tasks like perform data analysis operations.

grep
^^^^

grep is an extremely useful command that searches a file or files for text. For example let's say
created a program to solve laplace's equation but I can't remember the name of the file. So, I want to search
my directory for python files that contain the word "laplace"
::

  >> grep -Hi laplace *.py

In this context, the grep command has two required arguments, the
string to search for (laplace) and where to search (\*.py). This command tells Linux to search all the files  in the above directory that end with ".py" for the word laplace. The result will be
all the lines of text, all of which include that word.
I've also included two optional flags: the -H flag tells grep to return
the name of the file that the word appears in and the -i flag causes grep to ignore case sensitivity.
grep is obviously useful for searching files, but it can also be useful attached to other
commands::

  >> ps aux | grep -Hi ’username’

will tell you information about all the processes that are being run by you on this computer. There probably aren’t many. If you replace your username by mine, dpawlows,
you should see a few more.

ps
^^

The ps command is useful when you want to see what processes are eating up computational resources, and if you need to kill an unresponsive process, provided you are the
owner of the particular process. This is done using the kill command::

  >> kill ’pid’

where ’pid’ is the process id number, the number in the 2nd column of the ps output.
For example, try::

  >> emacs -nw &

Hit enter a couple times after that to bring the prompt back. You’ve just started the program emacs, a text editor,
and then put emacs in the *background*. This means
emacs is still running, but you can't interact with it until you bring it back to the *foreground*. Let's say you can’t get it back into the foreground in order to
close it. You can use ps and kill::

  >> ps aux | grep ’username’

note the pid of the emacs process. Then,
::

 >> kill ’pid’

You will need this because sooner or later, you will start a process and put it in the
background, forget about it and log out of the remote
computer. Since the process is in the background,
it will not necessarily end. Later on, you can find it again and kill it using this command.

Finding files
^^^^^^^^^^^^^

The most useful command for finding any file on your system is the *find* command. find
has a ton of options which may be useful, but the best uses are the following::

  >> find . -name ’string’ -print

will search the current directory (.) for a file called string. You can include wildcards in
both the directory (replace . with any directory), and in the string (if you include the
quotes). For example::

  >> cd ∼dpawlows/UpperAtmosphere
  >> find * -name ’champ*’ -print

will search my UpperAtmosphere directory for files starting with the string champ.
If you include the grep command, find can find a file anywhere in the system that
contains a string inside the file.
::

  >> cd ∼dpawlows/idl
  >>  find * -exec grep -Hi ’champ’ ’{}’ \; -print

will output the lines and files that include the word ’champ’ in them. The syntax is
complicated, but necessary. Note that this is useful if you really have no idea where the
file is, but remember a specific word or phrase contained in it.
Depending on how you use this, it can take a very long time and search a lot of stuff.
For this reason, the *locate* command can be better, if it is available.

Sort
^^^^

The sort command is a easy to use utility that can quickly sort data that
is stored in a file in a table format. Sort is pretty powerful, but
knowing the basics is usually enough to make quick work of examining a
dataset. Let's say you have the following data in a file
called fruit.dat:

=====     ====      ====
Banana    5.2       1001
Apple     32.1      1002
Pear      101.8     1003
Grape     7.5       1004
Melon     47.2      1005
=====     ====      ====

We can quickly sort the data using sort::

  >> sort fruit.dat

You should see the data has been sorted by the first
column in the file. Easy enough. However, there are a
couple flags that are needed to really use sort. First,
what if we want to sort based on the 2nd column?::

  >> sort -k2 fruit.dat

Note that something happened here, but maybe not what
was expected. Sort treats all data in a file the same,
as a character string. So in this example, sort looked at the data
an put the string that started with a "1" first. But most likely
we want that data to be sorted as if column 2 was numerical
data. To do that, we need another flag::

  >> sort -nk2 fruit.dat

That should give the expected result, with the banana
row at the top of the output and Pear at the bottom.

Don't forget that it can be useful to combine a sort
with redirection to send the output to a new file::

  >> sort -nk2 fruit.dat > fruitsorted.dat

Linking files
^^^^^^^^^^^^^

It is often useful to link two files together. For example, try::

  >> cd ∼
  >> ln -s ∼dpawlows/Public/Phy380/ Phy380

This will create a **soft link** in your home directory that points to the Public Phy380 folder.
Now, if you want to cd into that directory, you just have to do
::

  >> cd ∼/Phy379

and if you want to copy a file to that directory or a subdirectory of that directory, it's
quick and easy
::

  >> cp homework1 ∼/Phy380

This works even though the folder that Phy380 is linked to isn’t in a folder owned by you.
