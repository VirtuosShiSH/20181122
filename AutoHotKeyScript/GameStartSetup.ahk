#SingleInstance, Force
#KeyHistory, 0
SetBatchLines, -1
ListLines, Off
SendMode Input ; Forces Send and SendRaw to use SendInput buffering for speed.
SetTitleMatchMode, 3 ; A window's title must exactly match WinTitle to be a match.
SetWorkingDir, %A_ScriptDir%
SplitPath, A_ScriptName, , , , thisscriptname
#MaxThreadsPerHotkey, 1 ; no re-entrant hotkey handling
; DetectHiddenWindows, On
; SetWinDelay, -1 ; Remove short delay done automatically after every windowing command except IfWinActive and IfWinExist
; SetKeyDelay, -1, -1 ; Remove short delay done automatically after every keystroke sent by Send or ControlSend
; SetMouseDelay, -1 ; Remove short delay done automatically after Click and MouseMove/Click/Drag
#IfWinActive ahk_class UnrealWindow
^A::
Send ``
Sleep, 500
Send HideTslDebugInfomation
Sleep 50
Send {Enter}
Send ``
Sleep, 500
Send b.TeleportMode 1
Sleep 50
Send {Enter}
Sleep, 500
Send {CtrlDown}R
Sleep 50
Send ``
Sleep, 500
Send Admin VisibleInvulnerablilityEffect 0
Sleep 50
Send {Enter}
Send {CtrlDown}E
Sleep 500
Send 1
Sleep 1000
Send b
Sleep 1500
Send {CtrlDown}E
Sleep 500
Send {CtrlDown}E
Sleep 500
Send ``
Sleep, 500
Send Stat FPS
Sleep 50
Send {Enter}
Sleep 250
Send ``
Sleep, 500
Send Admin PauseBlueZone 1
Sleep 50
Send {Enter}
Sleep 100
Send n
return