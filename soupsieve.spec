#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : soupsieve
Version  : 2.1
Release  : 26
URL      : https://files.pythonhosted.org/packages/58/5d/445e21e92345848305eecf473338e9ec7ed8905b99ea78415042060127fc/soupsieve-2.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/58/5d/445e21e92345848305eecf473338e9ec7ed8905b99ea78415042060127fc/soupsieve-2.1.tar.gz
Summary  : A modern CSS selector implementation for Beautiful Soup.
Group    : Development/Tools
License  : MIT
Requires: soupsieve-license = %{version}-%{release}
Requires: soupsieve-python = %{version}-%{release}
Requires: soupsieve-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
[![Discord][discord-image]][discord-link]
        [![Build][github-ci-image]][github-ci-link]
        [![Coverage Status][codecov-image]][codecov-link]
        [![PyPI Version][pypi-image]][pypi-link]
        [![PyPI - Python Version][python-image]][pypi-link]
        ![License][license-image-mit]
        
        # Soup Sieve
        
        ## Overview
        
        Soup Sieve is a CSS selector library designed to be used with [Beautiful Soup 4][bs4]. It aims to provide selecting,
        matching, and filtering using modern CSS selectors. Soup Sieve currently provides selectors from the CSS level 1
        specifications up through the latest CSS level 4 drafts and beyond (though some are not yet implemented).
        
        Soup Sieve was written with the intent to replace Beautiful Soup's builtin select feature, and as of Beautiful Soup

%package license
Summary: license components for the soupsieve package.
Group: Default

%description license
license components for the soupsieve package.


%package python
Summary: python components for the soupsieve package.
Group: Default
Requires: soupsieve-python3 = %{version}-%{release}

%description python
python components for the soupsieve package.


%package python3
Summary: python3 components for the soupsieve package.
Group: Default
Requires: python3-core
Provides: pypi(soupsieve)

%description python3
python3 components for the soupsieve package.


%prep
%setup -q -n soupsieve-2.1
cd %{_builddir}/soupsieve-2.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1607735238
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/soupsieve
cp %{_builddir}/soupsieve-2.1/LICENSE.md %{buildroot}/usr/share/package-licenses/soupsieve/bb9c4f272c1b7a041df0ca4dff99588d6ad958c8
cp %{_builddir}/soupsieve-2.1/docs/src/markdown/about/license.md %{buildroot}/usr/share/package-licenses/soupsieve/aed22c356adf0d9eddf6a06b96e4672094334f1d
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/soupsieve/aed22c356adf0d9eddf6a06b96e4672094334f1d
/usr/share/package-licenses/soupsieve/bb9c4f272c1b7a041df0ca4dff99588d6ad958c8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
