# Connectivity Kit术语

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/terminology_

A

[h2]A2DP

Advanced Audio Distribution Profile，即增强音频分发协议。支持传输高品质音频。例如：使用蓝牙耳机听音乐。该协议定义了2种角色：A2DP Source和A2DP Sink。

[h2]A2DP Sink

A2DP协议中的音频接收设备，负责解码并播放音频。典型设备如：蓝牙耳机、音箱等。

[h2]A2DP Source

A2DP协议中的音频源设备端，负责编码并发送音频数据。典型设备如：手机、平板等。

[h2]ACL

Asynchronous Connectionless Link，即异步无连接链路。在蓝牙子系统中，表示设备间物理链路的连接情况。

B

[h2]BLE

Bluetooth Low Energy，即低功耗蓝牙。从蓝牙4.0开始支持的协议，相比于传统蓝牙，是支持低功耗、长续航的蓝牙通信技术。

[h2]BR

Basic Rate，即蓝牙基础率。是一种蓝牙无线通信技术，用来表示传统蓝牙，主要用于文件和音频流的传输场景。

[h2]Bluetooth SIG

Bluetooth Special Interest Group，即蓝牙技术联盟，发布蓝牙技术规范的组织。开发者可以在其官网获取详细的蓝牙技术文档。

C

[h2]Characteristic

GATT服务（Service）的核心数据单元，可进行数据读写，通过UUID标识。

D

[h2]Descriptor

GATT特征值（Characteristic）的数据单元，用于描述特征值的附加信息和属性，可进行数据读写，通过UUID标识。

E

[h2]EDR

Enhanced Data Rate，即蓝牙增强数据率。是蓝牙BR的增强版本，具有更高的数据传输速率，和BR统称为传统蓝牙。

G

[h2]GATT

Generic Attribute Profile，即通用属性协议。是BLE的核心协议，定义了基于服务（Service）、特征值（Characteristic）和描述符（Descriptor）进行蓝牙通信和传输数据的机制。

H

[h2]HF

Hands-Free unit，即HFP协议中的免提设备。是蓝牙通话音频中的远程控制端‌，提供物理交互界面（如按钮）及音频输入/输出（如麦克风、扬声器）。典型设备如：蓝牙耳机、车载蓝牙等。

[h2]HFP

Hands-Free Profile，即免提协议。用于实现蓝牙设备间的免提通话，支持双向语音通话和控制等功能。该协议定义了2种角色：HFP AG和HF。

[h2]HFP AG

Hands-Free Audio Gateway，即HFP协议中的音频网关。是蓝牙通话音频中的音频处理中心，负责通话控制（如执行接听/挂断指令）、管理音频输入/输出等功能。典型设备如：手机、平板等。

[h2]HID

Human Interface Device Profile，即人机接口协议，为传统蓝牙设计。可用于实现蓝牙无线人机交互设备连接间的低延迟双向通信。例如：键盘、鼠标、游戏手柄等设备与主机（如手机、平板）间传输数据。该协议定义了2种角色：HID Host和HID Device。

在HID协议中， 数据传输通道分为2种，分别是中断通道和控制通道。其中中断通道用于传输单向低延迟实时数据；控制通道用于传输双向可靠实时数据，包含以下三种请求：

GET_REPORT：表示HID主机发起的数据读取请求，用于获取HID设备的状态信息。

SET_REPORT：表示HID主机发起的数据写入请求，用于向HID设备发送控制指令。

SET_PROTOCOL：表示HID主机发起的协议模式切换请求。

[h2]HID Device

HID设备，是向HID Host设备提供人机数据输入/输出的设备。典型设备如：鼠标、键盘等。

[h2]HID Host

HID主机设备，负责处理和接收HID Device的输入数据，并执行对应操作。典型设备如：手机、平板等。

[h2]HOGP

HID over GATT Profile，基于低功耗蓝牙的GATT协议实现的HID规范，将传统HID功能移植到BLE设备上复用，兼容键盘、鼠标、自拍杆等BLE设备的HID交互逻辑。

