import os
import glob
from collections import defaultdict
import re

def main():
    input_file_path = "data.txt"  # Girdi dosyası
    output_directory = "output"  # Çıktı dosyalarının saklanacağı klasör
    combined_output_directory = os.path.join(output_directory, "combined")  # Kombine edilmiş dosyaları tutacak klasör

    # Çıktı klasörünü oluştur (eğer yoksa)
    os.makedirs(output_directory, exist_ok=True)
    os.makedirs(combined_output_directory, exist_ok=True)

    gps = [
        "Sao Paulo GP",
        "Mexcio City GP",
        "United States GP",
        "Singapore GP",
        "Azerbaijan GP",
        "Italian GP",
        "Dutch GP",
        "Belgian GP",
        "Hungarian GP",
        "British GP",
        "Austrian GP",
        "Spanish GP",
        "Canadian GP",
        "Monaco GP",
        "Emilia Romagna GP",
        "Miami GP",
        "Chinese GP",
        "Japanese GP",
        "Austrilian GP",
        "Saudi Arabian GP",
        "Bahrain GP",
        "Pre-Season Testing",
    ]

    sessions = {
        0: "Race",
        1: "Qualifying",
        2: "FP3",
        3: "FP2",
        4: "FP1",
    }
    years = {
        0: "2024",
        1: "2023",
        2: "2022",
        3: "2021",
        4: "2020",
        5: "2019",
        6: "2018",
    }

    driver_data = defaultdict(list) # Create a dictinary for each driver data
    csv_file_count = 0 # Initialize counter

    with open(input_file_path, "r", encoding="utf-8") as reader:
        
        for line in reader:
            line = line.strip()  # Satır başı boşlukları kaldır
            if "," not in line:
                continue
            if ", Done For" in line:
                 line = line[line.index(", D") + 2:]
            if (" AM" in line or " PM" in line) and line.count(":") == 2:
                continue
            if line.count(",") == 2:
                line = line.split(",")[1].lstrip() + "," + line.split(",")[2]  # remove first space in second split item
            if " AM" not in line and "PM" not in line and not line.startswith("Done For"):
                if ":" not in line:
                    continue
                line = "No Time, " + line
           
            if line.startswith("Done For"):

                
                if not driver_data: #If empty do not continue
                   continue

                # Yeni: Sadece sayıları al
                match = re.search(r"Done For (\d+,\d+,\d+)", line)
                if match:
                    numbers_str = match.group(1)
                    indexs = list(map(int, numbers_str.split(",")))
                else:
                    continue

                year = years[indexs[0]]
                gp = gps[indexs[1]]
                session = sessions[indexs[2]]
                driver = list(driver_data.keys())[0].split(",")[1].split(":")[0].strip() #Get the driver from keys

                file_name = f"{year}-{gp}-{session}-{driver}.csv"
                with open(os.path.join(output_directory, file_name), "w", encoding="utf-8") as output_file: #write mode
                    for l in driver_data.get(list(driver_data.keys())[0]):
                        output_file.write(l + "\n")  # Write data to file
                csv_file_count += 1 #Increase counter after each file is created
                driver_data = defaultdict(list)
                continue
            if driver_data.get(line) == None:
                driver_data[line] = []
            driver_data[list(driver_data.keys())[0]].append(line)


    print("CSV dosyaları başarıyla oluşturuldu.")
    print(f"Toplam {csv_file_count} adet CSV dosyası oluşturuldu.")
    print("Combine İşlemi Başladı!")

    csv_files = glob.glob(os.path.join(output_directory, "*.csv"))  # Get all CSV files

    # Create a dictionary to hold data for each piste-pilot combination
    piste_pilot_data = defaultdict(list)  # defaultdict can handle new key cases without errors

    for file in csv_files:
        # Extract piste and pilot identifiers from the file name
        file_parts = os.path.basename(file).split('-')
        piste = file_parts[1]  # Piste (e.g., "Miami GP")
        pilot = file_parts[3].split('.')[0]  # Pilot code (e.g., "STR")

        print(f"P:{piste}")
        print(f"p:{pilot}")
        # Combine piste and pilot into a unique key
        piste_pilot_key = f"{piste}-{pilot}"
        # Read the file content
        with open(file, "r", encoding="utf-8") as file_reader:
            file_content = file_reader.read()
        piste_pilot_data[piste_pilot_key].append(file_content)

    # For each piste-pilot combination, write the distinct content to respective output files
    for key, data_list in piste_pilot_data.items():
        output_file_name = os.path.join(combined_output_directory, f"{key}.csv")
        print(f"Creating file: {output_file_name}")

        # Combine all data for the current piste-pilot combination
        all_data = []
        for data in data_list:
            all_data.extend(data.splitlines())
        
        # Write distinct lines to the combined file, preserving order
        seen_lines = []
        with open(output_file_name, "w", encoding="utf-8") as output_file:
            for line in all_data:
                if line not in seen_lines and line.strip():
                   output_file.write(line.strip() + "\n")
                   seen_lines.append(line)
            

    print("CSV'ler pist-pilot kombinasyonlarına göre birleştirildi.")

    clean(combined_output_directory)
    input()  # Wait for keyboard

def clean(input_directory):
    for file in glob.glob(os.path.join(input_directory, "*.csv")):
        print(f"Processing file: {file}")

        with open(file, 'r', encoding="utf-8") as f:
            lines = f.readlines()
           
        # Remove duplicates and empty lines
        cleaned_lines = []
        seen_lines = []
        for line in lines:
            cleaned_line = line.strip()
            if cleaned_line and cleaned_line not in seen_lines:
                cleaned_lines.append(cleaned_line)
                seen_lines.append(cleaned_line)

        with open(file, 'w', encoding="utf-8") as f:
            for line in cleaned_lines:
                f.write(line + "\n")
        
        print(f"Cleaned file: {file}")

    print("All files cleaned.")

main()