import json

class User:
    id: int
    first_name: str
    last_name: str
    gender: str
    email: str
    phone_number: str
    address: list

    def __init__(self, id_: int):
        self.id = id_

    def __enter__(self):
        with open('users.json', 'r') as f:
            self.users = json.load(f)
            for user in self.users:
                if user.get('id') == self.id:
                    for key, value in user.items():
                        setattr(self, key, value)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        for user in self.users:
            if user.get('id') == self.id:
                user['first_name'] = self.first_name
                user['last_name'] = self.last_name
        with open('users.json', 'w') as f:
            json.dump(self.users, f, indent=4)
