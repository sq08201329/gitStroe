cmd.exe /c "chcp 65001"
cmd.exe /c "C:\Windows\System32\schtasks.exe /query"
#cmd.exe /c "C:\Windows\System32\schtasks.exe /create /sc  [MINUTE|DAILY|WEEKLY|MONTHLY|ONCE|ONSTART|ONLOGON|ONIDLE] /mo [num]/tn 'taskname' /tr "cmd_name" /st 06:00:01 /ed 08:00:00"
#cmd.exe /c "C:\Windows\System32\schtasks.exe /run /tn "taskname""
#cmd.exe /c "C:\Windows\System32\schtasks.exe /end /tn "taskname""