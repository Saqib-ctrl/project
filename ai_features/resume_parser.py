from pyresparser import ResumeParser
import os

def parse_resume(file_path):
    if not os.path.exists(file_path):
        return {"error": "File not found"}

    data = ResumeParser(file_path).get_extracted_data()
    return data