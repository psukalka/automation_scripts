from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['mandara-xenon']
analysis_coll = db.analysis_control
# status = analysis_coll.find_one_and_update({"sample_id": "STRESS-TEST-16", "sub_ctgy" : "pbs"},{'$set': {'status': 'initialised'}})
result = analysis_coll.find_one_and_update({"sub_ctgy" : "urine", "sample_id": "R4684120-20"},{'$set': {'status': 'TESTING'}})
# status = analysis_coll.find_one_and_update({"sample_id":"FORUS-1550160220272", "sub_ctgy" : "fundus"},{'$set': {'status': 'initialised'}})
# status = analysis_coll.find_one_and_update({"sample_id":"3444_19", "sub_ctgy" : "fundus"},{'$set': {'status': 'initialised'}})
# status = analysis_coll.find_one_and_update({"sample_id" : "FORUS-1550160220272", "sub_ctgy" : "fundus"},{'$set': {'status': 'initialised'}})
# status = analysis_coll.find_one_and_update({"sample_id" : "R5562566-17"},{'$set': {'status': 'initialised'}})
# status = analysis_coll.find_one_and_update({"sample_id":"Sixth", "sub_ctgy" : "fundus"},{'$set': {'status': 'initialised'}})
print(result['_id'])
print('Updated status')
