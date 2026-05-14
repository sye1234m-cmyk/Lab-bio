# ЕМЕЛЬЯНЕНКО АНАСТАСИЯ
# ЛАБОРАТОРНАЯ РАБОТА 4
# ВАРИАНТ 6
#ЗАДАНИЕ 1
from Bio import Entrez
from Bio import SeqIO

Entrez.email = "stasysye00@gmail.com" #email для доступа к NCBI



def get_data(name, num=5): #поиск записей с сайта NCBI
    search = Entrez.esearch(db="nucleotide",
                            term=f"{name}[Organism] AND complete cds",
                            retmax=num)
    ids = Entrez.read(search)["IdList"]

    data = []
    for id in ids: #cкачивание каждой записи в формате genbank
        nucl = Entrez.efetch(db="nucleotide", id=id, rettype="gb", retmode="text")
        data.append(SeqIO.read(nucl, "genbank"))
        nucl.close()

    print(f"Получили {len(data)} для {name}")
    return data


first = get_data("Apis mellifera", 5)
second = get_data("Malus domestica", 5)

all_data = first + second
SeqIO.write(all_data, "l4sequences.gb", "genbank")
print(f"Файл готов, в итоге: {len(all_data)} записей")

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

