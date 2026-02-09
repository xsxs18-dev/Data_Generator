import os
import shutil

OUT_DIR = "output"
CHUNK_SIZE = 1024 * 1024  # 1 MB

os.makedirs(OUT_DIR, exist_ok=True)

try:
    size_gb = float(input("Total size in GB: "))
    file_count = int(input("Number of files: "))
except ValueError:
    print("Invalid input.")
    raise SystemExit(1)

if size_gb <= 0 or file_count <= 0:
    print("Values must be positive.")
    raise SystemExit(1)

# decimal GB (1 GB = 1,000,000,000 bytes)
total_bytes = int(round(size_gb * 1_000_000_000))

free_space = shutil.disk_usage(OUT_DIR).free
if free_space < total_bytes:
    print("Not enough disk space.")
    raise SystemExit(1)

base_size = total_bytes // file_count
remainder = total_bytes % file_count

zero_chunk = b"\0" * CHUNK_SIZE

for i in range(file_count):
    target_size = base_size + (1 if i < remainder else 0)
    path = os.path.join(OUT_DIR, f"file_{i}.bin")

    with open(path, "wb") as f:
        remaining = target_size
        while remaining > 0:
            n = min(CHUNK_SIZE, remaining)
            f.write(zero_chunk[:n])
            remaining -= n

print("Done.")