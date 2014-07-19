
Name:           avtranscoder
Version:        0.1
Release:        0
License:        GPL-3.0+
Summary:        C++ API under LibAV and FFmpeg libraries
Url:            http://www.TuttleOFX.org
Group:          Development/Languages/C and C++
BuildRequires:  scons
BuildRequires:  gcc-c++
BuildRequires:  swig
BuildRequires:  java-1_7_0-openjdk-devel
BuildRequires:  python-devel
BuildRequires:  libavutil-devel
BuildRequires:  libavformat-devel
BuildRequires:  libavcodec-devel
BuildRequires:  libswscale-devel
BuildRequires:  libavresample-devel
BuildRequires:  freeglut-devel
Source:         %{name}-%{version}.tar.xz
Provides:       avmeta
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
High level API to read, decode, transform, encode and write video formats using FFmpeg or LibAV.

%package -n libAvTranscoder0
Summary: Library %{name}

%description -n libAvTranscoder0
Shared libraries for the package %{name}.

%package devel
Summary: Development files for %{name}

%description devel
Header files and static libraries for the package %{name}.

%package python
Summary: Python binding for %{name}

%description python
Provide the python binding upon %{name} C++ library	.

%package java
Summary: Java binding for %{name}

%description java
Java binding for %{name}. Require more updates for complete deployement.

%prep
%setup -q -n %{name}-%{version}

%build
cd avTranscoder
cp tools/scons.opensuse.cfg scons.cfg
scons


%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{py_sitedir}/AvTranscoder
install -D -m 0755 avTranscoder/build/app/av++ %{buildroot}%{_bindir}
install -D -m 0755 avTranscoder/build/app/avmeta %{buildroot}%{_bindir}
install -D -m 0755 avTranscoder/build/app/avinfo %{buildroot}%{_bindir}
install -D -m 0755 avTranscoder/build/app/avprocessor %{buildroot}%{_bindir}

install -D -m 0644 avTranscoder/app/*/av++.man %{buildroot}%{_mandir}/man1/av++.1
install -D -m 0644 avTranscoder/app/*/avinfo.man %{buildroot}%{_mandir}/man1/avinfo.1
install -D -m 0644 avTranscoder/app/*/avmeta.man %{buildroot}%{_mandir}/man1/avmeta.1
install -D -m 0644 avTranscoder/app/*/avprocessor.man %{buildroot}%{_mandir}/man1/avprocessor.1

cp avTranscoder/build/src/lib*.so.0.0.1  %{buildroot}%{_libdir}
cp -P avTranscoder/build/src/lib*.so.0  %{buildroot}%{_libdir}
cp -P avTranscoder/build/src/lib*.so  %{buildroot}%{_libdir}
cp avTranscoder/build/src/libsAvTranscoder.a  %{buildroot}%{_libdir}
cp avTranscoder/build/src/AvTranscoder/AvTranscoder.py %{buildroot}%{py_sitedir}/AvTranscoder
touch %{buildroot}%{py_sitedir}/AvTranscoder/__init__.py

%post
/sbin/ldconfig

%post -n libAvTranscoder0
/sbin/ldconfig

%postun
/sbin/ldconfig

%postun -n libAvTranscoder0
/sbin/ldconfig


%files
%defattr(-,root,root)
/%{_bindir}/av*
/%{_mandir}/man1/*.1.gz

%files -n libAvTranscoder0
%defattr(-,root,root)
/%{_libdir}/libAvTranscoder.so
/%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root)
/%{_libdir}/libsAvTranscoder.a

%files python
%defattr(-,root,root)
/%{py_sitedir}

%files java
%defattr(-,root,root)
/%{_libdir}/libjAvTranscoder.so

%changelog
* Sat Mar 1 2014 - arnaud.marcantoine@gmail.com
- first release of packaging
