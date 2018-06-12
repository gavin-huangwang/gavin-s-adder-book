# coding:utf_8
import json
import os
import sys

class Person():
    filename='adder_1.json'
    def __init__(self,name,iphone):
        self.name=name
        self.iphone=iphone
        self.adder_dict={self.name:self.iphone}

    def add_adder(self):
        self.name=input('ENTER YOUR NAME:')
        if self.name in self.adder_dict:
            print('name is exits')
        else:
            self.iphone=input('ENTER YOUR IPHONE')
            self.adder_dict[self.name]=self.iphone
            print('add adder succese')

    def modify(self):
        self.name=input('ENTOR YOUR NAME')
        if self.name in self.adder_dict:
            self.iphone=input('ENTER YOUR IPHONE')
            self.adder_dict[self.name]=self.iphone
            print('modify succese')
        else:
            print('name is not in here')

    def dele(self):
        self.name = input('ENTOR YOUR NAME')
        if self.name in self.adder_dict:
            del self.adder_dict[self.name]
            print('deleta succes')
        else:
            print('name is not in here')

    def select(self):
        self.name = input('ENTOR YOUR NAME')
        if self.name in self.adder_dict:
            print('name:%d,iphone:%d'%(self.name,self.iphone))
        else:
            print('name is not in here')

    def save(self):
        with open(self.filename,'w') as f:
            json.dump(self.adder_dict,f)
            print('Your contacts list has been saved to file:%s successfully~' %self.filename)

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename) as f:
                self.adder_dict=json.load(f)

    def show(self):
        for self.name,self.iphone in self.adder_dict.items():
            print('name:%d,iphone:%d'%(self.name,self.iphone))

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
            






