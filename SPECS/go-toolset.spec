%global go_version 1.20.12

Name: go-toolset
Version: %{go_version}
Release: 1%{?dist}
Summary: Package that installs go-toolset
License: BSD and Public Domain

Requires: golang = %{go_version}
%ifarch x86_64
Requires: delve
%endif
ExcludeArch: %{ix86}

%description
This is the main package for go-toolset.

%files

%changelog
* Tue Dec 12 2023 David Benoit <dbenoit@redhat.com> - 1.20.12-1
- Update to Go 1.20.12
- Fix CVE-2023-39326
- Resolves: RHEL-19231

* Fri Oct 13 2023 David Benoit <dbenoit@redhat.com> - 1.20.10-1
- Update to Go 1.20.10
- Fix CVE-2023-39325
- Midstream patches
- Resolves: RHEL-12619

* Tue Aug 01 2023 Alejandro Sáez <asm@redhat.com> - 1.20.6-1
- Rebase to Go 1.20.6
- Resolves: rhbz#2226901

* Wed May 31 2023 Alejandro Sáez <asm@redhat.com> - 1.20.4-1
- Rebase to Go 1.20.4
- Resolves: rhbz#2204474

* Tue Apr 11 2023 David Benoit <dbenoit@redhat.com> - 1.20.3-1
- Rebase to Go 1.20.3
- Remove race archives
- Update static tests patches
- Resolves: rhbz#2185260

* Wed Dec 21 2022 David Benoit <dbenoit@redhat.com> - 1.19.4-1
- Rebase to Go 1.19.4
- Fix ppc64le linker issue
- Remove defunct patches
- Remove downstream generated FIPS mode patches
- Add golang-fips/go as the source for FIPS mode patches
- Resolves: rhbz#2144542

* Fri Oct 14 2022 Alejandro Sáez <asm@redhat.com> - 1.19.2-1
- Rebase to Go 1.19.2
- Resolves: rhbz#2132730

* Fri Sep 30 2022 Alejandro Sáez <asm@redhat.com> - 1.19.1-1
- Update Go to 1.19.1 and Delve to 1.9.1
- Resolves: rhbz#2131026

* Wed Jul 20 2022 David Benoit <dbenoit@redhat.com> - 1.18.4-1
- Update Go to version 1.18.4
- Resolves: rhbz#2109179

* Thu Jun 16 2022 David Benoit <dbenoit@redhat.com> - 1.18.2-1
- Update to Go 1.18.2
- Related: rhbz#2075162

* Wed Apr 13 2022 David Benoit <dbenoit@redhat.com> - 1.18.0-1
- Update Go to 1.18.0
- Resolves: rhbz#2075162

* Thu Feb 17 2022 David Benoit <dbenoit@redhat.com> - 1.17.7-1
- Rebase to Go 1.17.7
- Remove fips memory leak patch (fixed in tree)
- Resolves: rhbz#2015930

* Fri Dec 10 2021 David Benoit <dbenoit@redhat.com> - 1.17.5-1
- Rebase to Go 1.17.5
- Resolves: rhbz#2031112

* Fri Dec 03 2021 David Benoit <dbenoit@redhat.com> - 1.17.4-1
- Rebase Go to 1.17.4
- Add vdso_s390x_gettime patch
- Add remove_waitgroup_misuse_tests patch
- Related: rhbz#2014088
- Resolves: rhbz#2028570
- Resolves: rhbz#2022828
- Resolves: rhbz#2024686
- Resolves: rhbz#2028662

* Thu Oct 14 2021 Alejandro Sáez <asm@redhat.com> - 1.17.2-1
- Rebase to Go 1.17.2
- Rebase to Delve 1.7.2
- Resolves: rhbz#2014088

* Tue Aug 17 2021 David Benoit <dbenoit@redhat.com> - 1.16.7-1
- Rebase to Go 1.16.7
- Resolves: rhbz#1994079
- Add reject leading zeros patch
- Resolves: rhbz#1993314

* Wed Jul 21 2021 Derek Parker <deparker@redhat.com> - 1.16.6-2
- Fix TestBoringServerCurves failure when run by itself
- Resolves: rhbz#1976168

