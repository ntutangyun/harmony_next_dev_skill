# 方舟字节码基本原理

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-bytecode-fundamentals_

--------- ldlexvar 0x1, 0x2


|xxx|xxx|xxx|xxx|   <-- 当前词法环境
注意

lexical相关的逻辑是编译器的内部实现。随着方舟编译器的演进，可能会出现新的涉及lexical指令的场景。现有的lexical指令场景也可能会因需求演进和代码重构而不再涉及lexical的相关指令。

示例代码：

// Index.ts
function foo(): void {
  let a: number = 1;
  function bar(): number {
    return a;
  }
}
Index.ts

字节码中的相关指令：

.function any .foo(any a0, any a1, any a2) {
    newlexenv 0x1
    ...
    definefunc 0x0, .bar, 0x0
    sta v3
    ldai 0x1 
    ...
    stlexvar 0x0, 0x0
    ...
}    


.function any .bar(any a0, any a1, any a2) {
    ...
    ldlexvar 0x0, 0x0
    ...
}

指令newlexenv 0x1：创建一个槽位数为1的词法环境，将其存放到acc中，并进入该词法环境；

指令stlexvar 0x0, 0x0：将acc中的值存放到0个层次外的词法环境的0号槽位上；

指令ldlexvar 0x0, 0x0：将0个层次外的词法环境的0号槽位上的值存放到acc中。

共享词法环境

共享词法环境是一类特殊的词法环境。与一般词法环境的区别在于，共享词法环境中的每个词法变量都是sendable对象。方舟编译器通过共享词法环境实现词法变量在多线程中共享。

示例代码：

@Sendable
class A { }


@Sendable
class B {
  u: A = new A();
}
Index.ets

字节码中的相关指令：

.function any .#~B=#B(any a0, any a1, any a2) {
label_1:
label_0:
    callruntime.ldsendablevar 0x0, 0x0
    sta v0
    throw.undefinedifholewithname A
    ...
label_2:
}


.function any .func_main_0(any a0, any a1, any a2) {
label_1:
label_0:
    callruntime.newsendableenv 0x1
    ...
    callruntime.definesendableclass 0x0, .#~A=#A, _3, 0x0, v0
    callruntime.stsendablevar 0x0, 0x0
    ...
label_2:
}

指令callruntime.newsendableenv 0x1：创建一个槽位数为1的共享词法环境，并进入该词法环境；

指令callruntime.stsendablevar 0x0, 0x0：将acc中的值存放到0个层次外的共享词法环境的0号槽位上；

指令callruntime.ldsendablevar 0x0, 0x0：将0个层次外的共享词法环境的0号槽位上的值存放到acc中。

补丁变量

方舟编译器支持补丁模式的编译，当源文件发生修改时，经过补丁模式编译，生成一个补丁字节码，配合原字节码，完成功能的更新。方舟编译器在补丁模式下编译时，产生的补丁变量会被存放在一个特殊的补丁词法环境中。方舟字节码中使用补丁词法环境上的槽位编号来引用补丁变量。例如，指令ldpatchvar 0x1加载的是槽位号为1的补丁变量。

示例代码：

function bar(): void {} // 新增语句，编译补丁


function foo2(): void {
  bar(); // 新增语句，编译补丁
}
Index.ets

字节码中的相关指令：

.function any foo(...) {
    ...
    wide.ldpatchvar 0x0
    sta v4
    lda v4
    callarg0 0x0
    ...
}


.function any patch_main_0(...) {
    newlexenv 0x1
    definefunc 0x1, bar:(any,any,any), 0x0
    wide.stpatchvar 0x0
    ...
}

指令wide.stpatchvar 0x0：将函数bar存放到补丁词法环境的0号槽位；

指令wide.ldpatchvar 0x0：将补丁词法环境上0号槽位的值存放到acc中。

函数调用规范

对于一个包含了N个形参的方法，该方法所使用的寄存器中的最后N+3个会被用于传递参数。其中，前三个寄存器固定表示函数本身（FunctionObject）、new.target（NewTarget）和函数所在的词法环境中的this（this），后续的N个寄存器依次对应这N个形参。

示例代码：

function foo3(a: number, b: number): void {}
Index.ets

字节码中的相关指令：

.function any .foo(any a0, any a1, any a2, any a3, any a4) {
    // a0: FunctionObject
    // a1: NewTarget
    // a2: this 
    // a3: a
    // a4: b
}
字节码格式说明
助记符	语义说明
ID16	8位操作码，16位id。
IMM16	8位操作码，16位立即数。
IMM16_ID16	8位操作码，16位立即数，16位id。
IMM16_ID16_ID16_IMM16_V8	8位操作码，16位立即数，2个16位id，16位立即数，8位寄存器。
IMM16_ID16_IMM8	8位操作码，16位立即数，16位id，8位立即数。
IMM16_ID16_V8	8位操作码，16位立即数，16位id，8位寄存器。
IMM16_IMM16	8位操作码，2个16位立即数。
IMM16_IMM8_V8	8位操作码，16位立即数，8位立即数，8位寄存器。
IMM16_V8	8位操作码，16位立即数，8位寄存器。
IMM16_V8_IMM16	8位操作码，16位立即数，8位寄存器，16位立即数。
IMM16_V8_V8	8位操作码，16位立即数，2个8位寄存器。
IMM32	8位操作码，32位立即数。
IMM4_IMM4	8位操作码，2个4位立即数。
IMM64	8位操作码，64位立即数。
IMM8	8位操作码，8位立即数。
IMM8_ID16	8位操作码，8位立即数，16位id。
IMM8_ID16_ID16_IMM16_V8	8位操作码，8位立即数，2个16位id，16位立即数，8位寄存器。
IMM8_ID16_IMM8	8位操作码，8位立即数，16位id，8位立即数。
IMM8_ID16_V8	8位操作码，8位立即数，16位id，8位寄存器。
IMM8_IMM16	8位操作码，8位立即数，16位立即数。
IMM8_IMM8	8位操作码，2个8位立即数。
IMM8_IMM8_V8	8位操作码，2个8位立即数，8位寄存器。
IMM8_V8	8位操作码，8位立即数，8位寄存器。
IMM8_V8_IMM16	8位操作码，8位立即数，8位寄存器，16位立即数。
IMM8_V8_V8	8位操作码，8位立即数，2个8位寄存器。
IMM8_V8_V8_V8	8位操作码，8位立即数，3个8位寄存器。
IMM8_V8_V8_V8_V8	8位操作码，8位立即数，4个8位寄存器。
NONE	8位操作码。
PREF_IMM16	16位前缀操作码，16位立即数。
PREF_IMM16_ID16	16位前缀操作码，16位立即数，16位id。
PREF_IMM16_V8	16位前缀操作码，16位立即数，8位寄存器。
PREF_IMM16_V8_V8	16位前缀操作码，16位立即数，2个8位寄存器。
PREF_IMM8	16位前缀操作码，8位立即数。
PREF_NONE	16位前缀操作码。
PREF_V8	16位前缀操作码，8位寄存器。
PREF_V8_ID16	16位前缀操作码，8位寄存器，16位id。
PREF_V8_IMM32	16位前缀操作码，8位寄存器，32位立即数。
V16_V16	8位操作码，2个16位寄存器。
V4_V4	8位操作码，2个4位寄存器。
V8	8位操作码，8位寄存器。
V8_IMM16	8位操作码，8位寄存器，16位立即数。
V8_IMM8	8位操作码，8位寄存器，8位立即数。
V8_V8	8位操作码，2个8位寄存器。
V8_V8_V8	8位操作码，3个8位寄存器。
V8_V8_V8_V8	8位操作码，4个8位寄存器。
字节码汇总集合

下表中汇总了当前版本的所有方舟字节码，寄存器索引、立即数和id通过每四位宽度使用一个字符替代的形式来描述。

以指令defineclasswithbuffer RR, @AAAA, @BBBB, +CCCC, vDD为例：

defineclasswithbuffer：指示操作的操作码助记符。
RR：方舟运行时内部使用的8位保留数字，此处提及仅为完整展示指令格式，开发者无需关注。
@AAAA，@BBBB：16位id。
+CCCC：16位立即数。
vDD：8位寄存器索引。
操作码	格式	助记符/语法	参数	说明
0x00	NONE	ldundefined	-	将undefined加载进acc。
0x01	NONE	ldnull	-	将null加载进acc。
0x02	NONE	ldtrue	-	将true加载进acc。
0x03	NONE	ldfalse	-	将false加载进acc。
0x04	NONE	createemptyobject	-	创建一个空对象，并将其存放到acc中。
0x05	IMM8	createemptyarray RR	R：方舟运行时内部使用的8位保留数字	创建一个空数组，并将其存放到acc中。
0x06	IMM8_ID16	createarraywithbuffer RR, @AAAA	

