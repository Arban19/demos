import pandas as pd
import os

# Define the base path
base_path = '/mnt/e/work/eori/CRM/Final'

# Input and output file paths
input_file = os.path.join(base_path, 'AnalysisFile.xlsx')
output_file = os.path.join(base_path, 'export_analysis_results_reformatted.xlsx')

# Function to reformat a dataframe
def reformat_df(df, group_col, value_col):
    return df.groupby(group_col)[value_col].agg(lambda x: ', '.join(x.astype(str))).reset_index()

# List of sheets to process
sheets = [
    ('Top 5 Destinations', 'ExporterName', 'Country'),
    ('Top 5 Importers', 'ExporterName', 'ImporterName'),
    ('Top 5 Exporters', 'ImporterName', 'ExporterName'),
    ('Top 5 Products (Exporter)', 'ExporterName', 'HSNCode'),
    ('Top 5 Products (Importer)', 'ImporterName', 'HSNCode')
]

# Process each sheet
with pd.ExcelWriter(output_file) as writer:
    for sheet_name, group_col, value_col in sheets:
        # Read the sheet
        df = pd.read_excel(input_file, sheet_name=sheet_name)
        
        # Reformat the dataframe
        result = reformat_df(df, group_col, value_col)
        
        # Write to the new Excel file
        result.to_excel(writer, sheet_name=sheet_name, index=False)
        
        print(f"Processed {sheet_name}")
        print(result.head())
        print("\n")

print(f"Reformatting complete. Results saved to '{output_file}'")