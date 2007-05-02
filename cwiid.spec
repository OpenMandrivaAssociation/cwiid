%define name cwiid
%define version 0.5.03
%define release %mkrel 1
%define lib_major 0
%define lib_name %mklibname wiimote %{lib_major}
%define plugins_dir %{_libdir}/%{name}/plugins

Summary: CWiid Wiimote Interface
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.abstrakraft.org/%{name}-%{version}.tar.bz2
License: GPL
Group: System/Kernel and hardware
Url: http://www.wiili.org/index.php/CWiid
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: bison bluez-devel flex gtk+2-devel

%description
CWiid is a Wiimote Interface.
The cwwid package contains the following parts:
1.wiimote library - abstracts the interface to the wiimote by hiding
  the details of the underlying Bluetooth connection
2.wmif - provides a simple text-based interface to the wiimote.
3.wmgui - provides a simple GTK gui to the wiimote.

%package -n	%{lib_name}
Summary:	A Wiimote library
Group:		System/Libraries

%description -n	%{lib_name}
This package contains the library needed to run programs dynamically
linked with the Wiimote library.

%package -n	%{lib_name}-devel
Summary:	Development headers and libraries for programs using the Wiimote
Group:		Development/C
Requires:	%{lib_name} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{lib_name}-devel
This package contains the header files and libraries needed for
developing programs using the Wiimote library.

%prep
%setup -q

%build
%configure2_5x --disable-ldconfig --docdir=%{_docdir}/%{name}-%{version}
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%docdir %{_docdir}/%{name}-%{version}
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/wminput
%config(noreplace) %{_sysconfdir}/%{name}/wminput/*
%{_bindir}/lswm
%{_bindir}/wmgui
%{_bindir}/wminput
%{_mandir}/man1/*.1*

%files -n %{lib_name}
%{_libdir}/libwiimote.so.*
%{plugins_dir}/*.so

%files -n %{lib_name}-devel
%{_includedir}/wiimote.h
%{_libdir}/libwiimote.a
%{_libdir}/libwiimote.so
