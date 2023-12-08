import csv

filename = "lab11.csv"
try:
    csv_file = open(filename, "r")
    reader = list(csv.DictReader(csv_file))
    print("Year : Ukraine : USA")
    for year in range(2010, 2020):
        year_fmt = f"{year} [YR{year}]"
        ukraine_stat, usa_stat = [r[year_fmt] for r in reader]
        print(f"{year} : {ukraine_stat} : {usa_stat}")
    csv_file.close()
except Exception as e:
    print(f"Failed to open {filename}: {e}")

filename_w = "lab11_result.csv"
try:
    csv_file_w = open(filename_w, "w")
    fieldnames = ["Year", "Country with greater growth"]
    writer = csv.DictWriter(csv_file_w, fieldnames=fieldnames)
    writer.writeheader()
    print(filename)

    csv_file = open(filename, "r")
    reader = list(csv.DictReader(csv_file))
    print("writing...")
    for year in range(2010, 2020):
        year_fmt = f"{year} [YR{year}]"
        ukraine_stat, usa_stat = [r[year_fmt] for r in reader]

        writer.writerow({'Year':year, "Country with greater growth":("Ukraine" if ukraine_stat >= usa_stat else "USA")})

    csv_file.close()
    csv_file_w.close()
    
except Exception as e:
    print(f"Failed to open {filename}: {e}")
print("done!")