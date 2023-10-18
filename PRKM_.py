import pandas as pd

# Load the data from the CSV file
data = pd.read_csv("gene_expression_data.csv")

# Extract the relevant columns
read_count = data['Read_Count']
gene_length = data['Gene_Length']
total_reads = data['Total_Reads']

# Calculate RPKM for each gene
rpkm_values = []
for i in range(len(data)):
    rpkm = (read_count[i] / (gene_length[i] / 1000)) / (total_reads[i] / 1000000)
    rpkm_values.append(rpkm)

# Add RPKM values to the DataFrame
data['RPKM'] = rpkm_values

# Save the DataFrame with RPKM values to a new CSV file
data.to_csv("gene_expression_data_with_rpkm.csv", index=False)
