import argparse
import zipfile
import tarfile

def extract_zip(zip_file, output_dir):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(output_dir)

def extract_tar(tar_file, output_dir):
    with tarfile.open(tar_file, 'r:*') as tar_ref:
        tar_ref.extractall(output_dir)

def main():
    parser = argparse.ArgumentParser(description="Archive Extractor")
    parser.add_argument("archive", help="Path to the archive file")
    parser.add_argument("output_dir", help="Directory where the contents will be extracted")

    args = parser.parse_args()

    archive = args.archive
    output_dir = args.output_dir

    if archive.endswith(".zip"):
        extract_zip(archive, output_dir)
        print(f"Extracted '{archive}' to '{output_dir}'")
    elif archive.endswith(".tar") or archive.endswith(".tar.gz") or archive.endswith(".tgz"):
        extract_tar(archive, output_dir)
        print(f"Extracted '{archive}' to '{output_dir}'")
    else:
        print(f"Unsupported archive format: {archive}")

if __name__ == "__main__":
    main()
