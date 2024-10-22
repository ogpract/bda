## HDFS Commands

### 1. Help Command
- **Command:** `hdfs dfs -help`
- **Description:** Displays a list of available HDFS commands and their usage.

### 2. List Files and Directories
- **Command:** `hdfs dfs -ls <path>`
- **Description:** Lists files and directories in the specified path.

### 3. Create Directory
- **Command:** `hdfs dfs -mkdir <path>`
- **Description:** Creates a new directory at the specified path.

### 4. Recursive Listing
- **Command:** `hdfs dfs -ls -r <path>`
- **Description:** Recursively lists files and directories under the specified path.

### 5. Copy from HDFS to Local
- **Command:** `hdfs dfs -get <src> <dest>`
- **Description:** Copies files or directories from HDFS to the local filesystem.

### 6. Upload from Local to HDFS
- **Command:** `hdfs dfs -put <src> <dest>`
- **Description:** Uploads files or directories from the local filesystem to HDFS.

### 7. Display File Contents
- **Command:** `hdfs dfs -cat <path>`
- **Description:** Displays the contents of a file at the specified path.

### 8. Display Last Few Bytes
- **Command:** `hdfs dfs -tail <path>`
- **Description:** Displays the last few bytes of a file at the specified path.

### 9. Remove Files or Directories
- **Command:** `hdfs dfs -rm <path>`
- **Description:** Removes (deletes) files or directories at the specified path.

## Example Usage

The following example demonstrates how to use the `-put` and `-get` commands to move a file between the local system and HDFS, and how to delete a file from HDFS:

```bash
# Upload a file from local to HDFS
hdfs dfs -put D:\a.txt /mydir

# List the contents of the directory in HDFS
hdfs dfs -ls /mydir

# Display the contents of the uploaded file
hdfs dfs -cat /mydir/a.txt

# Copy the file back from HDFS to the local filesystem
hdfs dfs -get /mydir/a.txt D:\temp\

# Check the contents of the local directory
dir D:\temp\

# Output:
# Volume in drive D is Data
# Volume Serial Number is 40A8-1731
#
# Directory of D:\temp
#

# Remove the file from HDFS
hdfs dfs -rm /mydir/a.txt
# Output: Deleted /mydir/a.txt

# List the contents of the directory again to confirm deletion
hdfs dfs -ls /mydir
