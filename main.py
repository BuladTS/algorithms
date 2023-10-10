import random
names = ['Alex', 'Kate', 'Mishel', 'Anna',
         'Brok', 'David', 'John', 'Lisa',
         'Rose', 'Jennie', 'Jisoo']

languages = ['C++', 'C', 'Java', 'Python', 'Javascript',
            'Rust', 'C#', 'Pascal', 'PHP', 'R']

experiences = ['beginer', 'junior', 'middle', 'senior']

ages = [x for x in range(18, 30)]

count = 0

while count != 100:
    name = random.choice(names)
    language = random.choice(languages)
    experience = random.choice(experiences)
    age = random.choice(ages)
    print(f"('{name}', '{language}', '{experience}', {age}),")
    count += 1
