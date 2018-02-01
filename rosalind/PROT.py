from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

import for_input_and_output

name = "prot"

file = [x.strip() for x in for_input_and_output.read_file(name)]

seq = Seq(file[0], IUPAC.unambiguous_rna)

s = str(seq.translate(to_stop=True))

for_input_and_output.write_file(name, s)
