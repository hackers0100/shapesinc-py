import typing

class ShapeBase:
  def __init__(self, api_key: str, username: str):
    self.api_key = api_key
    self.username = username

  @property
  def api_key(self) -> str:
    return self.__api_key

  @api_key.setter
  def api_key(self, value: str):
    self.__api_key = value

  @property
  def model_name(self) -> str:
    return "shapesinc/"+self.username

  def prompt(self, *args, **kwargs) -> typing.Any:
    raise NotImplementedError


class Shape(ShapeBase):
  def prompt(self, message: str, user = None, channel = None):
    ...


class AsyncShape(ShapeBase):
  async def prompt(self, message: str, user = None, channel = None):
    ...
