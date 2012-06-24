%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	Encoding
Summary:	XML::Encoding Perl module
Summary(cs):	Modul XML::Encoding pro Perl
Summary(da):	Perlmodul XML::Encoding
Summary(de):	XML::Encoding Perl Modul
Summary(es):	M�dulo de Perl XML::Encoding
Summary(fr):	Module Perl XML::Encoding
Summary(it):	Modulo di Perl XML::Encoding
Summary(ja):	XML::Encoding Perl �⥸�塼��
Summary(ko):	XML::Encoding �� ����
Summary(no):	Perlmodul XML::Encoding
Summary(pl):	Modu� Perla XML::Encoding
Summary(pt):	M�dulo de Perl XML::Encoding
Summary(pt_BR):	M�dulo Perl XML::Encoding
Summary(ru):	������ ��� Perl XML::Encoding
Summary(sv):	XML::Encoding Perlmodul
Summary(uk):	������ ��� Perl XML::Encoding
Summary(zh_CN):	XML::Encoding Perl ģ��
Name:		perl-XML-Encoding
Version:	1.01
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6.1
BuildRequires:	perl-XML-Parser >= 2.18
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::Encoding - module for parsing XML encoding maps.

%description -l pl
XML::Encoding - modu� analizuj�cy mapy kodowania XML.

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
