#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-Rmpfr
Version  : 0.8.5
Release  : 45
URL      : https://cran.r-project.org/src/contrib/Rmpfr_0.8-5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/Rmpfr_0.8-5.tar.gz
Summary  : R MPFR - Multiple Precision Floating-Point Reliable
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-Rmpfr-lib = %{version}-%{release}
Requires: R-gmp
Requires: R-polynom
Requires: R-sfsmisc
BuildRequires : R-gmp
BuildRequires : R-polynom
BuildRequires : R-sfsmisc
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
%setup -q -c -n Rmpfr
cd %{_builddir}/Rmpfr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1633535658

%install
export SOURCE_DATE_EPOCH=1633535658
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Rmpfr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Rmpfr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Rmpfr
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc Rmpfr || :


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
/usr/lib64/R/library/Rmpfr/tests/bit-repr.Rout.save
/usr/lib64/R/library/Rmpfr/tests/create.R
/usr/lib64/R/library/Rmpfr/tests/functionals.R
/usr/lib64/R/library/Rmpfr/tests/lowlevel.R
/usr/lib64/R/library/Rmpfr/tests/matrix-ex.R
/usr/lib64/R/library/Rmpfr/tests/special-fun-ex.R
/usr/lib64/R/library/Rmpfr/tests/tstHexBin.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/Rmpfr/libs/Rmpfr.so
/usr/lib64/R/library/Rmpfr/libs/Rmpfr.so.avx2
/usr/lib64/R/library/Rmpfr/libs/Rmpfr.so.avx512
