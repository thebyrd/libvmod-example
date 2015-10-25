Summary: Dynamic Backend VMOD for Varnish
Name: vmod-dynamic
Version: 0.1
Release: 1%{?dist}
License: BSD
Group: System Environment/Daemons
Source0: lib%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires: varnish >= 4.0.2
BuildRequires: make
BuildRequires: python-docutils
BuildRequires: varnish >= 4.0.2
BuildRequires: varnish-libs-devel >= 4.0.2


%description
Dynamic Backend VMOD


%prep
%setup -n lib%{name}-%{version}


%build
%configure --prefix=/usr/
%{__make} %{?_smp_mflags}
%{__make} %{?_smp_mflags} check


%install
[ %{buildroot} != "/" ] && %{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
mv %{buildroot}/usr/share/doc/lib%{name} %{buildroot}/usr/share/doc/%{name}


%clean
[ %{buildroot} != "/" ] && %{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_libdir}/varnis*/vmods/
%doc /usr/share/doc/%{name}/*
%{_mandir}/man?/*


%changelog
* Sunday Oct 25 2015 David Byrd <dbyrd@do.co> - 0.1-0.20151025
- Initial version. Built from example vmod.
