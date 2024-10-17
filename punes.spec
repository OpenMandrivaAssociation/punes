%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	Nintendo Entertaiment System (NES) emulator
Name:		punes
Version:	0.78
Release:	3
License:	Freeware
Group:		Emulators
Url:		https://nesdev.parodius.com/bbs/viewtopic.php?t=6928
# Downloaded from dropbox account, see URL
Source0:	%{name}.32bit.tar.gz
Source1:	%{name}.64bit.tar.gz
Source2:	%{name}.png
BuildRequires:	imagemagick

%description
Close-sourced Nintendo Entertaiment System (NES) emulator with GUI.

Among other features it has Dendy mode support.

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_iconsdir}/hicolor/*/apps/%{name}.png

#----------------------------------------------------------------------------

%prep
%setup -q -c -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
%ifarch x86_64
cp %{name}64 %{buildroot}%{_bindir}/%{name}
%else
cp %{name}32 %{buildroot}%{_bindir}/%{name}
%endif

# icons
for N in 16 32 64; do convert %{SOURCE2} -resize ${N}x${N} $N.png; done
install -D 16.png %{buildroot}%{_miconsdir}/%{name}.png
install -D 32.png %{buildroot}%{_liconsdir}/%{name}.png
install -D 64.png %{buildroot}%{_iconsdir}/hicolor/64x64/apps/%{name}.png
install -D %{SOURCE2} %{buildroot}%{_iconsdir}/hicolor/128x128/apps/%{name}.png

# menu-entry
mkdir -p  %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=puNES
GenericName=Nintendo Entertaiment System emulator
GenericName[ru]=Эмулятор Nintendo Entertaiment System
Comment=Nintendo Entertaiment System emulator
Comment[ru]=Эмулятор Nintendo Entertaiment System
Exec=punes
Icon=punes
Type=Application
Categories=Game;Emulator;
MimeType=application/x-nes;application/x-nes-rom;
EOF

