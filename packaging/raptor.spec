Name:           raptor
Version:        2.0.8
Release:        0
Summary:        RDF Parser Toolkit
License:        LGPL-2.1+ or GPL-2.0+ or Apache-2.0
Group:          System/Libraries
Url:            http://www.redland.opensource.ac.uk/raptor/
Source0:        %{name}2-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  autoconf
BuildRequires:  curl-devel
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libxml-2.0)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Raptor is the RDF Parser Toolkit for Redland that provides a set of
standalone RDF parsers, generating triples from RDF/XML or N-Triples.

%package -n libraptor
Summary:        RDF Parser Toolkit
Group:          System/Libraries

%description -n libraptor
Raptor is the RDF Parser Toolkit for Redland that provides a set of
standalone RDF parsers, generating triples from RDF/XML or N-Triples.

%package -n libraptor-devel
Summary:        Development package for the raptor library
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libraptor = %{version}
Requires:       raptor = %{version}
Provides:       raptor-devel = %{version}
Obsoletes:      raptor-devel < %{version}

%description -n libraptor-devel
This package contains the files needed to compile programs that use the
raptor library.

%prep
%setup -q -n %{name}2-%{version}

%build
%configure --disable-gtk-doc --disable-static --with-pic --with-html-dir=%{_docdir}
make %{?_smp_flags}

%check
export MALLOC_CHECK_=2
make check
unset MALLOC_CHECK_

%install
%make_install
rm -rf %{buildroot}/%{_docdir}

%post -n libraptor -p /sbin/ldconfig

%postun -n libraptor -p /sbin/ldconfig


%remove_package 

%files
%defattr(-,root,root)
%license COPYING COPYING.LIB LICENSE.txt 
%{_bindir}/rapper

%files -n libraptor-devel
%defattr(-,root,root)
%{_libdir}/lib*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc

%files -n libraptor
%defattr(-,root,root)
%{_libdir}/libraptor2.so.0*

%changelog
