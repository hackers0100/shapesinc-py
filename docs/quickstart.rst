Quickstart
==========

Firstly, we will begin from installing shapesinc-py:

Installing
-----------

.. code-block:: shell

    pip install shapesinc -U

Then we will make an instance of our ``Shape``

Initialising
-------------

.. code-block:: python3

    from shapesinc import Shape

    shape = Shape("API_KEY", "my_shape")

Then we will send a message.

Creating a slashcommand
-----------------------

.. code-block:: python3

    resp = shape.prompt("Hi.")
    print(resp.choices[0].message)