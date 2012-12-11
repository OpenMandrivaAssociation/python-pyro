Name:           python-pyro
URL:            http://pyro.sourceforge.net/
Summary:        PYthon Remote Objects
Version:        3.10
Release:        %mkrel 3
License:        MIT
Group:          Development/Python
Source:         http://downloads.sourceforge.net/pyro/Pyro-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-${release}-root
BuildArch:	noarch
%py_requires -d

%description
Pyro provides an object-oriented form of RPC. You can use Pyro within a
single system but also use it for IPC. For those that are familiar with
Java, Pyro resembles Java's Remote Method Invocation (RMI). It is less
similar to CORBA - which is a system- and language independent Distributed
Object Technology and has much more to offer than Pyro or RMI.

%prep
%setup -q -n Pyro-%{version}

%build
%{__python} setup.py build

%install
[ -d %{buildroot} -a "%{buildroot}" != "" ] && rm -rf %{buildroot}
echo n | %{__python} setup.py install --root=%{buildroot}

mkdir -p %{buildroot}%_bindir
install -m 0755 bin/* %{buildroot}%_bindir

%clean
[ -d %{buildroot} -a "%{buildroot}" != "" ] && rm -rf  %{buildroot}

%files
%defattr(-,root,root)
%doc docs/* README.txt
%_bindir/*
%py_puresitedir/*


%changelog
* Sat Jan 29 2011 Guillaume Rousse <guillomovitch@mandriva.org> 3.10-3mdv2011.0
+ Revision: 633951
- rebuild for normalized python dependencies

* Sat Nov 06 2010 Funda Wang <fwang@mandriva.org> 3.10-2mdv2011.0
+ Revision: 594000
- rebuild for py2.7

* Mon Dec 21 2009 Lev Givon <lev@mandriva.org> 3.10-1mdv2010.1
+ Revision: 480711
- Update to 3.10.

* Sun Aug 23 2009 Lev Givon <lev@mandriva.org> 3.9.1-1mdv2010.0
+ Revision: 419984
- Update to 3.9.1.

* Mon Jan 12 2009 Funda Wang <fwang@mandriva.org> 3.8.1-1mdv2009.1
+ Revision: 328584
- import python-pyro


