import os  # Modulo per operazioni sul filesystem
import sys  # Modulo per l'interazione con il sistema e gli argomenti da riga di comando
from collections import Counter # Modulo per gestire il dizionario

def get_shebang(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            first_line = f.readline().strip()
            if first_line.startswith("#!"):
                return first_line
    except Exception:
        pass
    return None


def count_executables_by_shebang(directory):
    shebang_counter = Counter()

    if not os.path.isdir(directory):
        print(f"Errore: {directory} non è una directory valida.")
        sys.exit(1)

    for root, _, files in os.walk(directory):  # Scansiona la directory ricorsivamente ottenendo:
                                               # cartella auttuale, sottocartelle, file presenti
        for file in files:
            file_path = os.path.join(root, file)  # Costruisce il percorso completo del file
            if os.path.isfile(file_path) and os.access(file_path, os.X_OK):  # Verifica se il file è eseguibile
                shebang = get_shebang(file_path)
                if shebang:
                    shebang_counter[shebang] += 1

    return shebang_counter


def main():
    if len(sys.argv) != 2:
        print(f"Uso: {sys.argv[0]} <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    results = count_executables_by_shebang(directory)

    for shebang, count in results.most_common():  # Ordina e stampa i risultati
        print(f"{count} {shebang}")


if __name__ == "__main__":
    main()
