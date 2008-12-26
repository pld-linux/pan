#
# Conditional build:
%bcond_without	gtkspell	# no spelling checker
#
Summary:	A USENET newsreader for GNOME
Summary(es.UTF-8):	Uno leitor USENET para el GNOME
Summary(pl.UTF-8):	Czytnik USENET dla GNOME
Summary(pt_BR.UTF-8):	Um leitor USENET para o GNOME
Name:		pan
Version:	0.133
Release:	1
Epoch:		1
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://pan.rebelbase.com/download/releases/%{version}/source/%{name}-%{version}.tar.bz2
# Source0-md5:	ca165da8557605d89d327cff78891b89
Patch0:		%{name}-desktop.patch
URL:		http://pan.rebelbase.com/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gmime22-devel >= 2.2.0
BuildRequires:	gtk+2-devel >= 2:2.4.0
%{?with_gtkspell:BuildRequires:	gtkspell-devel >= 2.0.7}
BuildRequires:	intltool >= 0.23
BuildRequires:	pcre-devel >= 5.0
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
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

sed -i -e 's#sr@Latn#sr@latin#' po/LINGUAS
mv -f po/sr@{Latn,latin}.po

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with%{!?with_gtkspell:out}-gtkspell

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/pan
%{_desktopdir}/pan.desktop
%{_pixmapsdir}/pan.png
