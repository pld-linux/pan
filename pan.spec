Summary:	A USENET newsreader for GNOME
Summary(pl):	Czytnik USENET dla GNOME
Name:		pan
Version:	0.9.4
Release:	1
License:	GPL
Group:		X11/GNOME
Group(pl):	X11/GNOME
Source0:	http://pan.rebelbase.com/download/%{version}/%{name}-%{version}.tar.bz2
URL:		http://www.superpimp.org/
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel >= 1.0.16
BuildRequires:	gtk+-devel >= 1.2.6
BuildRequires:	gtkhtml-devel
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
Celem programu PIM jest umo¿liwienie u¿ytkownikowi prostego i efektywnego
czytania wiadomo¶ci USENET w ¶rodowisku GNOME. Interfejs u¿ytkownika jest
podobny do tych znanych z Windows.

%prep
%setup -q

%build
gettextize --copy --force
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
