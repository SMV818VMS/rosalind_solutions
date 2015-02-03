dnaSequence = "GTCTCTGTGCCTAGCTCCCCGGCGGTTCCTGTGCGATTCTTAACTATACCTTCGCGACTCCCATTGCCTAAACCATTGCTTCGGGACTATGTGGCGGCATCCAAAGATGGCCACGTATACTTAGGTAAGCACCCGAGCGTTTCAGCTTATTTATCCGCAAACAAGTTGTTTGGCACGCTTGGCGATGCATAGCCAAGAGCATAGGGTGACCCATCATATTCCTCTATCTTTTGGTGGGAGGGATTTCCAATCCGGTAACGAAACGCTCAGCACAACTTTCGGATACTGTAAAGCCTTGTACGGGATAAGGTAAAATCCTTGATACAGCCACAACATGTATTCCACTAAATAAGCCGCATTAGCACGGATGATTCATCGGGTAGACGGAGTAGAAAATCATGCGTGGAGGCTGTCGAAACAGATCTGATTTCCGGTGGGTTACAAGAGTGTTATTCATCGACTTGATGACCGAAATTCCGAAGCATCGAGGTGCCCGCATTGATAGAAAAACAAACGGACACCCGCACTTCCTCCCGTAGAGAAAGCATAAGCCCATGTGCCGGGACTTGCTGTGATGTCTACCCTTATTTTAGGTTCACATTCTTAGCACAAATAACTGTGGCTAGCCCGTATGTCGTTTATTTCGGGTGGCGTCGGACGCGGAGAGACACGTTACCGTTAACCCCCGGAAGACATGGTACGATGCCTCTACCCGTGCGTGAAAGATTCATTCGTGGCCTAAAACGCGCACTCTGCGGTCACTTTCCCCGCTGTAGGATCCGGCGCTAGCTGCTCCCCTAGAGTCCACCATGATAACGACCCTCTACGGATGCAGCACACGAGGGCCACCTGGACTATTCGAGCCGAGCGCGGGCCGCCCCTACCGGATTTGCCCTAACCTCGCACTGTGAGTCAGCTACTGACTTGGGAGCGAGTTCTTGTTCCGTATTTGTGTCT"

def get_comp(dna): 
	complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
	reverse_complement = "".join(complement.get(base, base) for base in reversed(dna))
	return reverse_complement


x= get_comp(dnaSequence)
print (x)