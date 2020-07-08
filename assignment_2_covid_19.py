age = str(input('Are you a cigarette addict older than 75 years old? (Yes/No):')).title().strip()
if age == 'Yes':
    age = True
else:
    age = False
chronic = str(input('Do you have a severe chronic disease? (Yes/No):')).title().strip()
if chronic == 'Yes':
    chronic = True
else:
    chronic = False
immune = str(input('Is your immune system too weak? (Yes/No):')).title().strip()
if immune == 'Yes':
    immune = True
else:
    immune = False
risk = age or chronic or immune
if risk == True:
    print('You are in risky group.')
else:
    print('You are not in risky group.')