L

[h2]L2CAP

Logical Link Control and Adaptation Protocol，即逻辑链路控制和适配协议。可支持上层协议和应用的多种传输需求，提供面向连接和无连接的数据服务，并提供多路复用，分段和重组操作。

M

[h2]MAP

Message Access Profile，即消息访问协议。可用于实现蓝牙设备间的消息同步，支持短信、邮件等数据传输。该协议定义了2种角色：MCE和MSE。

[h2]MCE

Message Client Equipment，即MAP协议中的消息客户端，可查看和管理MSE的消息。典型设备如：车载蓝牙。

[h2]MSE

Message Server Equipment，即MAP协议中的消息服务端，存储原始消息数据（如短信或邮件）。典型设备如‌：手机。

[h2]MTU

Maximum Transmission Unit，即最大传输单元。表示网络中单次传输的最大数据包大小，单位是字节。

N

[h2]NAP

Network Access Point，即PAN协议中的网络接入点，充当网关设备，提供互联网接入或本地网络共享功能。典型设备如：手机、平板等。

O

[h2]OPP

Object Push Profile，即对象推送协议。基于通用对象交换协议（Generic Object Exchange Profile，GOEP）构建，可用于实现设备间数据（如图片、文档等）传输。

[h2]OOB

Out of Band，即带外（通信），是指使用独立于主数据通道的其他信道进行信息传输。例如蓝牙设备在配对过程中可以通过WiFi网络或NFC等非蓝牙信道交换安全秘钥，从而提升配对的安全性。

P

[h2]PAN

Personal Area Network，即蓝牙个人局域网协议。支持设备间网络共享。在该协议中，NAP和PANU是两种核心角色。

[h2]PANU

Personal Area Network User，即PAN协议中的个人局域网用户，作为客户端设备，主动连接NAP以获取网络服务。

[h2]PBAP

Phone Book Access Profile，即蓝牙电话簿访问协议。可用于实现蓝牙设备间的电话簿数据同步，支持联系人、通话记录等数据传输。该协议定义了2种角色：PCE和PSE。

[h2]PCE

Phone Book Client Equipment，即PBAP协议中的电话簿客户端，作为数据请求方，可获取PSE的电话簿数据。典型设备如：车载蓝牙。

[h2]PSE

Phone Book Server Equipment，即PBAP协议中的电话簿服务端，存储原始电话簿数据（如联系人和通话记录）。典型设备如：手机。

[h2]Profile

在蓝牙子系统中，一般特指某种蓝牙技术协议或者能力。例如：A2DP、HFP和HID协议等。

[h2]PSM

Protocol/Service Multiplexer，即协议/服务多路复用器。用于标识L2CAP层上的不同服务或协议。

R

[h2]RFCOMM

Radio Frequency Communication，即无线电频率通信协议。用于模拟传统的RS232串行通信（一种常见的有线数据传输标准），提供一种简单可靠的数据传输方式，支持多个同时连接的通道。

[h2]RSSI

Received Signal Strength Indicator，是无线通信中用于量化接收端信号强度的指标，单位是dBm。

S

[h2]SCO

Synchronous Connection-Oriented，即同步连接链路。主要用于传输对时间敏感的音频数据，如语音通话等场景。

[h2]SDP

Service Discovery Protocol，即服务发现协议。用于发现和识别其他蓝牙设备所提供的服务。

[h2]Service

在蓝牙协议中，一般特指GATT协议中的服务。是一种包含多个特征值和所依赖的其他服务的数据结构，表示BLE设备的一种能力，通过UUID标识。

[h2]SPP

Serial Port Profile，即串口通信协议。可用于实现蓝牙设备间通信连接和传输数据。

U

[h2]UUID

Universally Unique Identifier，即通用唯一标识，是一个128比特的数据格式。在蓝牙技术中，可用于标识不同的Profile协议，也可用于GATT协议中的服务、特征值和描述符。
