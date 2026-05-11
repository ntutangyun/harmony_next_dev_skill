# ohpm dependency

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-dependency-check_

-------------------------------------------------------------------------------------------------------------------
checkupdate_pkgc3      1.2.0       1.2.0       1.2.0   match  update to date  library     prod            http://a.c
checkupdate_pkgc5      0.1.1       0.1.1       0.1.2   match  update to date  library     prod            http://a.c
checkupdate_pkgc2      2.0.0       2.0.0       2.0.0   match  update to date  library     prod            http://a.c
checkupdate_pkgea4     1.0.0       1.0.0       1.0.0   match  update to date  project     prod
@js-joda/core          5.5.2       5.5.2       5.6.0   match  update to date  project     prod            https://c.d
test-check-update      3.8.9-beta  3.8.9-beta  4.0.0   match  update to date  project     prod            https://a.y
Here are the recommended replacement packages for the following dependent packages :
checkupdate_pkgea4->checkupdate_test@2.0.0-beta, 三方测试库
checkupdate_pkgea4->@fdddd/test@1.1.5, 三方测试库
@js-joda/core->checkupdate_test@2.0.0-beta, 三方测试库
@js-joda/core->@fdddd/test@1.1.5, 三方测试库
test-check-update->checkupdate_test@2.0.0, 三方测试库
Here is the security update information: 2 package container 2 vulnerabilities，2 malwares
checkupdate_pkgea4@1.0.0, CVE-xxxx-xxxx test 跨站脚本漏洞,
checkupdate_pkgea4@1.0.0, asfasdf
test-check-update@3.8.9-beta, CVE-xxxx-xxxxx test 跨站脚本漏洞
test-check-update@3.8.9-beta, virusxxx
示例2

查询三方库的版本简要更新信息，执行一下命令。

ohpm dc --all -c

结果示例如下：

package                installed   wanted      latest  type     dependedBy                                                   
----------------------------------------------------------------------------
checkupdate_pkgc3      1.2.0       1.2.0       1.2.0   match    library     
checkupdate_pkgc5      0.1.1       0.1.1       0.1.2   match    library     
checkupdate_pkgc2      2.0.0       2.0.0       2.0.0   match    library     
checkupdate_pkgea4     1.0.0       1.0.0       1.0.0   match    project     
@js-joda/core          5.5.2       5.5.2       5.6.0   match    project     
test-check-update      3.8.9-beta  3.8.9-beta  4.0.0   match    project     
Here are the recommended replacement packages for the following dependent packages :
checkupdate_pkgea4->checkupdate_test@2.0.0-beta, 三方测试库
checkupdate_pkgea4->@fdddd/test@1.1.5, 三方测试库
@js-joda/core->checkupdate_test@2.0.0-beta, 三方测试库
@js-joda/core->@fdddd/test@1.1.5, 三方测试库
test-check-update->checkupdate_test@2.0.0, 三方测试库
Here is the security update information: 2 package container 2 vulnerabilities，2 malwares
checkupdate_pkgea4@1.0.0, CVE-xxxx-xxxx test 跨站脚本漏洞,
checkupdate_pkgea4@1.0.0, asfasdf
test-check-update@3.8.9-beta, CVE-xxxx-xxxxx test 跨站脚本漏洞
test-check-update@3.8.9-beta, virusxxx
ohpm convert
错误码
