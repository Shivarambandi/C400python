import csv

# Manually download the file and save it as 'taxi_zone_lookup.csv'

# Initialize variables
total_records = 0
unique_boroughs = set()
brooklyn_records = 0

# Read the CSV file and process data
with open('taxi_zone_lookup.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        total_records += 1  # Count total records
        unique_boroughs.add(row['Borough'])  # Add borough to the set
        if row['Borough'] == 'Brooklyn':  # Count Brooklyn records
            brooklyn_records += 1

# Convert unique boroughs to a sorted list
sorted_boroughs = sorted(unique_boroughs)

# Save output to taxi_zone_output.txt
output_file = "taxi_zone_output.txt"
with open(output_file, 'w') as f:
    f.write(f"Total Records: {total_records}\n")
    f.write(f"Unique Boroughs (Ascending): {', '.join(sorted_boroughs)}\n")
    f.write(f"Brooklyn Borough Records: {brooklyn_records}\n")

print("Data processing complete, file saved to taxi_zone_output.txt.")