R：方舟运行时内部使用的8位保留数字

A：16位的literal id

	使用索引A对应的字面量数组，创建一个数组对象，并将其存放到acc中。
0x07	IMM8_ID16	createobjectwithbuffer RR, @AAAA	

R：方舟运行时内部使用的8位保留数字

A：16位的literal id

	使用索引A对应的字面量数组，创建一个对象，并将其存放到acc中。
0x08	IMM8_IMM8_V8	newobjrange RR, +AA, vBB	

R：方舟运行时内部使用的8位保留数字

A：参数数量

B：类对象

B + 1, ..., B + A - 1：传递给构造函数的参数

	以B + 1, ..., B + A - 1作为参数，创建一个B类的实例，并将其存放到acc中。
0x09	IMM8	newlexenv +AA	A：词法环境中的槽位数目	创建一个槽位数为A的词法环境，将其存放到acc中，并进入该词法环境。
0x0a	IMM8_V8	add2 RR, vAA	

默认入参：acc：操作数

R：方舟运行时内部使用的8位保留数字

A：操作数

	计算A + acc，并将计算结果存放到acc中。
0x0b	IMM8_V8	sub2 RR, vAA	

默认入参：acc：操作数

R：方舟运行时内部使用的8位保留数字

A：操作数

	计算A - acc，并将计算结果存放到acc中。
0x0c	IMM8_V8	mul2 RR, vAA	

默认入参：acc：操作数

R：方舟运行时内部使用的8位保留数字

A：操作数

	计算A * acc，并将计算结果存放到acc中。
0x0d	IMM8_V8	div2 RR, vAA	

默认入参：acc：操作数

R：方舟运行时内部使用的8位保留数字

A：操作数

	计算A / acc，并将计算结果存放到acc中。
0x0e	IMM8_V8	mod2 RR, vAA	

默认入参：acc：操作数

R：方舟运行时内部使用的8位保留数字

A：操作数

	计算A % acc，并将计算结果存放到acc中。
0x0f	IMM8_V8	eq RR, vAA	

默认入参：acc：操作数

R：方舟运行时内部使用的8位保留数字

A：操作数

	计算A == acc，并将计算结果存放到acc中。
0x10	IMM8_V8	noteq RR, vAA	

默认入参：acc：操作数

R：方舟运行时内部使用的8位保留数字

A：操作数

	计算A != acc，并将计算结果存放到acc中。
0x11	IMM8_V8	less RR, vAA	

默认入参：acc：操作数

R：方舟运行时内部使用的8位保留数字

A：操作数

	计算A < acc，并将计算结果存放到acc中。
0x12	IMM8_V8	lesseq RR, vAA	

默认入参：acc：操作数

R：方舟运行时内部使用的8位保留数字

A：操作数

	计算A <= acc，并将计算结果存放到acc中。
0x13	IMM8_V8	greater RR, vAA	

默认入参：acc：操作数

R：方舟运行时内部使用的8位保留数字

A：操作数

	计算A > acc，并将计算结果存放到acc中。
0x14	IMM8_V8	greatereq RR, vAA	

默认入参：acc：操作数

R：方舟运行时内部使用的8位保留数字

A：操作数

	计算A >= acc，并将计算结果存放到acc中。
0x15	IMM8_V8	shl2 RR, vAA	

默认入参：acc：操作数

R：方舟运行时内部使用的8位保留数字

A：操作数

	计算A << acc，并将计算结果存放到acc中。
0x16	IMM8_V8	shr2 RR, vAA	

默认入参：acc：操作数

R：方舟运行时内部使用的8位保留数字

A：操作数

	计算A >>> acc，并将计算结果存放到acc中。
0x17	IMM8_V8	ashr2 RR, vAA	

默认入参：acc：操作数

R：方舟运行时内部使用的8位保留数字

A：操作数

	计算A >> acc，并将计算结果存放到acc中。
0x18	IMM8_V8	and2 RR, vAA	

默认入参：acc：操作数

R：方舟运行时内部使用的8位保留数字

A：操作数

	计算A & acc，并将计算结果存放到acc中。
0x19	IMM8_V8	or2 RR, vAA	

默认入参：acc：操作数

R：方舟运行时内部使用的8位保留数字

A：操作数

	计算A | acc，并将计算结果存放到acc中。
0x1a	IMM8_V8	xor2 RR, vAA	

默认入参：acc：操作数

R：方舟运行时内部使用的8位保留数字

A：操作数

	计算A ^ acc，并将计算结果存放到acc中。
0x1b	IMM8_V8	exp RR, vAA	

默认入参：acc：操作数

R：方舟运行时内部使用的8位保留数字

A：操作数

	计算A ** acc，并将计算结果存放到acc中。
0x1c	IMM8	typeof RR	

默认入参：acc：对象

R：方舟运行时内部使用的8位保留数字

	计算typeof acc，并将计算结果存放到acc中。
0x1d	IMM8	tonumber RR	

默认入参：acc：对象

R：方舟运行时内部使用的8位保留数字

	以acc作为参数，执行ToNumber，将结果存放到acc中。
0x1e	IMM8	tonumeric RR	

默认入参：acc：对象

R：方舟运行时内部使用的8位保留数字

	以acc作为参数，执行ToNumeric，将结果存放到acc中。
0x1f	IMM8	neg RR	

默认入参：acc：操作数

R：方舟运行时内部使用的8位保留数字

	计算-acc，并将计算结果存放到acc中。
0x20	IMM8	not RR	

默认入参：acc：操作数

R：方舟运行时内部使用的8位保留数字

	计算~acc，并将计算结果存放到acc中。
0x21	IMM8	inc RR	

默认入参：acc：操作数

R：方舟运行时内部使用的8位保留数字

	计算acc + 1，并将计算结果存放到acc中。
0x22	IMM8	dec RR	

默认入参：acc：操作数

R：方舟运行时内部使用的8位保留数字

	计算acc - 1，并将计算结果存放到acc中。
0x23	NONE	istrue	默认入参：acc：对象	计算acc == true，并将计算结果存放到acc中。
0x24	NONE	isfalse	默认入参：acc：对象	计算acc == false，并将计算结果存放到acc中。
0x25	IMM8_V8	isin RR, vAA	

默认入参：acc：对象

R：方舟运行时内部使用的8位保留数字

A：对象

	计算A in acc，并将计算结果存放到acc中。
0x26	IMM8_V8	instanceof RR, vAA	

默认入参：acc：对象

R：方舟运行时内部使用的8位保留数字

A：对象

	计算A instanceof acc，并将计算结果存放到acc中。
0x27	IMM8_V8	strictnoteq RR, vAA	

默认入参：acc：对象

R：方舟运行时内部使用的8位保留数字

A：对象

	计算acc !== A，并将计算结果存放到acc中。
0x28	IMM8_V8	stricteq RR, vAA	

默认入参：acc：对象

R：方舟运行时内部使用的8位保留数字

A：对象

	计算acc === A，并将计算结果存放到acc中。
0x29	IMM8	callarg0 RR	

默认入参：acc：函数对象

R：方舟运行时内部使用的8位保留数字

	不传递参数，直接调用acc中存放的函数对象，并将结果存放到acc中。
0x2a	IMM8_V8	callarg1 RR, vAA	

默认入参：acc：函数对象

R：方舟运行时内部使用的8位保留数字

A：参数

	以A作为参数，调用acc中存放的函数对象，并将结果存放到acc中。
0x2b	IMM8_V8_V8	callargs2 RR, vAA, vBB	

默认入参：acc：函数对象

R：方舟运行时内部使用的8位保留数字

A, B：参数

	以A，B作为参数，调用acc中存放的函数对象，并将结果存放到acc中。
0x2c	IMM8_V8_V8_V8	callargs3 RR, vAA, vBB, vCC	

默认入参：acc：函数对象

R：方舟运行时内部使用的8位保留数字

A, B, C：参数

	以A, B, C作为参数，调用acc中存放的函数对象，并将结果存放到acc中。
0x2d	IMM8_V8	callthis0 RR, vAA	

默认入参：acc：函数对象

R：方舟运行时内部使用的8位保留数字

A：对象

	将this的值设置为A，不传递参数，调用acc中存放的函数对象，并将结果存放到acc中。
0x2e	IMM8_V8_V8	callthis1 RR, vAA, vBB	

默认入参：acc：函数对象

R：方舟运行时内部使用的8位保留数字

A：对象

B：参数

	将this的值设置为A，以B作为参数，调用acc中存放的函数对象，并将计算结果存放到acc中。
0x2f	IMM8_V8_V8_V8	callthis2 RR, vAA, vBB, vCC	

默认入参：acc：函数对象

R：方舟运行时内部使用的8位保留数字

A：对象

