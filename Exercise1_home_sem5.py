'''
Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
'''
#variant1
'''
text = input("Enter the text= ")
list1 = text.split()
print("list1= ", list1)

frig = "абв"
list1 = [x for x in list1 if not frig in x]
answer_text = " ".join(list1)
print("answer_text =", answer_text)
'''
#variant2
text = input('Enter the text= ')
list1 = text.split()
print(list1)
list2 = list(filter(lambda x: not 'абв' in x, list1))
print(list2)
text_result = ' '.join(list2)
print(text_result)