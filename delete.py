import xlrd 

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('local-market-454fa-699abed26d04.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

ref = u'products'


docs = db.collection(ref).where(u'name', u'==', input("Product title? ")).stream()


for doc in docs:
    obj = doc.to_dict()
    # print(u'{} => {}'.format(doc.id, obj))

    for k in obj:
    	print(k, "=>", obj[k])
    what_to_do = input("Bhai karna kya chate ho delete/update/esc? ")
    if what_to_do == 'delete':
    	db.collection(ref).document(doc.id).delete()
    elif what_to_do == 'update':
    	while True:
	    	key = input('key / break?')
	    	if key == 'break':
	    		break
	    	val = input('value?')
	    	obj[key] = val


    	print("updating", obj)
    	db.collection(ref).document(doc.id).set(obj)
    	print('updated!')
    else:
    	print('esc')

