Summary:	A USENET newsreader for GNOME
Summary(pl):	Czytnik USENET dla GNOME
Name:		pan
Version:	0.9.6
Release:	4
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	http://pan.rebelbase.com/download/%{version}/%{name}-%{version}.tar.bz2
Patch0:		%{name}-use_AM_GNU_GETTEXT.patch
URL:		http://www.superpimp.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel >= 1.0.16
BuildRequires:	gtk+-devel >= 1.2.6
BuildRequires:	gtkhtml-devel >= 0.9.2
BuildRequires:	libtool
BuildRequires:	bison
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11/GNOME
%define		_localstatedir	/var

%description
PAN is Pimp Ass Newsreader. Its goal is to make a user-friendly and
powerful USENET newsreadre for GNOME. Its user interface is based
loosely on popular newsreaders for Windows. This is alpha software, so
don't expect everything to work correctly or even at all.

%description -l pl
Celem programu PIM jest umożliwienie użytkownikowi prostego i
efektywnego czytania wiadomości USENET w środowisku GNOME. Interfejs
użytkownika jest podobny do tych znanych z Windows.

%prep
%setup -q
%patch -p1

%build
rm missing
libtoolize --copy --force
gettextize --copy --force
aclocal -I macros
autoconf
automake -a -c
%configure \
	--enable-html \
	--with-gnome
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Productivitydir=%{_applnkdir}/Network/News

gzip -9nf README ChangeLog AUTHORS TODO CREDITS

%find_lang %{name} --with-gnome

%clean
rm -r $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Network/News/*
%{_pixmapsdir}/*