B, C：参数

	将this的值设置为A，以B，C作为参数，调用acc中存放的函数对象，并将计算结果存放到acc中。
0x30	IMM8_V8_V8_V8_V8	callthis3 RR, vAA, vBB, vCC, vDD	

默认入参：acc：函数对象

R：方舟运行时内部使用的8位保留数字

A：对象

B, C, D：参数

	将this的值设置为A，以B, C, D作为参数，调用acc中存放的函数对象，并将计算结果存放到acc中。
0x31	IMM8_IMM8_V8	callthisrange RR, +AA, vBB	

默认入参：acc：函数对象

R：方舟运行时内部使用的8位保留数字

A：参数数量

B：对象

B + 1, ..., B + A：参数

	将this的值设置为B，以B + 1，...，B + A作为参数，调用acc中存放的函数对象，并将计算结果存放到acc中。
0x32	IMM8_IMM8_V8	supercallthisrange RR, +AA, vBB	

R：方舟运行时内部使用的8位保留数字

A：参数数量

B, ..., B + A - 1：参数

	

以B, ..., B + A - 1作为参数, 调用super函数，并将结果存放到acc中。

当A的值是0时，B是undefined。

此指令仅出现在非箭头函数中。


0x33	IMM8_ID16_IMM8	definefunc RR, @AAAA, +BB	

R：方舟运行时内部使用的8位保留数字

A：method id

B：方法A的形参数量

	创建方法A的函数对象，并将其存放到acc中。
0x34	IMM8_ID16_IMM8	definemethod RR, @AAAA, +BB	

默认入参：acc：类对象或类对象的对象原型，方法为静态方法时，acc中是类对象

R：方舟运行时内部使用的8位保留数字

A：method id

B：方法A的形参数量

	创建方法A的函数对象，将acc中的对象设置为该函数对象的HomeObject属性，并将该函数对象存放到acc中。
0x35	IMM8_ID16_ID16_IMM16_V8	defineclasswithbuffer RR, @AAAA, @BBBB, +CCCC, vDD	

R：方舟运行时内部使用的8位保留数字

A：类的构造函数的method id

B：literal id

C：方法A的形参数量

D：父类

	使用索引B对应的字面量数组和父类D，创建A的类对象，并将其存放到acc中。
0x36	V8	getnextpropname vAA	A：迭代器	执行for-in迭代器A的next方法，并将结果存放到acc中。
0x37	IMM8_V8	ldobjbyvalue RR, vAA	

默认入参：acc：属性键值

R：方舟运行时内部使用的8位保留数字

A：对象

	加载A对象的键值为acc的属性，并将结果存放到acc中。
0x38	IMM8_V8_V8	stobjbyvalue RR, vAA, vBB	

默认入参：acc：值

R：方舟运行时内部使用的8位保留数字

A：对象

B：属性键值

	将acc中的值存放到对象A的键值为B的属性上。
0x39	IMM8_V8	ldsuperbyvalue RR, vAA	

默认入参：acc：属性键值

R：方舟运行时内部使用的8位保留数字

A：对象

	在当前函数中，获取super的键值为acc的属性，并将其存放到acc中。若该属性为访问器属性，则将A中的对象作为调用该属性getter函数时的this参数。
0x3a	IMM8_IMM16	ldobjbyindex RR, +AAAA	

默认入参：acc：对象

R：方舟运行时内部使用的8位保留数字

A：属性键值

	加载acc中所存对象的键值为A的属性，并将其存放到acc中。
0x3b	IMM8_V8_IMM16	stobjbyindex RR, vAA, +BBBB	

默认入参：acc：值

R：方舟运行时内部使用的8位保留数字

A：对象

B：属性键值

	将acc中的值存放到对象A的键值为B的属性上。
0x3c	IMM4_IMM4	ldlexvar +A, +B	

A：词法环境层级

B：槽位号

	将A个层次外的词法环境的B号槽位上的值存放到acc中。
0x3d	IMM4_IMM4	stlexvar +A, +B	

默认入参：acc：值

A：词法环境层级

B：槽位号

	将acc中的值存放到A个层次外的词法环境的B号槽位上。
0x3e	ID16	lda.str @AAAA	A：string id	将索引A对应的字符串存放到acc中。
0x3f	IMM8_ID16	tryldglobalbyname RR, @AAAA	

R：方舟运行时内部使用的8位保留数字

A：string id

	将名称为索引A对应的字符串的全局变量存放进acc中，不存在名称为A的全局变量时，抛出异常。
0x40	IMM8_ID16	trystglobalbyname RR, @AAAA	

默认入参：acc：值

R：方舟运行时内部使用的8位保留数字

A：string id

	将acc中的值存放到名称为索引A对应的字符串的全局变量上，不存在名称为A的全局变量时，抛出异常。
0x41	IMM16_ID16	ldglobalvar RRRR, @AAAA	

R：方舟运行时内部使用的16位保留数字

A：string id

	将名称为索引A对应的字符串的全局变量的值存放到acc中，该变量一定存在。
0x42	IMM8_ID16	ldobjbyname RR, @AAAA	

默认入参：acc：对象

R：方舟运行时内部使用的8位保留数字

A：string id

	加载acc中所存对象的键值为索引A对应的字符串的属性，并将其存放到acc中。
0x43	IMM8_ID16_V8	stobjbyname RR, @AAAA, vBB	

默认入参：acc：值

R：方舟运行时内部使用的8位保留数字

A：string id

B：对象

	将acc中的值存放到对象B的键值为索引A对应的字符串的属性上。
0x44	V4_V4	mov vA, vB	A, B：寄存器索引	将寄存器B中的内容复制到寄存器A中。
0x45	V8_V8	mov vAA, vBB	A, B：寄存器索引	将寄存器B中的内容复制到寄存器A中。
0x46	IMM8_ID16	ldsuperbyname RR, @AAAA	

默认入参：acc：对象

R：方舟运行时内部使用的8位保留数字

A：string id

	在当前函数中，获取super的键值为索引A对应的字符串的属性，并将其存放到acc中。若该属性为访问器属性，则将acc中的对象作为调用该属性getter函数时的this参数。
0x47	IMM16_ID16	stconsttoglobalrecord RRRR, @AAAA	

默认入参：acc：值

R：方舟运行时内部使用的16位保留数字

A：string id

	将acc的值存放到全局变量中以const定义的名字为索引A对应的字符串的常量。
0x48	IMM16_ID16	sttoglobalrecord RRRR, @AAAA	

默认入参：acc：值

R：方舟运行时内部使用的16位保留数字

A：string id

	将acc的值存放到全局变量中以let定义的名字为索引A对应的字符串的变量。
0x49	IMM8_ID16	ldthisbyname RR, @AAAA	

R：方舟运行时内部使用的8位保留数字

A：string id

	加载this的键值为索引A对应的字符串的属性，并把结果存放到acc中。
0x4a	IMM8_ID16	stthisbyname RR, @AAAA	

默认入参：acc：值

R：方舟运行时内部使用的8位保留数字

A：string id

	将acc中的值存放到this的键值为索引A对应的字符串的属性上。
0x4b	IMM8	ldthisbyvalue RR	

默认入参：acc：属性键值

R：方舟运行时内部使用的8位保留数字

	加载this的键值为acc的属性，并将结果存放到acc中。
0x4c	IMM8_V8	stthisbyvalue RR, vAA	

默认入参：acc：值

R：方舟运行时内部使用的8位保留数字

A：属性键值

	将acc中的值存放到this的键值为A的属性上。
0x4d	IMM8	jmp +AA	A：有符号的分支偏移量	无条件跳转到分支A。
0x4e	IMM16	jmp +AAAA	A：有符号的分支偏移量	无条件跳转到分支A。
0x4f	IMM8	jeqz +AA	

默认入参：acc：值

A：有符号的分支偏移量

	计算acc == 0，如果为真，则跳转到分支A。
0x50	IMM16	jeqz +AAAA	

默认入参：acc：值

A：有符号的分支偏移量

	计算acc == 0，如果为真，则跳转到分支A。
0x51	IMM8	jnez +AA	

默认入参：acc：值

A：有符号的分支偏移量

	计算acc != 0，如果为真，则跳转到分支A。
0x52	IMM8	jstricteqz +AA	

默认入参：acc：值

A：有符号的分支偏移量

	

计算acc === 0，如果为真，则跳转到分支A。

指令功能未使能，暂不可用。


0x53	IMM8	jnstricteqz +AA	

默认入参：acc：值

A：有符号的分支偏移量

	

计算acc !== 0，如果为真，则跳转到分支A。

指令功能未使能，暂不可用。


0x54	IMM8	jeqnull +AA	

默认入参：acc：值

A：有符号的分支偏移量

	

计算acc == null，如果为真，则跳转到分支A。

指令功能未使能，暂不可用。


0x55	IMM8	jnenull +AA	

