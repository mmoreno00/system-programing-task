import os, random
import sqlite3   #mySQLdb

nameMaleList = [ capitalLetter + smallLeters for line in open( 'names.txt', "r" ).readlines() if len( str.split( line ) ) == 4 for capitalLetter in str.split( str.split( line )[ 1 ], '/' )[ 0 ][ 0 ]  for smallLeters in  map( str.lower, [ str.split( str.split( line )[ 1 ], '/' )[ 0 ][ 1 : ]  ] )  ]

nameFemaleList = [ capitalLetter + smallLeters for line in open( 'names.txt', "r" ).readlines() if len( str.split( line ) ) == 4 for capitalLetter in str.split( str.split( line )[ 3 ], '/' )[ 0 ][ 0 ]  for smallLeters in  map( str.lower, [ str.split( str.split( line )[ 3 ], '/' )[ 0 ][ 1 : ]  ] )  ]

surNameList = [ str.split( line )[ 1 ] for line in open( 'surnames.txt', "r" ).readlines() if ',' in str.split( line )[ 2 ] ]


######################################################################################

myDataBase = 'myThirdDataBase.sqlite'

myFolder = './'
myFiles = os.listdir( myFolder )

if myDataBase in myFiles :
  print( 3 * '\n' )
  answer = str.lower( input( 3 * '\n' + 'DataBase: "' + myDataBase + '" exists. Delete? (Y/n) \n') )
  if answer == '' :
     answer = 'y'
  if answer == 'y' :
     os.remove( myDataBase )

######################################################################################

connection = sqlite3.connect( myDataBase )
cursor = connection.cursor()

cursor.execute( "CREATE TABLE IF NOT EXISTS families ( id INTEGER PRIMARY KEY AUTOINCREMENT, husbandName TEXT, wifeName TEXT, surname TEXT )" )
cursor.execute( "CREATE TABLE IF NOT EXISTS children ( id INTEGER PRIMARY KEY AUTOINCREMENT, familyID INTEGER, name TEXT, date TEXT, sex INTEGER )" )

for i in range( 200 ) :
   husbandName = random.choice( nameMaleList )
   wifeName = random.choice( nameFemaleList )
   surName = random.choice( surNameList )
   myNumber = random.randint( 0, 4 )
   cursor.execute( "%s ( '%s', '%s', '%s' )" % ( 'INSERT INTO families ( husbandName, wifeName, surname ) VALUES', husbandName, wifeName, surName ) )

   if myNumber > 0 :
      cursor.execute( 'SELECT id from families ORDER BY id DESC' )
      familiesID = cursor.fetchone()
      for nameNumber in range( myNumber ) :
         sex = random.randint( 0, 1 )
         if sex == 0 :
            childName = random.choice( nameMaleList )
         else :
            childName = random.choice( nameFemaleList )
         year = random.randint( 2000, 2021 )
         leapYear = False
         if year % 4 == 0 :
            leapYear = True

         month = random.randint( 1, 12 )
         if ( month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12 ) :
            day = random.randint( 1, 31 )
         elif ( month == 4 or month == 6 or month == 9 or month == 11 ) :
            day = random.randint( 1, 30 )
         elif ( month == 2 and leapYear ) :
            day = random.randint( 1, 29 )
         else :
            day = random.randint( 1, 28 )
         birthDate = "%4d-%02d-%02d" % ( year, month, day )
         cursor.execute( "%s ( '%s', '%s', '%s', '%s' )" % ( 'INSERT INTO children ( familyID, name, sex, date ) VALUES', familiesID[ 0 ], childName, sex, birthDate ) )

connection.commit()

connection.close()
