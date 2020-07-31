name=input("what is your name?")
birth_year=int(input("when were you born?"))


print(f"hello, {name}")

from datetime import datetime
this_year=datetime.now().year
age=this_year - birth_year

print(f"you must be {age}")
print(f"goodbye, {name}")