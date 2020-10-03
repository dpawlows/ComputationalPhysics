Root Finding
============

A common problem in scientific computing is to find the solutions, or roots, of some equation
.. math::

  f(x) = 0

in a single variable x. Numerical techniques are useful because we aren’t required to come up
with a general solution in a closed form, i.e. a function. Typically, a numerical solution is found
by starting with approximation to the answer, :math:`p_0`, and steadily improving the solution :math:`p_1`, :math:`p_2`, ...
until we have obtained a value that is within a certain error tolerance. There are a variety of
methods for doing this. The best methods are ones that ensure convergence and do so with the fewest number of iterations.

So, what is meant by convergence? Given a sequence of approximations to a solution for p:
:math:`p_0`, :math:`p_1`, :math:`p_2`, :math:`p_3`,... if the solution converges to the answer :math:`p`, then the differences, or errors, :math:`e_n = p_n − p`
must get smaller and smaller as n approaches infinity. To put it another way, if we take the ratio
of successive errors, it should be less than 1. In reality, as we perform more and more iterations,
then this ratio should approach a non-zero constant that is less than 1:

.. math::

  \lim_{n\rightarrow\infty}\frac{|e_{n+1}|}{|e_n|}=k<1.

More generally, it is possible to have:

.. math::

  \lim_{n\rightarrow\infty}\frac{|e_{n+1}|}{|e_n|^\alpha}=k<1.

where α is some positive power called the order of convergence. When :math:`\alpha = 1` then we have linear
convergence. When :math:`\alpha = 2` then we have quadratic convergence, i.e. our solution improves much
faster than with linear convergence.

Using such an iterative approach to problem solving means that n really could go to infinity,
which really isn’t practical for scientific computing. Instead, we define a tolerance, :math:`\epsilon` such
that when :math:`|e_n| < \epsilon` we stop iterating and declare our solution good enough. This is called a
**stopping condition**. Careful though, just because
:math:`|e_n| < \epsilon` it is not necessarily true that our solution is with in :math:`\epsilon` of the
unknown solution. It is always possible that the error could start growing again for one reason
or another. For this reason it is helpful to have a physical understanding of the problem, or even
to experiment with larger than normal values of n.

Roots of a Quadratic
--------------------

One of the most common problems is finding the solution (roots) of a quadratic equation:

.. math::

  ax^2 + bx + c = 0.

For which the standard solution can be applied:

.. math::

  x = \frac{−b \pm \sqrt{b^2 − 4ac}}{2a}.

Certainly this equation should produce the correct solution, and in fact there is no need to
perform any sort of iteration. However, in general introducing a computer into the solution
process can lead to one potential source of error: **round-off error**.

Precision and Round-Off Error
-----------------------------

When we use a computer to store a number, the computer does this physically by utilizing a
limited number of binary bits. Historically, floating point numbers (normal decimal numbers) take up 32 bits and double
precision numbers take up 64 bits. Regarding precision:
there is a limit on
the number of significant digits that can be stored by the computer.

Most computers use the *IEEE 754*
storage standard to represent numbers. In this manner, floating point numbers are stored as a
combination of three parts: the **sign**, **mantissa**, and
**exponent**. Consider as an analog a number
displayed in exponential format, i.e.:
:math:`0.74723\times10^5`.
In this case, the sign is +, the mantissa
is 0.74723, and the exponent is 5. Single precision floats have roughly 23 bits reserved for the
mantissa, 8 for the exponent, and 1 for the sign, while double precision numbers have 52 bits
reserved for the mantissa, 11 for the exponent, and 1 for the sign.

What this all means is that a number that requires an infinite number of digits to be represented
must be rounded to a finite number of digits. The problem isn’t typically that the computer can’t
represent large enough numbers: single precision numbers can have exponents that range from
:math:`\pm 126`. Rather, issues pop up when subtracting two numbers that have very similar magnitude.
In this case, it is possible that significant digits may be lost.
In the example of the quadratic formula, such errors can manifest themselves if the product of :math:`4ac` is much
smaller than :math:`b`.

