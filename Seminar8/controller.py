import os
import view as vw
import sqlite3 as sl
import createDB

def pathdata():
    a = os.path.basename(__file__)
    return os.path.abspath(__file__).replace(a, '')

def init():
    pth=pathdata()+'data.db'
    db = sl.connect(pth)
    createDB.createUsers(db)
    createDB.createCabinet(db)
    vw.option(db)

  
  