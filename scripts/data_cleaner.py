# Simple Data Engineering Utility: Data Cleaner
def clean_string(text):
    return text.strip().capitalize()

raw_data = ["  nairobi", "kenya  ", " DATA engineering  "]
cleaned_data = [clean_string(item) for item in raw_data]

print("Raw Data:", raw_data)
print("Cleaned Data:", cleaned_data)