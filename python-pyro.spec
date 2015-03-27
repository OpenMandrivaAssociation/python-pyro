Name:           python-pyro
URL:            http://pyro.sourceforge.net/
Summary:        PYthon Remote Objects
Version:        4.27
Release:        1
License:        MIT
Group:          Development/Python
Source:         https://pypi.python.org/packages/source/P/Pyro4/Pyro4-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:  python-devel

%description
Pyro provides an object-oriented form of RPC. You can use Pyro within a
single system but also use it for IPC. For those that are familiar with
Java, Pyro resembles Java's Remote Method Invocation (RMI). It is less
similar to CORBA - which is a system- and language independent Distributed
Object Technology and has much more to offer than Pyro or RMI.

%prep
%setup -q -n Pyro-%{version}

%build
python setup.py build

%install
[ -d %{buildroot} -a "%{buildroot}" != "" ] && rm -rf %{buildroot}
echo n | python setup.py install --root=%{buildroot}

mkdir -p %{buildroot}%{_bindir}
install -m 0755 bin/* %{buildroot}%{_bindir}

%clean
[ -d %{buildroot} -a "%{buildroot}" != "" ] && rm -rf  %{buildroot}

%files
%doc docs/* README.txt
%{_bindir}/*
%{py_puresitedir}/*
