import os
import shutil
from datetime import datetime

source_dir = '.'  # Change to the directory you want to backup
files = os.listdir(source_dir)
print("Files to backup:", files)

backup_dir = 'backup'
if not os.path.exists(backup_dir):
    os.makedirs(backup_dir)

# Форматування назви файла
backup_name = os.path.join(backup_dir, datetime.now().strftime('Backup_Date_%d_Month_%m_Hour_%H_Minute_%M'))
shutil.make_archive(backup_name, 'zip', source_dir)

print(f"Backup created: {backup_name}.zip")