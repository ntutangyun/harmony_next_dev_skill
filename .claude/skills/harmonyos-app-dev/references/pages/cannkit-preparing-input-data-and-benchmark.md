# 输入数据和标杆数据准备

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-preparing-input-data-and-benchmark_

在算子信息json配置文件中，将gen_data配置为false，data_file配置为输入数据、标杆数据对应的路径（必须为绝对路径），示例如下。

{
    "gen_data": false,
    "inputs": [
        {
            "data_file": "/path/to/input_data_q.bin"
        }
    ],
    "outputs": [
        {
            "data_file": "/path/to/golden_data_out.bin"
        }
    ]
}

若外部提供的数据是.pt文件，需要转换为.bin文件，以PyTorch为例：

import torch
model = torch.load('model.pt')   # 加载.pt文件
torch.save(model, 'model.bin')   # 将模型参数保存为二进制文件

方式2：采用已生成过的input/golden数据，无需重新生成。

当开发者需要多次重跑，建议直接使用历史生成的数据，避免重复生成，导致调测耗时过长。

在算子信息json配置文件中，将gen_data配置为false，data_file配置为输入数据、标杆数据对应的bin文件名（不含路径信息，默认在当前路径下查找数据文件），示例如下。

{
    "gen_data": false,
    "inputs": [
        {
            "data_file": "input_data_q.bin"
        }
    ],
    "outputs": [
        {
            "data_file": "golden_data_out.bin"
        }
    ]
}

方式3：采用工具随机生成input数据。

开发者未准备任何数据，可采用工具随机生成的input数据，生成的bin数据文件默认在当前路径下的对应算子的data文件夹中。该场景下没有golden数据，因此不支持精度比对。

在算子信息json配置文件中，将gen_data配置为true，data_script配置为空字符串或null，data_file配置为输入数据、标杆数据对应的bin文件名（不含路径信息，默认在当前路径下查找数据文件），示例如下。

"data_script": "",
"gen_data": true,


"shape": [1, 16384],
"data_file": "sample.bin",

方式4：采用脚本生成input/golden数据。

开发者自行准备数据生成脚本（一般是.py文件），同时配置算子信息json配置文件。

将gen_data配置为true，data_script配为数据生成脚本路径（以FlashAttentionScore算子为例），data_file配置为输入数据、标杆数据对应的bin文件名（不含路径信息，默认在当前路径下查找数据文件），示例如下。

"data_script": "${fa_case_dir}/flash_attention_score_golden.py",
"gen_data": true,


"data_file": "sample.bin",

生成数据时，会调用该脚本，并固定传入以下参数：

sys.argv[1]：输入的算子json配置文件。

sys.argv[2]：输出bin文件路径（工作路径下的data文件夹，例如debug_workspace/FlashAttentionScore/data/）。

开发者需要根据输入的sys.argv[1]读取算子json配置文件内容，获取生成数据所需的算子shape信息、数据文件的文件名，并在脚本中适配生成的文件名。
开发者需要根据输入的sys.argv[2]设置存放input/output数据文件的路径，将生成的文件保存到该路径下。
数据准备和配置说明
算子json配置模板获取
