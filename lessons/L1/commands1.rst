Basic Linux Commands 1
======================

In order to work with a Linux based operating system, you have to become familiar with
Linux commands. There are many, and throughout this course you will become familiar
with a lot of them. Here we will get started with some of the most basic ones.

Nearly every Linux command has documentation called **man pages**. You can access the man
pages by typing:
``>> man command-name``
for the appropriate command. This will bring up a document in your terminal window that you can navigate through
using the up and down arrows to scroll line by line, and the space bar to advance to the
next page. Man pages tend to be a bit cryptic in that they are meant to be brief and
understood by people with a strong Linux background. Understanding the details may
be tricky, but you should be able to look at a man page and get an understanding of
what a particular command is supposed to do, and also see some of the options for that
command.

We talked about command arguments in the introduction to :ref:`theterminal`. Additionally, just about every Linux command has some options that you can specify when using
the command. These options are referred to as **flags** and  are either indicated by a single
hyphen “-” followed by a letter (e.g. -r), or a double hyphen “\\-\\-” followed by one
or more words (e.g. \\-\\-recursive). These flags may be similar or different for different
commands (often commands that do similar things have similar flags).

Files and Directories
---------------------

Linux is all about manipulating files. The following commands will allow you to work
with files (and directories); you will use these a lot.
First, a little more detail about what is going on when you are working in the terminal.
When you first login to a Linux system, the directory that you are accessing will be your
**home directory**. The home directory has the same name as your user name, and it is
where all of your personal files and subdirectories will reside. You will be able to create,
remove, or move files and directories in you home directory, but you will not be able to
do so in any directories higher in the file hierarchy (more on this later).

Lets start doing
a few things in your home directory.

ls (list)
^^^^^^^^^

To find out what is in the current directory, you can use the ``ls`` command. This will list
all the files and directories that are in your current working directory (which I will call
**cwd** for short). On a typical computer you might see several files such as Desktop,
Documents, Downloads, etc. These files are actually directories and may or may not
contain other directories or files.

The ls command as you used it only told you the contents, nothing about the contents.
To see more, use::

  >> ls -l

The -l flag stands for “long”. This tells you much more information about what is in
a directory. We will talk about some of the information later, but a few notes on what
you are looking at:

1. If there is a “d” in the first character of a line, that means the
corresponding file is a directory.
2. You should see your username in the 3rd row. This
tells you that you are the owner of the file, and therefore, you control the permissions
(who can read, write, or execute) for the file.
3. The row before the date tells you the
size of the file or directory in kilobytes.
4. The date is the timestamp that signifies the
last time the file or directory was modified.

Another useful flag for ls is **-a**::

  >> ls -a

This will show any “hidden” files. A file may be hidden in Linux by having the first
character of the filename start with '..' You will notice that there are 2 strange files
’ . ’ and ’ .. ’ . The directory, ’ . ’ is Linux for "the directory that you are currently in", while ' .. ' is Linux for the
directory one level up in the hierarchy. So, for example you could execute:
``>> ls -a .``
and you would see the contents of your cwd, exactly the same as ls -a. Or, you could do:
``>> ls -a ..``
to see the contents of the directory one level up.

In the last two examples, ' . ' and ' .. ' were arguments provided to the ls command. I
could replace the either of those with another directory to see its contents. Also, you can
combine flags::

  >> ls -la Documents

would show you the contents of the Documents directory, in long format, including hidden files.
There are many more flags that you can use with ls, and I’ll leave it to you to explore
them. Those covered here tend to be the most useful.

cd (change directory)
^^^^^^^^^^^^^^^^^^^^^

Now that you can see the contents of a directory, it is useful to be able to more around
the file system. The command
``>> cd directory``
will change the cwd to “directory”. For example, assuming you are in your home
directory, you can change to Documents using::

  >> cd Documents

Now you can do an *ls* to see the contents, if there are any. To get back to your home
directory, which is one level up in the hierarchy, you do::

  >> cd ..

You can confirm to yourself that you are back in your home directory by doing a ls.

**Try it yourself: What happens if you run the command cd . ?**

One last note on cd, if you type the ``cd`` command with no arguments, you will change
directories to your home directory.

mkdir (make directory)
^^^^^^^^^^^^^^^^^^^^^^

The ``mkdir`` command will create a new directory. mkdir
needs one argument: the name of the directory to be created.
::

  >> mkdir Linux

After executing this command, typing ``ls Linux`` will show the contents of your newly created directory, which should of
course, be empty.

pwd (print working directory)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A **file path** tells you where you are in relation to the entire Linux filesystem. Let’s say
you are in your home directory. Executing the command::

  >> pwd

