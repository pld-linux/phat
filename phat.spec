Summary:	PHAT Audio Toolkit
Summary(pl.UTF-8):   PHAT Audio Toolkit - zestaw kontrolek dla aplikacji dźwiękowych
Name:		phat
Version:	0.3.1
Release:	1
License:	GPL v.2
Group:		X11/Libraries
Source0:	http://www.gazuga.net/phatfiles/%{name}-%{version}.tar.gz
# Source0-md5:	f0b1ff27207a37690468ec1175d267cb
URL:		http://www.gazuga.net/phat.php
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	libgnomecanvas-devel
BuildRequires:	libtool
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Collection of GTK+ widgets useful for audio applications.

%description -l pl.UTF-8
Kolekcja kontrolek GTK+ użytecznych dla aplikacji dźwiękowych.

%package devel
Summary:	Header files for PHAT
Summary(pl.UTF-8):   Pliki nagłówkowe dla PHAT
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and development documentation for the PHAT Audio Toolkit.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja dla PHAT Audio Toolkit.

%package static
Summary:	PHAT static library
Summary(pl.UTF-8):   Biblioteka statyczna PHAT
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description static
PHAT static library.

%description static -l pl.UTF-8
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

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

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
