%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	Encoding
Summary:	XML::Encoding perl module
Summary(pl):	Modu³ perla XML::Encoding
Name:		perl-XML-Encoding
Version:	1.01
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6.1
BuildRequires:	perl-XML-Parser >= 2.18
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::Encoding - module for parsing XML encoding maps.

%description -l pl
XML::Encoding - modu³ analizuj±cy mapy kodowania XML.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README maps
%attr(755,root,root) %{_bindir}/*
%{perl_sitelib}/XML/Encoding.pm
%{_mandir}/man3/*
