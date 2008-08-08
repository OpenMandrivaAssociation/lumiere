%define name 	lumiere
%define version 0.4
%define release %mkrel 14

Name: 		%{name}
Summary: 	Capable, customizable, embeddable video player for GNOME2
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://www.nongnu.org/lumiere
License:	GPL
Group:		Video
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	mplayer
BuildRequires:	gob2
BuildRequires:	libxine-devel >= 1 
BuildRequires:  libgnomeui2-devel libmesaglu-devel
BuildRequires:  gtkglarea2-devel libglade2.0-devel freetype2-static-devel desktop-file-utils

%description
Lumiere is a GNOME frontend to mplayer the great movie player for *nix. and to
libxine from the xine project.  It includes full support for bonobo control,
a CORBA server for handling video files, and Nautilus View integrates lumiere
inside Nautilus.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
rm -fr $RPM_BUILD_ROOT/%{_sysconfdir}

#menu

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --remove-category="Multimedia" \
  --add-category="GNOME" \
  --add-category="AudioVideo;Video;Player" \
  --add-category="X-MandrivaLinux-Multimedia-Video" \
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
%doc README AUTHORS COPYING ChangeLog 
%{_bindir}/%name
%{_libdir}/bonobo/servers/*
%{_libdir}/lumiere-control
%{_libdir}/midentify
%{_datadir}/applications/%name.desktop
%{_datadir}/gnome-2.0/ui/*.xml
%{_datadir}/pixmaps/*
%{_datadir}/%name


