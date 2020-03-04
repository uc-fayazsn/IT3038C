import-module 'Carbon'

$OSType = Test-OSIs64Bit
Write-Host("Testing if your OS Type is 64-Bit, the result is: $OSType")


$InstallDiretory = Install-Directory -Path C:\IT3038C\CARBON
Write-Host("Creating your Directory for Carbon in the IT3038C drive." )

$TestFeature = Test-WindowsFeature -Name IIS-Server 

Write-Host("We have just tested the IIS-Server")

Write-Host("Congratulations, all three of the Carbon Functions worked :)")


