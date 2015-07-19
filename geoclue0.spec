%define oname	geoclue

%define geoclue_major 0
%define geoclue %mklibname geoclue %{geoclue_major}
%define develname %mklibname -d geoclue

Name:		geoclue0
Version:	0.12.99
Release:	3
Summary:	A modular geoinformation service
Group:		Geography
License:	LGPLv2
URL:		http://geoclue.freedesktop.org/
Source0:	http://freedesktop.org/~hadess/%{oname}-%{version}.tar.gz
Patch0:		geoclue-0.12.0-gps.patch
BuildRequires:	pkgconfig(dbus-glib-1) >= 0.86
BuildRequires:	pkgconfig(gio-2.0) >= 2.25.7
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gypsy) >= 0.7.1
BuildRequires:	pkgconfig(libgps) >= 2.91
BuildRequires:	pkgconfig(libnm-glib)
BuildRequires:	pkgconfig(libnm-glib-vpn)
BuildRequires:	pkgconfig(libnm-util)
BuildRequires:	pkgconfig(libsoup-gnome-2.4)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	xsltproc
Requires:	dbus

%description
Geoclue is a modular geoinformation service built on top of the D-Bus
messaging system. The goal of the Geoclue project is to make creating
location-aware applications as simple as possible.

%files
%doc AUTHORS COPYING README
%dir %{_datadir}/geoclue-providers
%{_datadir}/dbus-1/services/org.freedesktop.Geoclue.Master.service
%{_datadir}/dbus-1/services/org.freedesktop.Geoclue.Providers.Example.service
%{_datadir}/dbus-1/services/org.freedesktop.Geoclue.Providers.Geonames.service
%{_datadir}/dbus-1/services/org.freedesktop.Geoclue.Providers.Hostip.service
%{_datadir}/dbus-1/services/org.freedesktop.Geoclue.Providers.Localnet.service
%{_datadir}/dbus-1/services/org.freedesktop.Geoclue.Providers.Manual.service
%{_datadir}/dbus-1/services/org.freedesktop.Geoclue.Providers.Nominatim.service
%{_datadir}/dbus-1/services/org.freedesktop.Geoclue.Providers.Plazes.service
%{_datadir}/dbus-1/services/org.freedesktop.Geoclue.Providers.Skyhook.service
%{_datadir}/dbus-1/services/org.freedesktop.Geoclue.Providers.Yahoo.service
%{_datadir}/geoclue-providers/geoclue-example.provider
%{_datadir}/geoclue-providers/geoclue-geonames.provider
%{_datadir}/geoclue-providers/geoclue-hostip.provider
%{_datadir}/geoclue-providers/geoclue-localnet.provider
%{_datadir}/geoclue-providers/geoclue-manual.provider
%{_datadir}/geoclue-providers/geoclue-nominatim.provider
%{_datadir}/geoclue-providers/geoclue-plazes.provider
%{_datadir}/geoclue-providers/geoclue-skyhook.provider
%{_datadir}/geoclue-providers/geoclue-yahoo.provider
%{_libexecdir}/geoclue-example
%{_libexecdir}/geoclue-geonames
%{_libexecdir}/geoclue-hostip
%{_libexecdir}/geoclue-localnet
%{_libexecdir}/geoclue-manual
%{_libexecdir}/geoclue-nominatim
%{_libexecdir}/geoclue-master
%{_libexecdir}/geoclue-plazes
%{_libexecdir}/geoclue-skyhook
%{_libexecdir}/geoclue-yahoo
%{_datadir}/GConf/gsettings/geoclue
%{_datadir}/glib-2.0/schemas/org.freedesktop.Geoclue.gschema.xml

#--------------------------------------------------------------------

%package -n %geoclue
Summary:   A modular geoinformation service
Group: System/Libraries

%description -n %geoclue
A modular geoinformation service

%files -n %geoclue
%_libdir/libgeoclue.so.%{geoclue_major}*

#--------------------------------------------------------------------

%package -n %develname
Summary: Development package for geoclue
Group:    Development/Other
Provides: %name-devel
Requires: %geoclue = %version-%release

%description -n %develname
Files for development with geoclue.

%files -n %develname
%{_includedir}/geoclue
%{_libdir}/pkgconfig/geoclue.pc
%{_libdir}/libgeoclue.so

#--------------------------------------------------------------------

%package doc
Summary: Developer documentation for geoclue
Group:   Documentation
Requires: %{name}-devel = %{version}-%{release}
BuildArch: noarch
Obsoletes: %{oname}-doc < 0.12.99-4

%description doc
Developer documentation for geoclue

%files doc
%doc %{_datadir}/gtk-doc/html/geoclue/

#--------------------------------------------------------------------

%package gui
Summary: Testing gui for geoclue
Group: Geography
Requires: %{name} = %{version}-%{release}
Obsoletes: %{oname}-gui < 0.12.99-4

%description gui
Testing gui for geoclue

%files gui
%{_bindir}/geoclue-test-gui

#--------------------------------------------------------------------

%package gypsy
Summary: gypsy provider for geoclue
Group: Geography
Requires: %{name} = %{version}-%{release}
Obsoletes: %{oname}-gypsy < 0.12.99-4

%description gypsy
A gypsy provider for geoclue

%files gypsy
%{_libexecdir}/geoclue-gypsy
%{_datadir}/geoclue-providers/geoclue-gypsy.provider
%{_datadir}/dbus-1/services/org.freedesktop.Geoclue.Providers.Gypsy.service

#--------------------------------------------------------------------

%package gpsd
Summary: gpsd provider for geoclue
Group: Geography
Conflicts: geoclue < 0.12.99-2
Requires: %{name} = %{version}-%{release}
Obsoletes: %{oname}-gpsd < 0.12.99-4

%description gpsd
A gpsd provider for geoclue

%files gpsd
%{_libexecdir}/geoclue-gpsd
%{_datadir}/geoclue-providers/geoclue-gpsd.provider
%{_datadir}/dbus-1/services/org.freedesktop.Geoclue.Providers.Gpsd.service

#--------------------------------------------------------------------

%package gsmloc
Summary: gsmloc provider for geoclue
Group: Geography
Requires: %{name} = %{version}-%{release}
Obsoletes: %{oname}-gsmloc < 0.12.99-4

%description gsmloc
A gsmloc provider for geoclue

%files gsmloc
%{_libexecdir}/geoclue-gsmloc
%{_datadir}/geoclue-providers/geoclue-gsmloc.provider
%{_datadir}/dbus-1/services/org.freedesktop.Geoclue.Providers.Gsmloc.service

#--------------------------------------------------------------------

%prep
%setup -q -n %{oname}-%{version}
%apply_patches

%build
%configure --disable-static
%make

%install
%makeinstall_std

#Remove libtool archives.
find %{buildroot} -name '*.la' -delete

# Install the test gui as it seems the test isn't installed any more
mkdir %{buildroot}%{_bindir}
cp test/.libs/geoclue-test-gui %{buildroot}%{_bindir}/
