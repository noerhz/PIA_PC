Write-Host "Obteniendo el DNS del cache (comando: 'Get-DnsClientCache')..."
$dns1 = Get-DnsClientCache

Write-Host "Obteniendo el DNS del cache (comando: 'ipconfig /displaydns')..."
$dns2 = ipconfig /displaydns

Write-Host "Creando primer archivo txt..."
"COMMAND: Get-DnsClientCche `r`n -------------------------------------------------------------------------------------- `r`n", $dns1 | Out-File -FilePath "DNS1.txt"

Write-Host "Creando segundo archivo txt..."
"COMMAND: ifconfig /displaydns `r`n -------------------------------------------------------------------------------------- `r`n", $dns2 | Out-File -FilePath "DNS2.txt" 