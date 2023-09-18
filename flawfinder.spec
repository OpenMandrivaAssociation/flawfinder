Name:           flawfinder
Version:        2.0.19
Release:        1
Epoch:          0
Summary:        Examines C/C++ source code for security flaws
License:        GPLv2+
Group:          Development/C
URL:            https://www.dwheeler.com/flawfinder/
Source0:        https://www.dwheeler.com/flawfinder/flawfinder-%{version}.tar.gz
Requires:       python
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Flawfinder scans through C/C++ source code, identifying lines ("hits") with
potential security flaws. By default it reports hits sorted by severity, with
the riskiest lines first.

%prep
%setup -q

%build
%{make_build}

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_bindir}
%{__mkdir_p} %{buildroot}%{_mandir}/man1
%{__cp} -a flawfinder.py %{buildroot}%{_bindir}/flawfinder
/bin/zcat flawfinder.1.gz >%{buildroot}%{_mandir}/man1/flawfinder.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc announcement ChangeLog COPYING flawfinder.p{df,s} INSTALL.md README.md
%attr(0755,root,root) %{_bindir}/flawfinder
%{_mandir}/man1/flawfinder.1*




%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0:1.27-6mdv2011.0
+ Revision: 618304
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 0:1.27-5mdv2010.0
+ Revision: 428796
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0:1.27-4mdv2009.0
+ Revision: 245197
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0:1.27-2mdv2008.1
+ Revision: 140730
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Jan 17 2007 David Walluck <walluck@mandriva.org> 1.27-2mdv2007.0
+ Revision: 109767
- fix included docs
- 1.27
- Import flawfinder

* Thu Sep 09 2004 Frederic Lepied <flepied@mandrakesoft.com> 1.26-1mdk
- New release 1.26

