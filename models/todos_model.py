from datetime import datetime
from odmantic import Model

class Todo(Model):
    title: str
    complete: bool = False
    created: datetime = datetime.now()
