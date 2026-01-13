#
# Conditional build:
%bcond_with	tests	# do not perform "make test"
#
%define		pdir	CGI
%define		pnam	Session
Summary:	CGI::Session - persistent storage of complex data in CGI
Summary(pl.UTF-8):	CGI::Session - trwałe przechowywanie złożonych struktur danych w CGI
Name:		perl-CGI-Session
Version:	4.48
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7f8983aaeb92a0ba77eca8bca6d8d43a
URL:		http://search.cpan.org/dist/CGI-Session/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-DB_File
BuildRequires:	perl-FreezeThaw
BuildRequires:	perl-CGI-Simple
BuildRequires:	perl-YAML-Syck
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI::Session is Perl5 library that provides an easy persistent session
management system across HTTP requests.

%description -l pl.UTF-8
CGI::Session jest biblioteką dla Perla5, udostępniającą łatwy system
zarządzania trwałą sesją pomiędzy zapytaniami HTTP.

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
%doc Changes
%{perl_vendorlib}/CGI/*.pm
%{perl_vendorlib}/CGI/Session
%{_mandir}/man3/*
