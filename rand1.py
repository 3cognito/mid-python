import random
import secrets

print(random.random())
print(random.uniform(1, 10))
print(random.randint(1, 10))
print(random.randrange(1, 10))
print(random.normalvariate(4, 7))  # Revisit
print(random.choice([1, 2, 3, 4, 5]))
print(random.choices([1, 2, 3, 4, 5, 7, 7, 7, 7, 7], k=2))  # Revisit
print(random.sample([1, 2, 2, 2, 2], k=2))  # Revisit
list1 = [1, 2, 3, 4, 5]
random.shuffle(list1)
print(list1)


print(secrets.randbelow(10))
print(secrets.randbits(64))
print(secrets.choice([1, 2, 3, 4, 5]))
