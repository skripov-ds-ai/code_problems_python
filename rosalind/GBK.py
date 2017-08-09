# todo

from Bio import Entrez
import for_input_and_output
from my_own import email

name = "gbk"

file = [x.strip() for x in for_input_and_output.read_file(name)]

formats = ['Organism', 'Publication Date']
db = "nucleotide"
for_result = 'Count'

def get_from_genbank(file):
    Entrez.email = email
    term = "{file[0]}[%s] AND ({file[1]}[{0}] : {file[2]}[{0}])".format(formats[1], file=file) % formats[0]
    handle = Entrez.esearch(db=db, term=term)
    record = Entrez.read(handle=handle)
    return record[for_result]

s = get_from_genbank(file)
print(s)

for_input_and_output.write_file(name, s)