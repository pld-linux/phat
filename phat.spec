Summary:	PHAT Audio Toolkit
Name:		phat
Version:	0.2.2
Release:	1
License:	GPL v.2
Group:		X11/Libraries
Source0:	http://www.gazuga.net/phatfiles/%{name}-%{version}.tar.gz
# Source0-md5:	5b56ac404289bd43b2a09ae66a71a200
URL:		http://www.gazuga.net/phat.php
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Collection of gtk+ wigets useful for audio applications.

%description -l pl
Kolekcja kontrolek gtk+ u�ytecznych dla aplikacji d�wi�kowych.

%package devel
Summary:	Header files for PHAT
Summary(pl):	Pliki nag��wkowe dla PHAT
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and development documentation for the PHAT Audio Toolkit.

%description devel -l pl
Pliki nag��wkowe i dokumentacja dla PHAT Audio Toolkit.

%package static
Summary:	PHAT static library.
Summary(pl):	Biblioteka statyczna PHAT
Group:		Development/Libraries
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
%{_gtkdocdir}/*
%{_includedir}/phat
%{_libdir}/lib*.la
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a