# 附录

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mdm-kit-appendix_

可委托策略列表

策略名称	对应接口	说明
disallow_add_local_account	accountManager.disallowOsAccountAddition accountManager.isOsAccountAdditionDisallowed	不传accountId参数，禁止设备创建本地用户。 不传accountId参数，查询是否禁止设备创建本地用户。
disallow_add_os_account_by_user	accountManager.disallowOsAccountAddition accountManager.isOsAccountAdditionDisallowed	需传入accountId参数，禁止指定用户添加账号。 需传入accountId参数，查询是否禁止指定用户添加账号。
disallow_running_bundles	applicationManager.addDisallowedRunningBundlesSync applicationManager.removeDisallowedRunningBundlesSync applicationManager.getDisallowedRunningBundlesSync	添加应用至应用运行禁止名单，添加至禁止名单的应用不允许在当前/指定用户下运行。 从应用运行禁止名单中移除应用。 获取当前/指定用户下的应用运行禁止名单。
manage_auto_start_apps	applicationManager.addAutoStartApps applicationManager.removeAutoStartApps applicationManager.getAutoStartApps	添加开机自启动应用名单。 从开机自启动应用名单中移除应用。 查询开机自启动应用名单。
allowed_bluetooth_devices	bluetoothManager.addAllowedBluetoothDevices bluetoothManager.removeAllowedBluetoothDevices bluetoothManager.getAllowedBluetoothDevices	添加蓝牙设备可用名单。 从蓝牙设备可用名单中移除。 查询蓝牙设备可用名单。
set_browser_policies	browser.setPolicySync browser.getPoliciesSync	为指定的浏览器设置浏览器子策略。 获取指定浏览器的策略。
allowed_install_bundles	bundleManager.addAllowedInstallBundlesSync bundleManager.removeAllowedInstallBundlesSync bundleManager.getAllowedInstallBundlesSync	添加应用至应用程序包安装允许名单，添加至允许名单的应用允许在当前/指定用户下安装，否则不允许安装。 从应用程序包安装允许名单中移除应用。 获取当前/指定用户下的应用程序包安装允许名单。
disallowed_install_bundles	bundleManager.addDisallowedInstallBundlesSync bundleManager.removeDisallowedInstallBundlesSync bundleManager.getDisallowedInstallBundlesSync	添加应用至应用程序包安装禁止名单，添加至禁止名单的应用不允许在当前/指定用户下安装。 从应用程序包安装禁止名单中移除应用。 获取当前/指定用户下的应用程序包安装禁止名单。
disallowed_uninstall_bundles	bundleManager.addDisallowedUninstallBundlesSync bundleManager.removeDisallowedUninstallBundlesSync bundleManager.getDisallowedUninstallBundlesSync	添加应用至应用程序包卸载禁止名单，添加至禁止名单的应用不允许在当前/指定用户下卸载。 从应用程序包卸载禁止名单中移除应用。 获取当前/指定用户下的应用程序包卸载禁止名单。
get_device_info	deviceInfo.getDeviceInfo	获取设备信息。
location_policy	locationManager.setLocationPolicy locationManager.getLocationPolicy	设置位置服务管理策略。 查询位置服务策略。
disabled_network_interface	networkManager.setNetworkInterfaceDisabledSync networkManager.isNetworkInterfaceDisabledSync	禁止设备使用指定网络。 查询指定网络接口是否被禁用。
global_proxy	networkManager.setGlobalProxySync networkManager.getGlobalProxySync	设置网络全局代理。 获取网络全局代理。
disabled_bluetooth	restrictions.setDisallowedPolicy restrictions.getDisallowedPolicy	feature传入bluetooth，禁用/启用蓝牙能力。 feature传入bluetooth，查询是否禁用蓝牙能力。
disallow_modify_datetime	restrictions.setDisallowedPolicy restrictions.getDisallowedPolicy	feature传入modifyDateTime，禁用/启用设置系统时间能力。 feature传入modifyDateTime，查询是否禁用修改系统时间能力。
disabled_printer	restrictions.setDisallowedPolicy restrictions.getDisallowedPolicy	feature传入printer，禁用/启用打印能力。 feature传入printer，查询是否禁用打印能力。
disabled_hdc	restrictions.setDisallowedPolicy restrictions.getDisallowedPolicy	feature传入hdc，禁用/启用被其他设备通过HDC连接、调试的能力。 feature传入hdc，查询是否禁用被其他设备通过HDC连接、调试的能力。
disable_microphone	restrictions.setDisallowedPolicy restrictions.getDisallowedPolicy	feature传入microphone，禁用/启用麦克风能力。 feature传入microphone，查询是否禁用麦克风能力。
fingerprint_auth	restrictions.setDisallowedPolicy restrictions.getDisallowedPolicy restrictions.setDisallowedPolicyForAccount restrictions.getDisallowedPolicyForAccount	feature传入fingerprint，禁用/启用指纹认证能力。 feature传入fingerprint，查询是否禁用指纹认证能力。 feature传入fingerprint，禁用/启用指定用户的指纹认证能力。 feature传入fingerprint，查询是否禁用指定用户的指纹认证能力。
disable_usb	restrictions.setDisallowedPolicy restrictions.getDisallowedPolicy	feature传入usb，禁用/启用USB能力。 feature传入usb，查询是否禁用USB能力。
disable_wifi	restrictions.setDisallowedPolicy restrictions.getDisallowedPolicy	feature传入wifi，禁用/启用Wi-Fi能力。 feature传入wifi，查询是否禁用Wi-Fi能力。
disallowed_tethering	restrictions.setDisallowedPolicy restrictions.getDisallowedPolicy	feature传入tethering，禁用/启用网络共享能力。 feature传入tethering，查询是否禁用网络共享能力。
inactive_user_freeze	restrictions.setDisallowedPolicy restrictions.getDisallowedPolicy	feature传入inactiveUserFreeze，禁用/启用非活跃用户运行能力。 feature传入inactiveUserFreeze，查询是否禁用非活跃用户运行能力。
snapshot_skip	restrictions.addDisallowedListForAccount restrictions.removeDisallowedListForAccount restrictions.getDisallowedListForAccount	feature传入snapshotSkip，禁用屏幕快照能力的应用名单。 feature传入snapshotSkip，从禁用屏幕快照能力的应用名单中移除。 feature传入snapshotSkip，查询禁用屏幕快照能力的应用名单。
password_policy	securityManager.setPasswordPolicy securityManager.getPasswordPolicy	设置设备锁屏口令策略。 获取设备锁屏口令策略。
clipboard_policy	securityManager.setAppClipboardPolicy securityManager.getAppClipboardPolicy	设置设备剪贴板策略。 获取设备剪贴板策略。
watermark_image_policy	securityManager.setWatermarkImage securityManager.cancelWatermarkImage	设置水印策略，当前仅支持PC/2in1使用。 取消水印策略，当前仅支持PC/2in1使用。
ntp_server	systemManager.setNTPServer systemManager.getNTPServer	设置NTP服务器的策略。 获取NTP服务器信息。
set_update_policy	systemManager.setOtaUpdatePolicy systemManager.getOtaUpdatePolicy	设置升级策略。 查询升级策略。
notify_upgrade_packages	systemManager.notifyUpdatePackages systemManager.getUpdateResult	通知系统更新包信息。 获取系统更新结果。
allowed_usb_devices	usbManager.addAllowedUsbDevices usbManager.removeAllowedUsbDevices usbManager.getAllowedUsbDevices	添加USB设备可用名单。 移除USB设备可用名单。 获取USB设备可用名单。
usb_read_only	usbManager.setUsbStorageDeviceAccessPolicy usbManager.getUsbStorageDeviceAccessPolicy	设置USB存储设备访问策略。 获取USB存储设备访问策略。
disallowed_usb_devices	usbManager.addDisallowedUsbDevices usbManager.removeDisallowedUsbDevices usbManager.getDisallowedUsbDevices	添加禁止使用的USB设备类型。 移除禁止使用的USB设备类型。 获取禁止使用的USB设备类型。
disallowed_sms	restrictions.setDisallowedPolicy restrictions.getDisallowedPolicy	feature传入sms，禁用/启用设备接收、发送短信的能力，当前仅支持手机、平板设备使用。 feature传入sms，查询是否禁用设备接收、发送短信的能力，当前仅支持手机、平板设备使用。
disallowed_mms	restrictions.setDisallowedPolicy restrictions.getDisallowedPolicy	feature传入mms，禁用/启用设备接收、发送彩信的能力，当前仅支持手机、平板设备使用。 feature传入mms，查询是否禁用设备接收、发送彩信的能力，当前仅支持手机、平板设备使用。
disable_backup_and_restore	restrictions.setDisallowedPolicy restrictions.getDisallowedPolicy	feature传入backupAndRestore，禁用/启用备份和恢复能力，当前仅支持手机、平板使用。 feature传入backupAndRestore，查询是否禁用备份和恢复能力，当前仅支持手机、平板使用。
installed_bundle_info_list	bundleManager.getInstalledBundleList	获取设备指定用户下已安装应用列表。
clear_up_application_data	applicationManager.clearUpApplicationData	清除应用产生的所有数据。
disallow_unmute_device	restrictions.setDisallowedPolicy restrictions.getDisallowedPolicy	feature传入unmuteDevice，禁用/启用设备媒体播放声音能力。 feature传入unmuteDevice，查询是否禁用设备媒体播放声音能力。
disabled_hdc_remote	restrictions.setDisallowedPolicy restrictions.getDisallowedPolicy	feature传入hdcRemote，禁用/启用设备通过HDC调试其他设备的能力。 feature传入hdcRemote，查询是否禁用设备通过HDC调试其他设备的能力。

