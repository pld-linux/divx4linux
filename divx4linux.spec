Summary:	MPEG-4 implementation
Summary(pl):	Implementacja dekodera MPEG-4
Name:		divx4linux
Version:	20010824
Release:	1
License:	DIVXNETWORKS Inc. End-user license
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	http://download.projectmayo.com/dnload/divx4linux/%{name}-%{version}.tgz
URL:		http://www.projectmayo.com/linux/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DivX MPEG-4 decoder

%package devel
Summary:	Header files
Summary(pl):	Pliki nag³ówkowe
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files

%description -l pl devel
Pliki nag³ówkowe

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_libdir}
install -d $RPM_BUILD_ROOT/%{_includedir}/divx
cp *.so $RPM_BUILD_ROOT/%{_libdir}
cp *.h $RPM_BUILD_ROOT/%{_includedir}/divx

gzip -9nf RELNOTES.linux "Codec Core Interface.txt" license.txt

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/*.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/divx/*.h
