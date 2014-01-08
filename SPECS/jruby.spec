Name: jruby
Version: 1.7.9
Release: 1%{?dist}
License: EPL/GPL/LGPL
Group: Development/Languages
URL: http://jruby.org
Summary: A Java implementation of the Ruby language
Source0:  http://jruby.org.s3.amazonaws.com/downloads/%{version}/%{name}-bin-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: java-1.7.0-openjdk
%description: jruby
A Java implementation of the Ruby language

%prep

%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/opt
mkdir -p $RPM_BUILD_ROOT/%{_docdir}/%{name}
cp -r  $RPM_BUILD_DIR/%{name}-%{version} $RPM_BUILD_ROOT/opt/jruby
cp -r $RPM_BUILD_DIR/%{name}-%{version}/docs/* $RPM_BUILD_ROOT/%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc %{_docdir}/%{name}
/opt/jruby
/usr/bin

%changelog
* Wed Jan 8 2014 Simon Thulbourn <simon.thulbourn@bbc.co.uk> 1.7.9-1
- Initial release
