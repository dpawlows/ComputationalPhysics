Latex
=====

Latex is a document preparation system for high-quality typesetting. It is used by a large
to create documents by a large part of the scientific community
as well as to prepare technical documents in a wide range of fields. I'll start
by saying Latex is not a
word processor. The whole point of Latex is to allow the author to focus on their writing,
and not on the document styling. Latex is great for preparing journal quality articles and
has features that can handle sectioning, cross-references, tables, and figures. It makes
the typesetting of math formulae straightforward and quick. It automatically generates
bibliographies and indices, and seamlessly accommodates the inclusion of graphics.
And yes, it also handles formatting, but it separates the formatting
process out from the writing process so that, again, the focus can stay on the
writing.

Learning how to use Latex can be a frustrating process. But, I absolutely promise that
once you get through the learning pains, Latex will save you an huge amount of time
when preparing your documents. Additionally, they will look much more professional than if
you used other word processors. Ultimately, Latex makes things that are very
difficult to do in other software relatively easy. The cost of this is a
little more effort to get your documents set up. The figure below
summarizes the idea quite well:

.. figure:: images/wordvlatex.png
  :width: 400px
  :alt: Word vs. Latex
  :align: center

  Word vs. Latex: a summary (this version of the plot by JL Blanco, MappingIgnorance.org)

Basics
------

To get started, you will need access to a Latex distribution. There are many.
If you don't have any other option, serenity has a distribution installed
that you can use via the command line. However, in recent years,
web based latex solutions have popped up online and are probably
the easiest way to get started as you don't have to download any
extra software. Today, `Overleaf <https://overleaf.com>`_ is one of the better
options for web based Latex. You can set up a free account which even includes
some limited collaboration options.
If you would prefer to download a Latex distribution, `MikTex <https://miktex.org/download>`_ and `Texlive <https://www.tug.org/texlive/>`_ are both good options.
Before you go any further, set up an account on Overleaf or download and install a
latex distribution.

Many people make the claim that using Latex is like coding your papers. In a sense,
it is. The file that contains your writing also has commands that define the document
structure and formatting. In addition, in order to produce the final document, you have
to compile the latex document. In that sense, using latex isn't as simple
as opening up a document and starting to write. We need to specify some
basic commands to tell Latex what we are doing.

Three things every Latex document must have
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There are three commands every Latex document must have for Latex to compile
(compiling takes the latex commands and allows them to operate on the
content of the document to produce some sort of output, e.g. a final pdf)
successfully. Those commands are: **`\documentclass{ }`, `\begin{document}`
** and **`\end{document}`**. Before we create our first document, let's
talk about these commands in a general sense.

First, note the Latex syntax. All latex commands start with the character
`\`. The backslash is a special character in Latex, which means you can't
just go around using it willy-nilly. If you type that key in a Latex document,
you have to use it properly. Next, each of the commands above were followed by
a set of curly brackets `{ }`. Anytime you see curly brackets in Latex, those
represent a place where you need to include a *required argument*.
Alternatively, you may see commands that use square brackets, `[ ]`. Those
enclose *optional* arguments.

To the first required command. `\documentclass{ }` is required of every
Latex document and it requires 1 argument: the document class. There are several
to choose from: `proc`, `report`, `book`, `slides`, etc. But, you will always be
using the `article` class in this course.

The other two required commands, `\begin{document}` and `\end{document}` tell
latex where the content of the document begins and ends. The `\begin` and `\end`
commands generally define a Latex *environment*. You will use them
often, but with different arguments. The basically allow you to add a variety of
your elements, including figures and tables, to your document. But
the main *environment* is of course the document. Anything that you want to
actually show up in your final document must go between the `\begin{document}`
and `\end{document}` commands. With that, let's create a very simple document::

  \documentclass{article}

  % preamble

  \begin{document}

  Hello World!!

  \end{document}

Use whatever Latex distribution you are using to create a first document
and compile it (typically, if you are using web based software, there is a
recompile or compile button that you can click on). If you have just these
elements, you should see the text "Hello World!" in the output.

In this simple example, I made use of a Latex comment, which is designated
using the `%` character. Any lines that start with that character are
ignored by the Latex compiler. In this example, I wrote the word "preamble".
Any content in our document that comes after the `\documentclass` but
before `\begin{document}` is referred to as the preamble. This space is
reserved for configuration options for our document, defining and redefining commands, and generally setting up preferences. We will talk more
about some of this stuff later, but **generally**
the preamble contains information about document-wide formatting, as well as
information about Latex packages that you may use in the body. The body contains the
content of the document, as well as small scale text formatting commands.
