#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	Encoding
Summary:	XML::Encoding - module for parsing XML encoding maps
Summary(pl):	XML::Encoding - modu³ analizuj±cy mapy kodowañ XML
Name:		perl-XML-Encoding
Version:	1.01
Release:	11
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a2ed80f2e1e95de518ca131044dff650
BuildRequires:	perl-XML-Parser >= 2.18
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module, which is built as a subclass of XML::Parser, provides a
parser for encoding map files, which are XML files. The file
maps/encmap.dtd in the distribution describes the structure of these
files. Calling a parse method returns the name of the encoding map
(obtained from the name attribute of the root element). The contents
of the map are processed through the callback functions push_prefix,
pop_prefix, and range_set.

%description -l pl
Ten modu³, stworzony jako podklasa XML::Parser, udostêpnia analizator
dla plików map kodowañ bêd±cych plikami XML. Plik maps/encmap.dtd
zawarty w pakiecie opisuje strukturê tych plików. Wywo³anie metody
parse zwraca nazwê mapy kodowania (otrzyman± z atrybutu name elementu
g³ównego). Zawarto¶æ mapy jest przetwarzana poprzez funkcje wywo³añ
zwrotnych (callback) push_prefix, pop_prefix i range_set.

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
