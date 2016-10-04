import random

#Author: Felix Rieg-Baumhauer
#9/15/16
#randClasss() finds a random one of three classes
#studenter( section ) takes a section and procures a student

CLASSES =  {
    4: [ 'Ayman', 'Shaeq', 'Patrick', 'Yvonne', 'Wilson',
         'Brian', 'Farhan', 'Janet', 'Harry', 'Kevin',
         'Nicholas', 'Jason', 'Yikai', 'Emma', 'Kenneth',
         'Nala', 'Karol', 'Elias', 'Ely', 'Reo', 'Dhriaj',
         'Amy', 'Arvind', 'Nobel', 'Angela', 'Edward',
         'Jonathan', 'Celine', 'Daniel', 'Lindsey', 'Ziyan', 'Elina'],
    8: ['Julian', 'Sebastian', 'Jordan', 'Alan', 'Yuki',
        'Chloe', 'Noah', 'Edvic', 'Jia Qi', 'Shan', 'Rodda',
        'Anya', 'Edmond', 'Asher', 'Kathy', 'Sharon', 'Vncent',
        'Lawrence', 'Sachal', 'Gabriel', 'Jason', 'Daniel',
        'Felix', 'Jacob', 'Bayle', 'Fortune', 'Gio',
        'Kelly', 'William', 'Jordan', 'Haley', 'Henry'],
    9: ['James', 'Vanna', 'Zicheng', 'Quinn', 'Anthony C',
        'Joel', 'Steph', 'Xinhui', 'Richard', 'Misha',
        'Maddie', 'Winston', 'Shariar', 'Nancy', 'Jerry',
        'Michael', 'Stiven', 'Will',  'Olivia', 'Constantine',
        'Jessica', 'Kate', 'Shamaul', 'Max', 'Sarah', 'Anthony L',
        'Brandon', 'Nicole', 'Brian', 'Issac', 'Seiji', 'Lorenz']
} 

def randClass():
    randNum = (int) (random.random() * 4)
    if randNum == 0:
        return 4
    elif randNum == 1:
        return 8
    else:
        return 9
    return

def studenter(section):
    length = len(CLASSES[section])
    randStud = (int) (random.random() * length)
    theKid = CLASSES[section][randStud]
    return (theKid + " in period " + (str)(section))

print randClass() #test fxn 1
print studenter(randClass()) #test fxn 2
