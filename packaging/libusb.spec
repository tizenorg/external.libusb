%define keepstatic 1

Name:       libusb
Summary:    A library which allows userspace access to USB devices
Version:    0.1.12
Release:    16.41
Group:      System/Libraries
License:    LGPLv2+
URL:        http://sourceforge.net/projects/libusb/
Source0:    http://prdownloads.sourceforge.net/libusb/%{name}-%{version}.tar.gz
Patch0:     00_packed.diff
Patch1:     01_ansi.diff
Patch2:     02_usbpp.diff
Patch3:     03_const_buffers.diff
Patch4:     04_infinite_loop.diff
Patch5:     05_emdebian_libs.diff
Patch6:     90_am_maintainer_mode.diff
Patch7:     91_autoreconf.diff
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

# 00_packed.diff
%patch0 -p1
# 01_ansi.diff
%patch1 -p1
# 02_usbpp.diff
%patch2 -p1
# 03_const_buffers.diff
%patch3 -p1
# 04_infinite_loop.diff
%patch4 -p1
# 05_emdebian_libs.diff
%patch5 -p1
# 90_am_maintainer_mode.diff
%patch6 -p1
# 91_autoreconf.diff
%patch7 -p1

%build

%configure  \
    --disable-static --disable-build-docs

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install


mkdir -p %{buildroot}/lib/
mv %{buildroot}/usr/lib/libusb-0.1.so.* %{buildroot}/lib/
ln -sf /lib/libusb-0.1.so.4 %{buildroot}/usr/lib/libusb-0.1.so.4
ln -sf /lib/libusb-0.1.so.4.4.4 %{buildroot}/usr/lib/libusb.so


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig




%files
%defattr(-,root,root,-)
/lib/*.so.*
%{_libdir}/*.so.*


%files devel
%defattr(-,root,root,-)
%{_bindir}/libusb-config
%{_libdir}/pkgconfig/libusb.pc
%{_includedir}/*
%{_libdir}/*.so

