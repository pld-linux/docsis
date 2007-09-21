Summary:	Enconding Configuration File Settings into binary configuration files as specified by the DOCSIS RFI 1.1
#Summary(pl.UTF-8):	-
Name:		docsis
Version:	0.9.5
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/docsis/%{name}-%{version}.tar.gz
# Source0-md5:	2b89cf254a5eb07b0ee8b6331238ea96
URL:		http://docsis.sourceforge.net/
Patch0:		%{name}-gnu-m4-detect.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex
BuildRequires:	net-snmp-devel
Requires:	net-snmp-mibs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Enconding Configuration File Settings into binary configuration files
as specified by the DOCSIS RFI 1.1.

#%description -l pl.UTF-8

%prep
%setup -q
%patch0 -p1

%build
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
