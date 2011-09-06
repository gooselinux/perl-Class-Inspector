Name: 		perl-Class-Inspector
Version: 	1.24
Release: 	4%{?dist}
Summary: 	Get information about a class and its structure
License: 	GPL+ or Artistic
Group: 		Development/Libraries
URL: 		http://search.cpan.org/dist/Class-Inspector/
Source0: 	http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/Class-Inspector-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildArch: noarch

BuildRequires:	perl(Test::More)

# For better test coverage
BuildRequires: perl(Test::Pod) >= 1.00
BuildRequires: perl(Test::CPAN::Meta) >= 0.12
BuildRequires: perl(Perl::MinimumVersion) >= 1.20
BuildRequires: perl(Test::MinimumVersion) >= 0.008

%description
Class::Inspector allows you to get information about a loaded class.
Most or all of this information can be found in other ways, but they aren't
always very friendly, and usually involve a relatively high level of Perl
wizardry, or strange and unusual looking code. Class::Inspector attempts to
provide an easier, more friendly interface to this information.

%prep
%setup -q -n Class-Inspector-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%clean
rm -rf $RPM_BUILD_ROOT

%check
make test AUTOMATED_TESTING=1

%files
%defattr(-,root,root,-)
%doc Changes LICENSE README
%{perl_vendorlib}/Class
%{_mandir}/man3/*

%changelog
* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 1.24-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 17 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.24-2
- BR: perl(Test::MinimumVersion) >= 0.008

* Mon May 11 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.24-1
- Upstream update.
- Remove Class-Inspector-1.23.diff.

* Fri Feb 27 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.23-3
- Unconditionally BR: perl(Test::CPAN::Meta).
- Adjust minimum perl version in META.yml (Add Class-Inspector-1.23.diff).

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jun 10 2008 Ralf Corsépius <rc040203@freenet.de> - 1.23-1
- Upstream update.

* Tue Mar 11 2008 Ralf Corsépius <rc040203@freenet.de> - 1.22-1
- Upstream update.

* Thu Feb 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.20-3
- Rebuild normally, second pass

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.20-2
- Rebuild for perl 5.10 (again), first pass

* Thu Feb 14 2008 Ralf Corsépius <rc040203@freenet.de> - 1.20-1
- Upstream update.

* Mon Jan 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.18-3
- rebuild normally, second pass

* Sun Jan 13 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.18-2.1
- rebuild for new perl, first pass, disable TMV, tests

* Sun Nov 25 2007 Ralf Corsépius <rc040203@freenet.de> - 1.18-2
- Add BR: perl(Test::MinimumVersion).

* Tue Nov 20 2007 Ralf Corsépius <rc040203@freenet.de> - 1.18-1
- Upstream update.

* Fri Aug 17 2007 Ralf Corsépius <rc040203@freenet.de> - 1.17-1
- Upstream update.

* Thu Apr 19 2007 Ralf Corsépius <rc040203@freenet.de> - 1.16-3
- Reflect perl package split.

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 1.16-2
- Mass rebuild.

* Mon May 21 2006 Ralf Corsépius <rc040203@freenet.de> - 1.16-1
- Upstream update.

* Mon May 08 2006 Ralf Corsépius <rc040203@freenet.de> - 1.15-1
- Upstream update.

* Wed Mar 01 2006 Ralf Corsépius <rc040203@freenet.de> - 1.13-2
- Rebuild for perl-5.8.8.

* Thu Sep 29 2005 Ralf Corsepius <rc040203@freenet.de> - 1.13-1
- Upstream update.

* Tue Sep 13 2005 Ralf Corsepius <rc040203@freenet.de>
- Fix another typo in %%summary.

* Tue Sep 13 2005 Ralf Corsepius <rc040203@freenet.de> - 1.12-2
- Fix typo in %%summary.
- Spec file cleanup.

* Tue Sep 13 2005 Ralf Corsepius <rc040203@freenet.de> - 1.12-1
- FE submission.
