#!/usr/bin/python3
'''
This is the "1-my_list" module.

The 1-my_list module contains one class: MyList(list).

The MyList class inherits from 'list' and contains one public method:
print_sorted(self).

'''


class MyList(list):
    '''This is the MyList class.

    The MyList class inherits from the built-in list class.

    MyList contains one method: print_sorted(self).
    '''

    def print_sorted(self):
        '''This is the "print_sorted" method.

        print_sorted sorts a list in
        '''
        print(sorted(self))
