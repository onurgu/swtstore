# -*- coding utf-8 -*-
# classes/exceptions.py

from sqlalchemy.exc import DontWrapMixin

class AlreadyExistsError(Exception, DontWrapMixin):
    pass

