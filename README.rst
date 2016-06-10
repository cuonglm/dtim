dtim
====

dtim -- Python DateTime IMprovement

Installation
============

.. code:: sh

    pip install dtim

Why dtim
========

Python standard datetime.datetime is awesome, but lack some of common
methods like computing timestamps, checking naive, aware datetime
easily.

dtim comes in for simplification.

Usage
=====

.. code:: python

    from dtim import DateTime


    dt = DateTime.now()

    # Number of seconds since epoch
    print dt.epoch()

    # Check datetime is naive
    print dt.is_naive()

    # Check datetime is aware
    print dt.is_aware()

Output:

.. code:: sh

    1465591177.280863
    True
    False

Author
======

Cuong Manh Le cuong.manhle.vn@gmail.com

License
=======

See `LICENSE <https://github.com/Gnouc/dtim/blob/master/LICENSE>`__