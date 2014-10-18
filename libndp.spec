# based on PLD Linux spec git://git.pld-linux.org/packages/libndp.git
Summary:	Library for Neighbor Discovery Protocol
Name:		libndp
Version:	1.3
Release:	1
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: http://libndp.org/
Source0:	http://libndp.org/files/%{name}-%{version}.tar.gz
# Source0-md5:	e4ac1fce2faa664ba8b20df581bf30ea
URL:		http://libndp.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a library which provides a wrapper for IPv6
Neighbor Discovery Protocol. It also provides a tool named ndptool for
sending and receiving NDP messages.

%package devel
Summary:	Header files for libndp library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libndp library.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/ndptool
%attr(755,root,root) %ghost %{_libdir}/libndp.so.0
%attr(755,root,root) %{_libdir}/libndp.so.*.*.*
%{_mandir}/man8/ndptool.8*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libndp.so
%{_includedir}/ndp.h
%{_pkgconfigdir}/libndp.pc

