Name: GbtUtility
Version: 2.0.12
Release: 0%{?dist}
Summary: GbtUtility command line utility
Group: Utility/Hardware
License: Unknown
URL: https://www.gigabyte.com/
BuildArch: x86_64
Source0: server_utility_command_line_utility_2.0.zip

Requires: java >= 7
Requires: javaws
Requires: freeipmi
Requires: ipmitool
BuildRequires: unzip

%description
GbtUtility command line utility

%prep
%setup -T -c -n %{name}-%{version}
unzip %{SOURCE0}

%install
mkdir -m 0755 -p ${RPM_BUILD_ROOT}/opt/gbtutility
cp -rp * ${RPM_BUILD_ROOT}/opt/gbtutility

%files
%defattr(-,root,root,-)
/opt/gbtutility/

%changelog
* Tue Nov 06 2018 Tomoya KABE <kabe@elastic-infra.com> - 2.0.12
- packaged
