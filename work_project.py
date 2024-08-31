import pandas as pd
import os

base_path = '/mnt/e/work/eori/CRM/Final'

file_path = os.path.join(base_path, 'ConsigneeData.xlsx')
df = pd.read_excel(file_path)

print(df.head())
print(df.info())

df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')

def get_top_5(df, group_by, value_column):
    return df.groupby(group_by)[value_column].sum().nlargest(5).reset_index()

# Top 5 Sales destinations for each exporter
top_destinations = df.groupby(['ExporterName', 'Country'])['Sales'].sum().reset_index()
top_destinations = top_destinations.sort_values(['ExporterName', 'Sales'], ascending=[True, False])
top_destinations = top_destinations.groupby('ExporterName').head(5)

# Top 5 importers for each exporter
top_importers = df.groupby(['ExporterName', 'ImporterName'])['Sales'].sum().reset_index()
top_importers = top_importers.sort_values(['ExporterName', 'Sales'], ascending=[True, False])
top_importers = top_importers.groupby('ExporterName').head(5)

# Top 5 exporters for each importer
top_exporters = df.groupby(['ImporterName', 'ExporterName'])['Sales'].sum().reset_index()
top_exporters = top_exporters.sort_values(['ImporterName', 'Sales'], ascending=[True, False])
top_exporters = top_exporters.groupby('ImporterName').head(5)

# Top 5 products for each exporter
top_products_exporter = df.groupby(['ExporterName', 'HSNCode'])['Sales'].sum().reset_index()
top_products_exporter = top_products_exporter.sort_values(['ExporterName', 'Sales'], ascending=[True, False])
top_products_exporter = top_products_exporter.groupby('ExporterName').head(5)

# Top 5 products for each importer
top_products_importer = df.groupby(['ImporterName', 'HSNCode'])['Sales'].sum().reset_index()
top_products_importer = top_products_importer.sort_values(['ImporterName', 'Sales'], ascending=[True, False])
top_products_importer = top_products_importer.groupby('ImporterName').head(5)

output_path = os.path.join(base_path, 'export_analysis_results.xlsx')
with pd.ExcelWriter(output_path) as writer:
    top_destinations.to_excel(writer, sheet_name='Top 5 Destinations', index=False)
    top_importers.to_excel(writer, sheet_name='Top 5 Importers', index=False)
    top_exporters.to_excel(writer, sheet_name='Top 5 Exporters', index=False)
    top_products_exporter.to_excel(writer, sheet_name='Top 5 Products (Exporter)', index=False)
    top_products_importer.to_excel(writer, sheet_name='Top 5 Products (Importer)', index=False)

print(f"Analysis complete. Results saved to '{output_path}'")