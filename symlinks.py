
import os
import argparse
from pathlib import Path

def read_symlinks_file(path):
    with open(path, 'r') as file:
        symlinks = [line.strip() for line in file if line.strip() and not line.startswith("#")]
    return symlinks

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Read symlinks from a file.")
    parser.add_argument("file_path", type=str, help="Path to the file containing symlinks")
    args = parser.parse_args()

    # folder path of symlinks file is always the source path for relative files
    sourcepath = Path(args.file_path).resolve().parent
    symlinks = read_symlinks_file(args.file_path)

    print(f"Source path: {sourcepath}")

    for symlink in symlinks:
        mapping = symlink.split("->", 1)

        frommapping = mapping[0].strip()
        tomapping = mapping[1].strip()
        
        symsource = (sourcepath / frommapping).resolve()
        symtarget = os.path.normpath(sourcepath / tomapping)

        os.makedirs(Path(symtarget).parent, exist_ok=True)

        if os.path.exists(symsource): # generally the source exists
            if os.path.exists(symtarget): #symtarget already exists and is a link?
                if Path(symtarget).resolve() == symsource:
                    print(f"Skipping Symlink {symlink}. Reason: Already exists.")
                    continue
                else:
                    if os.path.islink(symtarget):
                        print(f"Symlink {symlink} out of date for {symtarget} {os.readlink(symtarget)}. Updating symlink.")
                        os.rmdir(symtarget)
                    else:
                        print(f"Symtarget from {symlink} is a real folder! Please remove manually")
                        continue

            print(f"Creating symlink {symlink}!")
            os.symlink(symsource, Path(symtarget).resolve(), target_is_directory=True)
        else:
            print(f"Unable to find symsource {symsource} for {symlink}")

