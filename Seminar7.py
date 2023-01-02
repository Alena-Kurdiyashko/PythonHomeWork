from os.path import exists
from Seminar7_creating import creating
from Seminar7_write import writing_scv
from Seminar7_write import writing_txt


path = 'Sem7_Phonebook.csv'
valid = exists(path)
if not valid:
    creating()

writing_scv()
writing_txt()