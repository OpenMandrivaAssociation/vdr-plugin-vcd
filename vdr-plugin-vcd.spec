%define plugin	vcd

Summary:	VDR plugin: VideoCD Player
Name:		vdr-plugin-%plugin
Version:	0.9
Release:	7
Group:		Video
License:	GPL
URL:		http://www.heiligenmann.de/vdr/vdr/plugins/vcd.html
Source:		http://www.heiligenmann.de/vdr/download/vdr-%plugin-%version.tgz
Patch0:		vcd-0.9-i18n-1.6.patch
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
%vdr_plugin_install

%post
%{_bindir}/gpasswd -a vdr cdrom >/dev/null
%{_bindir}/gpasswd -a vdr cdwriter >/dev/null

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README COPYING HISTORY




%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.9-5mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.9-4mdv2009.1
+ Revision: 359380
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.9-3mdv2009.0
+ Revision: 197994
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.9-2mdv2009.0
+ Revision: 197738
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt to gettext i18n of VDR 1.6 (semi-automatic patch)
- update URL

* Fri Feb 29 2008 Anssi Hannula <anssi@mandriva.org> 0.9-1mdv2008.1
+ Revision: 176880
- new version
- drop patches, fixed upstream

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.7-15mdv2008.1
+ Revision: 145241
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.7-14mdv2008.1
+ Revision: 103230
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.7-13mdv2008.0
+ Revision: 50061
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.7-12mdv2008.0
+ Revision: 42144
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.7-11mdv2008.0
+ Revision: 22720
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.7-10mdv2007.0
+ Revision: 90982
- rebuild for new vdr
- add vdr user to cdwriter group

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.7-9mdv2007.1
+ Revision: 74096
- rebuild for new vdr
- Import vdr-plugin-vcd

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.7-8mdv2007.0
- rebuild for new vdr

* Fri Sep 01 2006 Anssi Hannula <anssi@mandriva.org> 0.7-7mdv2007.0
- add vdr to cdrom group

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.7-6mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.7-5mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.7-4mdv2007.0
- rebuild for new vdr

* Tue Jun 20 2006 Anssi Hannula <anssi@mandriva.org> 0.7-3mdv2007.0
- rebuild for new vdr

* Mon Jun 05 2006 Anssi Hannula <anssi@mandriva.org> 0.7-2mdv2007.0
- rebuild for new vdr

* Fri Jun 02 2006 Anssi Hannula <anssi@mandriva.org> 0.7-1mdv2007.0
- initial Mandriva release

