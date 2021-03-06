#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pastel
Version  : 0.2.1
Release  : 8
URL      : https://files.pythonhosted.org/packages/76/f1/4594f5e0fcddb6953e5b8fe00da8c317b8b41b547e2b3ae2da7512943c62/pastel-0.2.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/76/f1/4594f5e0fcddb6953e5b8fe00da8c317b8b41b547e2b3ae2da7512943c62/pastel-0.2.1.tar.gz
Summary  : Bring colors to your terminal.
Group    : Development/Tools
License  : MIT
Requires: pypi-pastel-license = %{version}-%{release}
Requires: pypi-pastel-python = %{version}-%{release}
Requires: pypi-pastel-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(poetry_core)

%description
Pastel: Bring colors to your terminal
#####################################
Pastel is a simple library to help you colorize strings in your terminal.

%package license
Summary: license components for the pypi-pastel package.
Group: Default

%description license
license components for the pypi-pastel package.


%package python
Summary: python components for the pypi-pastel package.
Group: Default
Requires: pypi-pastel-python3 = %{version}-%{release}

%description python
python components for the pypi-pastel package.


%package python3
Summary: python3 components for the pypi-pastel package.
Group: Default
Requires: python3-core
Provides: pypi(pastel)

%description python3
python3 components for the pypi-pastel package.


%prep
%setup -q -n pastel-0.2.1
cd %{_builddir}/pastel-0.2.1
pushd ..
cp -a pastel-0.2.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656393152
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pastel
cp %{_builddir}/pastel-0.2.1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pastel/84661790a5df00ab944c2d37978d6ce5ac88e554
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
## Remove excluded files
rm -f %{buildroot}*/usr/lib/python3.*/site-packages/tests/__init__.py
rm -f %{buildroot}*/usr/lib/python3.*/site-packages/tests/__pycache__/__init__.cpython-3*.pyc
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pastel/84661790a5df00ab944c2d37978d6ce5ac88e554

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
