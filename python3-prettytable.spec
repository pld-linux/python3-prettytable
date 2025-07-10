#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Python 3 library for displaying tabular data in nice ASCII table format
Summary(pl.UTF-8):	Biblioteka Pythona 3 do wyświetlania danych tabelarycznych w ładnej tabelce ASCII
Name:		python3-prettytable
Version:	3.16.0
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/prettytable/
Source0:	https://files.pythonhosted.org/packages/source/p/prettytable/prettytable-%{version}.tar.gz
# Source0-md5:	85a6f1812e31ea2dcf8119f219c1a032
URL:		https://pypi.org/project/PrettyTable
%if %{with tests} && %(locale -a | grep -q '^C\.UTF-8$'; echo $?)
BuildRequires:	glibc-localedb-all
%endif
BuildRequires:	python3-build
BuildRequires:	python3-hatch-vcs
BuildRequires:	python3-hatchling >= 1.27
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.9
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest
BuildRequires:	python3-pytest-cov
BuildRequires:	python3-pytest-lazy-fixtures
BuildRequires:	python3-wcwidth
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple Python library for easily displaying tabular data in a
visually appealing ASCII table format.

%description -l pl.UTF-8
Prosta biblioteka Pythona do łatwego wyświetlania danych
tabelarycznych w ładnie wyglądającej tabelce ASCII.

%prep
%setup -q -n prettytable-%{version}

%build
%if %{with tests}
export LC_ALL=C.UTF-8
%endif

%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS=pytest_lazy_fixtures.plugin \
PYTHONPATH=$(pwd)/src \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%{py3_sitescriptdir}/prettytable
%{py3_sitescriptdir}/prettytable-%{version}.dist-info
