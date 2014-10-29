%define major %(echo %{version}|cut -d. -f1,2)
%define iconname sylpheed.png

%define libapi 0
%define libmajor 1
%define libname %mklibname %{name} %libapi %libmajor
%define develname %mklibname -d %{name}

Summary:	A GTK+2 based, lightweight, and fast e-mail client
Name:		sylpheed
Version:	3.4.2
Release:	1
Source0:	http://sylpheed.sraoss.jp/sylpheed/v3.4/%{name}-%{version}.tar.bz2
License:	GPLv2
URL:		http://sylpheed.sraoss.jp/
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	gpgme-devel > 0.4.5
BuildRequires:	imagemagick
BuildRequires:	pkgconfig(pilot-link)
BuildRequires:	openldap-devel
BuildRequires:	pkgconfig(gtkspell-2.0)
Patch0:		sylpheed-3.3.0-glib2.patch
Requires:	curl
Group:		Networking/Mail
Provides:	sylpheed-main = %{version}-%{release}
Provides:	sylpheed2
Obsoletes:	sylpheed2

%description
This program is an X based fast e-mail client which has features
(or go for it :-)) like:
	o user-friendly and intuitive interface
	o integrated NetNews client (partially implemented)
	o ability of keyboard-only operation
	o Mew/Wanderlust-like key bind
	o multipart MIME
	o built-in image view
	o external editor support
	o unlimited multiple account handling
	o message queueing
	o filtering
	o XML-based address book
See 'README' for more information.

%package -n %libname
Summary: Library files for %name
Group: Networking/Mail

%description -n %libname
This package contains shared library files for %{name}.

%package -n %develname
Summary: Development files for %name
Group: Networking/Mail
Requires: %libname = %{version}
Provides: %{name}-devel = %{version}-%{release}

%description -n %develname
This package contains development files for %{name}.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%build
%configure2_5x --enable-gpgme \
		--enable-jpilot \
		--enable-ssl \
		--enable-ldap \
		--enable-ipv6

%make

%install
%makeinstall_std

mkdir -p %{buildroot}{%{_miconsdir},%{_iconsdir},%{_liconsdir}}
convert sylpheed.png -geometry 48x48 %{buildroot}%{_liconsdir}/%{iconname}
convert sylpheed.png -geometry 32x32 %{buildroot}%{_iconsdir}/%{iconname}
convert sylpheed.png -geometry 16x16 %{buildroot}%{_miconsdir}/%{iconname}

%{find_lang} %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog* NEWS README* INSTALL* TODO*
%{_bindir}/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/faq
%lang(de) %doc %{_datadir}/%{name}/faq/de
%lang(en) %doc %{_datadir}/%{name}/faq/en
%lang(es) %doc %{_datadir}/%{name}/faq/es
%lang(fr) %doc %{_datadir}/%{name}/faq/fr
%lang(it) %doc %{_datadir}/%{name}/faq/it
%dir %{_datadir}/%{name}/manual
%lang(en) %doc %{_datadir}/%{name}/manual/en
%lang(ja) %doc %{_datadir}/%{name}/manual/ja
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/%{name}.png
%{_iconsdir}/%{iconname}
%{_liconsdir}/%{iconname}
%{_miconsdir}/%{iconname}

%files -n %libname
%{_libdir}/*-%{libapi}.so.%{libmajor}
%{_libdir}/*-%{libapi}.so.%{libmajor}.*

%files -n %develname
%{_libdir}/*.so
%{_includedir}/%{name}
