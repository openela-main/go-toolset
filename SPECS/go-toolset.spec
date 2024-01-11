%global go_version 1.19.13

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
* Fri Oct 13 2023 David Benoit <dbenoit@redhat.com> - 1.19.13-1
- Fix CVE-2023-39325
- Resolves: RHEL-12622

* Wed Sep 13 2023 Archana Ravindar <aravinda@redhat.com> - 1.19.12-2
- Add strict fips runtime detection patch
- Related: rhbz#2223637

* Fri Sep 1 2023 Archana Ravindar <aravinda@redhat.com> - 1.19.12-1
- Update to Go 1.19.12
- Resolves: rhbz#2223637

* Tue Jun 6 2023 David Benoit <dbenoit@redhat.com> - 1.19.10-1
- Update to Go 1.19.10
- Resolves: rhbz#2217626
- Resolves: rhbz#2217612
- Resolves: rhbz#2217584

* Tue May 23 2023 Alejandro Sáez <asm@redhat.com> - 1.19.9-2
- Rebuild without changes
- Related: rhbz#2204476

* Tue May 23 2023 David Benoit <dbenoit@redhat.com> - 1.19.9-1
- Update to Go 1.19.9
- Related: rhbz#2204476

* Wed Mar 29 2023 David Benoit <dbenoit@redhat.com> - 1.19.6-2
- Rebuild without changes
- Related: rhbz#2175174

* Wed Mar 01 2023 David Benoit <dbenoit@redhat.com> - 1.19.6-1
- Rebase to Go 1.19.6
- Resolves: rhbz#2174429
- Fix memory leak
- Resolves: rhbz#2157602
- Enable tests in check phase

* Wed Dec 21 2022 David Benoit <dbenoit@redhat.com> - 1.19.4-1
- Rebase to Go 1.19.4
- Fix ppc64le linker issue
- Remove defunct patches
- Remove downstream generated FIPS mode patches
- Add golang-fips/go as the source for FIPS mode patches
- Resolves: rhbz#2144539

* Mon Oct 24 2022 David Benoit <dbenoit@redhat.com> - 1.19.2-1
- Rebase to Go 1.19.2
- Resolves: rhbz#2134407

* Fri Sep 30 2022 Alejandro Sáez <asm@redhat.com> - 1.19.1-1
- Rebase to Go 1.19.1
- Related: rhbz#2131028

* Fri Aug 05 2022 Alejandro Sáez <asm@redhat.com> - 1.18.4-1
- Rebase to Go 1.18.4

* Mon May 02 2022 David Benoit <dbenoit@redhat.com> - 1.18.2-1
- Rebase to Go 1.18.2
- Resolves: rhbz#2075169

* Thu Dec 16 2021 Alejandro Sáez <asm@redhat.com> - 1.17.5-1
- Rebase to Go 1.17.5
- Related: rhbz#2031116

* Tue Nov 16 2021 Alejandro Sáez <asm@redhat.com> - 1.17.2-1
- Rebase to Go 1.17.2 and to Delve 1.7.2
- Related: rhbz#2014087

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 1.16.6-2
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Jul 23 2021 Derek Parker <deparker@redhat.com> - 1.16.6-1
- Rebase to 1.16.6
- Resolves: rhbz#1984124
- Replace symbols no longer present in OpenSSL 3.0 ABI
- Resolves: rhbz#1984110
- Fix TestBoringServerCurves failing when ran by itself
- Resolves: rhbz#1977914

* Tue May 18 2021 Alejandro Sáez <asm@redhat.com> - 1.16.4-1
- Rebase to 1.16.4
- Resolves: rhbz#1955035
- Resolves: rhbz#1957961

* Thu Apr 15 2021 Mohan Boddu <mboddu@redhat.com> - 1.16.1-2
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Mar 30 2021 Alejandro Sáez <asm@redhat.com> - 1.16.1-2
- Rebase to go 1.16.1 and delve 1.6.0
- Resolves: rhbz#1922455

* Fri Jan 22 2021 David Benoit <dbenoit@redhat.com> - 1.15.7-1
- Rebase to 1.15.7
- Resolves: rhbz#1892207
- Resolves: rhbz#1918755

* Tue Nov 24 2020 David Benoit <dbenoit@redhat.com> - 1.15.5-1
- Rebase to 1.15.5
- Resolves: rhbz#1899184
- Resolves: rhbz#1899185
- Resolves: rhbz#1899186

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
