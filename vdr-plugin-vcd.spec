
%define plugin	vcd
%define name	vdr-plugin-%plugin
%define version	0.9
%define rel	2

Summary:	VDR plugin: VideoCD Player
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.heiligenmann.de/vdr/vdr/plugins/vcd.html
Source:		http://www.heiligenmann.de/vdr/download/vdr-%plugin-%version.tgz
Patch0:		vcd-0.9-i18n-1.6.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi
Requires(post):	vdr-common

%description
This plugin adds the functionality to replay VideoCDs (and Super VideoCDs)
from within VDR (by Klaus Schmidinger).

%prep
%setup -q -n %plugin-%version
%patch0 -p1
%vdr_plugin_prep

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


