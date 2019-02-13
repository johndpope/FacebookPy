Write-Output "FacebookPy Windows Setup"
Write-Output =============================================================================================
Write-Output "Installing Selenium"
pip install selenium
python -m pip install pyvirtualdisplay
py get-pip.py
Write-Output " "
Write-Output "Installing GUI Tool"
$webclient = New-Object System.Net.WebClient
$webclient.DownloadFile("https://github.com/Nemixalone/GUI-tool-for-FacebookPy-script/releases/download/0.4/FacebookPy-GUI.exe","$pwd\FacebookPy-GUI.exe")
Move-Item "$pwd\FacebookPy-GUI.exe" "$pwd\..\FacebookPy-GUI.exe"
Write-Output " "
Set-Location ..\
Write-Output "Downloading Chrome Driver..."
$webclient = New-Object System.Net.WebClient
$webclient.DownloadFile("https://chromedriver.storage.googleapis.com/2.34/chromedriver_win32.zip","$pwd\chromedriver.zip")
Write-Output "Chrome Driver download completed."
Write-Output " "
Write-Output "Unzipping Chrome Driver..."
$shell = new-object -com shell.application
$zip = $shell.NameSpace("$pwd\chromedriver.zip")
foreach($item in $zip.items())
{
$shell.Namespace("$pwd\assets\").copyhere($item)
}
Move-Item "$pwd\assets\chromedriver.exe" "$pwd\assets\chromedriver"
Write-Output "Unzipping completed."
Write-Output " "
Write-Output "Removing unneeded files..."
Remove-Item chromedriver.zip
Write-Output "Removal completed."
Write-Output " "
python setup.py install
Write-Output "Setup is completed."
pause
