%define _disable_ld_no_undefined 1

%define lib_major 1
%define lib_name %mklibname %{name} %{lib_major}
%define devel_name %mklibname %{name} -d

%define plugins_dir %{_libdir}/%{name}/plugins

Summary:	Wiimote Interface
Name:		cwiid
Version:	0.6.01
Release:	5
License:	GPL
Group:		System/Kernel and hardware
Url:		http://abstrakraft.org/cwiid/
Source0:	http://www.abstrakraft.org/%{name}-%{version}.tar.xz
Patch0:		cwiid-0.6.01-fix-linkage.patch
Patch1:		cwiid-0.6.00-fix-str-fmt.patch
Patch2:		0001-fix-issues-with-unitialized-memory-illegal-memory-ac.patch
Patch3:		0001-fix-minor-memleak.patch
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	pkgconfig(bluez)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(python2)
Requires:	python-%{name}

%description
CWiid is a Wiimote Interface.
The %{name} package contains the following parts:
1.%{name} library - abstracts the interface to the wiimote by hiding
  the details of the underlying Bluetooth connection
2.wmif - provides a simple text-based interface to the wiimote.
3.wmgui - provides a simple GTK gui to the wiimote.

%package -n	%{lib_name}
Summary:	Wiimote library
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
%patch2 -p1
%patch3 -p1
autoreconf

%build
%configure \
	 PYTHON=python2 \
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
%{py2_platsitedir}/%{name}.so
%{py2_platsitedir}/*.egg-info
