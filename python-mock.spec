# Created by pyp2rpm-3.3.5
%global pypi_name mock

Name:           python-%{pypi_name}
Version:        5.2.0
Release:        1
Summary:        Rolling backport of unittest.mock for all Pythons
Group:          Development/Python
License:        BSD-2-Clause
URL:            https://github.com/testing-cabal/mock
Source0:        https://files.pythonhosted.org/packages/source/m/mock/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(python)
BuildRequires:  python%{pyver}dist(setuptools)

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
%py_build

%install
%py_install

%files -n python-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/%{pypi_name}
%{python_sitelib}/%{pypi_name}-%{version}-py%{pyver}.egg-info
