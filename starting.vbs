Set objShell = CreateObject("Shell.Application")
Set wshShell =wscript.CreateObject("WScript.Shell")
objShell.WindowSwitcher
WScript.Sleep 1000
WshShell.SendKeys "{TAB}{TAB}{TAB}"
WScript.Sleep 1000
WshShell.SendKeys "{ENTER}"
WScript.Sleep 1000
WshShell.SendKeys "%{F4}"
WScript.Sleep 1000