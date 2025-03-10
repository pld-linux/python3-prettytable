#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Python 2 library for displaying tabular data in nice ASCII table format
Summary(pl.UTF-8):	Biblioteka Pythona 2 do wyświetlania danych tabelarycznych w ładnej tabelce ASCII
Name:		python-prettytable
# keep 1.x here for python2 support
Version:	1.0.1
Release:	2
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/prettytable/
Source0:	https://files.pythonhosted.org/packages/source/p/prettytable/prettytable-%{version}.tar.gz
# Source0-md5:	b5bd0acec56ae7ccf5ac22d3f671c3a7
URL:		https://pypi.org/project/PrettyTable
%if %{with tests} && %(locale -a | grep -q '^C\.UTF-8$'; echo $?)
BuildRequires:	glibc-localedb-all
%endif
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple Python 2 library for easily displaying tabular data in a
visually appealing ASCII table format.

%description -l pl.UTF-8
Prosta biblioteka Pythona 2 do łatwego wyświetlania danych
tabelarycznych w ładnie wyglądającej tabelce ASCII.

%package -n python3-prettytable
Summary:	Python 3 library for displaying tabular data in nice ASCII table format
Summary(pl.UTF-8):	Biblioteka Pythona 3 do wyświetlania danych tabelarycznych w ładnej tabelce ASCII
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-prettytable
A simple Python 3 library for easily displaying tabular data in a
visually appealing ASCII table format.

%description -n python3-prettytable -l pl.UTF-8
Prosta biblioteka Pythona 3 do łatwego wyświetlania danych
tabelarycznych w ładnie wyglądającej tabelce ASCII.

%prep
%setup -q -n prettytable-%{version}

%build
%if %{with tests}
export LC_ALL=C.UTF-8
%endif

%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGELOG.md COPYING README.md
%{py_sitescriptdir}/prettytable.py[co]
%{py_sitescriptdir}/prettytable-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-prettytable
%defattr(644,root,root,755)
%doc CHANGELOG.md COPYING README.md
%{py3_sitescriptdir}/prettytable.py
%{py3_sitescriptdir}/__pycache__/prettytable.cpython-*.py[co]
%{py3_sitescriptdir}/prettytable-%{version}-py*.egg-info
%endif
