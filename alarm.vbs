Dim h,m,hn,hm,s,hr,min

hn=Hour(Time)
hm=Minute(Time)
s=Second(Time)

h=CStr(hn)
m=CStr(hm)

hr=12
min=13

alarm1="alarm 1"

Set speech=CreateObject("sapi.spvoice")
Set fi=CreateObject("WScript.Shell")

If hn=hr And hm=min And s=1 Then
  speech.Speak alarm1
Else
  fi.Run "alarm.vbs"
End If