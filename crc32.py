print(f"made by grapes")
import os
import zlib
import csv

def calculate_crc32(file_path):
    with open(file_path, "rb") as f:
        checksum = 0
        for chunk in iter(lambda: f.read(4096), b""):
            checksum = zlib.crc32(chunk, checksum)
    return checksum & 0xFFFFFFFF


def scan_directory(directory):
    """scan"""
    print(f"scaning directory and calculateing the hash(es)")
    results = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            crc32 = calculate_crc32(file_path)
            results.append((file, crc32))
    return results


def export_to_csv(results, output_file):
    print(f"exporting")
    """export"""
    with open(output_file, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["file name", "crc32"])
        for file_name, crc32 in results:
            writer.writerow([file_name, format(crc32, "08X")])


if __name__ == "__main__":
    """variables"""
    # keep r string otherwise it wont scan
    directory_to_scan = r"C:\Users\xxxxxxxx"  # change directory. might only work if this script is on the same drive as path
    output_csv_file = "output_crc.csv"
    results = scan_directory(directory_to_scan)
    export_to_csv(results, output_csv_file)

    print(f"list has been exported to {output_csv_file}")
