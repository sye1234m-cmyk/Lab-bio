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