Summary:	A USENET newsreader for GNOME
Summary(es):	Uno leitor USENET para el GNOME
Summary(pl):	Czytnik USENET dla GNOME
Summary(pt_BR):	Um leitor USENET para o GNOME
Name:		pan
Version:	0.14.2
Release:	1
Epoch:		1
License:	GPL v2
Group:		X11/Applications
Source0:	http://pan.rebelbase.com/download/releases/%{version}/SOURCE/%{name}-%{version}.tar.bz2
# Source0-md5:	ed3188e7059bb6d6c209ee5d46ac1852
Patch0:		%{name}-desktop.patch
URL:		http://pan.rebelbase.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	aspell-devel
BuildRequires:	bison
BuildRequires:	gettext-devel
BuildRequires:	gnet-devel >= 2.0.1
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	gtkspell-devel >= 2.0.2
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.4.24
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PAN is Pimp Ass Newsreader. Its goal is to make a user-friendly and
powerful USENET newsreader for GNOME. Its user interface is based
loosely on popular newsreaders for Windows. This is alpha software, so
don't expect everything to work correctly or even at all.

%description -l es
Pan is a powerful and easy newsreader for GNOME. It has many features
for easy reading and posting, displaying and saving attachments, and
offline newsreading. It is also the only Unix newsreader to receive a
perfect score

%description -l pl
Celem programu PAN jest umo�liwienie u�ytkownikowi prostego i
efektywnego czytania wiadomo�ci USENET w �rodowisku GNOME. Interfejs
u�ytkownika jest podobny do tych znanych z Windows.

%description -l pt_BR
Pan � um leitor de Usenet News f�cil e poderoso para o GNOME Ele tem
muitas caracter�sticas que facilitam ler e postar, mostrando e
salvando anexos e leitura "offline".

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__libtoolize}
glib-gettextize -c -f
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-gtkspell

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Productivitydir=%{_desktopdir}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ANNOUNCE.html AUTHORS ChangeLog CREDITS NEWS README TODO docs/*.html
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