默认入参：acc：值

A：有符号的分支偏移量

	

计算acc != null，如果为真，则跳转到分支A。

指令功能未使能，暂不可用。


0x56	IMM8	jstricteqnull +AA	

默认入参：acc：值

A：有符号的分支偏移量

	

计算acc === null，如果为真，则跳转到分支A。

指令功能未使能，暂不可用。


0x57	IMM8	jnstricteqnull +AA	

默认入参：acc：值

A：有符号的分支偏移量

	

计算acc !== null，如果为真，则跳转到分支A。

指令功能未使能，暂不可用。


0x58	IMM8	jequndefined +AA	

默认入参：acc：值

A：有符号的分支偏移量

	

计算acc == undefined，如果为真，则跳转到分支A。

指令功能未使能，暂不可用。


0x59	IMM8	jneundefined +AA	

默认入参：acc：值

A：有符号的分支偏移量

	

计算acc != undefined，如果为真，则跳转到分支A。

指令功能未使能，暂不可用。


0x5a	IMM8	jstrictequndefined +AA	

默认入参：acc：值

A：有符号的分支偏移量

	

计算acc === undefined，如果为真，则跳转到分支A。

指令功能未使能，暂不可用。


0x5b	IMM8	jnstrictequndefined +AA	

默认入参：acc：值

A：有符号的分支偏移量

	

计算acc !== undefined，如果为真，则跳转到分支A。

指令功能未使能，暂不可用。


0x5c	V8_IMM8	jeq vAA, +BB	

默认入参：acc：值

A：值

B：有符号的分支偏移量

	

计算acc == A，如果为真，则跳转到分支B。

指令功能未使能，暂不可用。


0x5d	V8_IMM8	jne vAA, +BB	

默认入参：acc：值

A：值

B：有符号的分支偏移量

	

计算acc != A，如果为真，则跳转到分支B。

指令功能未使能，暂不可用。


0x5e	V8_IMM8	jstricteq vAA, +BB	

默认入参：acc：对象

A：对象

B：有符号的分支偏移量

	

计算acc === A，如果为真，则跳转到分支B。

指令功能未使能，暂不可用。


0x5f	V8_IMM8	jnstricteq vAA, +BB	

默认入参：acc：对象

A：对象

B：有符号的分支偏移量

	

计算acc !== A，如果为真，则跳转到分支B。

指令功能未使能，暂不可用。


0x60	V8	lda vAA	A：寄存器索引	将寄存器A中的内容存放到acc中。
0x61	V8	sta vAA	

默认入参：acc

A：寄存器索引

	将acc中的内容存放到寄存器A中。
0x62	IMM32	ldai +AAAAAAAA	A：常量字面量	将整型字面量A存放到acc中。
0x63	IMM64	fldai +AAAAAAAAAAAAAAAA	A：常量字面量	将双精度浮点型字面量A存放到acc中。
0x64	NONE	return	默认入参：acc：值	返回acc中的值。
0x65	NONE	returnundefined	-	返回undefined。
0x66	NONE	getpropiterator	默认入参：acc：对象	将acc中所存的对象的for-in迭代器存放到acc中。
0x67	IMM8	getiterator RR	

默认入参：acc：对象

R：方舟运行时内部使用的8位保留数字

	执行GetIterator(acc, sync)方法，并将结果存放到acc中。
0x68	IMM8_V8	closeiterator RR, vAA	

R：方舟运行时内部使用的8位保留数字

A：对象

	以类型为 iteratorRecord 的A作为参数，执行IteratorClose，并将结果存放到acc中。
0x69	NONE	poplexenv	-	跳出当前的词法环境，进入外面一层词法环境。
0x6a	NONE	ldnan	-	将nan存放到acc中。
0x6b	NONE	ldinfinity	-	将infinity存放到acc中。
0x6c	NONE	getunmappedargs	-	将当前函数的arguments存放到acc中。
0x6d	NONE	ldglobal	-	将global对象存放到acc中。
0x6e	NONE	ldnewtarget	-	

将当前函数的隐式参数NewTarget存放到acc中。

指令功能未使能，暂不可用。


0x6f	NONE	ldthis	-	将this存放到acc中。
0x70	NONE	ldhole	-	将hole存放到acc中。
0x71	IMM8_ID16_IMM8	createregexpwithliteral RR, @AAAA, +BB	

R：方舟运行时内部使用的8位保留数字

A：string id

B：指代正则表达式修饰符

	

使用索引A对应的字符串和B指代的修饰符，创建一个正则表达式，并存放到acc中。

B和所指代的修饰符的对应关系为：0（默认值，无修饰符），1（g），2（i），4（m），8（s），16（u），32（y）；B也可以指代符合语法规范的修饰符的组合，例如3，指代的修饰符是gi。


0x72	IMM16_ID16_IMM8	createregexpwithliteral RRRR, @AAAA, +BB	

R：方舟运行时内部使用的16位保留数字

A：string id

B：指代正则表达式修饰符

	

使用索引A对应的字符串和B指代的修饰符，创建一个正则表达式，并存放到acc中。

B和所指代的修饰符的对应关系为：0（默认值，无修饰符），1（g），2（i），4（m），8（s），16（u），32（y）；B也可以指代符合语法规范的修饰符的组合，例如3，指代的修饰符是gi。


0x73	IMM8_IMM8_V8	callrange RR, +AA, vBB	

默认入参：acc：函数对象

R：方舟运行时内部使用的8位保留数字

A：参数数量

B,..., B + A - 1：参数

	以B, ..., B + A - 1作为参数，调用acc中存放的函数对象，并将结果存放到acc中。
0x74	IMM16_ID16_IMM8	definefunc RRRR, @AAAA, +BB	

R：方舟运行时内部使用的16位保留数字

A：method id

B：方法A的形参数量

	创建方法A的函数对象，并将其存放到acc中。
0x75	IMM16_ID16_ID16_IMM16_V8	defineclasswithbuffer RRRR, @AAAA, @BBBB, +CCCC, vDD	

R：方舟运行时内部使用的16位保留数字

A：类的构造函数的method id

B：literal id

C：方法A的形参数量

D：父类

	使用索引B对应的字面量数组和父类D，创建A的类对象，并将其存放到acc中。
0x76	IMM8	gettemplateobject RR	

默认入参：acc：对象

R：方舟运行时内部使用的8位保留数字

	执行GetTemplateObject(acc)，并将结果存放到acc中。
0x77	IMM8_V8	setobjectwithproto RR, vAA	

默认入参：acc：对象

R：方舟运行时内部使用的8位保留数字

A：值

	将acc中存放对象的 __proto__ 属性设置为A。
0x78	IMM8_V8_V8	stownbyvalue RR, vAA, vBB	

默认入参：acc：值

R：方舟运行时内部使用的8位保留数字

A：对象

B：属性键值

	将acc中的值存放到对象A的键值为B的属性上。
0x79	IMM8_V8_IMM16	stownbyindex RR, vAA, +BBBB	

默认入参：acc：值

R：方舟运行时内部使用的8位保留数字

A：对象

B：属性键值

	将acc中的值存放到对象A的键值为B的属性上。
0x7a	IMM8_ID16_V8	stownbyname RR, @AAAA, vBB	

默认入参：acc：值

R：方舟运行时内部使用的8位保留数字

A：string id

B：对象

	将acc中的值存放到对象B的键值为索引A对应的字符串的属性上。
0x7b	IMM8	getmodulenamespace +AA	A：模块索引	对第A个模块，执行GetModuleNamespace，并将结果存放到acc中。
0x7c	IMM8	stmodulevar +AA	

默认入参：acc：值

A：槽位号

	将acc中的值存放到槽位号为A的模块变量中。
0x7d	IMM8	ldlocalmodulevar +AA	A：槽位号	将槽位号为A的局部模块变量存放到acc中。
0x7e	IMM8	ldexternalmodulevar +AA	A：槽位号	将槽位号为A的外部模块变量存放到acc中。
0x7f	IMM16_ID16	stglobalvar RRRR, @AAAA	

默认入参：acc：值

R：方舟运行时内部使用的16位保留数字

A：string id

	将acc中的值存放到名字为索引A对应的字符串的全局变量上，这个变量一定存在。
0x80	IMM16	createemptyarray RRRR	R：方舟运行时内部使用的16位保留数字	创建一个空数组，并将其存放到acc中。
0x81	IMM16_ID16	createarraywithbuffer RRRR, @AAAA	

R：方舟运行时内部使用的16位保留数字

A：literal id

	使用索引A对应的字面量数组，创建一个数组对象, 并将其存放到acc中。
0x82	IMM16_ID16	createobjectwithbuffer RRRR, @AAAA	

R：方舟运行时内部使用的16位保留数字

A：literal id

	使用索引A对应的字面量数组，创建一个对象, 并将其存放到acc中。
