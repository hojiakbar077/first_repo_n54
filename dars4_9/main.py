"""
Context managers
"""

from dars4_9.db import User

with User(1) as user:
    print(user.id)
    user.first_name = 'Anatar'
    print(user.first_name)
    print(user.last_name)
