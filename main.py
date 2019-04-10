'''
Plik startowy projektu - nie obsługuje danych testowych !!!!

'''


import representation.dnavec as dnavec
from Bio import SeqIO
import visualization.visualization as visualization
import classification.svm as svm
import data_working.basic_working
import os.path


print ("Witaj w projekcie licencjackim dotyczącym klasyfikacji DNA! Pamiętaj o umieszczeniu koniecznych danych wejściowych (w "
       "formie pojedynczego pliku fasta zawierajacego w każdym rekordzie jeden pełny genom i nazwę gatunku w id,"
       "bądź w formie całego folderu, gdzie każdy plik jest jednym gatunkiem, każdy rekord fragmentem genomu, a nazwa pliku to nazwa genomu)"
       "W FOLDERZE 'input' !!! ")

print("Dostępne możliwe formy reprezentacji danych to:"
      "\n 'dnavec' "
      "\n Proszę wybrać sposób reprezentacji danych")

reprezentacja = input()

print("Czy konieczna jest wstępna obróbka danych? (Czy dane nie są w 2 plikach genomy_plstd.fasta i genomy_prcr.fasta odpowiednio pofragmentowane?")
odpo = input()
if odpo == "tak" or odpo == "T" or odpo == "t" or odpo == "TAK":
    data_working.basic_working.start(os.path.dirname(__file__) + "/../input/TOBBGENOMES", os.path.dirname(__file__) + "/../input/plstd.fasta")

# tworzenie pustej zmiennej na późniejsze wektory dnavec. lista ta będzie zawierała je wszystkie (format wektorów, wymiary 450)
data = []

if reprezentacja == "dnavec":
    # Do funkcjonowania tej metody reprezentacji konieczny jest korpus językowy (można go utworzyć, co jest długie, bądź wczytać z wcześniej zapisanego pliku
    print('Tworzyć nowy korpus? (T/N)')
    z = input()
    if (z == 'T'):
        print("Pamiętaj, że tworzenie nowego korpusu jest bardzo czasochłonne! Jeżeli nie masz nowych danych w stosunku do "
              "poprzedich prób, być może nie ma to sensu. Wpisz 'zrozumiałem' ")
        przypomnienie = input()
        if przypomnienie == 'zrozumiałem':
            model = dnavec.DnaVec([os.path.dirname(__file__) +'/../input/genomy_plstd', os.path.dirname(__file__) + '/../input/genomy_prcr'])
    elif (z == 'N'):
        model = dnavec.DnaVec(corpus=True)



    # Generalnie jeżeli nie ma się więcej danych niż przy tworzeniu tego programu to własny korpus jest raczej bezsensowny
    print("Korpus wczytany pomyślnie!")

    for record in SeqIO.parse("input/genomy_plstd.fasta", 'fasta'):
        vec = model.to_vecs(record)
        # korpus ma postać 3 x 150 wymiarów - zamiana na 1 x 450
        vec = vec[0] + vec[1] + vec[2]
        vec = [vec, 'plstd']
        data.append(vec)
    for record in SeqIO.parse("dataset/genomy_prcr.fasta", 'fasta'):
        vec = model.to_vecs(record)
        vec = vec[0] + vec[1] + vec[2]
        vec = [vec, 'prcr']
        data.append(vec)
else:
    print("Przykro mi, ale nie obsługujemy podanego trybu")

# Na tym momencie działania programu model został poprawnie wczytany
# Teraz możliwe jest przeprowadzanie klasyfikacji i wizualizacji

print("Reprezentacja i dane wczytane pomyślnie")

print("Wybierz co chcesz dalej robić! Dostępne metody klasyfikacji:"
      "\n'svm-test' "
      "\n (tu powstanie możliwość przeprowadznia eksperymentu na już wytrenowanych i ustalonych klasyfikatorach"
      "\n Proszę podać model klasyfikacji danych!")

klasyfikacja = input()

if klasyfikacja == 'svm-test':
    pass
else:
    print("Wybacz, ale nie obsługujemy tej metody klasyfikacji")