0x83	IMM16_IMM8_V8	newobjrange RRRR, +AA, vBB	

R：方舟运行时内部使用的16位保留数字

A：参数数量

B：类对象

B + 1, ..., B + A - 1：传递给构造函数的参数

	以B + 1, ..., B + A - 1作为参数，创建一个B类的实例，并将其存放到acc中。
0x84	IMM16	typeof RRRR	

默认入参：acc：对象

R：方舟运行时内部使用的16位保留数字

	计算typeof acc，并将计算结果存放到acc中。
0x85	IMM16_V8	ldobjbyvalue RRRR, vAA	

默认入参：acc：属性键值

R：方舟运行时内部使用的16位保留数字

A：对象

	加载A对象的键值为acc的属性，并将结果存放到acc中。
0x86	IMM16_V8_V8	stobjbyvalue RRRR, vAA, vBB	

默认入参：acc：值

R：方舟运行时内部使用的16位保留数字

A：对象

B：属性键值

	将acc中的值存放到对象A的键值为B的属性上。
0x87	IMM16_V8	ldsuperbyvalue RRRR, vAA	

默认入参：acc：属性键值

R：方舟运行时内部使用的16位保留数字

A：对象

	在当前函数中，获取super的键值为acc的属性，并将其存放到acc中。若该属性为访问器属性，则将A中的对象作为调用该属性getter函数时的this参数。
0x88	IMM16_IMM16	ldobjbyindex RRRR, +AAAA	

默认入参：acc：对象

R：方舟运行时内部使用的16位保留数字

A：属性键值

	加载acc中所存对象的键值为A的属性，并将其存放到acc中。
0x89	IMM16_V8_IMM16	stobjbyindex RRRR, vAA, +BBBB	

默认入参：acc：值

R：方舟运行时内部使用的16位保留数字

A：对象

B：属性键值

	将acc中的值存放到对象A的键值为B的属性上。
0x8a	IMM8_IMM8	ldlexvar +AA, +BB	

A：词法环境层级

B：槽位号

	将A个层次外的词法环境的B号槽位上的值存放到acc中。
0x8b	IMM8_IMM8	stlexvar +AA, +BB	

默认入参：acc：值

A：词法环境层级

B：槽位号

	将acc中的值存放到A个层次外的词法环境的B号槽位上。
0x8c	IMM16_ID16	tryldglobalbyname RRRR, @AAAA	

R：方舟运行时内部使用的16位保留数字

A：string id

	将名称为索引A对应的字符串的全局变量存放进acc中，不存在名称为A的全局变量时，抛出异常。
0x8d	IMM16_ID16	trystglobalbyname RRRR, @AAAA	

默认入参：acc：值

R：方舟运行时内部使用的16位保留数字

A：string id

	将acc中的值存放到名称为索引A对应的字符串的全局变量上，不存在名称为A的全局变量时，抛出异常。
0x8e	IMM8_ID16_V8	stownbynamewithnameset RR, @AAAA, vBB	

默认入参：acc：函数对象

R：方舟运行时内部使用的8位保留数字

A：string id

B：对象

	将acc中的函数对象存放到对象B的键值为索引A对应的字符串的属性上，并将函数的名称设置为索引A对应的字符串。
0x8f	V16_V16	mov vAAAA, vBBBB	A, B：寄存器索引	将寄存器B中的内容复制到寄存器A中。
0x90	IMM16_ID16	ldobjbyname RRRR, @AAAA	

默认入参：acc：对象

R：方舟运行时内部使用的16位保留数字

A：string id

	加载acc中所存对象的键值为索引A对应的字符串的属性，并将其存放到acc中。
0x91	IMM16_ID16_V8	stobjbyname RRRR, @AAAA, vBB	

默认入参：acc：值

R：方舟运行时内部使用的16位保留数字

A：string id

B：对象

	将acc中的值存放到对象B的键值为索引A对应的字符串的属性上。
0x92	IMM16_ID16	ldsuperbyname RRRR, @AAAA	

默认入参：acc：对象

R：方舟运行时内部使用的16位保留数字

A：string id

	在当前函数中，获取super的键值为索引A对应的字符串的属性，并将其存放到acc中。若该属性为访问器属性，则将acc中的对象作为调用该属性getter函数时的this参数。
0x93	IMM16_ID16	ldthisbyname RRRR, @AAAA	

R：方舟运行时内部使用的16位保留数字

A：string id

	加载this的键值为索引A对应的字符串的属性，并把结果存放到acc中。
0x94	IMM16_ID16	stthisbyname RRRR, @AAAA	

默认入参：acc：值

R：方舟运行时内部使用的16位保留数字

A：string id

	将acc中的值存放到this的键值为索引A对应的字符串的属性上。
0x95	IMM16	ldthisbyvalue RRRR	

默认入参：acc：属性键值

R：方舟运行时内部使用的16位保留数字

	加载this的键值为acc的属性，并将结果存放到acc中。
0x96	IMM16_V8	stthisbyvalue RRRR, vAA	

默认入参：acc：值

R：方舟运行时内部使用的16位保留数字

A：属性键值

	将acc中的值存放到this的键值为A的属性上。
0x97	V8	asyncgeneratorreject vAA	

默认入参：acc：异常

A：生成器

	使用generator A和acc中存放的异常，执行AsyncGeneratorReject，并将结果存放到acc中。
0x98	IMM32	jmp +AAAAAAAA	A：有符号的分支偏移量	无条件跳转到分支A。
0x99	IMM8_V8_V8	stownbyvaluewithnameset RR, vAA, vBB	

默认入参：acc：函数对象

R：方舟运行时内部使用的8位保留数字

A：对象

B：属性键值

	将acc中的值存放到对象A的键值为B的属性上，并将函数的名称设置为B。
0x9a	IMM32	jeqz +AAAAAAAA	

默认入参：acc：值

A：有符号的分支偏移量

	计算acc == 0，如果为真，则跳转到分支A。
0x9b	IMM16	jnez +AAAA	

默认入参：acc：值

A：有符号的分支偏移量

	计算acc != 0，如果为真，则跳转到分支A。
0x9c	IMM32	jnez +AAAAAAAA	

默认入参：acc：值

A：有符号的分支偏移量

	计算acc != 0，如果为真，则跳转到分支A。
0x9d	IMM16	jstricteqz +AAAA	

默认入参：acc：值

A：有符号的分支偏移量

	

计算acc === 0，如果为真，则跳转到分支A。

指令功能未使能，暂不可用。


0x9e	IMM16	jnstricteqz +AAAA	

默认入参：acc：值

A：有符号的分支偏移量

	

计算acc !== 0，如果为真，则跳转到分支A。

指令功能未使能，暂不可用。


0x9f	IMM16	jeqnull +AAAA	

默认入参：acc：值

A：有符号的分支偏移量

	

计算acc == null，如果为真，则跳转到分支A。

指令功能未使能，暂不可用。


0xa0	IMM16	jnenull +AAAA	

默认入参：acc：值

A：有符号的分支偏移量

	

计算acc != null，如果为真，则跳转到分支A。

指令功能未使能，暂不可用。


0xa1	IMM16	jstricteqnull +AAAA	

默认入参：acc：值

A：有符号的分支偏移量

	

计算acc === null，如果为真，则跳转到分支A。

指令功能未使能，暂不可用。


0xa2	IMM16	jnstricteqnull +AAAA	

默认入参：acc：值

A：有符号的分支偏移量

	

计算acc !== null，如果为真，则跳转到分支A。

指令功能未使能，暂不可用。


0xa3	IMM16	jequndefined +AAAA	

默认入参：acc：值

A：有符号的分支偏移量

	

计算acc == undefined，如果为真，则跳转到分支A。

指令功能未使能，暂不可用。


0xa4	IMM16	jneundefined +AAAA	

默认入参：acc：值

A：有符号的分支偏移量

	

计算acc != undefined，如果为真，则跳转到分支A。

指令功能未使能，暂不可用。


0xa5	IMM16	jstrictequndefined +AAAA	

默认入参：acc：值

A：有符号的分支偏移量

	

计算acc === undefined，如果为真，则跳转到分支A。

指令功能未使能，暂不可用。


0xa6	IMM16	jnstrictequndefined +AAAA	

默认入参：acc：值

A：有符号的分支偏移量

	

计算acc !== undefined，如果为真，则跳转到分支A。

指令功能未使能，暂不可用。


0xa7	V8_IMM16	jeq vAA, +BBBB	

默认入参：acc：值

A：值

B：有符号的分支偏移量

	

计算acc == A，如果为真，则跳转到分支B。

指令功能未使能，暂不可用。


0xa8	V8_IMM16	jne vAA, +BBBB	

默认入参：acc：值

A：值

B：有符号的分支偏移量

	

