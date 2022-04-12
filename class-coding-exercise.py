class Animal:
    def __init__(self, type):
        print('Initializing type')
        self.__type = type
    
    @property
    def type(self):
        print('Getting type')
        return self.__type

    @property
    def classification(self):
        print('Getting classification')
        return self.__classification
    
    @property
    def color(self):
        print('Getting color')
        return self.__color

    def eat(self):
        print('Eating')

    def move(self):
        print('Moving')

    def sleep(self):
        print('Sleeping')


class Vehicle:
    def __init__(self,make):
        print('Initializing make')
        self.__make = make

    @property
    def model(self):
        print('Getting model')
        return self.__model 

    @property
    def year(self):
        print('Getting year')
        return self.__year

    @property
    def owner(self):
        print('Getting owner')
        return self.__owner

    @property
    def currentRegistration(self):
        print('Getting current registration year')
        return self.__currentRegistration

    @property
    def lastWork(self):
        print('Getting last mechanic work')
        return self.__lastWork

    def park(self):
        print('Parking')

    def drive(self):
        print('Driving')

    def reverse(self):
        print('Reversing')


class Book:
    def __init__(self,title):
        print('Initializing title')
        self.__title = title

    @property
    def author(self):
        print('Getting author')
        return self.__author

    @property
    def editor(self):
        print('Getting editor')
        return self.__editor

    @property
    def publisher(self):
        print('Getting publisher')
        return self.__publisher

    @property
    def yearPub(self):
        print('Getting publishing year')
        return self.__yearPub

    @property
    def genre(self):
        print('Getting genre')
        return self.__genre

    @property
    def readerLevel(self):
        print('Getting reader level')
        return self.__readerLevel
    

    
    

