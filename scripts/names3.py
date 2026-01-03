import os, random
import sqlite3

nameMaleList = [ capitalLetter + smallLeters for line in open( os.path.join( '..', 'names.txt' ), "r" ).readlines() if len( str.split( line ) ) == 4 for capitalLetter in str.split( str.split( line )[ 1 ], '/' )[ 0 ][ 0 ]  for smallLeters in  map( str.lower, [ str.split( str.split( line )[ 1 ], '/' )[ 0 ][ 1 : ]  ] )  ]

nameFemaleList = [ capitalLetter + smallLeters for line in open( os.path.join( '..', 'names.txt' ), "r" ).readlines() if len( str.split( line ) ) == 4 for capitalLetter in str.split( str.split( line )[ 3 ], '/' )[ 0 ][ 0 ]  for smallLeters in  map( str.lower, [ str.split( str.split( line )[ 3 ], '/' )[ 0 ][ 1 : ]  ] )  ]

surNameList = [ str.split( line )[ 1 ] for line in open( os.path.join( '..', 'surnames.txt' ), "r" ).readlines() if ',' in str.split( line )[ 2 ] ]

######################################################################################

myDataBase = 'mySecondDataBase.sqlite'

myFolder = '.'
myFiles = os.listdir( myFolder )

for myFile in myFiles :
    if myFile == myDataBase :
        print( 3 * '\n' )
        answer = str.lower( input( 3 * '\n' + 'DataBase: "' + myDataBase + '" exists. Delete? (Y/n) \n') )
        if answer == '' :
            answer = 'y'
        if str.lower( answer[ 0 ] ) == 'y' :
            os.remove( myDataBase )

######################################################################################

connection = sqlite3.connect( myDataBase )
cursor = connection.cursor()

#cursor.execute( "CREATE TABLE IF NOT EXISTS families ( id INTEGER PRIMARY KEY AUTOINCREMENT, husbandName TEXT, wifeName TEXT, surname TEXT, childrenNumber INTEGER )" )
cursor.execute( "CREATE TABLE IF NOT EXISTS families ( id INTEGER PRIMARY KEY AUTOINCREMENT, husbandName TEXT, wifeName TEXT, surname TEXT )" )
cursor.execute( "CREATE TABLE IF NOT EXISTS children ( id INTEGER PRIMARY KEY AUTOINCREMENT, familyID INTEGER, name TEXT )" )

for i in range( 200 ) :
   husbandName = random.choice( nameMaleList )
   wifeName = random.choice( nameFemaleList )
   surName = random.choice( surNameList )
   myNumber = random.randint( 0, 4 )
   #cursor.execute(  "%s ( '%s', '%s', '%s', '%s' )" % ( 'INSERT INTO families ( husbandName, wifeName, surname, childrenNumber ) VALUES', husbandName, wifedName, surName, myNumber ) )
   cursor.execute(  "%s ( '%s', '%s', '%s' )" % ( 'INSERT INTO families ( husbandName, wifeName, surname ) VALUES', husbandName, wifeName, surName ) )
   #connection.commit()

   if myNumber > 0 :
      cursor.execute( 'SELECT id from families ORDER BY id DESC' )
      familiesID = cursor.fetchone()
      print( familiesID[ 0 ] )

      for nameNumber in range( myNumber ) :
         sex = random.randint( 0, 1 )
         if sex == 0 :
            childName = random.choice( nameMaleList )
         else :
            childName = random.choice( nameFemaleList )

         cursor.execute( "%s ( '%s', '%s' )" % ( 'INSERT INTO children ( familyID, name ) VALUES', familiesID[ 0 ], childName ) )
connection.commit()
connection.close()
