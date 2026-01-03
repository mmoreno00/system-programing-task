import sqlite3

connection = sqlite3.connect( 'myFirstDataBase.sqlite' )
cursor = connection.cursor()

sql = "SELECT surname, husbandName, wifeName, childrenNumber FROM families"  # <<-----------
cursor.execute( sql )
data = cursor.fetchall()

connection.close()

print( data )

for myRecord in data :
   print( " %20s|%-20s|%20s-%3d" % myRecord )
#
#print( 80 * '*' + '\n')
#
#for myRecord in data :
#   print( " %20s %-20s %20s %3d" % ( myRecord[ 2 ], myRecord[ 1 ], myRecord[ 0 ], myRecord[ 3 ] ) )
#
#print( 80 * '*' + '\n')
#
#for myRecord in data :
#   print( " %20s -->  %3d" % ( myRecord[ 0 ], myRecord[ 3 ] ) )
#
