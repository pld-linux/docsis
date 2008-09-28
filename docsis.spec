Summary:	DOCSIS RFI 1.1 Encoding Configuration File Settings into binary configuration files
Summary(pl.UTF-8):	Kodowanie ustawień konfiguracyjnych w plikach binarnych wg DOCSIS RFI 1.1
Name:		docsis
Version:	0.9.5
Release:	2
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/docsis/%{name}-%{version}.tar.gz
# Source0-md5:	2b89cf254a5eb07b0ee8b6331238ea96
Patch0:		%{name}-gnu-m4-detect.patch
Patch1:		%{name}-link.patch
URL:		http://docsis.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool	
BuildRequires:	flex
BuildRequires:	net-snmp-devel
Requires:	net-snmp-mibs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Encoding Configuration File Settings into binary configuration files
as specified by the DOCSIS RFI 1.1.

%description -l pl.UTF-8
Kodowanie ustawień konfiguracyjnych w binarnych plikach
konfiguracyjnych zgodnie z DOCSIS RFI 1.1.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%{__autoheader}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/snmp/mibs/*
