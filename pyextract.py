import argparse
import zipfile
import tarfile
import os

def extract_zip(zip_file, output_dir, interactive=False):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        total_files = len(zip_ref.namelist())
        extracted_files = 0

        for file_info in zip_ref.infolist():
            extracted_files += 1
            file_name = file_info.filename
            if interactive:
                choice = input(f"Extract '{file_name}'? (y/n): ").lower()
                if choice != 'y':
                    continue

            zip_ref.extract(file_name, output_dir)
            print(f"Extracted '{file_name}' to '{output_dir}' ({extracted_files}/{total_files})")

def extract_tar(tar_file, output_dir, interactive=False, specific_file=None):
    with tarfile.open(tar_file, 'r:*') as tar_ref:
        total_files = len(tar_ref.getnames())
        extracted_files = 0

        for member in tar_ref.getmembers():
            if specific_file and specific_file != member.name:
                continue

            extracted_files += 1
            if interactive:
                choice = input(f"Extract '{member.name}'? (y/n): ").lower()
                if choice != 'y':
                    continue

            tar_ref.extract(member, output_dir)
            print(f"Extracted '{member.name}' to '{output_dir}' ({extracted_files}/{total_files})")

def main():
    parser = argparse.ArgumentParser(description="Archive Extractor")
    parser.add_argument("archive", help="Path to the archive file")
    parser.add_argument("output_dir", help="Directory where the contents will be extracted")
    parser.add_argument("--interactive", action="store_true", help="Interactive mode for file selection")
    parser.add_argument("--specific-file", help="Specify a specific file to extract")

    args = parser.parse_args()

    archive = args.archive
    output_dir = args.output_dir
    interactive = args.interactive
    specific_file = args.specific_file

    if archive.endswith(".zip"):
        extract_zip(archive, output_dir, interactive)
        print(f"Extracted '{archive}' to '{output_dir}'")
    elif archive.endswith(".tar") or archive.endswith(".tar.gz") or archive.endswith(".tgz"):
        extract_tar(archive, output_dir, interactive, specific_file)
        print(f"Extracted '{archive}' to '{output_dir}'")
    else:
        print(f"Unsupported archive format: {archive}")

if __name__ == "__main__":
    main()
