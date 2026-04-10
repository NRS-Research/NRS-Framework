NRS-Framework / 国家韧性盈余框架

National Resilience Surplus Framework

An open-source implementation of the analytical core from The War of Guardians: Wealth, Power, and the Future of Nations. This framework operationalizes the National Resilience Surplus theory, transforming it from a strategic philosophical model into a verifiable, extensible, and collaborative analytical system for measuring and forecasting national strategic health.

本书《守护的战争：财富、权力与国家的未来》核心理论的代码实现。本框架将“国家韧性盈余”理论从一个战略哲学模型，转化为一套可验证、可扩展、可协作的，用于衡量与前瞻国家战略健康的开源分析系统。

One-Sentence Vision / 核心愿景

This project provides the open-source "dynamic operating system" for national strategic health, enabling anyone to quantify a nation's true wealth—its Resilience Surplus W—by calculating the net balance between its systemic potential (C∘D∘P∘Gᴰ)×S and its inevitable internal dissipation H_g, and to monitor its vital trends W', W'', and long-term trajectory ∫W dt.

本项目提供了一个开源的“国家战略健康动态操作系统”。它使任何人都能通过计算一个国家系统总潜能(C∘D∘P∘Gᴰ)×S与其必然的内部耗散H_g之间的净平衡，来量化其真正的财富——韧性盈余W，并监测其生命体征趋势W'、W''及长期轨迹∫W dt。

What's in this Repository? / 仓库内容

This repository contains all the necessary components to audit, replicate, extend, and apply the core analytical framework presented in the book.

本仓库包含了审计、复现、扩展和应用书中核心分析框架所需的所有组件。

•   /data/: Contains processed datasets and source references. / 包含已处理的数据集和来源参考。

    ◦   processed/: Key results, including the core indicator table (SSI, H_g, W for major nations, 2000-2023) and source data for the book's central charts. / 关键结果，包括核心指标表（主要国家2000-2023年的SSI、H_g、W值）及书中核心图表的源数据。

    ◦   metadata/: Detailed data dictionaries and sourcing information. / 详细的数据字典和来源信息。

•   /code/: The analytical engine. / 分析引擎。

    ◦   01_data_collection/: Scripts to fetch and pre-process raw data from primary sources (e.g., World Bank, SIPRI, IMF). / 从原始来源（如世界银行、SIPRI、IMF）获取和预处理数据的脚本。

    ◦   02_calculation/: Modular functions to compute the Sovereign Strength Index (SSI), Wealth Guarding Entropy (H_g), and the Resilience Surplus (W) and its derivatives. / 计算主权强度指数(SSI)、财富守护熵(H_g)、韧性盈余(W)及其导数的模块化函数。

    ◦   03_visualization/: Scripts to reproduce the book's key figures (e.g., US-China W trend comparison). / 复现书中关键图形（如中美W趋势对比）的脚本。

Quick Start: Reproduce a Key Chart in 5 Minutes / 快速开始：5分钟复现核心图表

Follow these steps to generate the central "US-China Resilience Surplus (W) Trend Comparison" chart from the book.

按照以下步骤生成书中的核心图表——“中美韧性盈余(W)趋势对比图”。

1. Clone the repository and set up the environment. / 克隆仓库并设置环境。
git clone https://github.com/NRS-Research/NRS-Framework.git
cd NRS-Framework
pip install -r code/requirements.txt


2. Run the visualization script. / 运行可视化脚本。
Navigate to the code/03_visualization/ directory and execute the provided script:
进入 code/03_visualization/ 目录并执行提供的脚本：
python plot_us_china_w_trend.py

This script will automatically use the pre-processed data in /data/processed/ to calculate the W values for the US and China and generate a comparative time-series plot, saving it as us_china_w_trend.png in your current directory.

该脚本将自动使用 /data/processed/ 中的预处理数据计算美国和中国的W值，并生成对比时间序列图，保存为当前目录下的 us_china_w_trend.png。

3. (Optional) Run the full pipeline. / （可选）运行完整流程。
To start from raw data, run the data collection and calculation pipelines first. Detailed instructions are in the /docs/methodology.md file.

若希望从原始数据开始，请先运行数据收集和计算流程。详细说明在 /docs/methodology.md 文件中。

Join the Global Thought Laboratory / 加入全球思想实验室

This framework is designed not as a finished product, but as a foundational protocol for a global community. We invite you to scrutinize, challenge, and improve it.

本框架并非一个成品，而是为全球社区设计的基础协议。我们邀请您来审查、挑战并改进它。

•   Start a Discussion: Have a question about the methodology, a suggestion for a new indicator, or a theoretical critique? Open an https://github.com/NRS-Research/NRS-Framework/issues using the discussion label. / 发起讨论：对方法论有疑问、有新指标建议或理论批判？请使用 discussion 标签开启一个https://github.com/NRS-Research/NRS-Framework/issues

•   Contribute Code or Analysis: Improved a calculation function, added a new country module, or conducted a novel case study? Please read our CONTRIBUTING.md guide and submit a Pull Request. / 贡献代码或分析：改进了计算函数、增加了新国家模块或进行了新颖的案例研究？请阅读我们的CONTRIBUTING.md指南并提交拉取请求。

•   Report Bugs: Found an error in data or code? Open an https://github.com/NRS-Research/NRS-Framework/issues with the bug label. / 报告错误：发现数据或代码错误？请使用 bug 标签开启一个https://github.com/NRS-Research/NRS-Framework/issues

How to Cite / 引用说明

To cite the book (the primary source): / 引用本书（主要来源）：
谢锋. (2026). The War of Guardians: Wealth, Power, and the Future of Nations. Publisher.

To cite this software/code repository: / 引用本软件/代码仓库：
NRS-Research. (2026). NRS-Framework (Version 1.0.0) [Computer software]. https://github.com/NRS-Research/NRS-Framework

This repository is the executable counterpart to the strategic philosophy presented in "The War of Guardians." It embodies the core principle of moving from a "monument of scholarship" to a "sharp instrument of thought."

本仓库是《守护的战争》中所阐述战略哲学的可执行对应物。它体现了从“学术丰碑”到“思想利器”跃迁的核心原则。
