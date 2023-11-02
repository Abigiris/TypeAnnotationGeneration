# Release checklist

````text
## <version number for release> - <date released>

### <release candidate version number>

*<Sentence about creation date and either release version and release date (if successful) or recall date (if merged back into master branch)>*

#### Bugfixing

If any bugs are noticed in the release candidate, either fix them directly on the release candidate's branch or merge the release candidate's branch back into `master` for more development. Either way, list the bugs below.

#### Housekeeping

- [ ] Make sure Version.xml has the proper version number, and change the "devbuild" value to False.
- [ ] Run [Better Code Hub](https://bettercodehub.com/)
  - *<list failed guidelines with their numbers>*

#### Testing

- [ ] Run sanity tests
- [ ] Run name generation performance test
- [ ] Run pylint

#### Documentation

- [ ] Check that changelog is updated and accurate, and that links and Table of Contents are functional
- [ ] Check that issues referenced in the changelog are closed/resolved and are properly linked
- [ ] Check that style guide remains up-to-date, and that links and Table of Contents are functional
- [ ] Review other documentation for glaring errors
````

## 0.10.3 - 2019-10-02

### 0.10.3-rc1

*Created on 2019-10-01, released as version 0.10.3 on 2019-10-2.*

#### Bugfixing

If any bugs are noticed in the release candidate, either fix them directly on the release candidate's branch or merge the release candidate's branch back into `master` for more development. Either way, list the bugs below.

- [x] [Issue #46: Performance tests don't run](https://github.com/AlexLemna/rosevomit/issues/46) - `AL 2019-10-01`

#### Housekeeping

- [x] Make sure Version.xml has the proper version number, and change the "devbuild" value to False. - `AL 2019-10-01`
- [x] Run [Better Code Hub](https://bettercodehub.com/) - `AL 2019-10-01`
  - *7 of 10. Failed guidelines were: #1: Write Short Units of Code, #2: Write Simple Units of Code, #9: Automate Tests (test code percentage: 46%)*

#### Testing

- [x] Run sanity tests - `AL 2019-10-02`
    ````text
    Rosevomit test suite results
    2019-Oct-02 (Wed) 10:02AM
    ______________________________________________________________________
                            GENERATOR SANITY TEST

    test_constant_types (sanitytests.ConstantTests)
    Are the constants of the correct type? ... ok
    test_constants_not_empty (sanitytests.ConstantTests)
    Are the constants empty? ... ok
    test_obvious (sanitytests.ConstantTests)
    Testing that I know how to write a test. ... ok
    test_func_one_file (sanitytests.LowLevelTests)
    Does one_file() return a string without newlines and spaces? ... ok
    test_func_two_files (sanitytests.LowLevelTests)
    Does two_files() return a string without newlines and spaces? ... ok
    test_name_generation (sanitytests.NameGenerationTests)
    Do we get the number of names we expect? ... ok
    test_angle_sanity_check_float (sanitytests.UtilityTests)
    Do we ever get angles larger than 360 degrees? (float version) ... ok
    test_angle_sanity_check_int (sanitytests.UtilityTests)
    Do we ever get angles larger than 360 degrees? (integer version) ... ok

    ----------------------------------------------------------------------
    Ran 8 tests in 25.625s

    OK
    ````
- [x] Run name generation performance test - `AL 2019-10-02`
    ````text
    ______________________________________________________________________
                            PERFORMANCE TEST

    Fastest performance when generating 10 names, per namelist:
    first: 42ms total, avg 4.23ms per name. (Real avg 4.54ms)
    firstfemale: 32ms total, avg 3.18ms per name. (Real avg 3.29ms)
    firstmale: 18ms total, avg 1.79ms per name. (Real avg 1.82ms)
    last: 483ms total, avg 48.3ms per name. (Real avg 48.58ms)
    fullfemale: 516ms total, avg 51.64ms per name. (Real avg 52.7ms)
    fullmale: 578ms total, avg 57.75ms per name. (Real avg 65.34ms)

    Fastest performance when generating 100 names, per namelist:
    first: 524ms total, avg 5.24ms per name. (Real avg 5.68ms)
    firstfemale: 389ms total, avg 3.89ms per name. (Real avg 4.02ms)
    firstmale: 206ms total, avg 2.06ms per name. (Real avg 2.2ms)
    last: 4803ms total, avg 48.03ms per name. (Real avg 53.15ms)
    fullfemale: 5062ms total, avg 50.62ms per name. (Real avg 51.9ms)
    fullmale: 4795ms total, avg 47.95ms per name. (Real avg 48.36ms)

    Fastest performance when generating 1,000 names, per namelist:
    first: 4254ms total, avg 4.25ms per name. (Real avg 4.29ms)
    firstfemale: 3256ms total, avg 3.26ms per name. (Real avg 3.26ms)
    firstmale: 1834ms total, avg 1.83ms per name. (Real avg 1.85ms)
    last: 46788ms total, avg 46.79ms per name. (Real avg 49.03ms)
    fullfemale: 52166ms total, avg 52.17ms per name. (Real avg 53.14ms)
    fullmale: 49818ms total, avg 49.82ms per name. (Real avg 51.27ms)
    ````
- [x] Run pylint - `AL 2019-10-02`
  - *Code rated at 9.62/10*

#### Documentation

- [x] Check that changelog is updated and accurate, and that links and Table of Contents are functional - `AL 2019-10-02`
- [x] Check that issues referenced in the changelog are closed/resolved and are properly linked - `AL 2019-10-02`
- [x] Check that style guide remains up-to-date, and that links and Table of Contents are functional - `AL 2019-10-02`
- [x] Review other documentation for glaring errors - `AL 2019-10-01`
