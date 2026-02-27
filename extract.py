import os
import sys
import subprocess

try:
    import pypdf
except ImportError:
    print("Installing pypdf...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pypdf"])
    import pypdf

def extract_text(pdf_path, out_path):
    try:
        reader = pypdf.PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            res = page.extract_text()
            if res:
                text += res + "\n"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Successfully extracted {pdf_path} to {out_path}")
    except Exception as e:
        print(f"Failed to extract {pdf_path}: {e}")

if __name__ == "__main__":
    extract_text("Chuckrow_Sachiel_Resume.pdf", "resume.txt")
    extract_text("SachielC_transcript.pdf", "transcript.txt")
