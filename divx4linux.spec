Summary:	MPEG-4 implementation
Summary(pl):	Implementacja MPEG-4
Name:		divx4linux
Version:	20020304
Release:	1
License:	DIVXNETWORKS Inc. End-user license
Group:		Libraries
#Source0:	http://download.projectmayo.com/dnload/divx4linux/%{name}-%{version}.tgz
Source0:	http://avifile.sourceforge.net/%{name}-%{version}.tgz
URL:		http://www.projectmayo.com/projects/detail.php?projectId=4
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libdivxdecore

%description
DivX MPEG-4 decoder and encoder.

%description -l pl
Dekoder i koder MPEG-4 DivX.

%package devel
Summary:	DivX header files
Summary(pl):	Pliki nag³ówkowe DivX
Group:		Development/Libraries
Requires:	%{name} = %{version}
Obsoletes:	libdivxdecore-devel

%description devel
Header files for libdivxdecore/libdivxencore.

%description -l pl devel
Pliki nag³ówkowe libdivxdecore/libdivxencore.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}/divx}

install *.so $RPM_BUILD_ROOT%{_libdir}
install *.h $RPM_BUILD_ROOT%{_includedir}/divx

gzip -9nf RELNOTES.linux license.txt

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc {RELNOTES.linux,license.txt}.gz
%attr(755,root,root) %{_libdir}/*.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/divx
