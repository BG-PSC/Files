# Skrypt do tworzenia zbiorczego pliku: KOD DZIAŁKA PUNKT_NAZWA

kod_dzialka_path = r'pliki\S19\kod-dzialka.txt'
punkty_path = r'pliki\S19\punkty.txt'
output_path = 'zbiorczy.txt'

def wczytaj_kod_dzialka(path): 
    pairs = []
    with open(path, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split('\t')
            if len(parts) >= 2:
                kod, dzialka = parts[0], parts[1]
                pairs.append((kod, dzialka))
    return pairs

def wczytaj_punkty(path):
    dzialka2punkty = {}
    with open(path, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split('\t')
            if len(parts) >= 2:
                dzialka, punkt = parts[0], parts[1]
                dzialka2punkty.setdefault(dzialka, []).append(punkt)
    return dzialka2punkty

def main():
    pairs = wczytaj_kod_dzialka(kod_dzialka_path)
    dzialka2punkty = wczytaj_punkty(punkty_path)
    with open(output_path, 'w', encoding='utf-8') as out:
        for kod, dzialka in pairs:
            punkty = dzialka2punkty.get(dzialka, [])
            for punkt in punkty:
                out.write(f"{kod}\t{dzialka}\t{punkt}\n")

if __name__ == "__main__":
    main()
