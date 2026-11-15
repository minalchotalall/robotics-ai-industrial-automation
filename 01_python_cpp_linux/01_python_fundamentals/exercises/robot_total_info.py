from pathlib import Path

print("\n--- EXERCISE 09: LINUX AND PROJECT MANAGEMENT ---")

# 1. Identify the current working directory
current_folder = Path.cwd()

print("\nCurrent folder:")
print(current_folder)

# 2. List all files in the current folder
print("\nFiles and folders in this directory:")

for item in current_folder.iterdir():
    if item.is_file():
        print("FILE:", item.name)
    elif item.is_dir():
        print("FOLDER:", item.name)

# 3. Count Python files and CSV files
python_files = list(current_folder.glob("*.py"))
csv_files = list(current_folder.glob("*.csv"))

print("\nNumber of Python files:", len(python_files))
print("Number of CSV files:", len(csv_files))

# 4. Calculate the total size of the files
total_size = 0

for item in current_folder.iterdir():
    if item.is_file():
        total_size += item.stat().st_size

print("Total file size:", total_size, "bytes")

# 5. Create a project report
report = current_folder / "project_report.txt"

with open(report, "w") as file:
    file.write("PROJECT REPORT\n")
    file.write("====================\n")
    file.write(f"Project folder: {current_folder}\n")
    file.write(f"Python files: {len(python_files)}\n")
    file.write(f"CSV files: {len(csv_files)}\n")
    file.write(f"Total file size: {total_size} bytes\n")

print("\nProject report created:", report.name)

print("\nExercise 09 completed!")