Examples
==========

Synchronous Shape Example
---------------------------

.. code-block:: python3

    from shapesinc import (
      shape,
      ShapeUser as User,
      ShapeChannel as Channel
    )
    
    my_shape = shape("API_KEY", "my_shape")
    user = User("u0")
    channel = Channel("cli")
    
    while True:
      inp = input(" >>> ")
      r = my_shape.prompt(inp, user = user, channel=channel)
      print(r.choices[0].message)
    
Asynchronous Shape Example
----------------------------

.. code-block:: python3

    from shapesinc import (
      shape,
      ShapeUser as User,
      ShapeChannel as Channel
    )
    
    my_shape = shape("API_KEY", "my_shape", synchronous=False)
    user = User("u0")
    channel = Channel("cli")
    
    async def run():
      while True:
        inp = input(" >>> ")
        r = await my_shape.prompt(inp, user = user, channel=channel)
        print(r.choices[0].message)
    
    import asyncio
    asyncio.run(run())


Image Message Examples
-----------------------

.. code-block:: python3

    from shapesinc import Message, MessageContent, ContentType as C
    
    msg = Message.new("Explain this image!", [dict(url = "URL OF IMAGE", type = c.image)])
    resp = my_shape.prompt(msg)
    
Audio Messages
---------------

.. code-block:: python3

    from shapesinc import Message, MessageContent, ContentType as C
    
    msg = Message.new(files = [dict(url = "URL OF AUDIO FILE", type = c.audio)])
    resp = my_shape.prompt(msg)
