%define _disable_ld_no_undefined 1

%define lib_major 1
%define lib_name %mklibname %{name} %{lib_major}
%define devel_name %mklibname %{name} -d

%define plugins_dir %{_libdir}/%{name}/plugins

Summary:	CWiid Wiimote Interface
Name:		cwiid
Version:	0.6.01
Release:	3
License:	GPL
Group:		System/Kernel and hardware
Url:		http://abstrakraft.org/cwiid/
Source0:	http://www.abstrakraft.org/%{name}-%{version}.tar.xz
Patch0:		cwiid-0.6.01-fix-linkage.patch
Patch1:		cwiid-0.6.00-fix-str-fmt.patch
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	pkgconfig(bluez)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	python-devel
Requires:	python-%{name}

%description
CWiid is a Wiimote Interface.
The %{name} package contains the following parts:
1.%{name} library - abstracts the interface to the wiimote by hiding
  the details of the underlying Bluetooth connection
2.wmif - provides a simple text-based interface to the wiimote.
3.wmgui - provides a simple GTK gui to the wiimote.

%package -n	%{lib_name}
Summary:	CWiid Wiimote library
Group:		System/Libraries

%description -n	%{lib_name}
This package contains the library needed to run programs dynamically
linked with the CWiid Wiimote library.

%package -n	%{devel_name}
Summary:	Development headers and libraries for CWiid
Group:		Development/C
Requires:	%{lib_name} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devel_name}
This package contains the header files and libraries needed for
developing programs using the CWiid Wiimote library.

%package -n	python-%{name}
Summary: 	Python bindings for the %{name} Wiimote library
Group:		System/Libraries

%description -n	python-%{name}
This package contains Python bindings for the %{name} Wiimote
library.

%prep
%setup -q
%patch0 -p1
%patch1 -p0

%build
autoreconf
%configure2_5x \
    --disable-ldconfig \
    --docdir=%{_docdir}/%{name}

%make WARNFLAGS="%{optflags} -Wall"

%install
%makeinstall_std

%files
%doc README
%docdir %{_docdir}/%{name}
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/wminput
%config(noreplace) %{_sysconfdir}/%{name}/wminput/*
%{_bindir}/lswm
%{_bindir}/wmgui
%{_bindir}/wminput
%{_mandir}/man1/*.1*

%files -n %{lib_name}
%{_libdir}/lib%{name}.so.%{lib_major}*
%{plugins_dir}/*.so

%files -n %{devel_name}
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.a
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/cwiid.pc

%files -n python-%{name}
%{py_platsitedir}/%{name}.so
%{py_platsitedir}/*.egg-info


%changelog
* Sat Jul 02 2011 Jani Välimaa <wally@mandriva.org> 0.6.01-2mdv2011.0
+ Revision: 688569
- move pkgconfig file to -devel subpackage
- remove changelog from .spec (it's generated from svn logs)

* Mon Jun 27 2011 Zombie Ryushu <ryushu@mandriva.org> 0.6.01-1
+ Revision: 687404
- Upgrade to latest SVN which is much better than stable

* Sat May 14 2011 Funda Wang <fwang@mandriva.org> 0.6.00-7
+ Revision: 674508
- use upstream tarball
- fix python module linkage

* Mon Nov 01 2010 Jani Välimaa <wally@mandriva.org> 0.6.00-6mdv2011.0
+ Revision: 591708
- rebuild for python 2.7

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 0.6.00-5mdv2010.0
+ Revision: 437206
- rebuild

* Sat Jan 10 2009 Funda Wang <fwang@mandriva.org> 0.6.00-4mdv2009.1
+ Revision: 328003
- fix linkage & str fmt

* Tue Nov 18 2008 Oden Eriksson <oeriksson@mandriva.com> 0.6.00-3mdv2009.1
+ Revision: 304234
- fix build
- use _disable_ld_as_needed and _disable_ld_no_undefined due to
  fugly autofoo
- fix build cflags

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.6.00-2mdv2008.1
+ Revision: 136524
- run ldconfig on post

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Aug 27 2007 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.6.00-1mdv2008.0
+ Revision: 71794
- new release: 0.6.00 final
- since tarball already being recompressed, use lzma for most optimal

* Wed Aug 22 2007 Olivier Blin <oblin@mandriva.com> 0.6.00-0.rc3.3mdv2008.0
+ Revision: 69107
- use new devel library policy
- use cwiid instead of wiimote in library package name
- wminput require python module (#32747)

* Wed Aug 22 2007 Olivier Blin <oblin@mandriva.com> 0.6.00-0.rc3.2mdv2008.0
+ Revision: 68788
- conflict with old wiimote library package

* Tue Aug 21 2007 Olivier Blin <oblin@mandriva.com> 0.6.00-0.rc3.1mdv2008.0
+ Revision: 68226
- update URL
- adapt summary and descriptions to new library name
- add python sub-package
- ensure major is correct in file list
- major is now 1
- library is now named cwiid
- new docdir policy
- 0.6.00_rc3

* Wed May 02 2007 Olivier Blin <oblin@mandriva.com> 0.5.03-1mdv2008.0
+ Revision: 20505
- 0.5.03
- add lswm
- add man pages
- do not package wmdemo
- remove packaging hacks now that upstream has DESTDIR support

* Fri Apr 20 2007 Olivier Blin <oblin@mandriva.com> 0.5.02-1mdv2008.0
+ Revision: 15603
- buildrequire bison
- buildrequire flex
- 0.5.02


* Sat Jan 27 2007 Olivier Blin <oblin@mandriva.com> 0.4.01-1mdv2007.0
+ Revision: 114311
- 0.4.01

* Thu Jan 18 2007 Olivier Blin <oblin@mandriva.com> 0.3.51-1mdv2007.1
+ Revision: 110452
- 0.3.51

* Wed Jan 10 2007 Olivier Blin <oblin@mandriva.com> 0.3.01-1mdv2007.1
+ Revision: 107202
- 0.3.01

* Fri Jan 05 2007 Olivier Blin <oblin@mandriva.com> 0.3.00-2mdv2007.1
+ Revision: 104344
- package wminput

* Fri Jan 05 2007 Olivier Blin <oblin@mandriva.com> 0.3.00-1mdv2007.1
+ Revision: 104334
- 0.3.00 (IR support)

* Tue Jan 02 2007 Olivier Blin <oblin@mandriva.com> 0.2.00-1mdv2007.1
+ Revision: 103087
- 0.2.00

* Fri Dec 29 2006 Olivier Blin <oblin@mandriva.com> 0.1.00-1mdv2007.1
+ Revision: 102632
- buildrequires gtk+2-devel
- fix library symlinks so that wmgui is linked with libwiimote
- initial cwiid Wiimote interface package
- Create cwiid

