
%define stamp 20020418
Summary:	DivX MPEG-4 implementation
Summary(pl):	Implementacja DivX MPEG-4
Name:		divx4linux
Version:	5.01.%{stamp}
Release:	1
Epoch:		1
License:	DIVXNETWORKS Inc. End-user license
Group:		Libraries
Source0:	http://download.divx.com/divx/divx4linux501-%{stamp}.tgz
URL:		http://www.divx.com/
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libdivxdecore
Obsoletes:	divx4linux5

%description
DivX MPEG-4 encoder and decoder.

%description -l pl
Enkoder i dekoder DivX MPEG-4.

%package devel
Summary:	DivX header files
Summary(pl):	Pliki nag³ówkowe DivX
Group:		Development/Libraries
Requires:	%{name} = %{version}
Obsoletes:	libdivxdecore-devel
Obsoletes:	divx4linux5-devel

%description devel
Header files for DivX.

%description devel -l pl
Pliki nag³ówkowe kodeka DivX.

%prep
%setup -q -n %{name}-%{stamp}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}/divx}

install *.so $RPM_BUILD_ROOT%{_libdir}
install *.h $RPM_BUILD_ROOT%{_includedir}/divx

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README* license*
%attr(755,root,root) %{_libdir}/*.so

%files devel
%defattr(644,root,root,755)
%doc *.htm*
%{_includedir}/divx
