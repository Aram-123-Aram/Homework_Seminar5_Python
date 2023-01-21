'''
Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
'''
text = input("Enter the text= ")
list1 = text.split()
print("list1= ", list1)
#enum_list = list(enumerate(list1))
#print("enum_list= ", enum_list)

frig = "абв"
list1 = [x for x in list1 if not frig in x]
answer_text = " ".join(list1)
print("answer_text =", answer_text)