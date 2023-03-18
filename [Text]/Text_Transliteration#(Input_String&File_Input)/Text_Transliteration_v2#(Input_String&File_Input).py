# Text_Transliteration_v2#(Input_String&File_Input).py
# Транслитерация введеной строки или файла

# https://www.cyberforum.ru/python-tasks/thread2186279.html


# !/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys

from time import strftime, localtime

# PROJECT_PATH = os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + ("\\" if sys.platform == "win32" else "/")
PROJECT_PATH = os.path.abspath(os.path.join(os.getcwd())) + ("\\" if sys.platform == "win32" else "/")

print(PROJECT_PATH)


file_name = "Data_Output_" + str(strftime("%d-%b_%H-%M-%S", localtime())) + ".txt"


def main():
    dic = {'Ь': '', 'ь': '', 'Ъ': '', 'ъ': '', 'А': 'A', 'а': 'a', 'Б': 'B', 'б': 'b', 'В': 'V', 'в': 'v',
           'Г': 'G', 'г': 'g', 'Д': 'D', 'д': 'd', 'Е': 'E', 'е': 'e', 'Ё': 'E', 'ё': 'e', 'Ж': 'Zh', 'ж': 'zh',
           'З': 'Z', 'з': 'z', 'И': 'I', 'и': 'i', 'Й': 'I', 'й': 'i', 'К': 'K', 'к': 'k', 'Л': 'L', 'л': 'l',
           'М': 'M', 'м': 'm', 'Н': 'N', 'н': 'n', 'О': 'O', 'о': 'o', 'П': 'P', 'п': 'p', 'Р': 'R', 'р': 'r',
           'С': 'S', 'с': 's', 'Т': 'T', 'т': 't', 'У': 'U', 'у': 'u', 'Ф': 'F', 'ф': 'f', 'Х': 'Kh', 'х': 'kh',
           'Ц': 'Tc', 'ц': 'tc', 'Ч': 'Ch', 'ч': 'ch', 'Ш': 'Sh', 'ш': 'sh', 'Щ': 'Shch', 'щ': 'shch', 'Ы': 'Y',
           'ы': 'y', 'Э': 'E', 'э': 'e', 'Ю': 'Iu', 'ю': 'iu', 'Я': 'Ia', 'я': 'ia'}

    alphabet = ['Ь', 'ь', 'Ъ', 'ъ', 'А', 'а', 'Б', 'б', 'В', 'в', 'Г', 'г', 'Д', 'д', 'Е', 'е', 'Ё', 'ё',
                'Ж', 'ж', 'З', 'з', 'И', 'и', 'Й', 'й', 'К', 'к', 'Л', 'л', 'М', 'м', 'Н', 'н', 'О', 'о',
                'П', 'п', 'Р', 'р', 'С', 'с', 'Т', 'т', 'У', 'у', 'Ф', 'ф', 'Х', 'х', 'Ц', 'ц', 'Ч', 'ч',
                'Ш', 'ш', 'Щ', 'щ', 'Ы', 'ы', 'Э', 'э', 'Ю', 'ю', 'Я', 'я']

    print("\nTransliteration v3"
          "\n[1] One"
          "\n[2] List"
          "\n"
          "\n[0] Delete Output"
          "\n[q] Quit\n")

    x = input(">>> ")
    if x == "q":
        exit(0)

    elif x == "1":
        print("=====One Transliteration (RUS -> ENG)=====\n"
              "\n[!b] Back"
              "\n[!q] Quit\n")

        while True:
            x = input(">>> ")
            if x == "!q":
                exit(0)
            elif x == "!b":
                main()
            else:
                st = x
                result = str()
                len_st = len(st)
                for i in range(0, len_st):
                    if st[i] in alphabet:
                        simb = dic[st[i]]
                    else:
                        simb = st[i]
                    result = result + simb
                print(result + "\n")

    elif x == "2":
        print("=====Starting List Transliteration=====")
        print("      ...the Process is being...       ")
        f = open("Data_Input.txt", encoding="utf-8")
        st = f.readlines()
        result = str()
        for i in st:
            for j in i:
                if j in alphabet:
                    temp = dic[j]
                    result = result + temp
                else:
                    temp = j
                    result = result + temp
        f.close()
        a = open(file_name, 'w')
        a.write(result)
        a.close()
        print("===== Ending List Transliteration =====")
        print("Create:", file_name)
        main()

    # Delete file
    elif x == "0":
        print("Deleting All.txt files")
        yes = 'y' in input("(Y)es/(N)o: ").lower().strip()
        if not yes:
            print("Not confirmed")
        print("Deleting All.txt files")
        files_in_directory = os.listdir(PROJECT_PATH)
        filtered_files = [file for file in files_in_directory if file.endswith(".txt")]
        for file in filtered_files:
            if file not in ("input.txt", "changes.txt"):
                path_to_file = os.path.join(PROJECT_PATH, file)
                os.remove(path_to_file)
        main()

    else:
        print("Command not Recognized")


main()
