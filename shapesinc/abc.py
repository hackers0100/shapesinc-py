import random
import typing

from datetime import datetime
from enum import IntEnum

MISSING = object()

class ABCBase:
  def __init__(self, id: str = MISSING):
    self.id = id

  @property
  def id(self) -> str:
    return self.__id

  @id.setter
  def id(self, value: str):
    if value is MISSING:
      value = str(random.randint(1,9))
      value += "".join(str(random.randint(0,9)) for _ in range(9))
      
    self.__id = value

  @classmethod
  def new(cls): return cls()

class ShapeUser(ABCBase): ...
class ShapeChannel(ABCBase): ...


class ContentType(IntEnum):
  text:  int = 1
  audio: int = 2
  image: int = 3
  
  def __repr__(self) -> str:
    return f"<ContentType 'shapesinc.ContentType.{self.name}'>"
    
  __str__ = __repr__

class MessageContent(ABCBase):
  def __init__(self, content: str, type: ContentType = ContentType.text):
    self.type = type
    super().__init__(content)

  @property
  def content(self) -> str:
    return self.id

  @content.setter
  def content(self, value: str):
    self.id = value
    
  @classmethod
  def from_dict(cls, data: dict):
    assert data["type"] in ["image_url", "audio_url", "text"], ValueError("Expected ContentType input")
    
    if data["type"]=="text":
      return cls("text", ContentType.text)
      
    return cls(
      data[data["type"]]["url"],
      ContentType.audio if data["type"] == "audio_url" else ContentType.image
    )
    
  def to_dict(self) -> dict[str, typing.Union[dict, str]]:
    return {
      "type": f"{self.type.name}_url",
      f"{self.type.name}_url": {
        "url": self.content
      }
    } if self.type != ContentType.text else {
      "type": "text",
      "text": self.content
    }
    
class Message:
  def __init__(self, content: list[MessageContent] = None, role: str = "user"):
    assert content, ValueError("Cannot create empty message!")
    self.content = content
    self.role = role
    
  def __repr__(self) -> str:
    if len(self.content)==1 and self.content[0].type==ContentType.text:
      return self.content[0].content
      
    return super().__repr__()
    
  __str__ = __repr__
  def to_dict(self) -> dict:
    return {
      "role": self.role,
      "content": [c.to_dict() for c in self.content]
    }
    
  @classmethod
  def from_dict(cls, data: dict):
    return cls(
      [MessageContent.from_dict(c) for c in data["content"]] if isinstance(data["content"], list) else [MessageContent(data["content"])],
      data["role"]
    )
    
  @classmethod
  def new(cls, text: str = "", files: dict[str, str] = {}, role: str = "user"):
    assert text or files, ValueError("Cannot create empty message!")
    c = []
    if text:
      c.append(MessageContent(text))
    if files:
      c.extend([MessageContent (f["url"], f["type"]) for f in files])
      
    return cls(c, role)
    
class TypedDict(dict):
  def __init__(self, **kwargs):
    for k, v in kwargs.items():
      v = getattr(self, "_parse_"+k, lambda x:x)(v)
      setattr(self, k, v)
      
    super().__init__(**kwargs)

class PromptResponse_Choice(TypedDict):
  index: int
  message: Message
  finish_reason: typing.Literal["stop", "length", "tool_calls", "content_filter", "function_call"]
  
  _parse_message = Message.from_dict

class PromptResponse_Usage(TypedDict):
  prompt_tokens: int
  total_tokens: int
  completion_tokens_details: typing.Optional[dict] = None
  prompt_tokens_details: typing.Optional[dict] = None

class PromptResponse(TypedDict):
  id: str
  model: str
  object: typing.Literal["chat.completion"]
  usage: typing.Optional[PromptResponse_Usage] = None
  created: datetime
  choices: list[PromptResponse_Choice]
  
  _parse_created = datetime.fromtimestamp
  _parse_choices = lambda _, cs: [PromptResponse_Choice(**c) for c in cs]
  _parse_usage = lambda _, u: PromptResponse_Usage(**u)
