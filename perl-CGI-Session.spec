#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	CGI
%define	pnam	Session
Summary:	CGI::Session - Persistent storage of complex data in CGI
Summary(pl):	CGI::Session - Trwa³e przechowywanie z³o¿onych struktur danych w CGI
Name:		perl-CGI-Session
Version:	3.92
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-DB_File
BuildRequires:	perl-FreezeThaw
BuildRequires:	perl-Storable
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI::Session is Perl5 library that provides an easy persistent session
management system across HTTP requests.

%description -l pl
CGI::Session jest bibliotek± dla Perla5, udostêpniaj±c± ³atwy system
zarz±dzania trwa³± sesj± pomiêdzy zapytaniami HTTP.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_sitelib}/%{pdir}/*.pm
%{perl_sitelib}/%{pdir}/%{pnam}
%{perl_sitelib}/auto/%{pdir}/%{pnam}
%{_mandir}/man3/*
