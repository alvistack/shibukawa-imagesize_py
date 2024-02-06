# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-imagesize
Epoch: 100
Version: 1.4.1
Release: 1%{?dist}
BuildArch: noarch
Summary: Getting image size from png/jpeg/jpeg2000/gif file
License: MIT
URL: https://github.com/shibukawa/imagesize_py/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
This module analyzes JPEG/JPEG 2000/PNG/GIF/TIFF/SVG/Netpbm image
headers and returns image size or DIP.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-imagesize
Summary: Getting image size from png/jpeg/jpeg2000/gif file
Requires: python3
Provides: python3-imagesize = %{epoch}:%{version}-%{release}
Provides: python3dist(imagesize) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-imagesize = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(imagesize) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-imagesize = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(imagesize) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-imagesize
This module analyzes JPEG/JPEG 2000/PNG/GIF/TIFF/SVG/Netpbm image
headers and returns image size or DIP.

%files -n python%{python3_version_nodots}-imagesize
%license LICENSE.rst
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-imagesize
Summary: Getting image size from png/jpeg/jpeg2000/gif file
Requires: python3
Provides: python3-imagesize = %{epoch}:%{version}-%{release}
Provides: python3dist(imagesize) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-imagesize = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(imagesize) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-imagesize = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(imagesize) = %{epoch}:%{version}-%{release}

%description -n python3-imagesize
This module analyzes JPEG/JPEG 2000/PNG/GIF/TIFF/SVG/Netpbm image
headers and returns image size or DIP.

%files -n python3-imagesize
%license LICENSE.rst
%{python3_sitelib}/*
%endif

%changelog
