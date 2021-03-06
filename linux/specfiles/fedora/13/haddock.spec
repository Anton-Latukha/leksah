%global pkg_name haddock

%global common_summary Haskell %{pkg_name} library

%global common_description  A documentation-generation tool for Haskell libraries

%global ghc_pkg_deps ghc-ghc-paths-devel,ghc-ghc-devel

%bcond_with shared

# debuginfo is not useful for ghc
%global debug_package %{nil}

Name:           %{pkg_name}
Version:        2.7.2
Release:        1%{?dist}
Summary:        Haskell %{pkg_name}

Group:          System Environment/Libraries
License:        BSD3
URL:            http://hackage.haskell.org/cgi-bin/hackage-scripts/package/%{name}
Source0:        http://hackage.haskell.org/packages/archive/%{name}/%{version}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
# fedora ghc archs:
ExclusiveArch:  %{ix86} x86_64 ppc alpha
BuildRequires:  ghc, ghc-rpm-macros >= 0.5.1
BuildRequires:  ghc-doc
BuildRequires:  ghc-prof
%{?ghc_pkg_deps:BuildRequires:  %{ghc_pkg_deps}, %(echo %{ghc_pkg_deps} | sed -e "s/\(ghc-[^, ]\+\)-devel/\1-doc,\1-prof/g")}

%description
%{common_description}

%ghc_lib_package

%prep
%setup -q

%build
%cabal_configure --ghc -p
%cabal build
%cabal haddock

%install
%cabal_install
%cabal_pkg_conf
mv $RPM_BUILD_ROOT/%{_bindir}/haddock $RPM_BUILD_ROOT/%{_bindir}/leksah-haddock

%ghc_gen_filelists

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc LICENSE
%attr(755,root,root) %{_bindir}/leksah-haddock
%attr(755,root,root) %{_datadir}/%{name}-%{version}/html

%changelog
* Fri May 28 2010 Fedora Haskell SIG <haskell-devel@lists.fedoraproject.org> - 2.7.2-0
- initial packaging for Fedora automatically generated by cabal2spec-0.21.3
