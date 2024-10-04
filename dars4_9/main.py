"""
Context managers
"""

from dars4_9.db import User

with User(4) as user:
    user.first_name = 'John'
