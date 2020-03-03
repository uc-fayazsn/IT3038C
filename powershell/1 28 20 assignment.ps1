function getIP {
(get-netipaddress).IPAddress | Select-String "192*"
}

function getWhoIsLoggedIn {
$env:USERNAME
}

function getHostsName {
$env:COMPUTERNAME
}

function getPowerShellVersion {
$HOST.Version
}



function getDate {
Get-Date
}


$IP = getIP
$whoIsLoggedIn = getWhoIsLoggedIn
$hostsName = getHostsName
$powerShellVersion = getPowershellVersion
$getDate = getDate
$getBody = "This machines IP is $IP, this user logged in is $whoIsLoggedIn, the Hostname is $hostsName. Currently using Powershell Version $powerShellVersion. Today's Date is $getDate"


Send-MailMessage -To "fayazsn@mail.uc.edu" -From "sfaya004@gmail.com" -Subject "IT3038C Windows SysInfo" -Body $getBody -SmtpServer smtp.gmail.com -port 587 -UseSSL -Credential (Get-Credential)

Write-host("Email Sent")