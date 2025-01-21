
letter = input("Please enter a word: \n")
reverse = letter[::-1]

if type(letter) == int:
    print("Only Alphabets are allowed")
elif letter == reverse:
    print(f"the string {letter} is palindrome")
else:
    print("string is not palindrome")



for i in range(1,10):
    if i == 5:
        #break
        #continue
        pass
    print(i)



count = 0
while count < 10:
    if count == 5:
        break
    print(count)
    count += 1


count = 0
while count < 10:
    count += 1
    if count == 5:
        continue
    print(count)


D1 = {'first_name' : 'Jim', 'age' : 23, 'height' : 6.0 , 'job' : 'developer', 'company': 'XYZ'}

def check_key(a):
    if a in D1:
        return "Yes"
    else:
        return "No"
print(check_key('jjj'))


D1 = {'first_name' : 'Jim', 'age' : 23, 'height' : 6.0 , 'job' : 'developer', 'company': 'XYZ'}
D2 = {'age' : 35, 'job' : 'senior data analyst'}

for key in D1:
    for key1 in D2:
        D1[key] = D2[key1]
print("The original dictionary: " + str(D1))
print("The updated dictionary: " + str(D2))