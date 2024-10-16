import biopython
from Bio.Seq import Seq

seq1 = Seq("ACGTAGCTACGATCACAGCTA")
print("DNA dizimiz:", seq1)

rc = seq1.reverse_complement()
print("Tamamlayıcı Ters Dizi:", rc)

rna = seq1.transcribe()
print("Kopyalanan Dizi:", rna)

protein = seq1.translate()
print("Protein Dizisi", protein)