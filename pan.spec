Summary:	A USENET newsreader for GNOME
Summary(es):	Uno leitor USENET para el GNOME
Summary(pl):	Czytnik USENET dla GNOME
Summary(pt_BR):	Um leitor USENET para o GNOME
Name:		pan
Version:	0.11.0.92
Release:	2
Epoch:		1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	http://pan.rebelbase.com/download/%{version}/SOURCE/%{name}-%{version}.tar.bz2
Patch0:		%{name}-ac_fix.patch
URL:		http://www.superpimp.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	gal-devel >= 0.19
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel >= 1.0.16
BuildRequires:	gtk+-devel >= 1.2.6
BuildRequires:	gtkhtml-devel >= 0.16
BuildRequires:	libtool
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

%description -l es
Pan is a powerful and easy newsreader for GNOME. It has many features
for easy reading and posting, displaying and saving attachments, and
offline newsreading. It is also the only Unix newsreader to receive a
perfect score

%description -l pl
Celem programu PIM jest umo¿liwienie u¿ytkownikowi prostego i
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
sed -e s/AM_GNOME_GETTEXT/AM_GNU_GETTEXT/ configure.in > configure.in.tmp
mv -f configure.in.tmp configure.in
rm -f missing
libtoolize --copy --force
gettextize --copy --force
aclocal
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
