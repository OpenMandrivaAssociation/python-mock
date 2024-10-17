# Created by pyp2rpm-3.3.5
%global pypi_name mock

Name:           python-%{pypi_name}
Version:        4.0.3
Release:        2
Summary:        Rolling backport of unittest.mock for all Pythons
Group:          Development/Python
License:        None
URL:            https://mock.readthedocs.org/en/latest/
Source0:        %{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
mock is a library for testing in Python. It allows you to replace parts of your
system under test with mock objects and make assertions about how they have
been used.mock is now part of the Python standard library, available as
unittest.mock < in Python 3.3 This package contains a rolling backport of the
standard library mock code compatible with Python 3.6 and up.Please see the
standard...

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
