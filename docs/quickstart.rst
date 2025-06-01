Quickstart
==========

Firstly, we will begin from installing shapesinc-py:

Installing
-----------

.. code-block:: shell

    pip install shapesinc -U

Then we will grab aur API keys.
API keys can be found `here <https://shapes.inc/developer>`_.

It is recommended to create "Application" type API key.

Then we will make an instance of our ``Shape``

Initialising
-------------

.. code-block:: python3

    from shapesinc import Shape

    shape = Shape("API_KEY", "my_shape", "app_id")

Then we will send a message.

Messaging the shape
----------------------

.. code-block:: python3

    resp = shape.prompt("Hi.")
    print(resp.choices[0].message)
