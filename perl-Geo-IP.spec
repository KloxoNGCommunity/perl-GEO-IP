Name:           perl-Geo-IP
Version:        1.51
Release:        2.kng%{?dist}
Summary:        Look up location and network information by IP Address
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Geo-IP/
Source0:        http://www.cpan.org/authors/id/M/MA/MAXMIND/Geo-IP-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  perl(base)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-macros
BuildRequires:  perl-devel
BuildRequires:  make
Requires:       perl(base)
Requires:       perl(DynaLoader)
Requires:       perl(Exporter)
Requires:       perl(strict)
Requires:       perl(vars)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Provides:       perl(Geo::IP)

%description
This module uses the GeoIP Legacy file based database. This database simply
contains IP blocks as keys, and countries as values. This database should
be more complete and accurate than reverse DNS lookups.

%prep
%setup -q -n Geo-IP-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes CONTRIBUTING.md cpanfile dist.ini LICENSE META.json README.md
#{perl_vendorlib}/auto/*
%{perl_vendorlib}/Geo*
%{_mandir}/man3/*

%changelog
* Tue Jun 18 2024 John Pierce <john@luckytanuki.com> 1.51-2
- Adapt for Kloxo 

* Tue Apr 30 2024 Peter Ajamian <pj@ghettoforge.org> 1.51-1
- Specfile autogenerated by cpanspec 1.78.
