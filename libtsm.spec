#
# Conditional build:
%bcond_without	tests		# don't perform "make check"
#
Summary:	Terminal-emulator State Machine library
Summary(pl.UTF-8):	Biblioteka automatu emulatora terminala
Name:		libtsm
Version:	3
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://www.freedesktop.org/software/kmscon/releases/%{name}-%{version}.tar.xz
# Source0-md5:	c1b297a69d11a72f207ec35ae5ce7d69
# specified in libtsm.pc, but 404 for now
#URL:		http://dvdhrm.github.io/libtsm
# general ksmcon URL
URL:		https://github.com/dvdhrm/kmscon/wiki/KMSCON
BuildRequires:	check
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libxkbcommon-devel
BuildRequires:	xz
Conflicts:	kmscon-libs < 8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TSM is a state machine for DEC VT100-VT520 compatible terminal
emulators. It tries to support all common standards while keeping
compatibility to existing emulators like xterm, gnome-terminal,
konsole, ...

%description -l pl.UTF-8
TSM to automat emulatora terminala zgodnego z DEC VT100-VT520.
Próbuje obsłużyć wszystkie popularne standardy, zachowując
zgodność z istniejącymi emulatorami, takimi jak xterm, gnome-terminal,
konsole...

%package devel
Summary:	Header files for TSM library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki TSM
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Conflicts:	kmscon-devel < 8

%description devel
Header files for TSM library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki TSM.

%package static
Summary:	Static TSM library
Summary(pl.UTF-8):	Statyczna biblioteka TSM
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Conflicts:	kmscon-static < 8

%description static
Static TSM library.

%description static -l pl.UTF-8
Statyczna biblioteka TSM.

%prep
%setup -q

%build
%configure

%{__make}

%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libtsm.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING NEWS README
%attr(755,root,root) %{_libdir}/libtsm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtsm.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtsm.so
%{_includedir}/libtsm.h
%{_pkgconfigdir}/libtsm.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libtsm.a
