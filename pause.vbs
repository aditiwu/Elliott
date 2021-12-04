Set objShell = CreateObject("Shell.Application")
Set wshShell =wscript.CreateObject("WScript.Shell")
WScript.Sleep 1000
objShell.WindowSwitcher
WScript.Sleep 1000
WshShell.SendKeys "{TAB}{TAB}{TAB}"
WScript.Sleep 1000
WshShell.SendKeys "{ENTER}"
WScript.Sleep 1000
wshshell.SendKeys " "
WScript.Sleep 1000
WshShell.SendKeys "%{TAB}"
WScript.Sleep 1000
objShell.WindowSwitcher
WScript.Sleep 1000
WshShell.SendKeys "{TAB}{TAB}{TAB}"
WScript.Sleep 1000
WshShell.SendKeys "{RIGHT}"
WScript.Sleep 1000
WshShell.SendKeys "{ENTER}"
WScript.Sleep 1000
