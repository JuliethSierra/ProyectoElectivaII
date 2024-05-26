import pymongo

url = 'mongodb+srv://andreasierra05:Sierra12345@cluster0.lagxyoh.mongodb.net/'

client = pymongo.MongoClient(url)
db = client['Todo_db']