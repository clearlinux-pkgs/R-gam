#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v19
# autospec commit: f35655a
#
Name     : R-gam
Version  : 1.22.5
Release  : 64
URL      : https://cran.r-project.org/src/contrib/gam_1.22-5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/gam_1.22-5.tar.gz
Summary  : Generalized Additive Models
Group    : Development/Tools
License  : GPL-2.0
Requires: R-gam-lib = %{version}-%{release}
Requires: R-foreach
BuildRequires : R-foreach
BuildRequires : buildreq-R

%description
# gam
gam repo

%package lib
Summary: lib components for the R-gam package.
Group: Libraries

%description lib
lib components for the R-gam package.


%prep
%setup -q -n gam
pushd ..
cp -a gam buildavx2
popd
pushd ..
cp -a gam buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1726238045

%install
export SOURCE_DATE_EPOCH=1726238045
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/gam/DESCRIPTION
/usr/lib64/R/library/gam/INDEX
/usr/lib64/R/library/gam/Meta/Rd.rds
/usr/lib64/R/library/gam/Meta/data.rds
/usr/lib64/R/library/gam/Meta/features.rds
/usr/lib64/R/library/gam/Meta/hsearch.rds
/usr/lib64/R/library/gam/Meta/links.rds
/usr/lib64/R/library/gam/Meta/nsInfo.rds
/usr/lib64/R/library/gam/Meta/package.rds
/usr/lib64/R/library/gam/NAMESPACE
/usr/lib64/R/library/gam/R/gam
/usr/lib64/R/library/gam/R/gam.rdb
/usr/lib64/R/library/gam/R/gam.rdx
/usr/lib64/R/library/gam/data/gam.data.RData
/usr/lib64/R/library/gam/data/gam.newdata.RData
/usr/lib64/R/library/gam/data/kyphosis.RData
/usr/lib64/R/library/gam/help/AnIndex
/usr/lib64/R/library/gam/help/aliases.rds
/usr/lib64/R/library/gam/help/gam.rdb
/usr/lib64/R/library/gam/help/gam.rdx
/usr/lib64/R/library/gam/help/paths.rds
/usr/lib64/R/library/gam/html/00Index.html
/usr/lib64/R/library/gam/html/R.css
/usr/lib64/R/library/gam/ratfor/backfit.r
/usr/lib64/R/library/gam/ratfor/backlo.r
/usr/lib64/R/library/gam/ratfor/linear.r
/usr/lib64/R/library/gam/ratfor/lo.r
/usr/lib64/R/library/gam/ratfor/splsm.r
/usr/lib64/R/library/gam/tests/testthat.R
/usr/lib64/R/library/gam/tests/testthat/test_example.R
/usr/lib64/R/library/gam/tests/testthat/test_results/gam-1.20-results.RDS

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/gam/libs/gam.so
/V4/usr/lib64/R/library/gam/libs/gam.so
/usr/lib64/R/library/gam/libs/gam.so
