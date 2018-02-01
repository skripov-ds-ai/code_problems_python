from Bio.Seq import Seq

import for_input_and_output

name = "revp"

seq = for_input_and_output.read_seq(name, 'fasta')

print(seq)

s = ''

for_input_and_output.write_file(name, s)
