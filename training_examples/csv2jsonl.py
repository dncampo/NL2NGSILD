import csv
import json

# Define the system message
SYSTEM_MESSAGE = {
    "role": "system",
    "content": "I need you to perform as an expert in NGSI-LD with a background on semantic modeling and Smart Data Models (SDM). I will then send you some queries in Natural Language and you should convert them into NGSI-LD fully executable code to run in a FIWARE system (a Context Broker). Assume you are connected to a context broker in localhost and port 1026 and that your answers will be directly forwarded to the context broker; so send only the set of commands that would be sent to the CB, no explanation at all unless requested."
}

def convert_csv_to_jsonl(csv_file_path, jsonl_file_path, delimiter="|"):
    with open(csv_file_path, mode='r', encoding='iso-8859-1') as csv_file, open(jsonl_file_path, mode='w', encoding='utf-8') as jsonl_file:
        reader = csv.DictReader(csv_file, delimiter=delimiter)
        for row in reader:
            message = [
                SYSTEM_MESSAGE,
                {"role": "user", "content": row["prompt"]},
                {"role": "assistant", "content": row["response"]}
            ]
            json_line = json.dumps({"messages": message}, ensure_ascii=False)
            jsonl_file.write(json_line + "\n")

if __name__ == "__main__":
    csv_file_path = "queries_get_v3_convert.csv"  # Change to your actual CSV file path
    jsonl_file_path = "queries_get_v3.jsonl"  # Change to your desired output JSONL file path
    convert_csv_to_jsonl(csv_file_path, jsonl_file_path)
    print(f"Conversion complete. JSONL saved to {jsonl_file_path}")