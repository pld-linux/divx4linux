
%define stamp 20030428
Summary:	DivX MPEG-4 implementation
Summary(pl.UTF-8):	Implementacja DivX MPEG-4
Name:		divx4linux
Version:	5.05.%{stamp}
Release:	1
Epoch:		1
License:	restricted, non-distributable (DIVXNETWORKS EULA)
Group:		Libraries
Source0:	http://download.divx.com/divx/divx4linux-std-%{stamp}.tar.gz
# NoSource0-md5:	6332d98ad949a40c588681acbf4078f4
URL:		http://www.divx.com/
NoSource:	0
Obsoletes:	libdivxdecore
Obsoletes:	divx4linux5
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DivX MPEG-4 encoder and decoder.

%description -l pl.UTF-8
Enkoder i dekoder DivX MPEG-4.

%package devel
Summary:	DivX header files
Summary(pl.UTF-8):	Pliki nagłówkowe DivX
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}
Obsoletes:	libdivxdecore-devel
Obsoletes:	divx4linux5-devel

%description devel
Header files for DivX.

%description devel -l pl.UTF-8
Pliki nagłówkowe kodeka DivX.

%prep
%setup -q -n %{name}-%{stamp}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}/divx}

install *.so $RPM_BUILD_ROOT%{_libdir}
install *.h $RPM_BUILD_ROOT%{_includedir}/divx

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so

%files devel
%defattr(644,root,root,755)
%doc *.htm*
%{_includedir}/divx
