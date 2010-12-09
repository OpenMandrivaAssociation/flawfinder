Name:           flawfinder
Version:        1.27
Release:        %mkrel 6
Epoch:          0
Summary:        Examines C/C++ source code for security flaws
License:        GPL
Group:          Development/C
URL:            http://www.dwheeler.com/flawfinder/
Source0:        http://www.dwheeler.com/flawfinder/flawfinder-%{version}.tar.gz
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
%{make}

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_bindir}
%{__mkdir_p} %{buildroot}%{_mandir}/man1
%{__cp} -a flawfinder %{buildroot}%{_bindir}/flawfinder
/bin/zcat flawfinder.1.gz >%{buildroot}%{_mandir}/man1/flawfinder.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc announcement ChangeLog COPYING flawfinder.p{df,s} INSTALL.txt README 
%attr(0755,root,root) %{_bindir}/flawfinder
%{_mandir}/man1/flawfinder.1*


