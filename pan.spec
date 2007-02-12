#
# Conditional build:
%bcond_without	gtkspell	# no spelling checker
#
Summary:	A USENET newsreader for GNOME
Summary(es.UTF-8):   Uno leitor USENET para el GNOME
Summary(pl.UTF-8):   Czytnik USENET dla GNOME
Summary(pt_BR.UTF-8):   Um leitor USENET para o GNOME
Name:		pan
Version:	0.14.2.91
Release:	2
Epoch:		1
License:	GPL v2
Group:		X11/Applications
Source0:	http://pan.rebelbase.com/download/releases/%{version}/SOURCE/%{name}-%{version}.tar.bz2
# Source0-md5:	4770d899a1c1ba968ce96bc5aeb07b62
Patch0:		%{name}-po.patch
Patch1:		%{name}-intltool.patch
Patch2:		%{name}-gcc4.patch
URL:		http://pan.rebelbase.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	aspell-devel
BuildRequires:	bison
BuildRequires:	gettext-devel
BuildRequires:	gnet-devel >= 2.0.4
BuildRequires:	gtk+2-devel >= 2:2.2.0
%{?with_gtkspell:BuildRequires: gtkspell-devel >= 2.0.2}
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.4.24
BuildRequires:	pcre-devel >= 4.0
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PAN is Pimp Ass Newsreader. Its goal is to make a user-friendly and
powerful USENET newsreader for GNOME. Its user interface is based
loosely on popular newsreaders for Windows. This is alpha software, so
don't expect everything to work correctly or even at all.

%description -l pl.UTF-8
Celem programu PAN jest umożliwienie użytkownikowi prostego i
efektywnego czytania wiadomości USENET w środowisku GNOME. Interfejs
użytkownika jest podobny do tych znanych z Windows.

%description -l pt_BR.UTF-8
Pan é um leitor de Usenet News fácil e poderoso para o GNOME Ele tem
muitas características que facilitam ler e postar, mostrando e
salvando anexos e leitura "offline".

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

mv -f po/{no,nb}.po

%build
rm -f missing
%{__sed} -i 's,\(^ALL_LINGUAS=.*\)\(no\),\1nb,' configure.in
%{__aclocal}
%{__libtoolize}
glib-gettextize -c -f
intltoolize -c -f
%{__autoconf}
%{__automake}
%configure \
	--%{?with_gtkspell:enable}%{!?with_gtkspell:disable}-gtkspell

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

echo "Categories=GTK;Network;News;" >> pan.desktop
echo "# vi: encoding=utf-8" >> pan.desktop

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
