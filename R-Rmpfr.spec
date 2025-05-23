#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v26
# autospec commit: 99a7985
#
Name     : R-Rmpfr
Version  : 1.1.0
Release  : 73
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/Rmpfr_1.1-0.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/Rmpfr_1.1-0.tar.gz
Summary  : Interface R to MPFR - Multiple Precision Floating-Point Reliable
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-Rmpfr-lib = %{version}-%{release}
Requires: R-gmp
BuildRequires : R-gmp
BuildRequires : buildreq-R
BuildRequires : gmp-dev
BuildRequires : mpfr-dev

%description
arbitrary precision floating point numbers, including transcendental
  ("special") functions.  To this end, the package interfaces to
  the 'LGPL' licensed 'MPFR' (Multiple Precision Floating-Point Reliable) Library
  which itself is based on the 'GMP' (GNU Multiple Precision) Library.

%package lib
Summary: lib components for the R-Rmpfr package.
Group: Libraries

%description lib
lib components for the R-Rmpfr package.


%prep
%setup -q -n Rmpfr
pushd ..
cp -a Rmpfr buildavx2
popd
pushd ..
cp -a Rmpfr buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1747233188

%install
export SOURCE_DATE_EPOCH=1747233188
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
/usr/lib64/R/library/Rmpfr/DESCRIPTION
/usr/lib64/R/library/Rmpfr/INDEX
/usr/lib64/R/library/Rmpfr/Meta/Rd.rds
/usr/lib64/R/library/Rmpfr/Meta/demo.rds
/usr/lib64/R/library/Rmpfr/Meta/features.rds
/usr/lib64/R/library/Rmpfr/Meta/hsearch.rds
/usr/lib64/R/library/Rmpfr/Meta/links.rds
/usr/lib64/R/library/Rmpfr/Meta/nsInfo.rds
/usr/lib64/R/library/Rmpfr/Meta/package.rds
/usr/lib64/R/library/Rmpfr/Meta/vignette.rds
/usr/lib64/R/library/Rmpfr/NAMESPACE
/usr/lib64/R/library/Rmpfr/NEWS.Rd
/usr/lib64/R/library/Rmpfr/R/Rmpfr
/usr/lib64/R/library/Rmpfr/R/Rmpfr.rdb
/usr/lib64/R/library/Rmpfr/R/Rmpfr.rdx
/usr/lib64/R/library/Rmpfr/check-tools.R
/usr/lib64/R/library/Rmpfr/demo/hjkMpfr.R
/usr/lib64/R/library/Rmpfr/doc/Maechler_useR_2011-abstr.R
/usr/lib64/R/library/Rmpfr/doc/Maechler_useR_2011-abstr.Rnw
/usr/lib64/R/library/Rmpfr/doc/Maechler_useR_2011-abstr.pdf
/usr/lib64/R/library/Rmpfr/doc/Rmpfr-pkg.R
/usr/lib64/R/library/Rmpfr/doc/Rmpfr-pkg.Rnw
/usr/lib64/R/library/Rmpfr/doc/Rmpfr-pkg.pdf
/usr/lib64/R/library/Rmpfr/doc/index.html
/usr/lib64/R/library/Rmpfr/doc/log1mexp-note.R
/usr/lib64/R/library/Rmpfr/doc/log1mexp-note.Rnw
/usr/lib64/R/library/Rmpfr/doc/log1mexp-note.pdf
/usr/lib64/R/library/Rmpfr/help/AnIndex
/usr/lib64/R/library/Rmpfr/help/Rmpfr.rdb
/usr/lib64/R/library/Rmpfr/help/Rmpfr.rdx
/usr/lib64/R/library/Rmpfr/help/aliases.rds
/usr/lib64/R/library/Rmpfr/help/paths.rds
/usr/lib64/R/library/Rmpfr/html/00Index.html
/usr/lib64/R/library/Rmpfr/html/R.css
/usr/lib64/R/library/Rmpfr/tests/arith-ex.R
/usr/lib64/R/library/Rmpfr/tests/binomial-etc.R
/usr/lib64/R/library/Rmpfr/tests/bit-repr.R
/usr/lib64/R/library/Rmpfr/tests/create.R
/usr/lib64/R/library/Rmpfr/tests/functionals.R
/usr/lib64/R/library/Rmpfr/tests/lowlevel.R
/usr/lib64/R/library/Rmpfr/tests/matrix-ex.R
/usr/lib64/R/library/Rmpfr/tests/special-fun-dgamma.R
/usr/lib64/R/library/Rmpfr/tests/special-fun-ex.R
/usr/lib64/R/library/Rmpfr/tests/tstHexBin.R

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/Rmpfr/libs/Rmpfr.so
/V4/usr/lib64/R/library/Rmpfr/libs/Rmpfr.so
/usr/lib64/R/library/Rmpfr/libs/Rmpfr.so
