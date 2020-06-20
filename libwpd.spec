#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libwpd
Version  : 0.10.3
Release  : 4
URL      : https://dev-www.libreoffice.org/src/libwpd-0.10.3.tar.xz
Source0  : https://dev-www.libreoffice.org/src/libwpd-0.10.3.tar.xz
Summary  : A library for reading and writing Corel WordPerfect(tm) documents
Group    : Development/Tools
License  : LGPL-2.1 MPL-2.0-no-copyleft-exception
Requires: libwpd-bin = %{version}-%{release}
Requires: libwpd-lib = %{version}-%{release}
Requires: libwpd-license = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : doxygen
BuildRequires : pkgconfig(librevenge-0.0)
BuildRequires : pkgconfig(librevenge-generators-0.0)

%description
libwpd is a library for import of WordPerfect documents. It is used by,
for example, AbiWord and LibreOffice.

%package bin
Summary: bin components for the libwpd package.
Group: Binaries
Requires: libwpd-license = %{version}-%{release}

%description bin
bin components for the libwpd package.


%package dev
Summary: dev components for the libwpd package.
Group: Development
Requires: libwpd-lib = %{version}-%{release}
Requires: libwpd-bin = %{version}-%{release}
Provides: libwpd-devel = %{version}-%{release}
Requires: libwpd = %{version}-%{release}

%description dev
dev components for the libwpd package.


%package doc
Summary: doc components for the libwpd package.
Group: Documentation

%description doc
doc components for the libwpd package.


%package lib
Summary: lib components for the libwpd package.
Group: Libraries
Requires: libwpd-license = %{version}-%{release}

%description lib
lib components for the libwpd package.


%package license
Summary: license components for the libwpd package.
Group: Default

%description license
license components for the libwpd package.


%prep
%setup -q -n libwpd-0.10.3
cd %{_builddir}/libwpd-0.10.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1592625018
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1592625018
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libwpd
cp %{_builddir}/libwpd-0.10.3/COPYING.LGPL %{buildroot}/usr/share/package-licenses/libwpd/3704f4680301a60004b20f94e0b5b8c7ff1484a9
cp %{_builddir}/libwpd-0.10.3/COPYING.MPL %{buildroot}/usr/share/package-licenses/libwpd/9744cedce099f727b327cd9913a1fdc58a7f5599
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/wpd2html
/usr/bin/wpd2raw
/usr/bin/wpd2text

%files dev
%defattr(-,root,root,-)
/usr/include/libwpd-0.10/libwpd/WPDocument.h
/usr/include/libwpd-0.10/libwpd/libwpd.h
/usr/lib64/libwpd-0.10.so
/usr/lib64/pkgconfig/libwpd-0.10.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/libwpd/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libwpd-0.10.so.10
/usr/lib64/libwpd-0.10.so.10.0.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libwpd/3704f4680301a60004b20f94e0b5b8c7ff1484a9
/usr/share/package-licenses/libwpd/9744cedce099f727b327cd9913a1fdc58a7f5599
