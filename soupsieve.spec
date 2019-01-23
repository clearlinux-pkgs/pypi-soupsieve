#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : soupsieve
Version  : 1.7.3
Release  : 6
URL      : https://files.pythonhosted.org/packages/a0/ac/fc877f0cfe74c8ca93eb2cd873786fd0b4e92e1cb8d8aaa82aa8fcfd259d/soupsieve-1.7.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/a0/ac/fc877f0cfe74c8ca93eb2cd873786fd0b4e92e1cb8d8aaa82aa8fcfd259d/soupsieve-1.7.3.tar.gz
Summary  : A CSS4 selector implementation for Beautiful Soup.
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
[![Unix Build Status][travis-image]][travis-link]
[![Windows Build Status][appveyor-image]][appveyor-link]
[![Coverage Status][codecov-image]][codecov-link]
[![PyPI Version][pypi-image]][pypi-link]

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

%description python3
python3 components for the soupsieve package.


%prep
%setup -q -n soupsieve-1.7.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1548254441
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/soupsieve
cp LICENSE.md %{buildroot}/usr/share/package-licenses/soupsieve/LICENSE.md
cp docs/src/markdown/about/license.md %{buildroot}/usr/share/package-licenses/soupsieve/docs_src_markdown_about_license.md
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/soupsieve/LICENSE.md
/usr/share/package-licenses/soupsieve/docs_src_markdown_about_license.md

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
