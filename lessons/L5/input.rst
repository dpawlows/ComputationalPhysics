Python Input and Output
=======================

There are many methods to reading and writing
input from/to a file in python. Here, we will
cover the basics and emphasize an approach that
will work for just about any programming language.

Reading data from a file
------------------------

In order to read from a file, there are really 4
steps that you need to follow:

1. Open the file
2. Read the file
3. Parse the input
4. Close the file

Steps 1 and 4 are pretty simple and implementing them is basically the same for all circumstances. Steps
2 and 3 will depend on the particular problem that you want to solve.

Opening the file
is done using the ``open()`` function. Given
a file called "data.dat" we can open it with::

    >>> f = open('data.dat','r')

Notice that the ``open()`` function requires two
arguments- the name of the file that you want to
open and a second string, 'r' in this case. The
'r' tells python that we want to *read* the file.
We could have opted for 'w' if we wanted to
*write* to the file, 'r+' if we wanted to
read and write (update) to it, and 'a' if
we wanted to read and append to it.

The other thing to note is that we saved the result
of this function, which creates a python *file object*, to a variable, *f*. We must do that
so that we can access the tools (or methods) of the
file object that allow us to read the file, close it,
etc.

One of the methods of the file object is ``read()``::

  >>> mydata = f.read()

This will read the entire file and store it as a character string in the variable *mydata*.
I don't think that this is particularly useful, as
parsing the data in that file can be a bit tricky.

At this point, if you try to read the file again::

  >> mydata = f.read()

you will get an empty string. This is
because python keeps track of the parts of the file that have been read already. Think of it as
python setting a marker at the beginning of the
file when it is opened, and then moving the marker
as each part of the file is read. So, if the entire file
has been read, python's marker will be at the end of the file, with no more data available to be read.

At this point, the only thing to do is to close the
file::

  >>> f.close()

The technique that I suggest to use when reading
a data file is to read line by line. Python makes
this really easy. Let's open the file again so
we can start fresh::

  f = open('data.dat','r')
  for line in f:
     print(line)

Python treats a file object as an iterable! Further,
each line is a single element of the iterable.
So, we can use a for loop to iterate through
the file and read it line by line.

At this point, all that is left is for us to parse
the data. This is really where it comes down
to the specific problem that you are working on.
However, there are a few specific tools to be
aware of.

First, when python reads a file, it stores the result
as a string. You can verify that by using the
type function::

  type(line)

In physics, we often deal with numerical data that is organized in columns with in a file. For this
reason, it can make sense to take that string
and split it on a delimiter. For example,
let's say you just read a single line and
it has the following data::

  2003 10 26 03 25 00 5.4 3.2 100 95.2

Upon reading, python stores all of that information
as a single string, not very useful to us. Luckily,
I can parse that string and turn it in to a python
list using the ``split()`` method of the string
object::

  data = line.split()

This will result in a new variable called data
which is a list that is made up of the data in
the line variable. By default, ``split()`` will
break the data up by whitespace. So our data
list should have 10 elements. Note that
if my data were separated by a different delimiter::

  2003, 10, 26, 03, 25, 00, 5.4, 3.2, 100, 95.2

I can specify a delimiter when using ``split()``::

  data = line.split(',')

Splitting a string may be useful when reading data
in from a file, but really, it depends on how
the data is formatted in that file. Just
know that there are many tools that come with
the **string** datatype that can help you
to parse your data, including the ability
to search for a substring, extract a substring,
etc. Additionally, at this point, you may
need to perform some type conversion operations,
store only part of the imported dataset, etc.
This can all be handled within the for loop
during the file read.

Finally, don't forget to close the file
when you are done reading it::

  f.close()

As a complete working example, imagine that
I wanted to read a file called "euv.dat" that
consisted of several lines formatted as above::

  2003 10 26 03 25 00 5.4 3.2 100 95.2
  2003 10 26 04 25 00 5.2 3.0 110 98.3
  ...

I only want to save information about the date
and the 8th column of the dataset. The following code snippet should do the job, including type conversion::

  from datetime import datetime

  filename = 'euv.dat'
  f = open(filename,'r')
  date = []
  data = []
  for line in f:
    temp = line.split()
    date.append(datetime(temp[0],temp[1],temp[2],\
      temp[3],temp[4],temp[5]))
    data.append(float(temp[7]))

  f.close()


Writing to a file
-----------------

Another method of a file object is write. Open up another file::

  >>> g = open(’somedata.txt’,’w’)

Now we can use the write method to write to the file::

  >>> g.write(’Hello there!\n’)
  >>> g.write(’This is some text...\n’)

You need to include the "\n" character if you want to start a new line. if you want to write
something other than a string, you have to convert it to a string first::

  >>> value = (’the answer’, 42)
  >>> s = str(value)
  >>> g.write(s+’\n’)

Again, remember to close the file when you are done.
::

  >>> g.close()

Once the file is closed, you can look at it in a text editor.
