%define major 2.4
%define iconname sylpheed.png

Summary:	A GTK+2 based, lightweight, and fast e-mail client
Name:		sylpheed
Version:	%{major}.3
Release:	%mkrel 1
Source0:	http://sylpheed.sraoss.jp/sylpheed/v%{major}/sylpheed-%{version}.tar.bz2
Source1:	http://sylpheed.sraoss.jp/sylpheed/v%{major}/sylpheed-%{version}.tar.bz2.asc
License:	GPL
URL:		http://sylpheed.good-day.net/
BuildRequires:	desktop-file-utils
BuildRequires:	gtk+2-devel
BuildRequires:	gpgme-devel > 0.4.5
BuildRequires:	imagemagick
BuildRequires:	libpilot-link-devel
BuildRequires:	openldap-devel
Group:		Networking/Mail
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Provides:	sylpheed-main
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
install -m 644 sylpheed.desktop $RPM_BUILD_ROOT%{_datadir}/applications

mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat > $RPM_BUILD_ROOT%{_menudir}/%{name} <<EOF
?package(%{name}):\
command="%{name}"\
icon="%{name}.png"\
title="Sylpheed"\
longtitle="A fast GTK+2 based Mail client"\
needs="x11"\
section="Internet/Mail" \
xdg="true"
EOF

desktop-file-install --vendor="" \
--remove-category="Application" \
--add-category="GTK" \
--add-category="X-MandrivaLinux-Internet-Mail" \
--dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*
 
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
%dir %{_datadir}/%{name}/*
%dir %{_datadir}/%{name}/*/*
%doc %dir %{_datadir}/%{name} 
%doc %dir %{_datadir}/%{name}/manual/*/*
%doc %{_datadir}/%{name}/faq/*/*.html  
%{_bindir}/* 
%{_datadir}/applications/*.desktop
%{_menudir}/*
%{_iconsdir}/%{iconname}
%{_liconsdir}/%{iconname}
%{_miconsdir}/%{iconname}

