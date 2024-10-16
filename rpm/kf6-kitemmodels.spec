%global  kf_version 6.6.0

Name:		kf6-kitemmodels
Version: 6.6.0
Release:	1%{?dist}
Summary:	KDE Frameworks 6 Tier 1 addon with item models

License:	CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only
URL:		https://invent.kde.org/frameworks/%{framework}
Source0: %{name}-%{version}.tar.bz2

BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	extra-cmake-modules >= %{version}
BuildRequires:	kf6-rpm-macros
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Qml)
BuildRequires:  qt6-qttools-devel

%description
KDE Frameworks 6 Tier 1 addon with item models.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	qt6-qtbase-devel
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
%autosetup -n %{name}-%{version}/upstream -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%files
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/kitemmodels.*
%{_kf6_libdir}/libKF6ItemModels.so.*
%{_kf6_qmldir}/org/kde/kitemmodels/

%files devel
%doc README.md
%license LICENSES/*.txt
%{_kf6_includedir}/KItemModels/
%{_kf6_libdir}/libKF6ItemModels.so
%{_kf6_libdir}/cmake/KF6ItemModels/
%{_qt6_docdir}/*.tags
 
%files doc
%{_qt6_docdir}/*.qch

