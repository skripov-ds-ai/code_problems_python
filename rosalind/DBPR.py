import for_input_and_output
from Bio import ExPASy
from Bio import SwissProt


name = "dbpr"

file = [x.strip() for x in for_input_and_output.read_file(name)]

gene_ontology = "GO"
colon = ':'

s = ""


def get_list(uniprot_id):
    handle = ExPASy.get_sprot_raw(uniprot_id)
    record = SwissProt.read(handle)
    s = '\n'.join([x[2].split(colon)[1] for x in record.cross_references if x[0] == gene_ontology and x[2].startswith('P')])
    return s


s += get_list(file[0])

print(s)

for_input_and_output.write_file(name, s)
