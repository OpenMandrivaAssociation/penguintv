%define name	penguintv
%define version 3.0
%define release %mkrel 3

Name: 	 	%{name}
Summary: 	Media-rich RSS reader
Version: 	%{version}
Release: 	%{release}

Source:		http://prdownloads.sourceforge.net/penguintv/PenguinTV-%{version}.tar.gz
URL:		http://penguintv.sourceforge.net/
License:	GPL
Group:		Networking/News
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	python-devel 
BuildRequires:	pygtk2.0 pygtk2.0-libglade pygtk2.0-devel
BuildRequires:	python-sqlite2 python-curl
BuildRequires:	gnome-python-gtkhtml2
BuildRequires:  gnome-python gnome-python-gnomevfs
BuildRequires:	python-pyxml
BuildRequires:	ImageMagick
BuildRequires:	desktop-file-utils
BuildRequires:	gnome-python-gtkmozembed python-gnome-devel
Requires:	pygtk2.0 pygtk2.0-libglade
Requires:	python-sqlite2 python-curl
Requires:	gnome-python-gtkhtml2
Requires:	gnome-python gnome-python-gnomevfs
Requires:	python-pyxml
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
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_prefix}
python setup.py install --prefix=$RPM_BUILD_ROOT%{_prefix}
#cp %buildroot/%{_datadir}/pixmaps/* %buildroot/%{_datadir}/%name

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 share/penguintvicon.png $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 share/penguintvicon.png $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 share/penguintvicon.png $RPM_BUILD_ROOT/%_miconsdir/%name.png

desktop-file-install --vendor="" \
--remove-category="Application" \
--add-category="X-MandrivaLinux-Network;News" \
--dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

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
%{_datadir}/%name
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{py_sitedir}/%name
%{py_sitedir}/*.egg-info
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png
