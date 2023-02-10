# Install Biopython
!pip install biopython

from google.colab import drive
drive.mount('/content/drive')

'''
Save all the Protein IDs of ATPase genes from the first Galdieria sulphuraria whole genome scaffold that you find.  
Save them into a file called G_sulphuraria_atpase_ids.  

Hint:  You are going to have to modify my “retrieve_nucleotide_genbank_example.py” to search for feature types of CDS then look for feature qualifiers of products that contain ATPase  (if  ‘ATPase’ in feature.qualifiers['product'][0]).  
Hint #2:  Note that instead of extracting the DNA sequence, you will need to write the feature qualifier named ‘protein_id’ out to a file).

'''

## Call appropriate modules to run BioPython and retreive NCBI data.
from Bio import Entrez
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

# Bypass NCBI email address input requirement.
Entrez.email = 'ugwupaschal@gmail.com'

#Get the G. suphuraria whole genome
handle = Entrez.esearch(db="nucleotide", term="Galdieria sulphuraria[ORGN] AND ATPase AND scaf_4")
records = Entrez.read(handle)
handle.close()
print(records['Count'])

#Get first record
print(records['IdList'][0])
handle = Entrez.efetch(db="nucleotide", id=records['IdList'][0], rettype="gb", retmode="text")
record = SeqIO.read(handle, "genbank")
handle.close()

# Look for Coding regions and look to see if ATPase is in the product
ATPase_list = []
for feature in record.features:
    if feature.type == 'CDS':
        if "ATPase" in feature.qualifiers["product"][0]:
            print(feature.qualifiers["product"])
            ATPase_list.append(feature.qualifiers["protein_id"][0])
            print(feature.qualifiers["protein_id"][0])

#Output IDs to a file
output_handle = open("/content/drive/My Drive/Colab Notebooks/Galdieria sulphuraria_atpase_ids","w")
output_handle.write("\n".join(ATPase_list))
output_handle.close()
