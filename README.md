# CreateBackup

This project creates a backup of files in the specified directory and saves it in ZIP format with a well-formatted name.

<img width="362" alt="image" src="https://github.com/user-attachments/assets/15563c78-e400-4e60-b37f-51ebdd8b0f61" />


## Usage

1. Clone the repository or download the project files.
2. Open a terminal and navigate to the project directory.
3. Run the `CreateBackup.py` script:

    ```sh
    python CreateBackup.py
    ```

4. The script will create a backup of the files in the current directory and save it in the `backup` subdirectory with a name formatted as `Backup_Date_DD_Month_MM_Hour_HH_Minute_MM.zip`.

## Configuration

- You can change the directory to be backed up by modifying the `source_dir` variable.
- You can change the directory where backups are saved by modifying the `backup_dir` variable.
