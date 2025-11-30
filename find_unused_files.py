import os
import time

folder_to_scan = r"C:"
days_unused = 180

current_time = time.time()
print(current_time)

cuttoff_time = current_time - (days_unused * 24 * 60 * 60)

unused_files = []
total_size = 0

for root, dirs, files in os.walk(folder_to_scan):
    for file in files:
        file_path = os.path.join(root, file)
        
        try:
            total_size += os.path.getsize(file_path)
            last_access_time = os.path.getatime(file_path)
            # print(last_access_time)
            if last_access_time < cuttoff_time:
                unused_files.append(file_path)
                # os.remove(file_path)
        except Exception as e:
            print(f"Error accessing {file_path}: {e}")

if unused_files:
    print(f"Files not access n the last {days_unused} days:")
    for f in unused_files:
        print(os.path.getsize(f))
        if os.path.getsize(f) == (30*1024*1024):
            os.remove(f)
        # print(f"{f}: {(os.path.getsize(f) / (1024*1024)):.2f} mb")
else:
    print(f"No unused files found in {folder_to_scan}")
            
# print(f"Length: {len(}")
print(f"Total Size: {(total_size / (1024*1024)):.2f} mb")
        
            
        