Name:           python-pyro
URL:            https://pypi.org/project/Pyro4/
Summary:        PYthon Remote Objects
Version:        4.82
Release:        1
License:        MIT
Group:          Development/Python
Source:         https://files.pythonhosted.org/packages/source/P/Pyro4/Pyro4-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:  python-sphinx_rtd_theme
BuildRequires:	python-sphinx
%py_requires -d
Requires:	python

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
%_bindir/*
%{_docdir}/*
%py_puresitedir/*
