Name: valkyrie
Version: 1.4.0
Release: %mkrel 1
Group: Development/Other
Summary: A Qt3 based GUI for the Valgrind 3.3.X
License: GPLv2+
URL: http://valgrind.org
Source0: http://valgrind.org/downloads/valkyrie-1.4.0.tar.bz2
Patch0: valkyrie-1.4.0-qt3-build.patch
BuildRequires: qt3-devel
BuildRequires: valgrind
BuildRoot: %{_tmppath}/{%name}-buildroot

%description
A Qt3 based GUI for the Valgrind 3.3.X.

%files
%defattr(-,root,root)
%_bindir/*
%_datadir/*

#-------------------------------------------------------------------

%prep
%setup -q 
%patch0 -p0 -b .orig

%build
QTDIR=%{qt3dir}
export QTDIR

%configure_qt3 \
	--with-Qt-lib-dir=%{qt3lib}

%make

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

