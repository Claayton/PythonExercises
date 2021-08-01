# Ex101.2
"""Create a program that has a function called vote() that will receive as a parametes the year of birth of a person, returning a literal value indicating wheter a person has a DENID, OPTIONAL or MANDATORY vote in elections."""

def vote():
    from datetime import date
    print('\033[35m--\033[m' * 25)
    today = date.today().year
    born = int(input('\033[34mWhat year were you born? \033[m'))
    age = today - born
    if age < 16:
        return f'\033[35mWith {age} year old your vote is \033[31mDENID!\033[m\n\033[35m{"--" * 25}\033[m'
    elif 16 >= age > 18 or age > 65:
        return f'\033[35mWith {age} year old your vote is \033[36mOPTIONAL!\033[m\n\033[35m{"--" * 25}\033[m'
    else:
        return f'\033[35mWith {age} year old your vote is \033[32mMANDATORY!\033[m\n\033[35m{"--" * 25}\033[m'
    
print(vote())
print('xD')
