import pandas as pd
import os

def pulisci_csv_da_duplicati(csv_master, csv_target, csv_output):
    """
    Rimuove dal 'csv_target' tutte le righe che sono già presenti nel 'csv_master'.
    Salva il risultato in 'csv_output'.
    """
    print(f"--- CONFRONTO: Master '{csv_master}' vs Target '{csv_target}' ---")
    
    # 1. Carica i file
    if not os.path.exists(csv_master) or not os.path.exists(csv_target):
        print("❌ Errore: Uno dei file non esiste!")
        return

    df_master = pd.read_csv(csv_master)
    df_target = pd.read_csv(csv_target)

    # 2. Arrotondamento (CRUCIALE per i file di machine learning)
    # Spesso i float differiscono per miliardesimi (es. 0.7142857 vs 0.7142858).
    # Arrotondiamo tutto a 4 cifre decimali per fare un confronto onesto.
    df_master = df_master.round(4)
    df_target = df_target.round(4)

    print(f"Righe Master: {len(df_master)}")
    print(f"Righe Target (prima): {len(df_target)}")

    # 3. IL TRUCCO: Merge con indicator=True
    # Uniamo il target col master. 
    # Le righe uguali avranno _merge='both'. Quelle uniche del target avranno _merge='left_only'.
    merged = df_target.merge(df_master, how='left', indicator=True)

    # 4. Filtriamo: teniamo SOLO quelle che non erano nel master ('left_only')
    df_pulito = merged[merged['_merge'] == 'left_only']

    # 5. Rimuoviamo la colonna tecnica '_merge'
    df_pulito = df_pulito.drop(columns=['_merge'])

    righe_rimosse = len(df_target) - len(df_pulito)
    print(f"Righe Target (dopo): {len(df_pulito)}")
    print(f"🗑️  Righe rimosse (perché già presenti nel master): {righe_rimosse}")

    # 6. Salvataggio
    df_pulito.to_csv(csv_output, index=False)
    print(f"✅ File pulito salvato come: {csv_output}\n")

# --- ESEMPIO DI UTILIZZO ---
# Sostituisci qui sotto i nomi dei tuoi file reali
file_1 = "csv/f1_search/search3_42_sorted.csv"
file_2 = "csv/f1_search/search3_999_sorted.csv"

pulisci_csv_da_duplicati(file_1, file_2, "csv/f1_search/search3_999_sorted.csv")
