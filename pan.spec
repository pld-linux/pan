Summary:	A USENET newsreader for GNOME
Name:		pan
Version:	0.7.5
Release:	1
License:	GPL
Group:		X11/GNOME
URL:		http://www.superpimp.org/
Source:		ftp://source.rebelbase.com/pub/pan/%{name}-%{version}.tar.gz
Patch:		%{name}-applnk.patch
BuildRoot:	/tmp/%{name}-%{version}-root
Requires:	gtk+ >= 1.2.6
Requires:	gnome-libs >= 1.0.16

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11/GNOME
%define		_localstatedir	/var
%define		_applnkdir	%{_datadir}/applnk

%description
This is version %{version} of PAN, the Pimp Ass Newsreader.  Its goal is to
make a user-friendly and powerful USENET newsreadre for GNOME.  Its user
interface is based loosely on popular newsreaders for Windows.  This is
alpha software, so don't expect everything to work correctly or even at
all.

%prep
%setup -q
%patch -p1
%build
automake
LDFLAGS="-s";export LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf README ChangeLog AUTHORS TODO COPYING CREDITS

%find_lang %{name}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {README,ChangeLog,AUTHORS,TODO,COPYING,CREDITS}.gz
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Networking/News/*

%clean
rm -r $RPM_BUILD_ROOT
