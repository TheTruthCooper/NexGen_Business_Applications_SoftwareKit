#!/bin/bash

# Set the size threshold in bytes (e.g., 100MB = 100 * 1024 * 1024 bytes)
SIZE_THRESHOLD=$((100 * 1024 * 1024))

# Find all files larger than the threshold
LARGE_FILES=$(find . -type f -size +${SIZE_THRESHOLD}c -print)

# Check if each large file is tracked by Git LFS
for FILE in $LARGE_FILES; do
  if git lfs track | grep -q "$FILE"; then
    echo "File $FILE is already tracked by Git LFS."
  else
    echo "File $FILE is larger than $((SIZE_THRESHOLD / 1024 / 1024))MB and not tracked by Git LFS."
    git lfs track "$FILE"
    echo "Tracked $FILE with Git LFS."
  fi
done
# Display the current tracking status
git lfs ls-filest