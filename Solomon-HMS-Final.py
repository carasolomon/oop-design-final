# Tacara Solomon- SWDV 630 Final Project
# Import SQLAlchemy for database

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Build classes

# Account class
class Account(Base):
    def __init__(self, fname, lname, address, zipcode, _accountNum):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.zipcode = zipcode
        self._accountNum = _accountNum

    def getName(self):
        return self.fname + ", " + self.lname

    def getAccountNum(self):
        return self._accountNum

        
    __tablename__ = 'Account'
    
    id = Column(Integer, primary_key=True)
    fname = (String)
    lname = (String)
    address = (String)
    zipcode = (String)
    _accountNum = (String)
    
    def __repr__(self):
        return '<Account(fname={0}, lname={1}, address={2}, zipcode={3}, _accountNum={4})>'.format(self.fname, self.lname, self.address, self.zipcode, self._accountNum)
     

# Rooms class
class Rooms(Base):
    def __init__(self, roomName, size, price, numOfRooms):
        self.roomName = roomName
        self.size = size
        self.price = price
        self.numOfRooms = numOfRooms # The max amount of rooms fitting this description that the hotel has.

    def getRoomDetails(self):
        return self.roomName + self.size + self.price

    def getRoomQuantity(self):
        return self.numOfRooms   

    __tablename__ = 'Room'
    
    id = Column(Integer, primary_key=True)
    name = (String)
    size = (String)
    price = (String)
    
    def __repr__(self):
        return '<room(name={0}, size={1},price={2})>'.format(self.name, self.size, self.price)
     
  

# Payment class

class Payment(Account):
    def __init__(self, fname, lname, _creditCardNum, zipcode):
        super().__init__(fname, lname, zipcode)
        self._creditCardNum = _creditCardNum

    __tablename__ = 'Payment'
    
    id = Column(Integer, primary_key=True)
    fname = (String)
    lname = (String)
    zipcode = (String)
    _creditCardNum = (String)
    
    
    def __repr__(self):
        return '<Payment(fname={0}, lname={1}, zipcode={2}, _creditCardNum={3})>'.format(self.fname, self.lname, self.zipcode, self._creditCardNum)
         


# Booking class

class Booking(Rooms):
    def __init__(self, roomName, price, lengthOfStay):
       super().__init__(roomName, price)
       self.lengthOfStay = lengthOfStay


def bookRoom():
    pass

# main function

def main():
    # Get information for new account
    fname = input('Enter your first name: ')
    lname = input('Enter your last name: ')
    address = input('Enter your address: ')
    zipcode = input('Enter your zipcode: ')
    accountNum = input('Enter your account number: ') 

    newAccount = Account(fname, lname, address, zipcode, accountNum) 
    print('The information that you entered for your account is: ', newAccount)

    # Database 
    engine = create_engine('sqlite:///:memory:', echo=False)
    
    Base.metadata.create_all(engine)
    
    room1 = Rooms('Single Bed Suite', 1, 160, 6)
    print(room1)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    session.add(room1)
    
    session.add_all([
        Rooms('Studio', 0, 60, 8),
        Rooms('Deluxe Suite', 2, 250, 4),
        Rooms('Romantic Getaway Suite', 1, 200, 3),
        Rooms('Penthouse Suite', 3, 345, 1)])
    session.commit()
    
    for row in session.query().all():
        print(row.name, row.price)




main()       