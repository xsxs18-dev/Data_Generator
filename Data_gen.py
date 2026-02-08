"""
File Dataset Generator
=====================

Generates a specified number of files with a total size in GB.
Useful for upload testing, cloud stress tests, app QA.

Works on: Windows, macOS, Linux, iOS (Pythonista / Pyto)
Python 3.x
"""

import os

# --------- CONFIG ---------
OUTPUT_FOLDER = "generated_files"  # output folder for generated files
# --------------------------

# Create folder if it doesn't exist
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

print("📦 File Dataset Generator\n")

# Ask user for input
while True:
    try:
        file_count = int(input("Enter number of files to generate: "))
        if file_count < 1:
            raise ValueError
        break
    except ValueError:
        print("⚠️ Please enter a valid positive integer.")

while True:
    try:
        total_size_gb = float(input("Enter total size in GB: "))
        if total_size_gb <= 0:
            raise ValueError
        break
    except ValueError:
        print("⚠️ Please enter a valid positive number.")

# Convert GB to bytes
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