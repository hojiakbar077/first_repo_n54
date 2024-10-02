"""
Context managers
"""

from dars4_9.db import User

with User(1) as user:
    print(user.id)
    print(user.first_name)
    user.first_name = 'John'
    print(user.last_name)
