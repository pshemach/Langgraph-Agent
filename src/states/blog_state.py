from pydantic import BaseModel, Field
from typing import TypedDict

class Blog(BaseModel):
    title: str = Field(description='title of the blog post')
    content: str = Field(description='main content of the blog post')
    
    
class BlogState(TypedDict):
    topic: str
    blog: Blog
    current_language:str