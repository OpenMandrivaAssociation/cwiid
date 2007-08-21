%define name cwiid
%define version 0.6.00
%define pre rc3
%define rel 1
%if %pre
%define release %mkrel 0.%{pre}.%{rel}
%define distname %{name}-%{version}_%{pre}
%else
%define release %mkrel %{rel}
%define distname %{name}-%{version}
%endif
%define lib_major 0
%define lib_name %mklibname wiimote %{lib_major}
%define plugins_dir %{_libdir}/%{name}/plugins

Summary: CWiid Wiimote Interface
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.abstrakraft.org/%{distname}.tar.bz2
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
%setup -q -n %{distname}

%build
%configure2_5x --disable-ldconfig --docdir=%{_docdir}/%{name}
%make

%install
rm -rf %{buildroot}
%makeinstall_std

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

%files -n %{lib_name}
%{_libdir}/lib%{name}.so.*
%{plugins_dir}/*.so

%files -n %{lib_name}-devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.a
%{_libdir}/lib%{name}.so
