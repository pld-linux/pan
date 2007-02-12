Summary:	A USENET newsreader for GNOME
Summary(es.UTF-8):   Uno leitor USENET para el GNOME
Summary(pl.UTF-8):   Czytnik USENET dla GNOME
Summary(pt_BR.UTF-8):   Um leitor USENET para o GNOME
Name:		pan
Version:	0.13.0
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	http://pan.rebelbase.com/download/releases/%{version}/SOURCE/%{name}-%{version}.tar.bz2
URL:		http://pan.rebelbase.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	bison
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2.0.6
#BuildRequires:	gtkspell-devel
BuildRequires:	libxml2-devel >= 2.4.24
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
PAN is Pimp Ass Newsreader. Its goal is to make a user-friendly and
powerful USENET newsreadre for GNOME. Its user interface is based
loosely on popular newsreaders for Windows. This is alpha software, so
don't expect everything to work correctly or even at all.

%description -l es.UTF-8
Pan is a powerful and easy newsreader for GNOME. It has many features
for easy reading and posting, displaying and saving attachments, and
offline newsreading. It is also the only Unix newsreader to receive a
perfect score

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

%build
#rm -f missing
#%{__libtoolize}
#%{__gettextize}
#aclocal
#%{__autoconf}
#%{__automake}
%configure
#	--enable-gtkspell
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
%doc README ChangeLog AUTHORS TODO CREDITS
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Network/News/*
%{_pixmapsdir}/*
