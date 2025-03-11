#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Cross-platform network interface and IP address enumeration library
Summary(pl.UTF-8):	Wieloplatformowa biblioteka do wyliczania interfejsów i adresów IP
Name:		python-ifaddr
# keep 0.1.x here for python2 support
Version:	0.1.7
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/ifaddr/
Source0:	https://files.pythonhosted.org/packages/source/i/ifaddr/ifaddr-%{version}.tar.gz
# Source0-md5:	97c4eb7505643b5f1fe17733cb42abd9
URL:		https://pypi.org/project/ifaddr/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-ipaddress
%endif
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
ifaddr is a small Python library that allows you to find all the IP
addresses of the computer. It is tested on Linux, OS X, and Windows.
Other BSD derivatives like OpenBSD, FreeBSD, and NetBSD should work
too, as well as Solaris/Illumos.

%description -l pl.UTF-8
ifaddr to mała biblioteka Pythona, pozwalająca uzyskać wszystkie
adresy IP komputera. Jest testowana na Linuksie, OS X oraz Windows.
Inne pochodne BSD, jak OpenBSD, FreeBSD i NetBSD powinny także
działać, podobnie jak Solaris/Illumos.

%package -n python3-ifaddr
Summary:	Cross-platform network interface and IP address enumeration library
Summary(pl.UTF-8):	Wieloplatformowa biblioteka do wyliczania interfejsów i adresów IP
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-ifaddr
ifaddr is a small Python library that allows you to find all the IP
addresses of the computer. It is tested on Linux, OS X, and Windows.
Other BSD derivatives like OpenBSD, FreeBSD, and NetBSD should work
too, as well as Solaris/Illumos.

%description -n python3-ifaddr -l pl.UTF-8
ifaddr to mała biblioteka Pythona, pozwalająca uzyskać wszystkie
adresy IP komputera. Jest testowana na Linuksie, OS X oraz Windows.
Inne pochodne BSD, jak OpenBSD, FreeBSD i NetBSD powinny także
działać, podobnie jak Solaris/Illumos.

%prep
%setup -q -n ifaddr-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m unittest discover -s ifaddr
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m unittest discover -s ifaddr
%endif
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
%doc LICENSE.txt README.rst
%{py_sitescriptdir}/ifaddr
%{py_sitescriptdir}/ifaddr-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-ifaddr
%defattr(644,root,root,755)
%doc LICENSE.txt README.rst
%{py3_sitescriptdir}/ifaddr
%{py3_sitescriptdir}/ifaddr-%{version}-py*.egg-info
%endif
