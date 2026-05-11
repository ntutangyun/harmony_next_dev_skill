# @typescript

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_strict-boolean-expressions_

// nullable values should be checked explicitly against null or undefined
function getNum(): number | undefined {
  return undefined;
}


const num: number | undefined = getNum();
if (num !== undefined) {
  console.log('num is defined');
}


function getStr(): string | null {
  return 'null';
}


const str: string | null = getStr();
if (str !== null) {
  console.log('str is not empty');
}
反例
// nullable values should be checked explicitly against null or undefined
function getNum(): number | undefined {
  return undefined;
}


const num: number | undefined = getNum();
if (num) {
  console.log('num is defined');
}


function getStr(): string | null {
  return 'null';
}


const str: string | null = getStr();
if (str) {
  console.log('str is not empty');
}
规则集
plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@typescript-eslint/space-infix-ops
@typescript-eslint/switch-exhaustiveness-check
