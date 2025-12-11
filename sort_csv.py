import pandas as pd
import os

# Percorsi dei file
input_csv = 'csv/f1_search/search2.csv'
output_csv = 'csv/f1_search/search2b_sorted.csv'

try:
    # 1. Leggi il CSV
    df = pd.read_csv(input_csv)
    
    # 2. Ordina il DataFrame
    # - Prima colonna: 'f1_macro_avg' -> Ascending=False (dal più alto al più basso)
    # - Seconda colonna: 'final_val_loss' -> Ascending=True (dal più basso al più alto)
    #   (La loss serve come spareggio: a parità di F1, vince chi ha loss minore)
    
    cols_to_sort = ['f1_macro_avg']
    sort_order = [False] # Decrescente per F1
    
    # Se hai salvato anche la loss nel csv, la usiamo per lo spareggio
    if 'final_val_loss' in df.columns:
        cols_to_sort.append('final_val_loss')
        sort_order.append(True) # Crescente per Loss (più bassa è meglio)
        
    df_sorted = df.sort_values(by=cols_to_sort, ascending=sort_order)

    # 3. Salva il nuovo CSV ordinato
    df_sorted.to_csv(output_csv, index=False)
    
    print(f"✅ Classifica salvata in: {output_csv}")
    print("\n🏆 --- TOP 3 MODELLI ---")
    
    # Seleziona alcune colonne interessanti da mostrare a video
    preview_cols = ['f1_macro_avg', 'layer_number', 'lr', 'batch_size']
    # Aggiungi loss se esiste
    if 'final_val_loss' in df.columns:
        preview_cols.append('final_val_loss')
        
    # Filtra solo colonne che esistono davvero nel csv per evitare errori di stampa
    valid_cols = [c for c in preview_cols if c in df_sorted.columns]
    
    print(df_sorted[valid_cols].head(3).to_string(index=False))

except FileNotFoundError:
    print(f"❌ Errore: Non trovo il file {input_csv}. Hai fatto girare il training?")
except KeyError as e:
    print(f"❌ Errore: Il nome della colonna nel CSV non è corretto. Controlla il CSV. {e}")