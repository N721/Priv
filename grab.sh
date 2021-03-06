#!/bin/bash
blue='\e[0;34'
cyan='\e[0;36m'
green='\e[0;34m'
okegreen='\033[92m'
lightgreen='\e[1;32m'
white='\e[1;37m'
red='\e[1;31m'
yellow='\e[1;33m'

checksite(){
COUNTER=$((COUNTER+1))
for tanggall in `seq $tanggal $tanggalnya`;
do
curlvar=$(curl -s "https://www.cubdomain.com/domains-registered-by-date/$tahun-$bulan-$tanggall/$page"| grep -Po '<a href="https://www.cubdomain.com/site/(.*?)">(.*?)</a>' | cut -d '<' -f2 | cut -d '>' -f2)
if [[ $curlvar =~ 'com' ||  $curlvar =~ 'net' ||  $curlvar =~ 'au' ||  $curlvar =~ 'org' || $curlvar =~ 'gov' ||  $curlvar =~ 'goid' ||  $curlvar =~ 'tech' ||  $curlvar =~ 'info' ||  $curlvar =~ 'uk' ||  $curlvar =~ 'ca' ||  $curlvar =~ 'co' ||  $curlvar =~ 'biz' ||  $curlvar =~ 'co' ||  $curlvar =~ 'online' ||  $curlvar =~ 'us' ||  $curlvar =~ 'xyz' ||  $curlvar =~ 'br' ||  $curlvar =~ 'nz' ||  $curlvar =~ 'gr' ||  $curlvar =~ 'fr' ||  $curlvar =~ 'sa' ||  $curlvar =~ 'sg' ||  $curlvar =~ 'my' ]];
then
dapetnya=$(echo "$curlvar" | wc -l)
resultnya=$(cat resultgrab1.txt | wc -l)
printf "${okegreen}[${COUNTER}] => [$tahun-$bulan-$tanggall] | [Page][$page] =>  [$dapetnya|$resultnya]\n";
echo "$curlvar" >> resultgrab1.txt
else
printf "${red}[${COUNTER}] => $red$domain => Limit Page Boss!\n";
result=$(cat resultgrab1.txt | wc -l)
printf "${okegreen}Total : $result\n";
fi
done
}

banner(){
echo -e $yellow"====================================="
echo -e $yellow"         Mass Grabbing Site          "
echo -e $yellow"       Copyright Mrcakil@2020        "
echo -e $yellow"====================================="
read -p "Tahun => " tahun;
read -p "Bulan => " bulan;
read -p "Tanggal => " tanggal;
read -p "Sampai Tanggal => " tanggalnya;
#read -p "Domain => " domain;
read -p "page => " pagenya;
}
banner

for page in `seq 1 $pagenya`;
do
checksite $page
done

result=$(cat resultgrab1.txt | wc -l)
printf "${okegreen}Total : $result\n";
