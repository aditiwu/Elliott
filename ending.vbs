Set objShell = CreateObject("Shell.Application")
set wshshell = wscript.CreateObject("wscript.shell")
WScript.Sleep 15000
WshShell.SendKeys "%{TAB}"
objShell.WindowSwitcher
WScript.Sleep 1000
WshShell.SendKeys "{TAB}{TAB}{TAB}"
WScript.Sleep 1000
WshShell.SendKeys "{RIGHT}"
WScript.Sleep 1000
WshShell.SendKeys "{ENTER}"
WScript.Sleep 1000