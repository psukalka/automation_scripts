from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['mandara-xenon']
print("extraction_count: %d", db.extraction_control.find().count())
print("clearing extraction control")
db.extraction_control.remove({})
print("extraction_count: %d", db.extraction_control.find().count())
print("analysis patches count: %d", db.analysis_patches.find().count())
print("clearing analysis patches")
db.analysis_patches.remove({})
print("analysis patches count: %d", db.analysis_patches.find().count())
print("fov patches count: %d", db.fov_patches.find().count())
print("clearing fov patches")
db.fov_patches.remove({})
print("fov patches count: %d", db.fov_patches.find().count())
