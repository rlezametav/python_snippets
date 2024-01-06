participants = [
    ('John', 16),
    ('Emma', 31),
    ('Michael', 17),
    ('Sophia', 52),
    ('Olivia', 28),
    ('Liam', 14),
    ('Isabella', 19)
]

def is_adult(participants) -> bool:
    name, age = participants
    return age >= 18

adult_participants = filter(is_adult, participants)

elegible_participants = list(adult_participants)

print(elegible_participants)