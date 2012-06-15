Name:       libusb
Summary:    A library which allows userspace access to USB devices
Version:    1.0.8
Release:    1
Group:      Base/Libraries
License:    LGPLv2+
URL:        http://sourceforge.net/projects/libusb/
Source0:    http://prdownloads.sourceforge.net/libusb/%{name}-%{version}.tar.bz2
Source1001: packaging/libusb.manifest 
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig


%description
This package provides a way for applications to access USB devices.


%package devel
Summary:    Development files for libusb
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
This package contains the header files, libraries  and documentation needed to
develop applications that use libusb.


%prep
%setup -q

%build
cp %{SOURCE1001} .

%configure  \
    --disable-static --disable-build-docs

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%manifest libusb.manifest
%defattr(-,root,root,-)
%{_libdir}/*.so.*

%files devel
%manifest libusb.manifest
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/*
%{_includedir}/libusb-1.0/*
%{_libdir}/*.so

