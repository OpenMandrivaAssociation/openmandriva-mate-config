Summary:	Package containing distro specific configuration and gschema overrides
Name:		openmandriva-mate-config
Version:	1.20.0
Release:	1
License:	GPLv2+ and LGPLv2+
Group:		Graphical desktop/GNOME
Url:		https://abf.io/openmandriva/
Source0:	https://abf.io/openmandriva/mate-openmandriva.gschema.override
Source1:	https://abf.io/openmandriva/openmandriva.layout
BuildArch:	noarch

Requires:	glib2.0-common
Requires:	distro-theme-OpenMandriva
Requires:	mate-themes

%description
This package contains distro specific configuration and gschema
overrides for the MATE desktop.

%files
%{_datadir}/glib-2.0/schemas/mate-openmandriva.gschema.override
%{_datadir}/mate-panel/layouts/openmandriva.layout

%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%postun
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

#----------------------------------------------------------------------------

%prep
# nothing to do here!

%build
# nothing to do here!

%install
# mate appearence
install -dm 0755 %{buildroot}%{_datadir}/glib-2.0/schemas/
install -pm 0644 %{SOURCE0} %{buildroot}%{_datadir}/glib-2.0/schemas/

# mate panel layout
install -dm 0755 %{buildroot}%{_datadir}/mate-panel/layouts/
install -pm 0644 %{SOURCE1} %{buildroot}%{_datadir}/mate-panel/layouts/
