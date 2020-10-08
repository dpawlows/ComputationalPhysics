Transferring Files
==================

It is often necessary to move files from one computer
to another. The process for doing this depends on the type of
systems involved. There are a number of graphical application
available for this purpose. On a Mac, I have used CyberDuck.
On Windows, winSCP and FileZilla are both free options. Regardless
of the software type, the process is similar from application to
application. The important thing is that whichever software you choose,
you must have the option to transfer files using either scp (secure copy)
or sftp (secure file transfer protocol).

Graphical Options
-----------------

Upon opening any of these software packages, you will first need to connect
to the remote computer. Often, there is a "Connect" button somewhere
in the menu or perhaps toolbar with some options. In all cases, you
will be asked to specify the Host (e.g. emich.edu or similar) that
you want to connect to
and your credentials on that computer. Depending on the application, you
may have to specify the port (typically 22) as well and you may
have to select which protocol you wish to use to connect (scp or sftp).
With this information
entered, you should be able to initialize a connection to the remote
computer, and if successful, you will be presented with two sub-windows:
one containing a snapshot of your local filesystem and one with a snapshot
of the remote filesystem.

.. figure:: images/filezilla.png
  :width: 550px
  :align: center
  :alt: filezilla main window

  The main window for FileZilla. Not pretty, but it gets the job done.

At this point, transferring files is a simple as dragging and dropping
a file from one computer to another. You should be able to navigate the
remote file system by clicking through folders on the system like
you would if it were local. You should be able to push files to the
remote as well as pull files from remote to local.

Linux scp
---------

While graphical options are available on Linux computers, there is also
a command line option: ``scp``.

The ``scp`` command is similar to ``cp``: you are copying a file from
one location to another. The difference is that since we are
moving a file from machine to machine, we need to include information about the
remote machine in the process. Usage is::

  scp [username]@hostname:’path of file to transfer’ [username]@hostname:’path to transfer to’

The first argument contains information about the file that you want to transfer, and the
second argument contains information about where you want to transfer to.
The username is optional and only necessary if you username on the
two machine differs. The hostname is only included for which ever system
is remote. You should,
in general, include the quote marks with the remote machine argument.

For example, if
I wanted to send a file called "images.tar" to a computer called **yipe**, I would do::

  % scp images.tar dpawlows@yipe.emich.edu:’∼/’

This will copy the file to my home directory on Yipe.

To get a file from yipe::

  % scp dpawlows@yipe.emich.edu:’∼/scripts.tar’ .

will bring the file to my local machine and put it in my current working directory.
If you want to transfer an entire directory, simply include the -r flag.
::

  % scp -r ∼/Documents/ yipe.emich.edu:’∼/’

will transfer my Documents directory and all of its contents to yipe. Note again
that I don’t
actually need to include my username if it is the same on the remote system as it is on
my local machine.
