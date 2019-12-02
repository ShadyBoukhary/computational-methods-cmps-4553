"""
Shady Boukhary
CMPS 4553
Computational Methods
Dr. Johnson
Fall 2019
Biopython Amino Acid Search

Seraches through a DNA sequence to find all Open Reading Frames.
Starts the search from a start codon ATG to a stop codon TAA, TAG, or TGA
Only looks for genes that are longer than 1000. Searches the sequence and its 
reverse complement as well. Prints the ORFs, their location, their length, and 
their corresponding translated amino acids.

"""
from Bio.Seq import Seq
from Bio import SeqIO

min_nuc_length = 1000
orfs = []

def is_start(codon):
  return codon == "ATG"

def is_end(codon):
  return codon in ["TAA", "TAG", "TGA"]

def find_orfs(nuc):
  """Finds all ORFs

  Searches the nucleotide for ORFs and appends them to the ORFs list.

  Args:
    nuc (str): The nucleotide to be searched
  """
  l = len(nuc) - 9
    # find starting point for orf
  for i in range(l):
    codon = nuc[i:i+3]
    # find stop codon after finding start codon
    if is_start(codon):
      start_loc = i
      next_codon_loc = start_loc + 3
      next_codon_end_loc = next_codon_loc + 3
      next_codon = nuc[next_codon_loc:next_codon_end_loc]
      # look for stop codon
      while not is_end(next_codon) and not next_codon_loc >= l:
        next_codon_loc += 3
        next_codon_end_loc += 3
        next_codon = nuc[next_codon_loc:next_codon_end_loc]
      end_loc = next_codon_end_loc
      # add valid orf to list
      if end_loc - start_loc >= min_nuc_length:
        orfs.append((nuc[start_loc:end_loc], start_loc, end_loc))


def print_results():
  """Prints the ORFs and corresponding amino acids"""
  # print header, didn't want to copy the header here lol
  with open("./main.py") as f:
    lines = f.readlines()
    print(''.join(lines[1:14]))

  print("ORFs found non-translated:")
  print("Total %i" % len(orfs))
  for s, start_loc, end_loc in orfs:
    print("%s...%s %i:%i, length %i" % (s[:30], s[-3:], start_loc, end_loc, end_loc - start_loc))

  print("Corresponding amino acids:")
  for s, start_loc, end_loc in orfs:
    ac = str(s.translate(1))
    print("%s...%s, length %i" % (ac[:50], ac[-3:], len(ac)))


if __name__ == "__main__":
  # load dna sequence from file
  for seq_record in SeqIO.parse("data.gb", "genbank"):
    seq = seq_record.seq
    # find orfs in seq and reverse complement
    for nuc in [seq, seq.reverse_complement()]:
      find_orfs(nuc)
      
  print_results()
  
