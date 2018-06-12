#coding=utf-8
from adress_book import Person
import json
import os
import sys

if __name__=='__main__':
    os.system('clear')
    commit=['add','modify','deleta','select','show','quit']
    person=Person('','')
    person.load()

    while True:
        print('gavin\'s adder book')
        str=input('WHAT ARE YOU GOING TO (add/modify/deleta/select/show/quit)?')

        if str in commit:
            if str == 'add':
                person.add_adder()
            elif str == 'modify':
                person.modify()
            elif str == 'deleta':
                person.dele()
            elif str == 'select':
                person.select()
            elif str == 'show':
                person.show()
            else:
                ch = input("Your contacts list hasn't  been saved,save it now?(Y/N)")
                if ch == 'y':
                    person.save()
                    sys.exit()
                    print('save succese')
                else:
                    sys.exit()
                print('exit sytem')
                break
        else:
            print('please input commit')
