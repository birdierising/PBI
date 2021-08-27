#!/usr/bin/python3

import argparse, datetime, pprint, sys
import mysql.connector as msc
from mysql.connector import errorcode

indoorconnection = msc.connect(option_files='/etc/mysql/conf.d/pbcli.cnf')

indoorcursor = indoorconnection.cursor()

# read section

def defaultsearch ( defaulttosearch ):
    defaulttosearch = sys.argv[1]

    defaultquery = f"SELECT plantid,common_name,location,notes FROM plants WHERE common_name like '%{defaulttosearch}%';"
    indoorcursor.execute(defaultquery)
    data = indoorcursor.fetchall()
    if not data:  
        print("No such plant in this collection yet")
    else:
        pprint.pprint(data)

def extrasdump ( extrastosearch ):
    extrastosearch = sys.argv[2]

    extrasquery = f"SELECT * FROM plants WHERE common_name like '%{extrastosearch}%';"
    indoorcursor.execute(extrasquery)
    data = indoorcursor.fetchall()
    if not data:  
        print("No such plant in this collection yet")
    else:
        pprint.pprint(data)

def flowersearch ( flowertosearch ):
    flowertosearch = sys.argv[2]

    flowerquery = f"SELECT common_name FROM plants WHERE flowering='{flowertosearch}';"
    indoorcursor.execute(flowerquery)
    data = indoorcursor.fetchall()
    if not data:  
        print("No such plant in this collection yet")
    else:
        pprint.pprint(data)

def idsearch ( idtosearch ):
    idtosearch = sys.argv[2]

    idquery = f"SELECT plantid,common_name FROM plants WHERE plantid='{idtosearch}';"
    indoorcursor.execute(idquery)
    data = indoorcursor.fetchall()
    if not data:  
        print("No such plant in this collection yet")
    else:
        pprint.pprint(data)

def latinnamesearch ( latinnametosearch ):
    latinnametosearch = sys.argv[2]

    latinnamequery = f"SELECT common_name,latin_name FROM plants WHERE latin_name like '%{latinnametosearch}%';"
    indoorcursor.execute(latinnamequery)
    data = indoorcursor.fetchall()
    if not data:  
        print("No such plant in this collection yet")
    else:
        pprint.pprint(data)

def locationsearch ( locationtosearch ):
    locationtosearch = sys.argv[2]

    locationquery = f"SELECT common_name,location FROM plants WHERE location like '%{locationtosearch}%';"
    indoorcursor.execute(locationquery)
    data = indoorcursor.fetchall()
    if not data:  
        print("No such plant in that location yet")
    else:
        pprint.pprint(data)

def commonnamesearch ( commonnametosearch ):
    commonnametosearch = sys.argv[2]

    commonnamequery = f"SELECT common_name FROM plants WHERE common_name like '%{commonnametosearch}%';"
    indoorcursor.execute(commonnamequery)
    data = indoorcursor.fetchall()
    if not data:  
        print("No such plant in this collection yet")
    else:
        pprint.pprint(data)

def datesearch ( datetosearch ):
    datetosearch = sys.argv[2]

    datequery = f"SELECT common_name,date_acquired FROM plants WHERE date_acquired like '%{datetosearch}%';"
    indoorcursor.execute(datequery)
    data = indoorcursor.fetchall()
    if not data:  
        print("No plant acquired on this date!")
    else:
        for (common_name, date_acquired) in data:
            print("{}: {:%b %d %Y}".format(
                common_name, date_acquired))

def notessearch ( notestosearch ):
    notestosearch = sys.argv[2]

    notesquery = f"SELECT common_name,notes FROM plants WHERE notes like '%{notestosearch}%';"
    indoorcursor.execute(notesquery)
    data = indoorcursor.fetchall()
    if not data:  
        print("No such plant with that note in this collection yet")
    else:
        pprint.pprint(data)

def plantgroupsearch ( plantgrouptosearch ):
    plantgrouptosearch = sys.argv[2]

    plantgroupquery = f"SELECT common_name FROM plants WHERE plant_group like '%{plantgrouptosearch}%';"
    indoorcursor.execute(plantgroupquery)
    data = indoorcursor.fetchall()
    if not data:  
        print("No such group in this collection yet")
    else:
        pprint.pprint(data)

def sunlightsearch ( sunlighttosearch ):
    sunlighttosearch = sys.argv[2]

    sunlightquery = f"SELECT common_name,sunlight FROM plants WHERE sunlight like '%{sunlighttosearch}%';"
    indoorcursor.execute(sunlightquery)
    data = indoorcursor.fetchall()
    if not data:  
        print("No such plant with those sunlight requirements in this collection yet")
    else:
        pprint.pprint(data)

