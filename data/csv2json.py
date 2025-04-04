import csv
import json
import sys

def csv_to_ngsild(csv_file, json_file, type="v2", delimiter=','):
    entities = []

    with open(csv_file, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=delimiter)

        for row in reader:
            entity = {
                "id": "urn:ngsi-ld:City:" + row['id'],
                "type": "City",
                "name": {
                    "type": "Text" if type=="v2" else "Property",
                    "value": row['name']
                },
                "country": {
                    "type": "Text" if type=="v2" else "Property",
                    "value": row['country']
                },
                "location": {
                    "type": "geo:json" if type=="v2" else "GeoProperty",
                    "value": {
                        "type": "Point",
                        "coordinates": list(map(float, [row['long'], row['lat']]))
                    }
                },
                "year_foundation": {
                    "type": "Integer" if type=="v2" else "Property",
                    "value": int(row['year_foundation'])
                },
                "min_temperature": {
                    "type": "Integer" if type=="v2" else "Property",
                    "value": float(row['min_temperature'])
                },
                "max_temperature": {
                    "type": "Integer" if type=="v2" else "Property",
                    "value": float(row['max_temperature']),
                },
                "mean_temperature": {
                    "type": "Integer" if type=="v2" else "Property",
                    "value": float(row['mean_temperature'])
                },
                "safe_index": {
                    "type": "Integer" if type=="v2" else "Property",
                    "value": float(row['safe_index'])
                },
                "population": {
                    "type": "Integer" if type=="v2" else "Property",
                    "value": float(row['population'])
                },
                "population_2100": {
                    "type": "Integer" if type=="v2" else "Property",
                    "value": int(row['population_2100'])
                },

                "hdi": {
                    "type": "Float" if type=="v2" else "Property",
                    "value": float(row['hdi'])
                }
            }

            entities.append(entity)

    with open(json_file, 'w', encoding='utf-8') as jsonfile:
        json.dump(entities, jsonfile, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    if len(sys.argv) <= 3 or len(sys.argv) > 4:
        print(sys.argv)
        print("Usage: python script.py <input_csv_file> <output_json_file> [v2]")
        sys.exit(1)

    csv_file = sys.argv[1]
    json_file = sys.argv[2]

    type = "ld"
    if len(sys.argv) == 4:
        type = sys.argv[3]

    csv_to_ngsild(csv_file, json_file, type)
