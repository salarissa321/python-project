'''
- user : height , weight
'''
'''
height = int(input('Enter your Height: '))
weight = int(input('Enter yout Weight : '))

bmi= (weight / (height*height))*10000
print(bmi)

if bmi <= 18.4:
    print('Underweight')

elif bmi > 18.4 and bmi < 24.9:
    print('Normal')

elif bmi > 25 and bmi < 39.9:
    print('Overweight')

else:
    print('obese')

'''



sentence='''

The BMI Calculator finds the body mass index given weight and height Calculate your BMI and find the BMI weight category for your height The calculator also finds the normal weight range given your height
Calculate BMI with weight in pounds, stones or kilograms. Enter height in inches, feet and inches, meters or centimeters.
'''
words= ['finds' , 'body' , 'height' , 'BMI']


#1
result1=[]
for w in words:
    result1.append(sentence.count(w))
print(result1)


#2
sentence_words= sentence.split(' ')
print(sentence_words)
result=[]
for w in words:
    count= 0
    for sw in sentence_words:
        if sw == w :
            count += 1
    result.append(count)
print(result)

   



































