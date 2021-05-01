from Utils import database_function
import sys
import os
import time
from Utils import text_fun


class start():
    def At_first(self):
        print(text_fun.first_text)
        input()
        database_function.create_word_table()
    os.system("cls")
    def to(self):
        i = False
        while i == False:
             print(text_fun.menu)
             choise = input(":>>> ")
             if choise in ('add','Add','ADD'):
                 add_word()
             elif choise in ('delete','DELETE','Delete'):
                 delete_word()
             elif choise in ('quiz','Quiz','QUIZ'):
                 pass
             elif choise in ('Check','check','CHECK'):
                 check_mode()
             else:
                 print("Not found this one, try again")


def add_word():
    english_form = input("Enter english form!!\n:>> ")
    knowing_form = input("Enter knowing form!!\n:>> ")
    level_knowing = input(" Enter level complicated\n:>> ")
    database_function.add_new_word(english_form, knowing_form, level_knowing)
    print("\n")
    print(f"Word: {english_form} succesfully added\n")

def delete_word():
    english_form = input("Enter english form!!\n:>> ")
    knowing_form = input("Enter knowing form!!\n:>> ")
    database_function.delete_word(english_form)
    print("Your row deleted!\n")

def check_mode():
    iter_pag = 0
    number = 1
    word = database_function.get_all_words()
    os.system("cls")
    for w in word:
        print("-------------------------------------------------------------------\n")
        print("№ " + str(number) + f"  |  {w['english_form']}  |  {w['knowing_form']}  | l_c: {w['level_complicate']}  | l_k: {w['level_knowing']}\n")
        print("-------------------------------------------------------------------\n")
        iter_pag = iter_pag + 1
        if iter_pag == 10:
            print("#########################################################\n")
            print("Press enter to move for next page :>>> ")
            input()
            os.system("cls")
            iter_pag = 0
        number = number + 1
    print("Enter to menu")
    input()

#def quiz_mod()
#def learn_mode()