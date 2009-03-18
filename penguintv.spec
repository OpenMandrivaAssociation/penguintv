%define name	penguintv
%define version 4.0.0
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	Media-rich RSS reader
Version: 	%{version}
Release: 	%{release}

Source:		http://prdownloads.sourceforge.net/penguintv/PenguinTV-%{version}.tar.gz
URL:		http://penguintv.sourceforge.net/
License:	GPLv2+
Group:		Networking/News
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	python-devel 
BuildRequires:	pygtk2.0 pygtk2.0-libglade pygtk2.0-devel
BuildRequires:	python-sqlite2 python-curl
BuildRequires:	gnome-python-gtkhtml2
BuildRequires:  gnome-python gnome-python-gnomevfs
BuildRequires:	python-pyxml python-imaging
BuildRequires:	imagemagick
BuildRequires:	desktop-file-utils
BuildRequires:	gnome-python-gtkmozembed gnome-python-devel
Requires:	pygtk2.0 pygtk2.0-libglade
Requires:	python-sqlite2 python-curl
Requires:	gnome-python-gtkhtml2
Requires:	gnome-python gnome-python-gnomevfs
Requires:	python-pyxml python-imaging
BuildArch:	noarch

%description
PenguinTV is not just another RSS feed reader. It is designed from the ground
up to work seamlessly with podcasts and video blogs (even as torrents),
allowing you to easily enjoy the audio, music, and video published around the
web in RSS format.

%prep
%setup -q -n PenguinTV-%version
perl -p -i -e 's|import sqlite|import pysqlite2||g' penguintv/__init__.py

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_prefix}
python setup.py install --prefix=%{buildroot}%{_prefix}


desktop-file-install --vendor="" \
--remove-category="Application" \
--add-category="X-MandrivaLinux-Network;News" \
--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%find_lang %name

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc CONTRIBUTORS LICENSE MANIFEST PKG-INFO README
%{_bindir}/PenguinTV
%{_datadir}/dbus-1/services/penguintv.service
%{_datadir}/%name
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{py_sitedir}/%name
%{py_sitedir}/*.egg-info
%{_iconsdir}/hicolor/*/*/penguintvicon.png

