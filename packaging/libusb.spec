Name:       libusb
Summary:    A library which allows userspace access to USB devices
Version: 1.0.9
Release:    15
Group:      System/Libraries
License:    LGPLv2.1
URL:        http://sourceforge.net/projects/libusb/
Source0:    http://prdownloads.sourceforge.net/libusb/%{name}-%{version}.tar.gz
Source1:	libusb.manifest
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
%setup -q -n %{name}-%{version}

%build
cp %{SOURCE1} .

%configure  \
    --disable-static --disable-build-docs

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

mkdir -p %{buildroot}/lib/
mv %{buildroot}/usr/lib/libusb-1.0.so.* %{buildroot}/lib/
ln -sf /lib/libusb-1.0.so.0 %{buildroot}/usr/lib/libusb-1.0.so.0
ln -sf /lib/libusb-1.0.so.0.1.0 %{buildroot}/usr/lib/libusb-1.0.so

mkdir -p %{buildroot}/usr/share/license
cp COPYING %{buildroot}/usr/share/license/%{name}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig




%files
%defattr(-,root,root,-)
/lib/*.so.*
%{_libdir}/*.so.*
/usr/share/license/%{name}


%files devel
%manifest libusb.manifest
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/libusb-1.0.pc
%{_includedir}/*
%{_libdir}/*.so