* Thu Jul 15 2021 David Benoit <dbenoit@redhat.com> - 1.16.6-1
- Rebase to go-1.16.6-1-openssl-fips
- Resolves: rhbz#1982281
- Addresses CVE-2021-34558

* Tue Jul 06 2021 Alejandro Sáez <asm@redhat.com> - 1.16.5-1
- Rebase to go 1.16.5
- Related: rhbz#1979677
- Related: rhbz#1968738
- Related: rhbz#1972420

* Wed May 26 2021 Alejandro Sáez <asm@redhat.com> - 1.16.4-1
- Rebase to go-1.16.4-1-openssl-fips
- Resolves: rhbz#1938071

* Wed Mar 17 2021 Alejandro Sáez <asm@redhat.com> - 1.16.1-1
- Rebase to 1.16.1
- Resolves: rhbz#1938071

* Fri Jan 22 2021 David Benoit <dbenoit@redhat.com> - 1.15.7-1
- Rebase to 1.15.7
- Resolves: rhbz#1870531
- Resolves: rhbz#1919261

* Tue Nov 24 2020 David Benoit <dbenoit@redhat.com> - 1.15.5-1
- Rebase to 1.15.5
- Resolves: rhbz#1898652
- Resolves: rhbz#1898660
- Resolves: rhbz#1898649

* Thu Nov 12 2020 David Benoit <dbenoit@redhat.com> - 1.15.3-1
- Rebase to 1.15.3
- fix x/text infinite loop
- Resolves: rhbz#1881539

* Fri Oct 23 2020 David Benoit <dbenoit@redhat.com> - 1.15.2-1
- Rebase to 1.15.2
- Related: rhbz#1870531
- Related: rhbz#1872622
- Related: rhbz#1888673
- Related: rhbz#1889437
- Related: rhbz#1891095

* Wed Sep 09 2020 Alejandro Sáez <asm@redhat.com> - 1.15.0-1
- Rebase to 1.15.0
- Related: rhbz#1870531

* Wed Aug 19 2020 Alejandro Sáez <asm@redhat.com> - 1.14.7-1
- Rebase to Go 1.14.7
- Resolves: rhbz#1820596
- Resolves: rbhz#1859442

* Tue Aug 04 2020 Alejandro Sáez <asm@redhat.com> - 1.14.6-1
- Rebase to Go 1.14.6
- Related: rhbz#1820596

* Fri Jun 26 2020 Alejandro Sáez <asm@redhat.com> - 1.14.4-1
- Rebase to Go 1.14.4
- Related: rhbz#1820596

* Mon Jun 15 2020 Alejandro Sáez <asm@redhat.com> - 1.14.2-4
- Delve is only available on x86_64 at the moment
- Resolves: rhbz#1837847

* Fri Jun 05 2020 Alejandro Sáez <asm@redhat.com> - 1.14.2-3
- Add reference to delve
- Related: rhbz#1835917

* Fri May 22 2020 Alejandro Sáez <asm@redhat.com> - 1.14.2-2
- Stop building for i686
- Related: rhbz#1752991

* Fri May 22 2020 Alejandro Sáez <asm@redhat.com> - 1.14.2-1
- Rebase to Go 1.14.2
- Related: rhbz#1820596

* Tue Dec 10 2019 Alejandro Sáez <asm@redhat.com> - 1.13.4-3
- Rebase to Go 1.13.4

* Tue Mar 26 2019 Derek Parker <deparker@redhat.com> - 1.11.5-2
- Rebuild for 2019.3 and improve README

* Thu Jan 31 2019 Derek Parker <deparker@redhat.com> - 1.11.5-1
- Rebase to 1.11.5

* Thu Jan 10 2019 Derek Parker <deparker@redhat.com> - 1.11.4-1
- Rebase to 1.11.4

* Tue Dec 11 2018 Derek Parker <deparker@redhat.com> - 1.11.2-1
- Rebase to 1.11.2

* Fri Oct 26 2018 Derek Parker <deparker@redhat.com> - 1.10.3-7
- Update to include fix for internal FIPS flag
- Resolves: BZ#1643652

