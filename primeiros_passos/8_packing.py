from datetime import date

d = [2023, 6, 17]

print(date(*d))

print("****************************************************************")

def new_user(active=False, admin=False):
    print("Is the user active? " + ("Yes" if active else "No"))
    print("Is the user admin? " + ("Yes"  if admin else "No"))

config = {
    "active": False,
    "admin": True,
    "nome": "Jean"
}



new_user(**config)