Name:           python-pyro
URL:            http://pyro.sourceforge.net/
Summary:        PYthon Remote Objects
Version:        4.79
Release:        1
License:        MIT
Group:          Development/Python
Source:         http://downloads.sourceforge.net/pyro/Pyro4-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-${release}-root
BuildArch:	noarch
BuildRequires:  python-sphinx_rtd_theme
BuildRequires:	python-sphinx
%py_requires -d

%description
Pyro provides an object-oriented form of RPC. You can use Pyro within a
single system but also use it for IPC. For those that are familiar with
Java, Pyro resembles Java's Remote Method Invocation (RMI). It is less
similar to CORBA - which is a system- and language independent Distributed
Object Technology and has much more to offer than Pyro or RMI.

%prep 
%setup -q -n Pyro4-%{version}

%build
%{__python} setup.py build
pushd docs
make html
popd

%install
[ -d %{buildroot} -a "%{buildroot}" != "" ] && rm -rf %{buildroot}
echo n | %{__python} setup.py install --root=%{buildroot}

mkdir -p %{buildroot}%_bindir
mkdir -p %{buildroot}%{_docdir}/%{name}
install -m 0644 build/sphinx/html/*.html %{buildroot}%{_docdir}/%{name}/
install -m 0644 build/sphinx/html/searchindex.js %{buildroot}%{_docdir}/%{name}/
install -m 0644 build/sphinx/html/objects.inv %{buildroot}%{_docdir}/%{name}/

%files
%defattr(-,root,root)
%doc  README.md
%_bindir/*
%{_docdir}/*
%py_puresitedir/*


