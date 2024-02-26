Summary:	Package containing distro specific configuration and gschema overrides
Name:		openmandriva-mate-config
Version:	1.28
Release:	1
License:	GPLv2+ and LGPLv2+
Group:		Graphical desktop/GNOME
Url:		https://www.openmandriva.org
Source0:	50_mate-openmandriva.gschema.override
Source1:	openmandriva.layout
BuildArch:	noarch

Requires:	glib2.0-common
Requires:	distro-release
Requires:	mate-themes

%description
This package contains distro specific configuration and gschema
overrides for the MATE desktop.

%files
%{_datadir}/glib-2.0/schemas/50_mate-openmandriva.gschema.override
%{_datadir}/mate-panel/layouts/openmandriva.layout

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

%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%postun
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

