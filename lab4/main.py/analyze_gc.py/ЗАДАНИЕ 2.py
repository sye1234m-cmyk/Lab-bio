#ЗАДАНИЕ 2
from Bio import SeqIO

file = open("l4sequences.gb")
results = []

for record in SeqIO.parse(file, "genbank"):
    for feature in record.features:
        if feature.type == "CDS":
            dna = feature.extract(record.seq)
            g = dna.count("G")
            c = dna.count("C")
            all_letters = len(dna)
            gc = (g + c) / all_letters

            organism = record.annotations.get('organism', 'Unknown') #название организма

            if 'product' in feature.qualifiers: #название гена (продукта)
                product = feature.qualifiers['product'][0]
            else:
                product = "CDS"

            results.append([gc, record.id, organism, product])
            break # беру только первую CDS в записи

results.sort() #от меньшего к большему

for gc, rec_id, organism, product in results:
    print(f"{rec_id}: {organism} {product} gene, complete cds, GC = {gc:.6f}")
