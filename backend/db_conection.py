import pymongo

url = 'mongodb+srv://andreasierra05:Sierra12345@cluster0.lagxyoh.mongodb.net/Todo_db?retryWrites=true&w=majority'

try:
    client = pymongo.MongoClient(url)
    db = client['Todo_db']
    print("Conexión exitosa")
except pymongo.errors.ConnectionError as err:
    print(f"Error de conexión: {err}")
