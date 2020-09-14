Shortcuts and wildcards
=======================

The only device that we use to interact with the
Terminal is the keyboard. So, in order to be able
to do things like navigate the filesystem quickly
and
perform operations on multiple files at once,
there are a variety of shortcuts that you
must know.

Directories
-----------

Because a user’s home directory is used so frequently, it is treated specially by Linux. To
see this, navigate away from your home directory, if you haven’t done so already. Now,
enter
::

  >> cd

(nothing after the cd command). After hitting enter and typing
::

  >> pwd

you will see that you are back in your home directory. Linux assumes if you do not enter an
argument after the cd command, you want to go to your home directory.

Next, type
::

  >> cd -

(that’s a hyphen). This should take you to the last directory that you were in. Using the hyphen is a quick
way to bounce back and forth between two locations in your
filesystem.

Now, let's say you wanted to go to your Documents directory. You could cd to your home
directory, then cd again to Documents. Or you could enter the full absolute path, */Users/dpawlows/Documents/*.
But, the easiest way is to do this is to use
::

  >> cd ~/Documents

Linux gives special meaning to the tilde: ~; when used
in the command line or in programming in general, ~  represents your home directory. Typing ~
is exactly the same as typing /Users/dpawlows/ (in my case). This is simply to make
life easier, as all the directories that you will create and use will reside beneath your
home directory.

Wildcards
---------

One of the most useful features of Linux are called wildcards. Think of these as placeholders for omitted characters. For example, say you are looking for a file, but
aren’t sure if you named it physicsprogram or physicsscript. You can include a wildcard to
stand for the part of the filename that you are uncertain about. For example, you can try
::

  >> ls phyics*

This would list all files that start with the letters "physics". This could include, if they
existed, physics, physicsprogram, physicspants, or physics help.
You can use wildcards for just about any purpose in Linux, and many programming/scripting languages (such as C++, python, and perl) understand them as well.
Here are a few guidelines:

  - Use ? as a placeholder for one character or number.
  - Use * as a placeholder for zero or more characters or
    numbers.
  - You can include a wildcard at any place in a name; the
    beginning, the middle, the
    end, it doesn’t matter. Also, feel free to use them in multiple places! i.e. *physics*.
  - The ˆ character can tell Linux to exclude a character

As an example, change directories to /usr/bin::

  >> cd /usr/bin

Try listing all files that begin with z. What about all files that have the word “mirror” in
them?
What happens if you do this::

  % ls z[ˆc]*
