#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	Encoding
Summary:	XML::Encoding Perl module
Summary(cs):	Modul XML::Encoding pro Perl
Summary(da):	Perlmodul XML::Encoding
Summary(de):	XML::Encoding Perl Modul
Summary(es):	Módulo de Perl XML::Encoding
Summary(fr):	Module Perl XML::Encoding
Summary(it):	Modulo di Perl XML::Encoding
Summary(ja):	XML::Encoding Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	XML::Encoding ÆÞ ¸ðÁÙ
Summary(nb):	Perlmodul XML::Encoding
Summary(pl):	Modu³ Perla XML::Encoding
Summary(pt):	Módulo de Perl XML::Encoding
Summary(pt_BR):	Módulo Perl XML::Encoding
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl XML::Encoding
Summary(sv):	XML::Encoding Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl XML::Encoding
Summary(zh_CN):	XML::Encoding Perl Ä£¿é
Name:		perl-XML-Encoding
Version:	1.01
Release:	11
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a2ed80f2e1e95de518ca131044dff650
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-XML-Parser >= 2.18
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::Encoding - module for parsing XML encoding maps.

%description -l pl
XML::Encoding - modu³ analizuj±cy mapy kodowania XML.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README maps
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/XML/Encoding.pm
%{_mandir}/man3/*