计算acc != A，如果为真，则跳转到分支B。

指令功能未使能，暂不可用。


0xa9	V8_IMM16	jstricteq vAA, +BBBB	

默认入参：acc：值

A：值

B：有符号的分支偏移量

	

计算acc === A，如果为真，则跳转到分支B。

指令功能未使能，暂不可用。


0xaa	V8_IMM16	jnstricteq vAA, +BBBB	

默认入参：acc：值

A：值

B：有符号的分支偏移量

	

计算acc !== A，如果为真，则跳转到分支B。

指令功能未使能，暂不可用。


0xab	IMM16	getiterator RRRR	

默认入参：acc：对象

R：方舟运行时内部使用的16位保留数字

	执行GetIterator(acc, sync)方法，并将结果存放到acc中。
0xac	IMM16_V8	closeiterator RRRR, vAA	

R：方舟运行时内部使用的16位保留数字

A：对象

	以类型为iteratorRecord的A作为参数，执行IteratorClose，并将结果存放到acc中。
0xad	NONE	ldsymbol	-	加载Symbol对象到acc中。
0xae	NONE	asyncfunctionenter	-	创建一个异步函数对象，并将这个对象存放到acc中。
0xaf	NONE	ldfunction	-	将当前的函数对象加载到acc中。
0xb0	NONE	debugger	-	调试时用于暂停执行。
0xb1	V8	creategeneratorobj vAA	A：函数对象	使用函数对象A，创建一个generator，并将其存放到acc中。
0xb2	V8_V8	createiterresultobj vAA, vBB	

A：对象

B：布尔值

	以 value A和 done B作为参数，执行CreateIterResultObject，并将结果存放到acc中。
0xb3	IMM8_V8_V8	createobjectwithexcludedkeys +AA, vBB, vCC	

A：范围寄存器数量

B：对象

C, ..., C + A：属性键值

	

基于对象B，创建一个排除了键值C, ..., C + A的对象，并将其存放到acc中。

这个指令用于支持使用析构和扩展语法创建对象。


0xb4	IMM8_V8	newobjapply RR, vAA	

默认入参：acc：参数列表

R：方舟运行时内部使用的8位保留数字

A：类对象

	使用acc中存放的参数列表，创建一个A类的实例，并将其存放到acc中。
0xb5	IMM16_V8	newobjapply RRRR, vAA	

默认入参：acc：参数列表

R：方舟运行时内部使用的16位保留数字

A：类对象

	使用acc中存放的参数列表，创建一个A类的实例，并将其存放到acc中。
0xb6	IMM8_ID16	newlexenvwithname +AA, @BBBB	

A：词法环境中的槽位数量

B：literal id

	使用索引B对应的字面量数组中所存放的词法变量名称，创建一个具有A个槽位的词法环境，将这个词法环境存放到acc中，并进入该词法环境。
0xb7	V8	createasyncgeneratorobj vAA	A：函数对象	基于函数对象A，创建一个异步的generator，并将其存放到acc中。
0xb8	V8_V8_V8	asyncgeneratorresolve vAA, vBB, vCC	

A：生成器

B：对象

C：布尔值

	以 generator A, value B和 done C作为参数，执行AsyncGeneratorResolve，并将结果存放到acc中。
0xb9	IMM8_V8	supercallspread RR, vAA	

默认入参：acc：类对象

R：方舟运行时内部使用的8位保留数字

A：参数列表

	以参数列表A作为参数，调用acc中所存类的父类构造函数，并将结果存放到acc中。
0xba	IMM8_V8_V8	apply RR, vAA, vBB	

默认入参：acc：函数对象

R：方舟运行时内部使用的8位保留数字

A：对象

B：参数列表

	将this设置为A，以参数列表B作为参数，调用acc中存放的函数对象，并将返回值存放到acc中。
0xbb	IMM8_IMM8_V8	supercallarrowrange RR, +AA, vBB	

默认入参：acc：类对象

R：方舟运行时内部使用的8位保留数字

A：参数数量

B, ..., B + A - 1：参数

	

以B, ..., B + A - 1作为参数，调用acc中所存类的父类的构造函数，并将结果存放到acc中。

如果A的值为0，则B为undefined。

此指令仅出现在箭头函数中。


0xbc	V8_V8_V8_V8	definegettersetterbyvalue vAA, vBB, vCC, vDD	

默认入参：acc：是否需要为访问器设置名称，是一个布尔值

A：对象

B：属性键值

C：getter函数对象

D：setter函数对象

	

以getter方法 C和setter方法 D作为参数，定义对象A的键值为B的属性的访问器，并将结果对象存放到acc中。

如果C是undefined，则不会设置getter，如果D是undefined，则不会设置setter。


0xbd	NONE	dynamicimport	默认入参：acc：值	使用acc中的值作为参数，执行ImportCalls，并把结果存放到acc中。
0xbe	IMM16_ID16_IMM8	definemethod RRRR, @AAAA, +BB	

默认入参：acc：类对象或类对象的对象原型，方法为静态方法时，acc中是类对象

R：方舟运行时内部使用的16位保留数字

A：method id

