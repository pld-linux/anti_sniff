Summary:	AntiSniff is a new class of proactive security monitoring tool
Summary(pl.UTF-8):	AntiSniff jest narzędziem do szukania podsłuchujących komputerów
Name:		anti_sniff
Version:	1.1.2
Release:	3
License:	Very Restrictive
Group:		Applications/Networking
Source0:	http://www.securitysoftwaretech.com/antisniff/dist/%{name}_researchv1-1-2.tar.gz
# Source0-md5:	0f6d71b4515eefde182516a1c5e1bf66
URL:		http://www.securitysoftwaretech.com/antisniff/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Anti-Sniffer runs on a local ethernet segment and reports whether
machines are in promiscuous mode or not. It does this through a
variety of tests designed to tickle certain drivers, operating
systems, and hardware filtering.

%description -l pl.UTF-8
Antysniffer działa w lokalnym segmencie ethernetowym i sprawdza, czy
jakaś maszyna ma kartę sieciową w trybie promiscuous. Sprawdzanie
polega na przeprowadzeniu różnorodnych testów napisanych dla różnych
driverów, systemów operacyjnych i filtrów sprzętowych.

%prep
%setup -q -n %{name}

%build
%{__make} linux-all CFLAGS="%{rpmcflags} " CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install anti_sniffer arptest echotest etherpingtest icmptimetest \
	watchdnstest $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ANTI_SNIFFER_DOCS CREDITS DSL_NOTES LINUX_NOTES NOTES README TODO
%attr(755,root,root) %{_bindir}/*
