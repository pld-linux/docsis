Summary:	DOCSIS RFI 1.1 Encoding Configuration File Settings into binary configuration files
Summary(pl.UTF-8):	Kodowanie ustawień konfiguracyjnych w plikach binarnych wg DOCSIS RFI 1.1
Name:		docsis
Version:	0.9.6
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://downloads.sourceforge.net/docsis/%{name}-%{version}.tar.bz2
# Source0-md5:	fd431046f04b10fe8e46c4dd1c178b58
Patch0:		%{name}-link.patch
Patch1:		%{name}-no-common.patch
URL:		http://docsis.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.8
BuildRequires:	bison >= 1.28
BuildRequires:	flex
BuildRequires:	libtool
BuildRequires:	m4
BuildRequires:	net-snmp-devel >= 5.0.7
Requires:	mibs-%{name} = %{version}-%{release}
Requires:	net-snmp-libs >= 5.0.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Encoding Configuration File Settings into binary configuration files
as specified by the DOCSIS RFI 1.1.

%description -l pl.UTF-8
Kodowanie ustawień konfiguracyjnych w binarnych plikach
konfiguracyjnych zgodnie z DOCSIS RFI 1.1.

%package -n mibs-%{name}
Summary:	MIBs from DOCSIS
Summary(pl.UTF-8):	MIB-y z DOCSIS
Group:		Base
Requires:	mibs-dirs
Requires:	mibs-net-snmp

%description -n mibs-%{name}
MIB (Management Information Base) files from DOCSIS.

%description -n mibs-%{name} -l pl.UTF-8
Pliki MIB (Management Information Base) z DOCSIS.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	mibsdir=%{_datadir}/mibs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/docsis
%{_datadir}/%{name}

%files -n mibs-%{name}
%defattr(644,root,root,755)
%{_datadir}/mibs/CLAB-DEF-MIB
%{_datadir}/mibs/DIFFSERV-DSCP-TC
%{_datadir}/mibs/DIFFSERV-MIB
%{_datadir}/mibs/DOCS-BPI-MIB
%{_datadir}/mibs/DOCS-BPI2-MIB
%{_datadir}/mibs/DOCS-CABLE-DEVICE-MIB
%{_datadir}/mibs/DOCS-CABLE-DEVICE-TRAP-MIB
%{_datadir}/mibs/DOCS-IF-EXT-MIB
%{_datadir}/mibs/DOCS-IF-MIB
%{_datadir}/mibs/DOCS-QOS-MIB
%{_datadir}/mibs/DOCS-SUBMGT-MIB
%{_datadir}/mibs/IGMP-STD-MIB
%{_datadir}/mibs/INTEGRATED-SERVICES-MIB
%{_datadir}/mibs/PKTC-EVENT-MIB
%{_datadir}/mibs/PKTC-IETF-SIG-MIB
%{_datadir}/mibs/PKTC-MTA-MIB
%{_datadir}/mibs/PKTC-SIG-MIB
%{_datadir}/mibs/RMON2-MIB
%{_datadir}/mibs/TOKEN-RING-RMON-MIB