B：方法A的形参数量

	创建方法A的函数对象，将acc中的对象设置为该函数对象的[[[HomeObject]]](https://262.ecma-international.org/12.0/#sec-ecmascript-function-objects)属性，并将该函数对象存放到acc中。
0xbf	NONE	resumegenerator	默认入参：acc：生成器	基于acc中存放的generator，执行GeneratorResume，并将结果存放到acc中。
0xc0	NONE	getresumemode	默认入参：acc：生成器	获取acc中所存放的generator的执行完成后恢复值的类型，并将其存放到acc中。
0xc1	IMM16	gettemplateobject RRRR	

默认入参：acc：对象

R：方舟运行时内部使用的16位保留数字

	执行GetTemplateObject(acc)，并将结果存放到acc中。
0xc2	V8	delobjprop vAA	

默认入参：acc：属性键值

A：对象

	删除对象A的键值为acc的属性。
0xc3	V8	suspendgenerator vAA	

默认入参：acc：值

A：生成器

	使用acc中所存放的值，挂起generator A，并将结果存放到acc中。
0xc4	V8	asyncfunctionawaituncaught vAA	

默认入参：acc：值

A：函数对象

	使用函数对象A和acc的值，执行AwaitExpression，并将结果存放到acc中。
0xc5	V8	copydataproperties vAA	

默认入参：acc：对象

A：目标对象

	将acc中所存放的对象的所有属性拷贝到A中，并将A存放到acc中。
0xc6	V8_V8	starrayspread vAA, vBB	

默认入参：acc：值

A：数组

B：数组索引

	将acc中的值按照SpreadElement的形式存放到数组A的以索引B起始的位置上，并将结果数组的长度存放到acc中。
0xc7	IMM16_V8	setobjectwithproto RRRR, vAA	

默认入参：acc：对象

R：方舟运行时内部使用的16位保留数字

A：值

	将acc中存放对象的 __proto__ 属性设置为A。
0xc8	IMM16_V8_V8	stownbyvalue RRRR, vAA, vBB	

默认入参：acc：值

R：方舟运行时内部使用的16位保留数字

A：对象

B：属性键值

	将acc中的值存放到对象A的键值为B的属性上。
0xc9	IMM8_V8_V8	stsuperbyvalue RR, vAA, vBB	

默认入参：acc：值

R：方舟运行时内部使用的8位保留数字

A：对象

B：属性键值

	在当前函数中，将acc中的值存放到super的键值为B的属性上。若该属性为访问器属性，则将A中的对象作为调用该属性setter函数时的this参数。
0xca	IMM16_V8_V8	stsuperbyvalue RRRR, vAA, vBB	

默认入参：acc：值

R：方舟运行时内部使用的16位保留数字

A：对象

B：属性键值

	在当前函数中，将acc中的值存放到super的键值为B的属性上。若该属性为访问器属性，则将A中的对象作为调用该属性setter函数时的this参数。
0xcb	IMM16_V8_IMM16	stownbyindex RRRR, vAA, +BBBB	

默认入参：acc：值

R：方舟运行时内部使用的16位保留数字

A：对象

B：属性键值

	将acc中的值存放到对象A的键值为B的属性上。
0xcc	IMM16_ID16_V8	stownbyname RRRR, @AAAA, vBB	

默认入参：acc：值

R：方舟运行时内部使用的16位保留数字

A：string id

B：对象

	将acc中的值存放到对象B的键值为索引A对应的字符串的属性上。
0xcd	V8	asyncfunctionresolve vAA	

默认入参：acc：值

A：异步的函数对象

	使用acc中的值，解析对象A的Promise对象，并将结果存放到acc中。
0xce	V8	asyncfunctionreject vAA	

默认入参：acc：值

A：异步的函数对象

	使用acc中的值，驳回对象A的Promise对象，并将结果存放到acc中。
0xcf	IMM8	copyrestargs +AA	A：形参列表中剩余参数所在的位次	复制剩余参数，并将复制出的参数数组副本存放到acc中。
0xd0	IMM8_ID16_V8	stsuperbyname RR, @AAAA, vBB	

默认入参：acc：值

R：方舟运行时内部使用的8位保留数字

A：string id

B：对象

	

在当前函数中，将acc中的值存放到super的键值为索引A对应的字符串的属性上。

若该属性为访问器属性，则将B中的对象作为调用该属性setter函数时的this参数。


0xd1	IMM16_ID16_V8	stsuperbyname RRRR, @AAAA, vBB	

默认入参：acc：值

R：方舟运行时内部使用的16位保留数字

A：string id

B：对象

	

在当前函数中，将acc中的值存放到super的键值为索引A对应的字符串的属性上。

若该属性为访问器属性，则将B中的对象作为调用该属性setter函数时的this参数。


0xd2	IMM16_V8_V8	stownbyvaluewithnameset RRRR, vAA, vBB	

默认入参：acc：函数对象

R：方舟运行时内部使用的8位保留数字

A：对象

B：属性键值

	将acc中的值存放到对象A的键值为B的属性上，并将函数的名称设置为B。
0xd3	ID16	ldbigint @AAAA	A：string id	基于索引A对应的字符串，创建BigInt类型的值，并将其存放到acc中。
0xd4	IMM16_ID16_V8	stownbynamewithnameset RRRR, @AAAA, vBB	

默认入参：acc：函数对象

R：方舟运行时内部使用的16位保留数字

A：string id

B：对象

	将acc中的函数对象存放到对象B的键值为索引A对应的字符串的属性上，并将函数的名称设置为索引A对应的字符串。
0xd5	NONE	nop	-	无操作。
0xd6	IMM8	setgeneratorstate +AA	

默认入参：acc：生成器对象

A：生成器状态

	

将acc中存放的generator的状态设置为A (参考：GeneratorState和AsyncGeneratorState)

A可能的值有以下几项：undefined(0x0)、suspendedStart(0x1)、suspendedYield(0x2)、executing(0x3)、completed(0x4)和awaitingReturn(0x5)。


0xd7	IMM8	getasynciterator RR	

默认入参：acc：对象

R：方舟运行时内部使用的8位保留数字

	执行GetIterator(acc, async)，并将结果存放到acc上。
0xd8	IMM8_IMM16_IMM16	ldprivateproperty RR, +AAAA, +BBBB	

默认入参：acc：对象

A：词法环境层级

B：槽位号

	加载A个层次外的词法环境的B号槽位上的值，作为属性键值，将acc中所存放对象的该键值对应的值存放到acc中。
0xd9	IMM8_IMM16_IMM16_V8	stprivateproperty RR, +AAAA, +BBBB, vCC	

A：词法环境层级

B：槽位号

C：对象

	加载A个层次外的词法环境的B号槽位上的值，作为属性键值，将acc中的值存放到C中所存放对象的该键值上。
0xda	IMM8_IMM16_IMM16	testin RR, +AAAA, +BBBB	

默认入参：acc：对象

A：词法环境层级

B：槽位号

	加载A个层次外的词法环境的B号槽位上的值，计算是否in acc，将结果存放到acc中。
0xdb	IMM8_ID16_V8	definefieldbyname RR, @AAAA, vBB	

默认入参：acc：值

A：string id

B：对象

	为对象B定义一个键值为A的属性，并将acc中的值存放到其中。
0xdc	IMM8_ID16_V8	definepropertybyname RR, @AAAA, vBB	

默认入参：acc：值

A：string id

B：对象

	为对象B定义一个键值为A的属性，并将acc中的值存放到其中。
0xfb	PREF_NONE	callruntime.notifyconcurrentresult	默认入参：acc：并发函数的返回值	

将并发函数的返回值通知运行时。

此指令仅出现在并发函数中。


0xfc	(deprecated)	-	-	（弃用的操作码）
0xfd	PREF_IMM16_V8_V8	wide.createobjectwithexcludedkeys +AAAA, vBB, vCC	

A：范围寄存器数量

B：对象

C, ..., C + A：属性键值

	

基于对象B，创建一个排除了键值C, ..., C + A的对象，并将其存放到acc中。

这个指令用例支持使用析构和扩展语法创建对象。


0xfe	PREF_NONE	throw	默认入参：acc：异常	抛出acc中存放的异常。
0x01fb	PREF_IMM8_V8_V8	callruntime.definefieldbyvalue RR, vAA, vBB	

默认入参：acc：值

A：属性键值

B：对象

	为对象B定义一个键值为A的属性，并将acc中的值存放到其中。
0x01fc	(deprecated)	-	-	（弃用的操作码）
0x01fd	PREF_IMM16_V8	wide.newobjrange +AAAA, vBB	

A：参数数量

B：类对象

B + 1, ..., B + A - 1：传递给构造函数的参数

	以B + 1, ..., B + A - 1作为参数，创建一个B类的实例，并将其存放到acc中。
0x01fe	PREF_NONE	throw.notexists	-	抛出异常：未定义的方法。
0x02fb	PREF_IMM8_IMM32_V8	callruntime.definefieldbyindex RR, +AAAAAAAA, vBB	

默认入参：acc：值

A：属性键值

B：对象

	为对象B定义一个键值为A的属性，并将acc中的值存放到其中。
0x02fc	(deprecated)	-	-	（弃用的操作码）
0x02fd	PREF_IMM16	wide.newlexenv +AAAA	A：词法环境中的槽位数目	创建一个槽位数为A的词法环境，将其存放到acc中，并进入该词法环境。
0x02fe	PREF_NONE	throw.patternnoncoercible	-	抛出异常：此对象不可以强制执行。
0x03fb	PREF_NONE	callruntime.topropertykey	默认入参：acc：值	将acc中的值转换为属性值，如果转换失败，则抛出错误。
0x03fc	(deprecated)	-	-	（弃用的操作码）
0x03fd	PREF_IMM16_ID16	wide.newlexenvwithname +AAAA, @BBBB	

A：词法环境中的槽位数量

B：literal id

	使用索引B对应的字面量数组中所存放的词法变量名称，创建一个具有A个槽位的词法环境，将这个词法环境存放到acc中，并进入该词法环境。
0x03fe	PREF_NONE	throw.deletesuperproperty	-	抛出异常：删除父类的属性。
0x04fb	PREF_IMM_16_ID16	callruntime.createprivateproperty +AAAA, @BBBB	

A：要创建的符号数量

B：literal id

	

创建A个符号；从索引B对应的字面量数组中获取存放的私有方法，如果其中存在私有实例方法，则额外创建一个符号（"method"），将所有创建出的符号按照创建顺序，依次放到当前类所在的词法环境的末尾。

此指令仅出现在定义类的时候。


0x04fc	(deprecated)	-	-	（弃用的操作码）
0x04fd	PREF_IMM16_V8	wide.callrange +AAAA, vBB	

默认入参：acc：函数对象

A：参数数量

B, ..., B + A - 1：参数

	以B, ..., B + A - 1作为参数，调用acc中存放的函数对象，并将结果存放到acc中。
0x04fe	PREF_V8	throw.constassignment vAA	A：常量变量的名称	抛出异常：对常量变量进行赋值。
0x05fb	PREF_IMM8_IMM_16_IMM_16_V8	callruntime.defineprivateproperty RR, +AAAA, +BBBB, vCC	

默认入参：acc：值

A：词法环境层数

B：槽位号

C：对象

	加载A个层次外的词法环境的B号槽位上的符号，赋值为acc，将其作为私有属性添加到对象C上。
0x05fc	(deprecated)	-	-	（弃用的操作码）
0x05fd	PREF_IMM16_V8	wide.callthisrange +AAAA, vBB	

默认入参：acc：函数对象

A：参数数量

B：对象

B + 1, ..., B + A：参数

	将this的值设置为B，以B + 1，...，B + A作为参数，调用acc中存放的函数对象，并将计算结果存放到acc中。
0x05fe	PREF_V8	throw.ifnotobject vAA	A：对象	如果A不是一个对象，抛出异常。
0x06fb	PREF_IMM8_V8	callruntime.callinit +RR, vAA	

acc：函数对象

R：方舟运行时内部使用的8位保留数字

A：对象

	将this的值设置为A，不传递参数，调用acc中存放的函数对象，并将结果存放到acc中。
0x06fc	(deprecated)	-	-	（弃用的操作码）
0x06fd	PREF_IMM16_V8	wide.supercallthisrange +AAAA, vBB	

A：参数数量

B, ..., B + A - 1：参数

	

以B, ..., B + A - 1作为参数, 调用super函数，并将结果存放到acc中。

当A的值是0时，B是undefined。

此指令仅出现在非箭头函数中。


0x06fe	PREF_V8_V8	throw.undefinedifhole vAA, vBB	

A：对象

B：对象名称

	如果A的值是hole，则抛出异常：B的值是undefined。
0x07fb	PREF_IMM16_ID16_ID16_IMM16_V8	callruntime.definesendableclass RRRR, @AAAA, @BBBB, +CCCC, vDD	

R：方舟运行时内部使用的16位保留数字

A：sendable class的构造函数的method id

B：literal id

C：方法A的形参数量

D：父类

	使用索引B对应的字面量数组和父类D，创建一个A类的对象，并将其存放到acc中。
0x07fc	(deprecated)	-	-	（弃用的操作码）
0x07fd	PREF_IMM16_V8	wide.supercallarrowrange +AAAA, vBB	

默认入参：acc：类对象

A：参数数量

B, ..., B + A - 1:参数

	

以B, ..., B + A - 1作为参数，调用acc中所存类的父类的构造函数，并将结果存放到acc中。

如果A的值为0，则B为undefined。

此指令仅出现在箭头函数中。


0x07fe	PREF_IMM8	throw.ifsupernotcorrectcall +AA	

默认入参：acc：对象

A：错误种类

	如果super没有被正确调用，抛出错误。
0x08fb	PREF_IMM16	callruntime.ldsendableclass +AAAA	A：词法环境层级	将A个层次外的词法环境的sendable class存放到acc中。
0x08fc	(deprecated)	-	-	（弃用的操作码）
0x08fd	PREF_IMM32	wide.ldobjbyindex +AAAAAAAA	

默认入参：acc：对象

A：属性键值

	加载acc中所存对象的键值为A的属性，并将其存放到acc中。
0x08fe	PREF_IMM16	throw.ifsupernotcorrectcall +AAAA	

默认入参：acc：对象

A：错误种类

	如果super没有被正确调用，抛出错误。
0x09fb	PREF_IMM8	callruntime.ldsendableexternalmodulevar +AA	A：槽位号	将槽位号为A的外部模块变量存放到acc中。此指令仅出现在sendable class和sendable function中。
0x09fc	(deprecated)	-	-	（弃用的操作码）
0x09fd	PREF_V8_IMM32	wide.stobjbyindex vAA, +BBBBBBBB	

默认入参：acc：值

A：对象

B：属性键值

	将acc中的值存放到对象A的键值为B的属性上。
0x09fe	PREF_ID16	throw.undefinedifholewithname @AAAA	

默认入参：acc：对象

A：string id

	如果acc中的值是hole，则抛出异常：A的值是undefined。
0x0afb	PREF_IMM16	callruntime.wideldsendableexternalmodulevar +AAAA	A：槽位号	将槽位号为A的外部模块变量存放到acc中。此指令仅出现在sendable class和sendable function中。
0x0afc	(deprecated)	-	-	（弃用的操作码）
0x0afd	PREF_V8_IMM32	wide.stownbyindex vAA, +BBBBBBBB	

默认入参：acc：值

A：对象

B：属性键值

	将acc中的值存放到对象A的键值为B的属性上。
0x0bfb	PREF_IMM8	callruntime.newsendableenv +AA	A：共享词法环境中的槽位数目	创建一个槽位数为A的共享词法环境，并进入该词法环境。
0x0bfc	(deprecated)	-	-	（弃用的操作码）
0x0bfd	PREF_IMM16	wide.copyrestargs +AAAA	A：形参列表中剩余参数起始的位次	复制剩余参数，并将复制出的参数数组副本存放到acc中。
0x0cfb	PREF_IMM16	callruntime.widenewsendableenv +AAAA	A：共享词法环境中的槽位数目	创建一个槽位数为A的共享词法环境，并进入该词法环境 。
0x0cfc	(deprecated)	-	-	（弃用的操作码）
0x0cfd	PREF_IMM16_IMM16	wide.ldlexvar +AAAA, +BBBB	

A：词法环境层级

B：槽位号

	将A个层次外的词法环境的B号槽位上的值存放到acc中。
0x0dfb	PREF_IMM4_IMM4	callruntime.stsendablevar +A +B	

默认入参：acc：值

A：共享词法环境层级

B：槽位号

	将acc中的值存放到A个层次外的共享词法环境的B号槽位上。
0x0dfc	(deprecated)	-	-	（弃用的操作码）
0x0dfd	PREF_IMM16_IMM16	wide.stlexvar +AAAA, +BBBB	

默认入参：acc：值

A：词法环境层级

B：槽位号

	将acc中的值存放到A个层次外的词法环境的B号槽位上。
0x0efb	PREF_IMM8_IMM8	callruntime.stsendablevar +AA +BB	

默认入参：acc：值

A：共享词法环境层级

B：槽位号

	将acc中的值存放到A个层次外的共享词法环境的B号槽位上 。
0x0efc	(deprecated)	-	-	（弃用的操作码）
0x0efd	PREF_IMM16	wide.getmodulenamespace +AAAA	A：模块索引	对第A个模块，执行GetModuleNamespace，并将结果存放到acc中。
0x0ffb	PREF_IMM16_IMM16	callruntime.widestsendablevar +AAAA +BBBB	

默认入参：acc：值

A：共享词法环境层级

B：槽位号

	将acc中的值存放到A个层次外的共享词法环境的B号槽位上。
0x0ffc	(deprecated)	-	-	（弃用的操作码）
0x0ffd	PREF_IMM16	wide.stmodulevar +AAAA	

默认入参：acc：值

A：槽位号

	将acc中的值存放到槽位号为A的模块变量中。
0x10fb	PREF_IMM4_IMM4	callruntime.ldsendablevar +A +B	

A：共享词法环境层级

B：槽位号

	将A个层次外的共享词法环境的B号槽位上的值存放到acc中。
0x10fc	(deprecated)	-	-	（弃用的操作码）
0x10fd	PREF_IMM16	wide.ldlocalmodulevar +AAAA	A：槽位号	将槽位号为A的局部模块变量存放到acc中。
0x11fb	PREF_IMM8_IMM8	callruntime.ldsendablevar +AA + BB	

A：共享词法环境层级

B：槽位号

	将A个层次外的共享词法环境的B号槽位上的值存放到acc中。
0x11fc	(deprecated)	-	-	（弃用的操作码）
0x11fd	PREF_IMM16	wide.ldexternalmodulevar +AAAA	A：槽位号	将槽位号为A的外部模块变量存放到acc中。
0x12fb	PREF_IMM16_IMM16	callruntime.wideldsendablevar +AAAA +BBBB	

A：共享词法环境层级

B：槽位号

	将A个层次外的共享词法环境的B号槽位上的值存放到acc中。
0x12fc	(deprecated)	-	-	（弃用的操作码）
0x12fd	PREF_IMM16	wide.ldpatchvar +AAAA	A：补丁变量槽位号	

将槽位号为A的补丁变量加载到acc中。

此指令仅出现在补丁模式编译场景下。


0x13fb	PREF_IMM8	callruntime.istrue +RR	

默认入参：acc：操作数

R：方舟运行时内部使用的8位保留数字

	计算acc == true，并将计算结果存放到acc中。
0x13fc	(deprecated)	-	-	（弃用的操作码）
0x13fd	PREF_IMM16	wide.stpatchvar +AAAA	

默认入参：acc：值

A：补丁变量槽位号

	

将acc中的值存放进槽位号为A的补丁变量中。

此指令仅出现在补丁模式编译场景下。


0x14fb	PREF_IMM8	callruntime.isfalse +RR	

默认入参：acc：操作数

R：方舟运行时内部使用的8位保留数字

	计算acc == false，并将计算结果存放到acc中。
0x15fb	PREF_IMM8	callruntime.ldlazymodulevar +AA	A：槽位号	将槽位号为A的外部模块变量存放到acc中。此指令仅适用于通过lazy import导入的模块变量。
0x16fb	PREF_IMM16	callruntime.wideldlazymodulevar +AAAA	A：槽位号	将槽位号为A的外部模块变量存放到acc中。此指令仅适用于通过lazy import导入的模块变量。
0x17fb	PREF_IMM8	callruntime.ldlazysendablemodulevar +AA	A：槽位号	将槽位号为A的外部模块变量存放到acc中。此指令仅适用于通过lazy import导入的模块变量且仅出现在sendable class和sendable function中。
0x18fb	PREF_IMM16	callruntime.wideldlazysendablemodulevar +AAAA	A：槽位号	将槽位号为A的外部模块变量存放到acc中。此指令仅适用于通过lazy import导入的模块变量且仅出现在sendable class和sendable function中。


0x14fc

0x15fc

...

0x2efc

	(deprecated)	-	-	（弃用的操作码）
方舟字节码文件格式
方舟字节码函数命名规则
