from dataclasses import dataclass, field

@dataclass
class User:
    id: int
    firstName: str
    lastName: str
    age: int
    
@dataclass
class Blog:
    id: int
    title: str
    userId: int
    body: str
    
@dataclass
class Comment:
    id: int
    blogId: int
    userId: int
    body: str
    


def classFactory(class_name: str, **kwargs) -> object:
    """
    Creates a class dynamically.
    """
    
    if class_name == 'User':
        return User(id=kwargs['id'], firstName=kwargs['firstName'], lastName=kwargs['lastName'], age=kwargs['age'])
    elif class_name == 'Blog':
        return Blog(id=kwargs['id'], title=kwargs['title'], userId=kwargs['userId'], body=kwargs['body'])
    else:
        return Comment(id=kwargs['id'], blogId=kwargs['blogId'], userId=kwargs['userId'], body=kwargs['body'])
