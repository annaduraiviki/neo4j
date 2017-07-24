#from neo4j.v1 import GraphDatabase

#driver = GraphDatabase.driver("bolt://localhost",auth=("neo4j", "test"))


#def add_friends(tx, name, friend_name):
#    tx.run("MERGE (a:Person {name: $name}) "
#           "MERGE (a)-[:KNOWS]->(friend:Person {name: $friend_name})",
#           name=name, friend_name=friend_name)

#def print_friends(tx, name):
#    for record in tx.run("MATCH (a:Person)-[:KNOWS]->(friend) WHERE a.name = $name "
#                         "RETURN friend.name ORDER BY friend.name", name=name):
#        print(record["friend.name"])


#a = neo()
#print add_friends('lx','A','S')
#print a
#with driver.session() as session:
#    driver.write_transaction(add_friends, "Arthur", "Guinevere")
#    session.write_transaction(add_friends, "Arthur", "Lancelot")
#    session.write_transaction(add_friends, "Arthur", "Merlin")
#    session.read_transaction(print_friends, "Arthur")

#from neo4jrestclient.client import GraphDatabase
#gdb = GraphDatabase("http://localhost")
#alice = gdb.nodes.create(name="Alice", age=30)
#bob = gdb.nodes.create(name="Bob", age=30)
#alice.relationships.create("Knows", bob, since=1980)
#people = gdb.labels.create("Person")
#============================================================== LOAD CSV =======================
#LOAD CSV WITH HEADERS FROM 'file:///Users/kushal/Desktop/Nepal Data/Municipalities_of_nepal.csv' AS line
#MERGE(d:District{name:line.District})
#CREATE (m:Municipality { name: line.Municipality})
#CREATE (d-[:MUNICIPALITY]->(m)
#return d,m;

#================================== WORKING CODE ++++++++++++++++++++++++++++++++++++#

from neo4j.v1 import GraphDatabase, basic_auth

driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", "test"))# user_name and pwd
session = driver.session()

session.run("CREATE (a:Person1 {name: {name}, title: {title}})",{"name": "donald", "title": "trump"})
session.run("CREATE (b:Person2 {name: {name}, title: {title}})",{"name": "arthur", "title": "king"})

result = session.run("MATCH (a:Person) WHERE a.name = {name} "  "RETURN a.name AS name, a.title AS title",{"name": "donald"})

#session.run("MATCH (a:Person1),(b:Person2)")
session.run("CREATE (a)-[r:FRIEND_OF]->(b)")
#session.run("return r")
for record in result:
    print("%s %s" % (record["title"], record["name"]))

#session.run("MATCH (n) detach delete n ")#To detach all nodes
#MATCH (a:Artist),(b:Album)
#WHERE a.Name = "Strapping Young Lad" AND b.Name = "Heavy as a Really Heavy Thing"
#CREATE (a)-[r:RELEASED]->(b)
#RETURN r

session.close()
#=======================================================================================
