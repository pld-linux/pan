Summary:	A USENET newsreader for GNOME
Summary(es):	Uno leitor USENET para el GNOME
Summary(pl):	Czytnik USENET dla GNOME
Summary(pt_BR):	Um leitor USENET para o GNOME
Name:		pan
Version:	0.11.4
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	http://pan.rebelbase.com/download/releases/%{version}/SOURCE/%{name}-%{version}.tar.bz2
# Source0-md5:	22993c47af617086b34211f707a84ace
Patch0:		%{name}-from-overflow.patch
URL:		http://pan.rebelbase.com/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	gdk-pixbuf-devel >= 0.10.1
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel >= 1.0.16
BuildRequires:	gtk+-devel >= 1.2.10
BuildRequires:	libtool
BuildRequires:	libxml-devel >= 1.8.17
Requires:	gdk-pixbuf >= 0.10.1
Requires:	gnome-libs >= 1.0.16
Requires:	gtk+ >= 1.2.10
Requires:	libxml >= 1.8.17
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
Celem programu PAN jest umo¿liwienie u¿ytkownikowi prostego i
efektywnego czytania wiadomo¶ci USENET w ¶rodowisku GNOME. Interfejs
u¿ytkownika jest podobny do tych znanych z Windows.

%description -l pt_BR
Pan é um leitor de Usenet News fácil e poderoso para o GNOME Ele tem
muitas características que facilitam ler e postar, mostrando e
salvando anexos e leitura "offline".

%prep
%setup -q
%patch0 -p1

%build
sed -e 's/AM_GNOME_GETTEXT/AM_GNU_GETTEXT/' configure.in | \
	grep -v '^ *po/Makefile\.in$' > configure.in.tmp
mv -f configure.in.tmp configure.in
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
%configure \
	--enable-html \
	--with-gnome
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Productivitydir=%{_applnkdir}/Network/News

%find_lang %{name} --with-gnome

%clean
rm -r $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Network/News/*
%{_pixmapsdir}/*
