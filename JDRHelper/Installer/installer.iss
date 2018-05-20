; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{094FA27F-BDE2-4FCD-8EE0-1DC98D542882}
AppName=JDRHelper
AppVersion=1.0
;AppVerName=JDRHelper 1.0
AppPublisher=Antoine Joly
DefaultDirName={pf}\JDRHelper
DisableProgramGroupPage=yes
OutputBaseFilename=setup
Compression=lzma
SolidCompression=yes

[Languages]
Name: "french"; MessagesFile: "compiler:Languages\French.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
Name: "quicklaunchicon"; Description: "{cm:CreateQuickLaunchIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked; OnlyBelowVersion: 0,6.1

[Files]
Source: "C:\Users\Antoine Joly\Documents\GitHub\JDRHelper\Installer\JDRHelper.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Antoine Joly\Documents\GitHub\JDRHelper\Installer\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{commonprograms}\JDRHelper"; Filename: "{app}\JDRHelper.exe"
Name: "{commondesktop}\JDRHelper"; Filename: "{app}\JDRHelper.exe"; Tasks: desktopicon
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\JDRHelper"; Filename: "{app}\JDRHelper.exe"; Tasks: quicklaunchicon

[Run]
Filename: "{app}\JDRHelper.exe"; Description: "{cm:LaunchProgram,JDRHelper}"; Flags: nowait postinstall skipifsilent

