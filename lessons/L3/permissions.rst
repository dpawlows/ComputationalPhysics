File Permissions
----------------

On a linux system, files can have different permissions
for different users. A given file may be readable, writeable, or executable (or none of these things). In
order to execute a command, it must be executable.
If you run::

  ls -l

and look at a given file in the list, you will see something like::

  -rw-r--r--

in the left most column. There may be more than 10
characters printed, but we only care about the 1st 10.
The first character, a hyphen in this case, tells us the
file type. Generally, there are two options here: a regular
file (which gets a hyphen) or a directory, in which
case we would see a ``d``.

Then, there are **three sets of three** characters. Each set
describes the file permissions for three different groups
of users. The
first set are the permissions for the user (u) that
owns the file (the owner is the third column in the output from ls -l). The 2nd set of three characters are the permissions
for the group that the file belongs to (4th column in the
ls -l output) and the 3rd set is for everyone else (o for other) that
has access to the computer.

New files that you create are assigned, by default, read/write (rw)
permissions for you (the owner) and read (r) permissions for
the group and other. If you want to change the permissions
of a file we
use the command chmod.

chmod takes at least 1 file as an argument, as well as
a sequence of letters or numbers that specify what the permissions should be. There are several different ways
to assign permissions.
In order to change the permissions for the u
that owns the file, you would do something like this::

  % chmod u=rwx file

Note that only the owner of a file, and root, can change the permissions of a file. This above
example tells Linux to give the user (u) that owns the file read (r), write (w), and execute
(x) permissions. Similarly, you can change the group’s permissions::

  % chmod g=rx file

gives all members of the group (g) that the file belongs to read and execute permission.
Finally, you can change the permissions for everyone else::

  % chmod o=r file

gives read only permission to other.

Chmod has a few shortcuts worth noting- let’s
say that you wanted to give everyone permission to do anything to a file::

  % chmod ugo=rwx file

Note that we just combined the 3 types of users.
Careful with that one, it means everyone with access to the
computer can do whatever they want to the file, including delete it. Alternatively, we could have done
::

  % chmod a=rwx file

where a stands for all types of users.
You can also add permissions to the existing ones by
::

  % chmod u+x file

This says to take the current permissions and add executable permission for the owner.

Finally, you may see usage examples where permissions are
specified with a number sequence, such as::

   % chmod 751 file

This is a shorthand which specifies the permissions for each
of the groups separately, each number corresponds to a
different user, e.g. u gets the number 7, g is assigned 5,
and o assigned 1. The numbers range from 0 - 7 and are derived by adding up the bits with values 4, 2, and 1.
Where 4 represents read permissions, 2 write, and 1 execute.

So in the example above, 7 = 4+2+1 means u gets rwx permissions, 5 = 4+1 means g gets rx, and 1 means
o gets just x permissions. This is the quickest way to
assign different permissions to all user classes.
