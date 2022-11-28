# Get the script directory
$ScriptPath = Split-Path -Parent $PSCommandPath
# Start the application
Start-Process -NoNewWindow -FilePath "$ScriptPath\python.exe" -ArgumentList "-m my_app1.app1"
