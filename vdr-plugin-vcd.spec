
%define plugin	vcd
%define name	vdr-plugin-%plugin
%define version	0.9
%define rel	1

Summary:	VDR plugin: VideoCD Player
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://vdr.heiligenmann.de/
Source:		http://vdr.heiligenmann.de/download/vdr-%plugin-%version.tgz
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.4.1-6
Requires:	vdr-abi = %vdr_abi
Requires(post):	vdr-common

%description
This plugin adds the functionality to replay VideoCDs (and Super VideoCDs)
from within VDR (by Klaus Schmidinger).

%prep
%setup -q -n %plugin-%version

%vdr_plugin_params_begin %plugin
# use DEV as the CD-ROM device
# default: /dev/cdrom
var=VCD_DEVICE
param=--vcd=VCD_DEVICE
%vdr_plugin_params_end

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%{_bindir}/gpasswd -a vdr cdrom >/dev/null
%{_bindir}/gpasswd -a vdr cdwriter >/dev/null
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README COPYING HISTORY


