Name: 		valkyrie
Version:	2.0.0
Release:	2
Summary:	Qt4-based GUI for the Memcheck and Helgrind Valgrind tools
License: 	GPLv2+
Group: 		Development/Other
URL: 		https://valgrind.org/
# a411dfb803f548dae5f988de0160aeb5
Source0:	http://www.valgrind.org/downloads/%{name}-%{version}.tar.bz2

BuildRequires:	qt4-devel

Patch0:		valkyrie-2.0.0-doc-path.patch
Patch1:		valkyrie-2.0.0-editor.patch

%description
Valkyrie is a Qt4-based GUI for the Valgrind 3.6.x and 3.7.x series, that
works for the Memcheck and Helgrind tools. It also has an XML merging tool
for Memcheck outputs (vk_logmerge). This tarball is known to build and work
with valgrind-3.6.0 and valgrind-3.7.0.

%prep
%setup -q

%patch0 -p1
%patch1 -p1

%build
qmake PREFIX=%{_prefix}
%make

%install
%make INSTALL_ROOT=%{buildroot} install
mkdir -p %{buildroot}%{_docdir}
mv -f %{buildroot}%{_datadir}/%{name}-%{version}/doc %{buildroot}%{_docdir}/%{name}

%files
%{_bindir}/valkyrie
%doc %{_docdir}/%{name}