will print the path of your current working directory. In my case, it is simply
“/Users/dpawlows”. We will talk more about the filesystem later, but you
should know that each of your home directories should be in the /Users directory. /Users or /Home is where you would  typically find the home directories of all users on a Linux
computer. You can
change into this directory and see this for yourself::

  >> cd /Users
  >> ls

Doing this should show you a list of everyone’s home directory. What happens if you
try to make a directory here?
::

  >> mkdir temp

Since you are not the **owner** of this directory, and the permissions for the directory are
set such that the owner is the only one that can write to it, you get an error. If you do a ``ls
-la``, you will see that the owner is someone named **root**. The root user, also know as the
**superuser**, is the user that has permission to do anything they want on the system. root
is an account on every Linux system, and it can be very dangerous to use the root account. When you are logged
on as root, you can delete, rename, modify, etc. any file on the system, including those
that are required for performing system tasks. For this reason, most people try to avoid
logging on as root unless it’s absolutely necessary. You will not have access to the root
account on this machine for obvious reasons.

mv (move)
^^^^^^^^^

You can move a file from one directory to another **and/or** change the name of the file itself using the
``mv`` command. This doesn’t copy the file; i.e. you only end up with one file after the
command has been executed. If you change directories to your home directory, and
make a new directory called ’temp’, you can change its name to MyFiles by typing::

  >> mv temp MyFiles

Alternatively, you could move the temp directory out of your home directory and into another directory completely by typing::

  >> mv temp Documents/

or do both::

  >> mv temp Documents/MyFiles

The system is smart enough to adapt its behavior based on the types of files that you are working with.

cp (copy)
^^^^^^^^^

If you want to copy a file or directory, you use the ``cp`` command. For example, try this::

  >> cp /Users/dpawlows/Public/Phy380/assignment1.txt .

Note the “ . ”. cp requires at least **2** arguments, the source file (1st argument, the file that you want to copy) and the target file (the directory and name of the file that you want to copy the file to). If
you just specify a directory for the target file, as in this case, then the target file has the
same name as the source file. This command should put a copy of the first homework
assignment in your working directory.

rm (remove file)
^^^^^^^^^^^^^^^^

To delete (remove) a file, use the rm command::

  >> cp assignment1.txt temp
  >> ls
  >> rm temp
  >> ls

You can use rmdir to remove a directory (make sure its empty) or ``rm -r`` to recursively
remove directories and all the files inside (**Careful, this can be dangerous!**). It is common
to include the -i flag when using rm, which stands for interactive; e.g. ask before actually
deleting anything.

cat (concatenate)
^^^^^^^^^^^^^^^^^

Lastly ``cat``: a pretty useful and powerful command.
Its primary use is to display the contents of a file to the screen. For example, in the
directory that you copied the first homework assignment, you can type::

  >> cat assignment1.txt

This will write out the contents of that file to the screen. Note that it doesn’t know what
to do with formatting, or program specific characters (i.e. if you tried to use cat on a
word document, you would get a big jumbled mess). ``cat`` can be used to read normal, basic,
text.
But cat can do more, you can also create a file using it::

  >> cat > newfile

When you use cat like this, the Linux prompt doesn’t come back! Linux is waiting for
you to do something. Anything that you type will be placed into a file called newfile.
When you are done typing, press control-d to tell Linux that you are done, and you will
be back at the prompt.

Here cat is being used as a
really basic text editor. The ">" symbol has special
meaning in Linux. When used, it is called **redirection** in that you redirect output from one command into a file (generally). Here, using the cat command with no arguments
gives us a simple space to enter some text. Then, that text would normally be written to the screen. Instead, we use redirection to print the text to a file.

If you do an::

  >> ls

you will see a file called newfile, and if you want to see the contents of the file, you can
use::

  >> cat newfile

You can use ``>`` with any
command that gives output. For example, try::

  >> ps aux > tempfile

This will print a bunch of information on the processes that are currently running on
your machine into the file tempfile. You can see this by typing::

  >> cat tempfile

You’ll notice that if you run the ps command above over and over again, you don’t
actually add anything to tempfile. When one ’>’ is used, Linux creates a new file, and
if one exists, it just overwrites it. However, if you use two of them ’>>’ then Linux will
**append** the file that you are trying to redirect to. For example::

  >> cat assignment1.txt >> tempfile

will place the contents of assignment1.txt at the end of the existing contents of tempfile.

In this manner, cat can be used to do powerful things. Later on we will talk about writing
scripts, small programs that are comprised of one or more lines of Linux (or
other) commands. Being able to manipulate files using cat can be extremely useful in
this context.
