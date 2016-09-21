#C:\Windows\System32\schtasks.exe /create /sc minute /mo 1 /tn "sunqi" /tr D:\Python\me\gitStroe\bash.sh
#C:\Windows\System32\schtasks.exe  | findstr /i "sunqi"
#cmd.exe /c 'chcp 65001'
#cmd.exe /c "C:\Windows\System32\schtasks.exe /create /sc minute /mo 1 /tn "sunqi" /tr D:\Python\me\gitStroe\bash.sh"
dt=$(date "+%Y年%m月%d日")
echo $dt >> ~/Desktop/cmd.txt