策略变更上报列表

接口名称	策略变更事件PolicyChangedEvent中parameters参数返回示例
setDomainAccountPolicy	{"domainAccountInfo":{"domain":"","accountName":"test"},"policy":{"authenticationValidityPeriod":300,"passwordValidityPeriod":420,"passwordExpirationNotification":60}}
setAllowedKioskApps	{"appIdentifiers":["6917****3569"]}
setPolicySync	{"appId":"com.example._/******5t5CoBM=","policyName":"InsecurePrivateNetworkRequestsAllowed","policyValue":"1"}
setValue	{"item":"screenOff","value":"30000"}
setHomeWallpaper	""
setUnlockWallpaper	""
setSwitchStatus	{"key":1,"value":0}
addFirewallRule	{"firewallRule":{"srcAddr":"192.168.1.1-192.168.22.66","destAddr":"10.1.1.1","srcPort":"8080","destPort":"8080","appUid":"9696","direction":1,"action":1,"protocol":2,"family": 1,"logType":0}}
removeFirewallRule	{"firewallRule":{"srcAddr":"192.168.1.1-192.168.22.66","destAddr":"10.1.1.1","srcPort":"8080","destPort":"8080","appUid":"9696","direction":1,"action":1,"protocol":2,"family": 1,"logType":0}}
addDomainFilterRule	{"domainFilterRule":{"domainName":"www.example.com","appUid":"9696","action":1,"direction":1,"family":1,"logType":0}}
removeDomainFilterRule	{"domainFilterRule":{"domainName":"www.example.com","appUid":"9696","action":1,"direction":1,"family":1,"logType":0}}
setGlobalProxySync	{"httpProxy":{"host":"192.168.xx.xxx","port":8080,"exclusionList":["192.168"]}}
setGlobalProxyForAccount	{"httpProxy":{"host":"192.168.xx.xx","port":8080,"exclusionList":["192.168"]},"accountId":100}
addApn	{"apnId":"3","apnName":"CTENT"}
deleteApn	{"apnId":"3","apnName":"CTENT"}
updateApn	{"apnInfo":{"apn":"CTENT","apnName":"CTENT","mcc":"460","mnc":"11"},"apnId":"1"}
setPreferredApn	{"apnId":"3","apnName":"CTENT"}
setEthernetConfig	{"networkInterface":"eth0"}
setPasswordPolicy	{"policy":{"complexityRegex":"^(?=.*[a-zA-Z])(?=.*\\d).{8},$","validityPeriod":1808309786000,"additionalDescription":"至少8个字符，且包含数字和字母。"}}
uninstallEnterpriseReSignatureCertificate	{"certificateAlias":"test.cer","accountId":100}
installEnterpriseReSignatureCertificate	{"certificateAlias":"test.cer","accountId":100}
setNTPServer	{"server":"ntpserver.com"}
setActivationLockDisabled	{"isAllowed":true}
setWifiProfileSync	{"profile":{"ssid":"guest-Wi-Fi","bssid":"AA:BB:CC:DD:EE:FF"}}
