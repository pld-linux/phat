Summary:	PHAT Audio Toolkit
Summary(pl):	PHAT Audio Toolkit - zestaw kontrolek dla aplikacji d¼wiêkowych
Name:		phat
Version:	0.2.3
Release:	1
License:	GPL v.2
Group:		X11/Libraries
Source0:	http://www.gazuga.net/phatfiles/%{name}-%{version}.tar.gz
# Source0-md5:	e06f136041c257c86a144345c10dd8fd
# Source0-size:	353417
URL:		http://www.gazuga.net/phat.php
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Collection of GTK+ widgets useful for audio applications.

%description -l pl
Kolekcja kontrolek GTK+ u¿ytecznych dla aplikacji d¼wiêkowych.

%package devel
Summary:	Header files for PHAT
Summary(pl):	Pliki nag³ówkowe dla PHAT
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and development documentation for the PHAT Audio Toolkit.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja dla PHAT Audio Toolkit.

%package static
Summary:	PHAT static library
Summary(pl):	Biblioteka statyczna PHAT
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description static
PHAT static library.

%description static -l pl
Biblioteka statyczna PHAT.

%prep
%setup -q

%{__perl} -pi -e 's/CFLAGS="-O3"/:/' configure.ac

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/phat*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/phat
%{_pkgconfigdir}/*.pc
%{_gtkdocdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
