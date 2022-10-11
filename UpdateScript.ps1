Add-Type -AssemblyName PresentationFramework;
$launcherPath = "$([System.Environment]::GetFolderPath([System.Environment+SpecialFolder]::Desktop))\Sussy Launcher.exe";
cmd.exe /c del /Q $launcherPath > $emptyvoid1 2> $emptyvoid2 3> $emptyvoid3
Invoke-RestMethod -Uri "https://raw.githubusercontent.com/Omena0/MSG-APP-V3/main/dist/client.exe" -OutFile $launcherPath; 
if (Test-Path -Path $launcherPath) {
    [System.Windows.MessageBox]::Show('The launcher is now on your desktop!');
} else {
    [System.Windows.MessageBox]::Show('could not download the launcher');
}
Exit