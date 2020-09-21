Editing Text
============

A computer would have limited use if we could only interact with it by typing
commands into the command line. Instead, most of the power on a computer comes
from being able to store commands in a file and to execute that file multiple
times. However, remember that for early computers, the only way to interact
with the machine was via the keyboard. This meant that there needed to
be software programs that were accessible via the Terminal that could be
used to write and exit text.

These **text editors** are fundamentally different than the **word processors** that
have become ubiquitous. While such software, including Microsoft Word and Google
Docs, is incredibly useful, they can't be easily used to write computer programs
or scripts because what you type is not actually what gets saved in the
file that you create. Instead, text editors are fundamentally what-you-see-is-
what-you-get (WYSIWYG); the software doesn't add formatting rules or notes
to your file, or attempt to automatically apply certain rules as you are
writing.

Linux computers always come with a variety of basic text editors. There are
wars over which of these is superior, but typically, the one that you learn
first is the one that you will prefer. For me, and likely for you, that one is
**Emacs**.

Emacs
-----

Emacs is a free, portable, and extensible text editor that you will find on pretty much
every Linux based system in existence. It works on a variety of architectures and other
operating systems, and as it is quite portable, no matter what system you are on, you
will find that the behavior of emacs is always the same. Emacs is extremely popular
with programmers. If you use a common programming language,
Emacs probably provides a mode
that makes it especially easy to edit code in that language, which provides context sensitive indentation and layout, colors, and even the ability to run programming sessions,
compile programs, debug your code, and interact directly with the language interpreter
inside the Emacs editor itself.

Emacs is much more than a WYSIWYG editor. However, we will be using it mostly in this
capacity.
A fantastic description of emacs resides at the `GNU Emacs website <https://www.gnu.org/software/emacs/>`_.

Notation
^^^^^^^^

Emacs was designed to run on systems that did not have access to devices other than the
screen and keyboard, i.e. no mice. Therefore, the only way to save, open, close, delete,
move the cursor, etc. was by using the keyboard. For this reason, there is an extensive
list of keyboard commands that will allow you to do everything that you need to do
when editing text using the keyboard.
Every keystroke in Emacs is a command. Typing the letter “A” is a command to insert
the letter “A”. There other commands that do not result in a character being printed to
the screen. The standard notation that describes these keystrokes follows:

C-x
"""
For any x, the character Control-x.

M-x
"""
For any x, the character Meta-x. The Meta character is usually the escape key as few
keyboards have the Meta character.

C-M-x
"""""
For any x, the character Control-Meta-x.

RET
"""
The return key.

SPC
"""
The space bar.

ESC
"""
The escape key.

Many, but not all, commands in emacs can be performed using some combination of
the keystrokes above. However, every command has a long name, like kill-line or deletebackward-char. Most typical commands are bound to keystrokes for convenience. This is
called key binding. One of the great things about emacs is that it is possible to create
custom key bindings, or change the default ones to suit your preferences.

Starting emacs
--------------

To get acquainted with emacs, lets start by opening the
editor by typing::

  % emacs temp.txt

at the Linux command prompt. The file temp.txt doesn’t have to exist, it will create one for you and you should find
yourself working within the emacs text editor and not the
command line.

There are just three Emacs commands you absolutely need to
know.
To start, type some stuff in the editor. Once you do that,
you’ll actually want
to **save** your work. So enter::

  C-x C-s

to accomplish this. Note that is two separate key strokes.
You type control-x then let
go and then type control-s in succession.

Obviously, there will be a time when you need to **undo** a
keystroke. This is accomplished
using the
::

  C-x u

key binding.

If you were done editing the file at this point, you would
want to **exit** emacs and return to the Terminal. To do
this you use::

  C-x C-c

Note that if you enter this command without saving your
work first, emacs is smart enough to know that and will ask
you if you want to save (in the minibuffer). In that case, typing 'y' or 'n' will allow you to proceed.

When you execute a command, for example ``C-x C-s``,
emacs will tell you that you just did something at
the bottom of the window in the part of the windows called
the **minibuffer**. When you open a file in emacs,
you open what is referred to as a buffer. You can have many buffers open at once, which
is nice as they are easy to switch through.
The minibuffer tells you information about a command that you may have entered,
provides a space to enter longer, more complicated commands, and gives you options
when working with certain commands.

More basic usage
----------------
Now that you saved a file, lets open another one. From
within emacs, type::

  C-x C-f

In the minibuffer, emacs wants you to specify a file. By default it sets you up to create a
new file in, or open a new file from, your current working directory.
In the minibuffer, type::

  temp2.txt

Now the active buffer should be a file called temp2.txt. You have opened 2 files in emacs
and it is easy to switch between them::

  C-b

This tells emacs that you want to switch to a different buffer. Note this is not the same
as opening a different file. The file already has to be loaded in the emacs’s memory. The
default is the last buffer that you were working with. Since temp.txt is the only other file
that we’ve been working with, that’s the only other option::

  Ret

Now temp.txt should be the active buffer. Open up a few more temporary files, temp3.txt,
and temp4.txt. Now lets switch back to temp2.txt::

  C-b

Note that in the minibuffer, the default is not temp2.txt, since that was not the last one
we worked with. You can just type temp2.txt in the minibuffer to access that one. Even
better though, type::

  temp2

in the minibuffer (leave off the .txt), and hit the tab key. Tab completion works in emacs
just like in the shell. If there are multiple options based on the letters that you entered,
then you will get a list of the possibilities.

If you do something that gives you access to the minibuffer, like type::

  C-x C-f

to open a file, and then decide that you don’t want to actually do that. You can quit the
minibuffer using the::

  C-g

key binding.

Other useful commands
---------------------

When programming especially, it is useful to be able to delete text quickly without
having to hit backspace for every character.
::

  M-d

will delete the word directly after the cursor, and
::

  M-delete

will delete the word preceding the cursor.
Also,
::

  C-k

will delete everything on a single line after the cursor. When doing any of these deletions, emacs automatically copies the word/words that were deleted into memory, and
you can then paste them elsewhere using::

  C-y

This is especially useful, especially for programmers when you often have multiple lines
that are identical, or very similar. Instead of re-typing the entire line, you simply go to
the beginning of the line, type::

  C-k
  C-y
  C-y

and you will now have a copy. See, much quicker.
Lastly, if you just want to move the cursor, but don’t want to have to hit the arrow keys
over and over again, there are a few commands to do that too::

  M-f

will move the cursor one word forward.
::

  M-b

will move it one word backwards.
::

  C-v

will move the cursor down one page
::

  M-v

will move it up one page.

Summary
-------
For now, those commands will get you using emacs, and doing so more efficiently than
a lot of people. Utilizing the word/line cutting key bindings and pasting along with
being able to move the cursor through text quickly can really speed up the text editing
process. And to be honest, it is remarkable how much time is saved by not having to
rely on the mouse to do a lot of things.
One last note. There are literally thousands of command options in emacs. These are
just the basics of the basics. Many of the commands need to be bound to keys manually.
This is done using a file that is read when ever emacs is started up, called .emacs (remember dot files!). This
file must be created by you, and must reside in your home directory (where all startup
files typically go). The syntax for adding or changing commands is a bit cryptic, which
is why its usually just easier to google whatever it is you want to do and find someone
that has done it before. A good place to start for some useful customization is my .emacs
file, which you are welcome to copy and use however you want.
