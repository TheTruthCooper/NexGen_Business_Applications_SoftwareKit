# Define size threshold
$SIZE_THRESHOLD = 100 * 1024 * 1024

# Find large files
$LARGE_FILES = Get-ChildItem -File -Recurse | Where-Object { $_.Length -gt $SIZE_THRESHOLD }

foreach ($FILE in $LARGE_FILES) {
    if (git lfs track | Select-String -Quiet "$($FILE.FullName)") {
        Write-Host "File $($FILE.FullName) is already being tracked by git lfs"
    } else {
        Write-Host "Adding $($FILE.FullName) to git lfs tracking"
        git lfs track "$($FILE.FullName)"
    }
}
