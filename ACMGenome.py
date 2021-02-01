from reportlab.lib import colors 
from reportlab.lib.units import cm 
from reportlab.lib.colors import PCMYKColor, PCMYKColorSep, Color, black, blue, red
from Bio.Graphics import GenomeDiagram
from Bio import SeqIO
#set colors to be used for genomes
red50transparent = Color( 100, 0, 0, alpha=0.5)
blue50transparent = Color( 0, 0, 100, alpha=0.5)
#create empty diagram, add empty track, add empty feature set
record = SeqIO.read("Genome.gb", "genbank")
diagram = GenomeDiagram.Diagram("Tomato curly stunt virus, complete genome") 
track = diagram.new_track(1, name="Annotated Features") 
feature_set = track.new_set()
#generate diagram feature for each SeqFeature obj in SeqRecord
#alternate color between transparent blue and red
for feature in record.features: 
   if feature.type != "gene": 
      continue 
   if len(feature) % 2 == 0: 
      color = red50transparent
   else: 
      color = blue50transparent
   feature_set.add_feature(feature, color=color, label=True)
#make output file named Virus0.pdf
diagram.draw(format = "circular", circular=True, pagesize = (20*cm,20*cm), start = 0, end = len(record), circle_core = 0.7)
diagram.write("Virus0.pdf", "PDF")