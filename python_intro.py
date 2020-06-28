if 3>2:
    print('It works')
if 5>2:
    print('yes')
else:
    print('no')
name= 'yuliya'
if name=='anya':
    print('hey, anya')
elif name=='yuliya':
    print('hey, yuliya')
else:
    print ('hey, anonymous')
#change the volume if it's too loud ot too quite
volume=88
if volume<20 or volume>80:
    volume=50
    print('that\'s better')
#create function
def hi():
    print('hi there')
    print('how are you?')
hi()
def hi(name):
    if name=='yuliya':
        print('hi, yuliya')
    elif name== 'anya':
        print('hi, anya')
    else:
        print ('hi, ananymous')
hi('yuliya')
hi('anya')
hi('sofia')
def hi(name):
    print('hi '+ name + '!')
hi('karina')
girls=['yuliya', 'anya', 'sofia', 'karina', 'you']
for name in girls:
    hi(name)
    print('next girl')
for i in range(1,5):
    print(i)
