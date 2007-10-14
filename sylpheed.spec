%define major 2.4
%define iconname sylpheed.png

Summary:	A GTK+2 based, lightweight, and fast e-mail client
Name:		sylpheed
Version:	%{major}.7
Release:	%mkrel 1
Source0:	http://sylpheed.sraoss.jp/sylpheed/v%{major}/sylpheed-%{version}.tar.bz2
Source1:	http://sylpheed.sraoss.jp/sylpheed/v%{major}/sylpheed-%{version}.tar.bz2.asc
License:	GPLv2
URL:		http://sylpheed.sraoss.jp/
BuildRequires:	desktop-file-utils
BuildRequires:	gtk+2-devel
BuildRequires:	gpgme-devel > 0.4.5
BuildRequires:	imagemagick
BuildRequires:	libpilot-link-devel
BuildRequires:	openldap-devel
Group:		Networking/Mail
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Provides:	sylpheed-main = %version-%release
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

%prep
%setup -q -n %{name}-%{version}

%build 
%configure2_5x --enable-gpgme \
		--enable-jpilot \
		--enable-ssl \
		--enable-ldap \
		--enable-ipv6

%make

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

mkdir -p %{buildroot}{%{_miconsdir},%{_iconsdir},%{_liconsdir}}
convert sylpheed.png -geometry 48x48 %{buildroot}%{_liconsdir}/%{iconname}
convert sylpheed.png -geometry 32x32 %{buildroot}%{_iconsdir}/%{iconname}
convert sylpheed.png -geometry 16x16 %{buildroot}%{_miconsdir}/%{iconname}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --vendor='' \
	--dir=%buildroot%_datadir/applications \
	sylpheed.desktop

%{find_lang} %name
 
%post
%update_menus
 
%postun
%clean_menus  

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
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
%{_iconsdir}/%{iconname}
%{_liconsdir}/%{iconname}
%{_miconsdir}/%{iconname}