* Wed Oct 10 2018 Derek Parker <deparker@redhat.com> - 1.10.3-6
- Update to include fix for UnreachableExceptTests bug
- Resolves: BZ#1634748

* Fri Oct 5 2018 Derek Parker <deparker@redhat.com> - 1.10.3-5
- Bump to include new golang package changes
- Resolves: BZ#1636220
- Related: BZ#1609886

* Tue Sep 25 2018 Derek Parker <deparker@redhat.com> - 1.10.3-4
- Fix GOPATH issue pointing to old go-toolset-7 SCL.
- Resolves: rhbz#1607823

* Tue Sep 25 2018 Derek Parker <deparker@redhat.com> - 1.10.3-4
- Include runtime FIPS detection patch.

* Tue Jul 31 2018 Derek Parker <deparker@redhat.com> - 1.10.3-3
- Un-revert SCL macro changes -- they actually should be applied.

* Tue Jul 31 2018 Derek Parker <deparker@redhat.com> - 1.10.3-2
- Revert RHEL8 SCL macro changes

* Tue Jul 17 2018 Derek Parker <deparker@redhat.com> - 1.10.3-1
- Rebase to 1.10.3

* Mon Jul 16 2018 Derek Parker <deparker@redhat.com> - 1.10.2-5
- Update SCL macro.

* Thu Jun 7 2018 Derek Parker <deparker@redhat.com> - 1.10.2-4
- Bump release for new golang package, providing patch for OpenSSL thread safety initialization.

* Wed Jun 6 2018 Derek Parker <deparker@redhat.com> - 1.10.2-3
- Bump for Go FIPS inclusion.

* Mon Jun 4 2018 Derek Parker <deparker@redhat.com> - 1.10.2-2
- Bump for backported test patch in golang.

* Wed May 23 2018 Derek Parker <deparker@redhat.com> - 1.10.2-1
- Bump to golang 1.10.2

* Fri Apr 6 2018 Derek Parker <deparker@redhat.com> - 1.10.1-1
- Bump to golang 1.10.1

* Thu Mar 1 2018 Derek Parker <deparker@redhat.com> - 1.8-14
- Fix issue removing nonexistent file
- Resolves: rhbz#1550079

* Tue Feb 27 2018 Derek Parker <deparker@redhat.com> - 1.8-13
- Move enable_gotoolset7 to runtime package
- Resolves: rhbz#1544492

* Tue Feb 27 2018 Derek Parker <deparker@redhat.com> - 1.8-12
- Add enable_gotoolset7 macro to make it easier to activate go-toolset-7 during package builds.

* Mon Feb 26 2018 Derek Parker <deparker@redhat.com> - 1.8-11
- Remove Dockerfiles subpackage
- Resolves: rhbz#1548034, rhbz#1521197

* Tue Oct 17 2017 Jakub Čajka <jcajka@redhat.com> - 1.8-10
- improve enable script
- Resolves: rhbz#1501760

* Wed Oct 04 2017 Jakub Čajka <jcajka@redhat.com> - 1.8-9
- Update docker archive

* Wed Sep 27 2017 Jakub Čajka <jcajka@redhat.com> - 1.8-8
- NVR bump

* Wed Sep 27 2017 Jakub Čajka <jcajka@redhat.com> - 1.8-7
- Update docker archive

* Wed Aug 09 2017 Tom Stellard <tstellar@redhat.com> - 1.8-6
- Add dockerfiles

* Wed Aug 09 2017 Tom Stellard <tstellar@redhat.com> - 1.8-5
- Add stub dockerfiles sub-package

* Thu Jun 29 2017 Jakub Čajka jcajka@redhat.com 1.8-4
- add ExclusiveArches
- Resolves: BZ#1466199

* Wed Jun 21 2017 Jakub Čajka jcajka@redhat.com 1.8-3
- fix macro definition

* Thu Jun 15 2017 Jakub Čajka jcajka@redhat.com 1.8-2
- regular build

* Wed May 10 2017 Jakub Čajka jcajka@redhat.com 1.8-1
- Initial package
