"""
Problem statement:
N people are standing in a circle such a way that each person has someone on left and someone on right to him/her
People are labeled from 1 to N and the person labelled with 1 has a gun.
The person having gun kills the person next to him/her(towards right) and passes the gun to third person(next to next person).
This process repeats until there is only one person.

Who is the survivor in the circle?
"""
def survivor_in_circle(people):
    previous_last_person = people[-1]  # last person at the beginning
    people = people[::2]
    while people:
        current_last_person = people[-1]
        number_of_people = len(people)
        if number_of_people == 1:
            break
        people = people[1 if current_last_person == previous_last_person else 0::2]
        previous_last_person = current_last_person
    return people[0]

# Test
# people = list(range(1, 101, 1))
# survivor = survivor_in_circle(people)
# print(survivor)