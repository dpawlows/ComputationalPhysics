Remote Computing Using SSH
==========================

As part of being a physics major, you have access to a
remote Linux server called *serenity*. Our first task will
be learning how to access this computer using an application
called SSH.

Linux/Mac Users
---------------

For Linux and Mac users, this is very easy. You simply need
to open up the Terminal and use the ``ssh`` command. Execution
looks like this:

``>> ssh [username@]hostname``

Again, the >> are meant to indicate the prompt. ssh takes
1 argument. That argument has a required part (hostname)
and an optional part (username@). When looking at documentation
for linux commands and often programing in general the [ ] symbols
are often used to designate optional parameters.

.. note:: ssh stands for "Secure Shell" which is a remote
          computing protocol that is "secure", i.e. people
          that are snooping on your internet connection can't
          see the information that you are sending to or receiving
          from the remote computer. This was not the case for all previous
          remote login commands.

The hostname is the name of the computer that you are logging into.
You all have an account on the computer **serenity.emich.edu**.
That is the complete hostname for serenity. Your username
on that computer is the same as your emich uniquename. The reason
the username is optional is if the username on your local
computer (the computer that you are sitting in front of) is the same as that on the remote computer, then
you don't have to write it out.

So, if I wanted to log into serenity, I would execute either

``>> ssh dpawlows@serenity.emich.edu``

or

``>> ssh serenity.emich.edu``

depending on if my username on serenity is the same as
that on my local machine.

Logging in for the first time
-----------------------------

Let's say I was going to log onto serenity for the very
first time using the command ``>> ssh serenity.emich.edu``.
When I execute this command, my local computer will check to see if the remote
host (serenity) is to be trusted. It
does this my looking in a file on your computer called the known hosts file
for information about
the remote computer. If it doesn't find any information
about that computer, it will tell you and then ask you
if you are sure that you want to proceed. Assuming you know
the computer that you are logging into, you should
answer "yes".

At that point, information about the remote computer
will be added to the known hosts list on your computer
and you won't get that message in the future (unless
something about that machine changes).
Then, you will be prompted for your password and you
can enter it. Note that as you type your password,
no characters will show up on the screen as this
would be an obvious security flaw.

If you entered your credentials correctly, you should be logged
into serenity, at which point you can interact with
the computer via the Terminal as if you were sitting in front
of it.

SSH using Windows
-----------------

Only recently has Windows made it possible to use ssh
to access remote computers via PowerShell. Still, doing
so can be a bit cumbersome as additional software
tools must be installed. Instead, historically Windows
users have opted to use a different SSH client.
One of the most popular of these is called **PuTTy**
and it can be downloaded at https://www.chiark.greenend.org.uk/~sgtatham/putty/
PuTTy doesn’t need to be installed; you just download it and put it somewhere, like the
desktop or in “Program Files” or something.
Once downloaded, just double click the icon, shortcut,
or whatever to open it up.

PuTTy gives you access to ssh via a simple GUI.
One you open PuTTy, you should see the configuration screen.

.. figure:: images/putty.png
    :width: 400
    :align: center

    The PuTTy configuration screen

The most important information that you need to specify
is the Host Name (serenity.emich.edu) and the port (22, the default port for ssh).
There are all sorts of
configuration options, but you don't need to deal with any of these unless you want to do exciting things
like change the color of the terminals that you open and use a specific
font size and type. As you get the hang of using PuTTy feel free to change these at will. Additionally, you can
save a session which will allow you to store information
about a hostname and other configuration options
for easy use in the future.

Once you have a hostname entered, you can click "open" and
PuTTy will attempt to establish a connection to the
remote machine. Again, if this is your first time connecting,
you will get a message about the remote computer
not being in the known hosts file and you can just say yes,
you do want to connect. Then, you will be prompted for your
username and password. If successful, you will be given a
terminal window which will allow you to enter commands
and run programs on the remote Linux computer.

SSH in Powershell
^^^^^^^^^^^^^^^^^

Like I mentioned, it is possible to use ssh via
PowerShell. There are a variety of ways to make this
happen. In my opinion, the easiest way is to install
the OpenSSH Client using a package manager (a utility that
handles the downloading, installation, and updating of
software packages so you don't have to). I don't have
much experience with Windows package managers, but I
have heard ok things about **Chocolatey**.

You can find instructions for downloading and installing OpenSSH and Chocolatey here: https://medium.com/@haxzie/using-ssh-in-windows-powershell-complete-installation-guide-ae029a9e3615

Once OpenSSH is installed, the ssh command should be
available to you via PowerShell and it can be
used just like described for `Linux/Mac Users`_.
