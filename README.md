# MetaAnalyzer
Praca licencjacka o zastosowaniu uczenia maszynowego w badaniach metagenomicznych

# Struktura projektu

1. dataset:
   fragmenty_plstd.fasta - losowa wybrana próbka 500 fragmnetów genomów mitochondrialnych
   fragmenty_prcr.fasta - losowo wybrana próbka 500 fragmentów genomów prokariotycznych
   fragmenty_wszystkie.fasta - plik ze wszystkimi fragmentami
   sample.txt - plik roboczy stworzony podczas formowania modelu dnavec
   dnavec.model.bin - zapisany model dnavec
   dnaveccorpus.txt - korpus stworzony z fragmentów 

2. representation:
   dnavec.py - tworzy metodę dnavec, do podziału na bazowy fragmenter i samą metodę
   randomtake.py - wybiera losowe fragmenty ze zbioru danych

3. visualization:
   visualization.py - plik zawiera wszystkie 3 metody wizualizacji tsne, pca i tsne + redukcja wymiaru z pca, w     przyszłości podział na oddzielne pliki

4. classification: 

5. test.py - Plik służący do testowego uruchamiania poszczególnych fragmentów projektu
6. main.py - plik odpowiadający za kontakt z używtkownikiem - główny plik (wciąż w fazie produkcji)
