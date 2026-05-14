#ЗАДАНИЕ 3
from Bio import SeqIO

file = open("l4sequences.gb")

for record in SeqIO.parse(file, "genbank"):
    for feature in record.features: #поиск  CDS в каждой записи
        if feature.type == "CDS":
            dna = feature.extract(record.seq)
            protein = dna.translate(to_stop=True) #трансляция ДНК в белок

            location = feature.location #плюс-цепь или минус-цепь
            if location.strand == 1:
                strand = "+"
            else:
                strand = "-"

            organism = record.annotations.get('organism', 'Unknown') #название организма из аннотации

            if 'product' in feature.qualifiers: # название гена (продукта)
                product = feature.qualifiers['product'][0]
            else:
                product = "CDS"

            print(f"{record.id}: {organism} {product}, complete cds")
            print(f"Coding sequence location = [{location.start}:{location.end}] ({strand})")
            print("Translation =")

            for i in range(0, len(protein), 60):
                print(protein[i:i + 60])
            print()

            break # беру только первую CDS в каждой записи

