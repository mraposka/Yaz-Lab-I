using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Security.Policy;

namespace CSV
{
    class Program
    {
        static void Main()
        {
            string inputFilePath = "data.txt"; // Girdi dosyası
            string outputDirectory = "output/"; // Çıktı dosyalarının saklanacağı klasör
            /*
            Directory.CreateDirectory(outputDirectory);

            string[] gps = new string[]
            {
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
            };

            string currentYear = "2024";
            string currentGP = "";
            string currentSession = "";

            Dictionary<int, string> sessions = new Dictionary<int, string>
            {
                { 0, "Race" },
                { 1, "Qualifying" },
                { 2, "FP3" },
                { 3, "FP2" },
                { 4, "FP1" }
            };
            Dictionary<int, string> years = new Dictionary<int, string>
            {
                { 0, "2024" },
                { 1, "2023" },
                { 2, "2022" },
                { 3, "2021" },
                { 4, "2020" },
                { 5, "2019" },
                { 6, "2018" }
            };

            using (var reader = new StreamReader(inputFilePath))
            {
                string line;
                int count = 0;
                List<string> lines = new List<string>();
                while ((line = reader.ReadLine()) != null)
                {
                    if (!line.Contains(","))
                        continue;
                    if (line.Contains(", Done For"))
                        line = line.Substring(line.IndexOf(", D") + 2);
                    if ((line.Contains(" AM") || line.Contains(" PM")) && line.Split(':').Count() == 2)
                        continue;
                    if (line.Split(',').Count() == 3)
                        line = line.Split(',')[1].Remove(0, 1) + "," + line.Split(',')[2];
                    if (!line.Contains(" AM") && !line.Contains("PM") && !line.StartsWith("Done For"))//Satır Done For değilse ve AM PM gibi bişey içermiyorsa bozuktur atla 
                    {
                        if (!line.Contains(':'))
                            continue;

                        line = "No Time, " + line;
                    }
                    if (line.StartsWith("Done For"))
                    {
                        if (lines.Count <= 0)//Done For gelmiş ama öncesinde bir veri yok bu boş session anlamına gelir veya o pilot için boş session anlamına gelir bozuktur atla
                            continue;
                        if (lines[0] == "Div bulunamadı!" || lines[0] == "" || lines[0] == null)//Div bulunamadı veya veri boş ise bozuktur atla
                            continue;
                        if (line.Split(',').Count() >= 5)
                            line = line.Split(':')[0].Substring(0, line.Split(':')[0].Length - 1);//Done For 0,0,1,171:33 PM, COL: 1:33.450 Bu veriyi done for olarak almak için yanındaki veri bozuk atla
                        int[] indexs = line
                         .Replace("Done For ", "")
                         .Split(',')
                         .Select(int.Parse)
                         .ToArray();

                        string year = years[indexs[0]];
                        string gp = gps[indexs[1]];
                        string session = sessions[indexs[2]];
                        //Console.WriteLine(lines[0]);
                        string driver = lines[0].Split(',')[1].Split(':')[0].Trim();
                        string fileName = year + "-" + gp + "-" + session + "-" + driver + ".csv";
                        File.AppendAllLines(outputDirectory + fileName, lines);
                        //Console.WriteLine(fileName + " CSV dosyası " + count.ToString() + " kayıtla başarıyla oluşturuldu.");
                        lines.Clear();
                        count = 0;
                        continue;
                    }
                    count++;
                    if (line.Split(',').Count() > 2)
                        line = line.Substring(0, line.IndexOf(','));

                    lines.Add(line);
                }
            }
            */
            /*
            Console.WriteLine("CSV dosyaları başarıyla oluşturuldu.");
            Console.WriteLine("Combine İşlemi Başladı!");
            string[] csvFiles = Directory.GetFiles(@"C:\Users\Can\Desktop\Yaz-Lab-I\CSV\bin\Debug\output", "*.csv"); // Get all CSV files

            // Create a dictionary to hold data for each piste-pilot combination
            Dictionary<string, List<string>> pistePilotData = new Dictionary<string, List<string>>();

            foreach (var file in csvFiles)
            {
                // Extract piste and pilot identifiers from the file name
                string[] fileParts = file.Split('\\').Last().Split('-');
                string piste = fileParts[1]; // Piste (e.g., "Miami GP")
                string pilot = fileParts[3].Split('.').First(); // Pilot code (e.g., "STR")

                // Combine piste and pilot into a unique key
                string pistePilotKey = $"{piste}-{pilot}";

                // Read the file content
                string fileContent = File.ReadAllText(file);

                // If the piste-pilot combination already exists, add the data to the existing list
                if (!pistePilotData.ContainsKey(pistePilotKey))
                {
                    pistePilotData[pistePilotKey] = new List<string>(); // Create a new list for this combination if not already present
                }

                // Add the file content to the list of data for the respective piste-pilot combination
                pistePilotData[pistePilotKey].Add(fileContent);
            }

            // For each piste-pilot combination, write the distinct content to respective output files
            foreach (var entry in pistePilotData)
            {
                string outputFileName = $"output/combined/{entry.Key}.csv";
                Console.WriteLine($"Creating file: {outputFileName}");

                foreach (var data in entry.Value.Distinct())
                {
                    // Write distinct data to the corresponding CSV file
                    File.AppendAllText(outputFileName, data + Environment.NewLine); // Add newline after each data entry
                }
            }

            Console.WriteLine("CSV'ler pist-pilot kombinasyonlarına göre birleştirildi.");
            */
            Clean();
            Console.ReadKey();



        }

        public static void Clean()
        {
            string inputDirectory = @"C:\Users\Can\Desktop\Yaz-Lab-I\CSV\bin\Debug\output\combined";

            foreach (var file in Directory.GetFiles(inputDirectory, "*.csv"))
            {
                Console.WriteLine($"Processing file: {file}");

                // Read all lines from the file
                var lines = File.ReadAllLines(file);

                // Remove duplicates and empty lines
                var cleanedLines = lines
                    .Select(line => line.Trim()) // Trim whitespace
                    .Where(line => !string.IsNullOrWhiteSpace(line)) // Remove empty lines
                    .Distinct() // Remove duplicate lines
                    .ToList();

                // Overwrite the same file with cleaned content
                File.WriteAllLines(file, cleanedLines);

                Console.WriteLine($"Cleaned file: {file}");
            }

            Console.WriteLine("All files cleaned.");
        }
    }
}
