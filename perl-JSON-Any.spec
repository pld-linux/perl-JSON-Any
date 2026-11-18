#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	JSON
%define	pnam	Any
Summary:	JSON::Any - Wrapper Class for the various JSON classes.
#Summary(pl.UTF-8):	
Name:		perl-JSON-Any
Version:	1.42
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/authors/id/E/ET/ETHER/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	95a1f70ef483ae50c7cbc57d19cc5cf5
URL:		http://search.cpan.org/dist/JSON-Any/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-JSON >= 2.02
BuildRequires:	perl-JSON-XS
BuildRequires:	perl-Test-Fatal
BuildRequires:	perl-Test-Needs
BuildRequires:	perl-Test-Warnings >= 0.009
BuildRequires:	perl-Test-Without-Module
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module will provide a coherent API to bring together the various
JSON modules currently on CPAN.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/JSON/*.pm
%{_mandir}/man3/*
