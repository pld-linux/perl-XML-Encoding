%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	XML-Encoding perl module
Summary(pl):	Modu� perla XML-Encoding
Name:		perl-XML-Encoding
Version:	1.01
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/XML-Encoding-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
BuildRequires:	perl-XML-Parser
%requires_eq	perl
Requires:	%{perl_sitearch}
Requires:	perl-XML-Parser
BuildRoot:	/tmp/%{name}-%{version}-root

%description
XML-Encoding - module for parsing XML encoding maps. 

%description -l pl
XML-Encoding - modu� analizuj�cy mapy kodowania XML.

%prep
%setup -q -n XML-Encoding-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/XML/Encoding
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README maps/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz maps
%attr(755,root,root) %{_bindir}/*

%{perl_sitelib}/XML/Encoding.pm
%{perl_sitearch}/auto/XML/Encoding

%{_mandir}/man3/*
