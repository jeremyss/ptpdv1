Name:           ptpdv1
Version:        1.0.0
Release:        1%{?dist}
Summary:        PTP daemon

License:        GPL
URL:            https://sourceforge.net/p/ptpd/code/HEAD/tree/branches/v1/
Source0:        ptpdv1-1.0.0.tgz

#BuildRequires:  
#Requires:       

%description
PTPd can coordinate the clocks of a group of LAN connected computers with each
other. It has been shown to achieve microsecond level coordination, even on
limited platforms.

%prep
%setup -q

%build
cd src
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
#ls $RPM_BUILD_ROOT
cd src
#make install
cp ptpd $RPM_BUILD_ROOT/%{_bindir}

%files
/usr/bin/ptpd
%doc

%changelog
