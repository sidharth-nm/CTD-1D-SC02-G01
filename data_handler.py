import os,io,json,copy

DB_FILE = "Database.json"
DB_FILE_PATH = os.path.join(os.getcwd(), DB_FILE)

#GET database
def get_data():
  with open(DB_FILE_PATH, 'r') as f:
    # Read the file content before deserialising all data   
    data_dict = json.loads(f.read())
  print(data_dict)
  return data_dict

#GET filtered list of book by a key
def get_filtered_books_list(key, value):
  filtered_books = []

  #return list of users who match the input
  for book in books:
    if book[key] == value:
      filtered_books.append(book)
  return filtered_books

#GET filtered list of users by a key
def get_filtered_users_list(key, value):
  filtered_users = []

  #return list of users who match the input
  for user in users:
    if user[key] == value:
      filtered_users.append(user)
  return filtered_users

#CREATE user data
def user(username, password):
  return {
      "username": username,
      "password": password
  }    

#ADD user data to database
def add_user(new_user):
  new_users_list = copy.deepcopy(users)
  print(new_users_list)
  new_users_list.append(new_user)
  update_database(database, new_users_list) 

#UPDATE the databases
def update_database(database, new_users = None):
  #update the dictionary variables
  if(new_users != None):
    database["users"] = new_users 
  books = database["books"]
  users = database["users"]

  #serialise the data
  database_json_string = json.dumps(database, indent=4)
  #update the db in the json file  
  with open(DB_FILE_PATH, "w") as f:
    f.write(database_json_string)

database = get_data()
books = database["books"]
users = database["users"]
