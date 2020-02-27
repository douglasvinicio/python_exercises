name1 = str(input('Enter your Full name here: ')).strip()
print('Analising your name....')
print('Your name in Upper Case is: {}'.format(name1.upper()))
print('Your name in Low Case is: {}'.format(name1.lower()))
print('Your name has {} characteres in total.'.format(len(name1) - name1.count(' ')))
#print(' '.join(name1))
division1 = (name1.split())
print(('Your first name is {} and the number of characteres of the first name is: {}').format(division1[0], len(division1[0])))

#alternative way
print("You first name has {} letters.".format(name1.find(' ')))

