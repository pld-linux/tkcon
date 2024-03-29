Summary:	Enhanced Tk console
Summary(pl.UTF-8):	Rozszerzona konsola Tk
Name:		tkcon
Version:	2.4
Release:	1
License:	distributable
Group:		Development/Languages/Tcl
Source0:	http://dl.sourceforge.net/tkcon/%{name}-%{version}.tar.gz
# Source0-md5:	415905fe3d81aa957f9c4424c219784e
URL:		http://tkcon.sourceforge.net/
Requires:	tk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tkcon is a replacement for the standard console that comes with Tk (on
Windows/Mac, but also works on Unix). The console itself provides many
more features than the standard console.

%description -l pl.UTF-8
Tkcon jest odpowiednikiem standardowej konsoli Tk (dostępnej domyślnie
w systemach Windows i Macintosh - ta działa także w systemach
uniksowych), o wiele większej funkcjonalności.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -D tkcon.tcl $RPM_BUILD_ROOT%{_bindir}/tkcon

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt release.txt ChangeLog index.html docs
%attr(755,root,root) %{_bindir}/tkcon
