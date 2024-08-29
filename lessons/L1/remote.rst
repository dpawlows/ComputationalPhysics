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
to access remote computers via PowerShell. In modern versions of Windows, ssh 
is included by default and can be used just like described for `Linux/Mac Users`_.

SSH keypairs
------------

Modern cybersecurity best practices include shutting off password authentication in favor of using a public/private
keypair for users that 
ssh into a remote computer. We will embrace this practice here. I won't go into the details 
of how public/private keypairs are implemented (see `e.g. here <https://en.wikipedia.org/wiki/Punched_card>`_ or 
other similar resources online). Essentially, we create a public/private key pair on our "local" computer. Then, we 
can share the public key with other remote computers that we would like to log in to. When we attempt to log in 
to such a computer, the remote computer confirms that we are a legitimate user by sending an encrypted message 
to your local computer than can only be decrypted with the private key. This is done and the unencrypted message 
is sent back to the remote computer proving that you should be allowed access. 

The process is as follows:
1. Create a public/private key pair using the ``ssh-keygen`` command in the .ssh folder on your local machine.
2. Transfer the file containing the public key to the remote computer.
3. Add the public key to the ~/.ssh/authorized_keys file on the remote computer.
4. Remove the file containing the public key on the remote computer (if desired).

With the two keys in the correct locations on each computer, you should be able to access the 
remote computer without using a password. The system administrator of the remote computer may require 
that you use ssh key authentication as part of the login process. 

Remember, private keys are *private*: they should never be shared. Public keys may be shared freely.