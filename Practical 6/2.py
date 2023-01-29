# Write a Python program to append text to a file and display the text

obj = open('D://Practicals//Python//Practical 6//Text_Files//2nd.txt','r')
print('Text in File Before Appending:')
print(obj.read())
obj.close()

obj = open('D://Practicals//Python//Practical 6//Text_Files//2nd.txt','a') #'a' used to append content
obj.write('\nText Line 5')
obj.writelines(['\nText Line 6','\nText Line 7'])
obj.close()

obj = open('D://Practicals//Python//Practical 6//Text_Files//2nd.txt','r')
print('Text in File After Appending:')
print(obj.read())
obj.close()