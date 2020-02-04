#!/bin/bash
#This script will email us our user, IP, hostname, and today's date
emailaddress=fayazsn@mail.uc.edu
todaysdate=$( date +"%d-%m-%Y")
vbash=$BASH_VERSION
ipfinder=$(ip a | grep 'dynamic ens192' | awk '{print $2}')
content="Username is $USER, Server name is #$HOSTNAME with the ip of $ipfinder. Today is $todaysdate, using bash version $vbash."
echo $content
mail -s "IT3038C Linux IP" $emailaddress <<< $(echo -e $content)

~
~

