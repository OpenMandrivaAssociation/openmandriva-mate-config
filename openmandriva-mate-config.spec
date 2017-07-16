Summary:	Package containing distro specific configuration and gschema overrides
Name:		openmandriva-mate-config
Version:	1.18.0
Release:	2
License:	GPLv2+ and LGPLv2+
Group:		Graphical desktop/GNOME
Url:		https://abf.io/openmandriva/
Source0:	https://abf.io/openmandriva/mate-openmandriva.gschema.override
Source1:	https://abf.io/openmandriva/openmandriva.layout
BuildArch:	noarch
Requires:	glib2.0-common

%description
This package contains distro specific configuration and gschema 
overrides for the MATE desktop.

%prep

%build

%install
install -d %{buildroot}%{_datadir}/glib-2.0/schemas
install -m 644 %{SOURCE0} %{buildroot}%{_datadir}/glib-2.0/schemas/
install -d %{buildroot}%{_datadir}/mate-panel/layouts
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/mate-panel/layouts/

%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%postun
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%files 
%{_datadir}/glib-2.0/schemas/mate-openmandriva.gschema.override
%{_datadir}/mate-panel/layouts/openmandriva.layout