It is important to note that round-off error is an issue with nearly every computer program. However, the precision of today's computers (python uses
64 bits for floating point numbers by default) typically makes
round-off error less important than other sources of error, such as truncation error, and the most
important source, user error.

Bisection Method
----------------

Say that you are given a function, :math:`f(x)` over the interval :math:`[a, b]`, and at some point in the interval
:math:`f(x)` changes sign. The bisection method is thus: our first step is to divide the interval in half and
note that :math:`f` must change sign on either the right half or the left half of the interval (or be zero at
the midpoint of the interval). Next, the interval
:math:`[a, b]` is replaced with the half-interval in which
:math:`f(x)` changes sign and we repeat the process. We iterate by halving the interval and selecting the
sub-interval that has a sign change until the sub-interval has a length of :math:`\epsilon`, or our tolerance

Note that since we are always reducing the interval by half, this method is linear in order of
convergence. Additionally, as long as our function,
:math:`f(x)` changes sign within our initial interval,
:math:`[a, b]`, the bisection method will converge, so it is an extremely reliable method, if not the most
efficient.

The bisection method may or may not work if there are more than one roots within our interval.
In particular, it will always work for an odd number of roots. If a given function has an even
number of roots, it is necessary to choose the initial interval such that it only brackets an odd
subset.

In order to implement such an algorithm, one would use the following steps:

1. Input the range, :math:`[a, b]`
2. Input the tolerance
3. Test the ends of the range to see if they are one of the roots or if they bracket a root
4. Begin iteration
5. set :math:`c = \frac{a+b}{2}`
6. if :math:`f(a)f(c) > 0` then :math:`a = c` else :math:`b = c`
7. repeat until :math:`abs(a − b) < tolerance`

Newton-Raphson Method
---------------------

In order to create an algorithm that is a bit more efficient than the bisection method, it is useful
to have a little bit more information about the function. One such method is based on expanding
our function :math:`f(x)` about the point :math:`x = p` as a Taylor series. If we do this and only keep first order
derivatives, we get:

.. math::

  f(p) = f(x) + f^\prime(x)(p-x)+\dots

Since we got rid of higher order terms, we can’t use this method to
find an exact solution, but we can still get a pretty decent approximation. Solving for :math:`p` in the
above equation gives:

.. math::

  p = x −\frac{f(x)}{f^\prime(x)}.

This defines an iterative method, so if we start with an initial guess :math:`p_0` then we would have a
method that looks like:

.. math::

  p_{n+1} = p_n − \frac{f(p_n)}{f^\prime(p_n)}

and we iterate over n until a sufficiently accurate
value is reached.
Unlike the bisection method that we already discussed,
there is no guarantee that Newton’s
method converges. This is obvious for the case where
:math:`f^\prime(p_n) = 0`.

Usually, Newton’s method
requires a that you choose your initial guess ”close” to the actual solution. If this is done, the
method converges quadraticaly.
In addition, since there is no guarantee that our method converges, it is always a good idea to
limit the number of iterations that your program can execute, less it runs forever. If the method
doesn’t converge by the time you reach some maximum number of iterations, you give up and
try to find an alternative.
Finally, in order to use Newton’s method, you need to have knowledge of your function’s derivative. Hopefully it is easy to find this analytically, as we have yet to discuss doing so numerically.
Implementation of Newton’s method should follow the following steps:

1. Input the initial guess :math:`p`
2. Test if :math:`f(p) = 0`. If it is, you’re done!
3. Begin iteration
4. Calculate :math:`f(p)` and :math:`f^\prime(p)`.
5. set :math:`p_{new} = p − f(p)/f^\prime(p)`
6. repeat until :math:`abs(p − p_{new}) < tolerance` or :math:`n > nmax`.
