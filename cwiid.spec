%define _disable_ld_no_undefined 1

%define name cwiid
%define oname CWiid
%define version 0.6.01
%define pre 0
%define rel 1
%if %pre
%define release %mkrel 0.%{pre}.%{rel}
%define distname %{name}-%{version}_%{pre}
%else
%define release %mkrel %{rel}
%define distname %{name}-%{version}
%endif
%define lib_major 1
%define lib_name %mklibname %{name} %{lib_major}
%define devel_name %mklibname %{name} -d
%define plugins_dir %{_libdir}/%{name}/plugins

Summary:	%{oname} Wiimote Interface
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://www.abstrakraft.org/%{distname}.tar.xz
Patch0:		cwiid-0.6.00-bluetooth_api_fix.diff
Patch1:		cwiid-0.6.00-fix-str-fmt.patch
Patch2:		cwiid-0.6.00-fix-linkage.patch
License:	GPL
Group:		System/Kernel and hardware
Url:		http://abstrakraft.org/cwiid/
BuildRequires:	bison bluez-devel flex gtk+2-devel python-devel
Requires:	python-%{name}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
%{oname} is a Wiimote Interface.
The %{name} package contains the following parts:
1.%{name} library - abstracts the interface to the wiimote by hiding
  the details of the underlying Bluetooth connection
2.wmif - provides a simple text-based interface to the wiimote.
3.wmgui - provides a simple GTK gui to the wiimote.

%package -n	%{lib_name}
Summary:	%{oname} Wiimote library
Group:		System/Libraries
Conflicts:	%mklibname wiimote 0
Obsoletes:	%mklibname wiimote 1

%description -n	%{lib_name}
This package contains the library needed to run programs dynamically
linked with the %{oname} Wiimote library.

%package -n	%{devel_name}
Summary:	Development headers and libraries for %{oname}
Group:		Development/C
Requires:	%{lib_name} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname wiimote 1 -d

%description -n	%{devel_name}
This package contains the header files and libraries needed for
developing programs using the %{oname} Wiimote library.

%package -n	python-%{name}
Summary: 	Python bindings for the %{name} Wiimote library
Group:		System/Libraries

%description -n	python-%{name}
This package contains Python bindings for the %{oname} Wiimote
library.

%prep
%setup -q -n %{distname}
# %patch0 -p0
%patch1 -p0
# %patch2 -p0

%build
autoreconf
%configure2_5x \
    --disable-ldconfig \
    --docdir=%{_docdir}/%{name}

%make WARNFLAGS="%{optflags} -Wall"

%install
rm -rf %{buildroot}

%makeinstall_std

%if %mdkversion < 200900
%post -n %{lib_name} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{lib_name} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%docdir %{_docdir}/%{name}
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/wminput
%config(noreplace) %{_sysconfdir}/%{name}/wminput/*
%{_bindir}/lswm
%{_bindir}/wmgui
%{_bindir}/wminput
%{_mandir}/man1/*.1*
%{_libdir}/pkgconfig/cwiid.pc

%files -n %{lib_name}
%{_libdir}/lib%{name}.so.%{lib_major}*
%{plugins_dir}/*.so

%files -n %{devel_name}
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.a
%{_libdir}/lib%{name}.so

%files -n python-%{name}
%{py_platsitedir}/%{name}.so
%{py_platsitedir}/*.egg-info
