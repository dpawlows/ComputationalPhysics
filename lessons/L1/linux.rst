Introduction to UNIX/Linux
==========================

A brief history
---------------
In the early days of computing in the 1960s,
software developers needed to find a way for users to provide
instructions to the computer so that it could perform
calculations. The method of using a
keypunch to `punch
holes <https://en.wikipedia.org/wiki/Punched_card>`_
in a piece of paper in a way that could be read by the
computer was cumbersome, time intensive, and prone to error.
Instead, early developers wanted a way to type programs in
to a terminal while enabling a computational environment
which facilitated sharing of resources between many
users. In 1969, a Bell Labs team lead by Ken Thomsen
and Dennis Ritchie accomplished this by creating
the UNIX operating system (OS).

Throughout the 70s and 80s, UNIX's popularity grew in the
computing world and Bell Labs was able to license
the UNIX operating system to a variety of commercial and
educational users. However, the cost of a license was
seen to be prohibitive to an individual user and before long,
members of the
software community looked to make the OS more
widely available by creating alternative versions. The
most famous and widely used version of UNIX was created
by Linus Torvalis in 1991. Linux is considered a UNIX-like
OS in that it retains many of the key components of UNIX
(specifically the `kernel <https://en.wikipedia.org/wiki/Kernel_(operating_system)>`_,
the `shell <https://en.wikipedia.org/wiki/Shell_(computing)>`_, and
the programs). While Torvalis originally released Linux
for no cost, today there exist a variety of free and not-free versions
of Linux, including `Rea Hat <https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux>`_,
`Ubuntu <https://ubuntu.com/>`_, `Suse <https://www.suse.com/>`_
to name a few.

The Linux OS is widely used in computing. It is
found on personal desktop and laptop computers, tablet devices,
mobile devices, servers, and supercomputers. The Android OS is
based on a modified version of Linux. The Mac OS,
while strictly speaking is a different UNIX-like system, has adopted some
Linux specific features over the years.

Reasons to use UNIX-like systems
--------------------------------

As personal computers came to be used more widely by the
generally public, it became necessary to develop software
that made using a computer relatively straightforward
for the lay person. As a result, most people are unaware
of some of the more useful features of the very computer that
they use on a daily basis.
Remember, UNIX, and subsequently Linux,
was designed to 1) make it easy for a user to give instructions
to the computer and 2) make it easy to multitask (or have
multiple users). These features of Linux are
still incredibly useful for today's software developers.
While modern Linux distributions come with sophisticated
graphical user interfaces (GUIs), all of them provide
the user with access to a Terminal program that can be used
to interact with the computer at a basic level.

I would argue that there are several reasons to use
the Linux operating system and the Terminal:

1. Anything that can be done via the GUI can be done (usually more quickly)
   using the Terminal.
2. The Terminal makes it easy and extremely fast to perform common workflow operations
   such as creating files, moving files, copying files, deleting files, etc.
3. The Terminal provides access to tools for logging in
   to remote systems, such as your work computer or a supercomputer.
4. You can use the Terminal to quickly navigate your filesystem and
   to keep track of where you are within it.
5. You can use it to execute many programs and perform operations
   on multiple files simultaneously.
6. The terminal can be used to control access to files that are on a
   shared computer so that certain users can access your files while
   others cannot.
7. The commands that are used to do work in the Terminal can be combined
   in a file and executed from the file, allowing you to essentially
   "program" your workflow.

There are certainly many more, but in summary, using the Terminal
makes performing routine tasks that are performed on a computer
much faster and more efficient. One of the goals of this course is
to get you started with using the Terminal so that you can use it
as an interface to access the true power of your computer.

A note on Windows
=================

You'll note that the Windows operating system was
not mentioned in any examples above. Windows is not
based on a UNIX-like OS and thus it lacks many of the
features that make Linux systems useful for
power users. Instead, from the beginning, Windows
aimed to make computers user-friendly by pursuing an
optimal GUI, one of the main reasons that Windows
dominated the OS market share for many years.
While Windows computers have always come with
a Command Line Interface (CLI) (Note that the Terminal
is often referred to as the command line), the CLI
provided access to lower level system commands via
MS-DOS. DOS was initially developed for single-user systems,
was not built to support multiple processes per
user, and lacks many of the basic commands that
make Linux powerful.

Recently, Windows computers have included a different
program that acts, in someway, to replicate the Linux Terminal: PowerShell.
Windows Powershell offers the user many of the same
commands and features that Linux users use regularly.
If you use a Windows machine, while you will
be logging in to a linux computer to complete assignments
in this course, you should also learn to
use the Powershell.

Linux vs. Windows
=================

None of this is to say that Windows machines are inferior
to Linux computers. Rather, they were initially designed
to be good at different things, and those initial design
choices are still evident in modern computers. Many
software developers choose to use Windows computers
as many choose Linux. My belief is that the Linux
OS offers efficiency benefits to those that perform
repetitive tasks on their computer and that these benefits
can lead to a large time savings over the course
of a project. As such, I personally use a Mac for all of
my work (you may ask why I do not simply use a pure Linux
computer and save $$, not sell my soul to Apple, etc. but that is an argument for a different time).

Many developers choose to purchase or build Windows computers
and then `partition <https://www.computerhope.com/jargon/p/partition.htm#:~:text=When%20referring%20to%20a%20computer,run%20on%20the%20same%20device.>`_
their hard drive so that they can `dual boot Linux <https://opensource.com/article/18/5/dual-boot-linux>`_.
I have also used this option in the past. Ultimately,
the decision of which computer to use often comes down
to which computer you learned to use first (if not which
computer does what you need it to do for less money) and that
is fine. I would urge you to learn how to use whatever
computer you are using at a more fundamental level and
to understand how it can help you do the work that you
normally do faster and more efficiently.
