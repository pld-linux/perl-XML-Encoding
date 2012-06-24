%include	/usr/lib/rpm/macros.perl
Summary:	XML-Encoding perl module
Summary(pl):	Modu� perla XML-Encoding
Name:		perl-XML-Encoding
Version:	1.01
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/XML-Encoding-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-XML-Parser
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML-Encoding - module for parsing XML encoding maps.

%description -l pl
XML-Encoding - modu� analizuj�cy mapy kodowania XML.

%prep
%setup -q -n XML-Encoding-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README maps/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz maps
%attr(755,root,root) %{_bindir}/*
%{perl_sitelib}/XML/Encoding.pm
%{_mandir}/man3/*
