#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	Encoding
Summary:	XML::Encoding - module for parsing XML encoding maps
Summary(pl.UTF-8):	XML::Encoding - moduł analizujący mapy kodowań XML
Name:		perl-XML-Encoding
Version:	2.07
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	802cca8bd9a4726641d13b794d6c28f9
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

%description -l pl.UTF-8
Ten moduł, stworzony jako podklasa XML::Parser, udostępnia analizator
dla plików map kodowań będących plikami XML. Plik maps/encmap.dtd
zawarty w pakiecie opisuje strukturę tych plików. Wywołanie metody
parse zwraca nazwę mapy kodowania (otrzymaną z atrybutu name elementu
głównego). Zawartość mapy jest przetwarzana poprzez funkcje wywołań
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
%{_mandir}/man?/*
