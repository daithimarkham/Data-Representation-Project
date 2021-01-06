# David Markham
# 19-11-2020
# Test code for DVD DAO program.

from DvdDAO import dvdDao

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
returnValue = dvdDao.getAll()
print(returnValue)
returnValue = dvdDao.findById(dvd1['serialNum'])
print("find By Id")
print(returnValue)
print("find By Id")
returnValue = dvdDao.update(dvd2)
print(returnValue)
returnValue = dvdDao.findById(dvd2['serialNum'])
print(returnValue) 
returnValue = dvdDao.delete(dvd2['serialNum'])
print(returnValue)
returnValue = dvdDao.getAll()
print(returnValue) 