"""
drug_engine.py
بحث مبدئي في بيانات الأدوية (سيكون موصول لاحقًا بقاعدة بيانات / API).
"""

DRUG_DB_SAMPLE = {
    "paracetamol": {
        "name": "Paracetamol",
        "dosage": "500 mg every 4-6 hours",
        "indications": ["Pain", "Fever"],
        "warnings": ["Do not exceed 4g/day", "Liver disease caution"]
    }
}

def get_drug_info(name: str):
    key = name.strip().lower()
    return DRUG_DB_SAMPLE.get(key, {"error": "Drug not found in local DB (sample)."})

if __name__ == "__main__":
    print(get_drug_info("paracetamol"))