def vendorsearch ( vendortosearch ):
    vendortosearch = sys.argv[2]

    vendorquery = f"SELECT common_name,vendor FROM plants WHERE vendor like '%{vendortosearch}%';"
    indoorcursor.execute(vendorquery)
    data = indoorcursor.fetchall()
    if not data:  
        print("No such plant from that vendor yet")
    else:
        pprint.pprint(data)

# writes section

def addplant ( planttoadd ):
    planttoadd = sys.argv[2]
    pid = int(input("Enter plant id: "))
    q = int(input("How many? "))
    ln = input("Enter Latin binomial: ")
    pg = input("Enter plant group: ")
    v = input("What vendor did this plant come from? ")
    s = input("What are its sun requirements? ")
    w = input("What are its watering needs? ")
    f = input("Does it flower? Y or N only ")
    l = input("Where does it live? ")
    n = input("Any additional notes? ")
    addquery = f"INSERT INTO plants (plantid, common_name, quantity, latin_name, plant_group, vendor, sunlight, water, flowering, location, notes) VALUES ({pid}, '{planttoadd}', '{q}', '{ln}', '{pg}', '{v}', '{s}', '{w}', '{f}', '{l}', '{n}');"
    indoorcursor.execute(addquery)
    indoorconnection.commit()
    checksuccess = f"SELECT * from plants WHERE common_name='{planttoadd}';"
    indoorcursor.execute(checksuccess)
    data = indoorcursor.fetchall()
    if not data:
        print("Something went wrong here")
    else:
        pprint.pprint(data)
    indoorcursor.close()
    indoorconnection.close()
    exit

def deleteplant ( planttodelete ):
    planttodelete = sys.argv[2]

    deletequery = f"DELETE FROM plants WHERE common_name='{planttodelete}';"
    indoorcursor.execute(deletequery)
    indoorconnection.commit()

def updateplantnote ( updateplantnote ):
    planttoupdate = sys.argv[2]

    notes = input("What notes need updated? ")
    updatequery = f"UPDATE plants SET notes='{notes}' WHERE common_name='{planttoupdate}';"
    indoorcursor.execute(updatequery)
    indoorconnection.commit()
    checksuccess = f"SELECT common_name,notes FROM plants WHERE common_name='{planttoupdate}';"
    indoorcursor.execute(checksuccess)
    data = indoorcursor.fetchall()
    if not data:
        print("Something went wrong here")
    else:
        pprint.pprint(data)

def updateplantquantity ( updateplantquantity ):
    planttoupdate = sys.argv[2]

    quantity = input("What plant quantity need updated? ")
    updatequery = f"UPDATE plants SET quantity='{quantity}' WHERE common_name='{planttoupdate}';"
    indoorcursor.execute(updatequery)
    indoorconnection.commit()
    checksuccess = f"SELECT common_name,quantity FROM plants WHERE common_name='{planttoupdate}';"
    indoorcursor.execute(checksuccess)
    data = indoorcursor.fetchall()
    if not data:
        print("Something went wrong here")
    else:
        pprint.pprint(data)

parser = argparse.ArgumentParser()
parser.add_argument("default",nargs='?',type=defaultsearch)
parser.add_argument('-b','--binomial','--latinname', type=latinnamesearch,action='store')
parser.add_argument('-c','--common-name', type=commonnamesearch,action='store')
parser.add_argument('-d', '--date', type=datesearch,action='store')
parser.add_argument('-e', '--extras', type=extrasdump,action='store')
parser.add_argument('-f', '--flowering', type=flowersearch,action='store')
parser.add_argument('-g', '--group', type=plantgroupsearch,action='store')
parser.add_argument('-i', '--id', type=idsearch,action='store')
parser.add_argument('-l', '--location', type=locationsearch,action='store')
parser.add_argument('-n', '--notes', type=notessearch,action='store')
parser.add_argument('-s', '--sunreqs', type=sunlightsearch,action='store')
parser.add_argument('-v', '--vendor', type=vendorsearch,action='store')
parser.add_argument('-a', '--add', type=addplant,action='store')
parser.add_argument('-u', '--updatenote', type=updateplantnote,action='store')
parser.add_argument('-q', '--updatequantity', type=updateplantquantity,action='store')
parser.add_argument('-z', '--delete', type=deleteplant,action='store')

args = parser.parse_args()
