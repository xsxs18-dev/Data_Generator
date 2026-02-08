# 📦 File Dataset Generator (PC + iOS)

**Generate large test datasets instantly – for uploads, storage testing, app QA, or cloud stress tests.**

---

## 🚀 Features

- Create any number of files
- Define total size in GB
- Works offline on Windows, macOS, Linux, and iOS (Pythonista / Pyto)
- Output files saved in a dedicated folder
- Fully copy-paste ready, no extra setup

---

## 📱 iOS Guide

1. Install **Pythonista** or **Pyto** app  
2. Copy `data_generator.py` into the app  
3. Run the script  
4. Enter number of files and total size in GB  
5. Generated files appear in `generated_files/`  

---

## 💻 PC Guide

1. Install Python 3.x  
2. Save `data_generator.py` in a folder  
3. Open terminal / command prompt  
4. Run script:
python dataset_generator.py
5. Enter number of files and total size in GB  
6. Generated files appear in `generated_files/`  

---

## 🧩 Example Use Cases

- **Upload Testing**: Check file upload limits in apps or cloud platforms  
- **QA / App Testing**: Generate reproducible test datasets  
- **Cloud / Server Testing**: Simulate real storage usage  
- **Development**: Stress-test disk usage, backups, or performance  

---

## 💡 How It Works

The script automatically calculates the size per file and generates files filled with zero bytes (`.bin`) into the `generated_files/` folder. Originals are never modified. Fully offline.

---

## 💸 Support / Donations (Optional)

If this tool saved you time or helped with testing, consider a voluntary crypto donation:

- **BTC:** bc1...  
- **USDT (TRC20):** T...  
- **ETH:** 0x...

Every contribution helps maintain and improve the project.

---

## 📝 License

MIT License – free to use, share, and improve.

---

# data_generator.py
# File Dataset Generator
# Generates files with a defined total size (GB)
# Works on Windows, macOS, Linux, iOS (Pythonista / Pyto)
# Python 3.x

import os

OUTPUT_FOLDER = "generated_files"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

print("📦 File Dataset Generator\n")

# User input
while True:
    try:
        file_count = int(input("Enter number of files: "))
        if file_count < 1:
            raise ValueError
        break
    except ValueError:
        print("⚠️ Please enter a valid positive integer.")

while True:
    try:
        total_size_gb = float(input("Enter total size (GB): "))
        if total_size_gb <= 0:
            raise ValueError
        break
    except ValueError:
        print("⚠️ Please enter a valid positive number.")

# Compute size per file
total_bytes = int(total_size_gb * 1024 * 1024 * 1024)
size_per_file = total_bytes // file_count

print(f"\nGenerating {file_count} files, total size: {total_size_gb} GB")
print(f"Each file will be ~{size_per_file / (1024*1024):.2f} MB\n")

# Generate files
for i in range(1, file_count + 1):
    filename = f"file_{i:03d}.bin"
    path = os.path.join(OUTPUT_FOLDER, filename)
    try:
        with open(path, "wb") as f:
            f.write(b"\0" * size_per_file)
        print(f"✅ Created: {filename}")
    except Exception as e:
        print(f"⚠️ Failed: {filename} | {e}")

print("\n🎉 All files generated successfully!")
print(f"Check the folder: '{OUTPUT_FOLDER}'")
