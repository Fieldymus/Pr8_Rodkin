import random
pas = ''
for x in range(11):
    pas = pas + \
        random.choice(
            list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
print('Your password is: ', pas)
