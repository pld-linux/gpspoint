Summary:	Software to interact with a garmin GPS device
Summary(pl):	Biblioteka do komunikacji z odbiornikami GPS garmina
Name:		gpspoint
Version:	2.030521
Release:	0.5
License:	GPL
Group:		Libraries
Source0:	http://gpspoint.dnsalias.net/gpspoint2/download/%{name}-%{version}.tar.gz
# Source0-md5:	90e263d5297608d695743a9b0122f930
Patch0:		%{name}-feedback.patch
Patch1:		%{name}-precision.patch
URL:		http://gpspoint.dnsalias.net/gpspoint2/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
With gpspoint you can interact with a garmin GPS device. Most
importantly you can down- and upload waypoints, routes and tracks.

%description -l pl
Biblioteka gpspoint s³u¿y do komunikacji z odbiornikami GPS garmina.
Pozwala miêdzy innymi na ¶ci±ganie i ³adowanie waypointów, tras 
i ¶ladów.

%package devel
Summary:	Header files for gpspoint library
Summary(pl):	Pliki nag³ówkowe biblioteki gpspoint
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for gpspoint library.

%description devel -l pl
Pliki nag³ówkowe biblioteki gpspoint.

%package static
Summary:	Static version of gpspoint library
Summary(pl):	Statyczna wersja biblioteki gpspoint
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version gpspoint.

%description static -l pl
Statyczna wersja gpspoint.

%package progs
Summary:	Gpspoint utility programs
Summary(pl):	Programy narzêdziowe gpspoint
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description progs
Gpspoint utility programs.

%description progs -l pl
Programy narzêdziowe gpspoint.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?debug:CPPFLAGS=-DDEBUG}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/gpspoint2

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
