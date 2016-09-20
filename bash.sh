#C:\Windows\System32\schtasks.exe /create /sc minute /mo 1 /tn "sunqi" /tr D:\Python\me\gitStroe\bash.sh
#C:\Windows\System32\schtasks.exe  | findstr /i "sunqi"
dt=$(date "+%Y年%m月%d日")
echo $dt >> ~/Desktop/cmd.txt
