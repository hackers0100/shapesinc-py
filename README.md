# shapesinc-py

## Installation

From PyPI:
```
pip install shapesinc -U
```

From GitHub:
```
pip install git+https://github.com/Rishiraj0100/shapesinc-py.git
```

## Examples

synchronous example
```py
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
```
asynchronous example
```py
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
```
