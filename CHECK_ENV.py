import os
from dotenv import load_dotenv

load_dotenv()

database_url = os.getenv("DATABASE_URL")

print("--- Checking Environment ---")
if database_url:
    print(f"DATABASE_URL found: {database_url}")
else:
    print("DATABASE_URL is NOT FOUND in the environment.")
print("--------------------------")