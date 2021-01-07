# David Markham
# 19-11-2020
# Test code for DVD DAO program.

from DvdDAO import DvdDao

dvd1 = {
    'serialNum': 1,
    'price': 4,
    'director': 'Stephen Spielberg',
    'title': 'Saving Private Ryan'
}

dvd2 = {
    'serialNum': 2,
    'price': 7,
    'director': 'Todd Philips',
    'title': 'The Hangover' 
}


#returnValue = bookDao.create(book)
returnValue = DvdDao.getAll()
print(returnValue)
