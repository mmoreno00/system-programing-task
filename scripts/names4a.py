import sqlite3, sys, os

connection = sqlite3.connect( 'myThirdDataBase.sqlite' )
cursor = connection.cursor()

cursor.execute( "SELECT children.name, families.surname, children.date FROM families, children WHERE families.id = children.familyID ORDER BY children.date DESC" )
data = cursor.fetchall()
# print( data )
connection.close()

for myData in data :
   print( "%-15s %-15s %-15s" % myData )

myOutputFile = str.split( str.split( sys.argv[ 0 ], os.sep )[ -1 ], '.' )[ 0 ] + '.txt'
out = open( myOutputFile, "w" )

print( data, file = out )
for myData in data :
   print( "%-15s %-15s %-15s" % myData, file = out )
out.close( )


