# Text_Concatenation#(File_Line).py
# Конкатенация # Сложение строк файлов

f1 = open("Data1.txt")
f2 = open("Data2.txt")
f3 = open("Data_Out.txt", "w")

n1 = f1.read().splitlines()
n2 = f2.read().splitlines()

s1 = input('Enter the separator(Разделитель) string:\n')

for i in range(len(n1)):
    print('Concatenated String =', (n1[i] + s1 + n2[i]))
    f3.writelines(n1[i] + s1 + n2[i] + "\n")
    # f3.writelines(n1[i] + "," + n2[i]+ "\n")

f1.close()
f2.close()
f3.close()
