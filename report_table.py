import matplotlib.pyplot as plt
import pandas as pd
name='report_bestcomb2'
input_filename=f'csv/report/{name}.csv'
def generate_styled_table_from_csv(file_path):
    df = pd.read_csv(file_path)

    df.rename(columns={df.columns[0]: 'Class'}, inplace=True)

    header_color = '#003366'      
    header_text_color = '#ffffff' 
    row_colors = ["#B2DAF1", "#ffffffff"] 
    edge_color = 'black'   

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.axis('tight')
    ax.axis('off')

    table = ax.table(cellText=df.values, colLabels=df.columns, loc='center', cellLoc='center')

    # 4. Styling
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1.2, 1.8) 

    for k, cell in table.get_celld().items():
        cell.set_edgecolor(edge_color)
        row, col = k
        
        if row == 0:
            cell.set_text_props(weight='bold', color=header_text_color, size=13)
            cell.set_facecolor(header_color)
        else:
            cell.set_facecolor(row_colors[row % 2])
            cell.set_text_props(color='#333333')
            
            class_name = df.iloc[row-1]['Class'] 
            if 'avg' in str(class_name) or 'total' in str(class_name):
                cell.set_text_props(weight='bold')

    
    output_img = f'images/report/{name}.jpg'
    plt.savefig(output_img, dpi=300, bbox_inches='tight')
    plt.show()

generate_styled_table_from_csv(input_filename)