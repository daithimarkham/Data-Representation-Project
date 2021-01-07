# David Markham 
# 12-11-2020
# Create a server for the virtual environment. 
# Basics of as Flask server
# More info in Doc For Flask


from flask import Flask, jsonify, request, abort, make_response
from DvdDAO import DvdDao

app = Flask(__name__, static_url_path='', static_folder='.')


#curl "http://127.0.0.1:5000/books"
@app.route('/dvds')
def getAll():
    #print("in getall")
    results = DvdDao.getAll()
    return jsonify(results)

#curl "http://127.0.0.1:5000/books/2"
@app.route('/dvds/<int:id>')
def findById(id):
    foundDvd = DvdDao.findByID(id) 
    return jsonify(foundDvd) 

#curl  -i -H "Content-Type:application/json" -X POST -d "{\"Title\":\"hello\",\"Author\":\"someone\",\"Price\":123}" http://127.0.0.1:5000/books
@app.route('/dvds', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    # other checking 
    dvd = {
        "Title": request.json['Title'],
        "Director": request.json['Director'],
        "Price": request.json['Price'],
    }
    values =(dvd['Title'],dvd['Director'],dvd['Price'])
    newId = DvdDao.create(values)
    dvd['id'] = newId
    return jsonify(dvd)

#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"Title\":\"hello\",\"Author\":\"someone\",\"Price\":123}" http://127.0.0.1:5000/books/1
@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
    foundDvd = DvdDao.findByID(id)
    if not foundDvd:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'Price' in reqJson and type(reqJson['Price']) is not int:
        abort(400)

    if 'Title' in reqJson:
        foundDvd['Title'] = reqJson['Title']
    if 'Director' in reqJson:
        foundDvd['Director'] = reqJson['Director']
    if 'Price' in reqJson:
        foundDvd['Price'] = reqJson['Price']

    values = (foundDvd['Title'],foundDvd['Director'],foundDvd['Price'],foundDvd['id'])

    DvdDao.update(values)
    
    return jsonify(foundDvd) 
        

    

@app.route('/dvds/<int:id>' , methods=['DELETE'])
def delete(id):
    DvdDao.delete(id)
    return jsonify({"done":True})




if __name__ == '__main__' :
    app.run(debug= True)