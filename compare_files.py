# execute: python compare_files.py
def compare_files(file1, file2):
    # Read the contents of both files and store them in sets
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        file1_lines = set(f1.readlines())  # Convert to set for efficient comparison
        file2_lines = set(f2.readlines())

    # 1. Lines in file1.txt but not in file2.txt
    missing_in_file2 = file1_lines - file2_lines

    # 2. Lines in file2.txt but not in file1.txt
    missing_in_file1 = file2_lines - file1_lines

    # 3. Lines that exist in both file1.txt and file2.txt
    same_in_both = file1_lines & file2_lines

    # Write the results to separate text files
    with open('missing_in_file2.txt', 'w') as f:
        f.writelines(missing_in_file2)

    with open('missing_in_file1.txt', 'w') as f:
        f.writelines(missing_in_file1)

    with open('same_in_both.txt', 'w') as f:
        f.writelines(same_in_both)

    print("Comparison complete! Results exported to missing_in_file2.txt, missing_in_file1.txt, and same_in_both.txt.")

# Call the function to compare and export
compare_files('file1.txt', 'file2.txt')
