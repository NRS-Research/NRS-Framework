CONTRIBUTING.md

贡献者指南

Thank you for your interest in contributing to the National Resilience Surplus Framework (NRS-Framework)! This document outlines the process for collaborating on this open-source analytical system. We welcome contributions that enhance the framework’s methodology, data, code, documentation, and applications.

感谢您对国家韧性盈余框架 (NRS-Framework) 开源分析系统的贡献意向！本文档旨在阐明协作流程，欢迎您为改进本框架的方法论、数据、代码、文档及应用贡献力量。

1. Collaboration Process | 协作流程

1.1. Reporting Issues | 提交议题

We use GitHub Issues to track bugs, enhancements, discussions, and data requests.
我们使用 GitHub Issues 来追踪错误、功能改进、学术讨论和数据请求。

•   Before submitting, please check if a similar issue already exists.

•   提交前，请先检查是否已有类似议题。

•   Use clear, descriptive titles and provide as much context as possible (e.g., expected vs. actual behavior, error messages, steps to reproduce).

•   请使用清晰、描述性的标题，并提供尽可能多的背景信息（例如，预期与实际情况、错误信息、复现步骤）。

•   Use labels appropriately (e.g., bug, enhancement, discussion, data-request).

•   请正确使用标签（如 bug, enhancement, discussion, data-request）。

1.2. Contributing Code or Data | 贡献代码或数据

We follow the Fork-and-Pull Request (PR) workflow.
我们遵循 Fork（派生）与拉取请求 (PR) 的工作流。

1.  Fork the repository to your own GitHub account.
1.  派生 (Fork) 本仓库到您的 GitHub 账户下。
2.  Clone your fork locally and create a new branch for your work (git checkout -b feature/your-feature-name).
2.  克隆您的派生仓库到本地，并为您的工作创建一个新的分支 (git checkout -b feature/您的功能名称)。
3.  Make your changes, adhering to the coding and data standards below.
3.  进行您的修改，并遵循下文所述的代码与数据标准。
4.  Commit your changes with clear, descriptive commit messages.
4.  提交您的更改，并附上清晰、描述性的提交信息。
5.  Push to your fork and then open a Pull Request (PR) against the main branch of the original NRS-Framework repository.
5.  推送 (Push) 到您的派生仓库，然后向原始 NRS-Framework 仓库的 main 分支发起一个拉取请求 (PR)。
6.  In your PR description, please:
6.  在您的 PR 描述中，请：
    ◦   Clearly describe the purpose and changes of the PR.

    ◦   清晰描述 PR 的目的和变更内容。

    ◦   Link to any related issues (e.g., “Closes #123”).

    ◦   关联到任何相关的议题（例如，“Closes #123”）。

    ◦   Ensure all automated checks (if any) pass.

    ◦   确保所有自动化检查（如有）通过。

2. Code & Data Standards | 代码与数据标准

2.1. Code Style | 代码风格

•   Language: Primary languages are Python and R. Please use the dominant language in the directory you’re modifying.

•   语言：主要语言为 Python 和 R。请使用您所修改目录中主导的语言。

•   Python: Follow https://www.python.org/dev/peps/pep-0008/ style guide. Use meaningful variable/function names and include docstrings for public functions/classes.

•   Python：遵循 https://www.python.org/dev/peps/pep-0008/ 风格指南。使用有意义的变量/函数名，并为公共函数/类包含文档字符串 (docstrings)。

•   R: Follow the http://style.tidyverse.org/.

•   R：遵循 http://style.tidyverse.org/。

•   Documentation: Comment your code to explain the “why,” not just the “what,” especially for complex logic.

•   文档：为代码添加注释，解释“为什么”，而不仅仅是“是什么”，特别是对于复杂逻辑。

2.2. Data Standards | 数据标准

•   Data Submission: For new or updated datasets, please submit them to the appropriate directory under /data/.

•   数据提交：对于新的或更新的数据集，请将其提交到 /data/ 下适当的目录中。

•   Format: Prefer open, non-proprietary formats (e.g., .csv, .parquet over .xlsx). Use UTF-8 encoding.

•   格式：优先使用开放、非专有格式（例如，首选 .csv, .parquet 而非 .xlsx）。使用 UTF-8 编码。

•   Metadata: Any new dataset must be accompanied by a README.md or data_dictionary.csv file in the same directory, describing the source, methodology, variables, units, and any processing steps.

•   元数据：任何新数据集必须在同一目录下附带一个 README.md 或 data_dictionary.csv 文件，描述其来源、方法论、变量、单位及任何处理步骤。

•   Provenance: Clearly document the original source (with a permanent URL/DOI if possible) and the steps taken to clean/transform the data. Scripts for data processing should be placed in /code/01_data_collection/.

•   来源：清晰记录原始来源（如有可能，提供永久链接/DOI）以及数据清洗/转换的步骤。数据处理脚本应放置在 /code/01_data_collection/ 中。

3. Discussion Norms | 讨论规范

We strive to foster a constructive, evidence-based, and inclusive community.
我们致力于营造一个建设性、基于证据且包容的社区环境。

•   Be Respectful: Engage with others professionally and courteously, even in disagreement.

•   互相尊重：即使存在分歧，也请以专业和礼貌的方式与他人交流。

•   Evidence-Based: When proposing changes to the core theory or methodology, ground your arguments in empirical evidence, logical reasoning, or references to established literature.

•   基于证据：当提议对核心理论或方法论进行修改时，请基于实证证据、逻辑推理或对现有文献的引用来阐述您的观点。

•   Focus on Ideas: Critique ideas, not individuals.

•   聚焦观点：对观点提出批评，而非针对个人。

•   Clarity is Key: Strive for clear and concise communication to facilitate productive dialogue.

•   清晰是关键：力求清晰、简洁的沟通，以促进富有成效的对话。

4. Contributor Recognition | 贡献者认可

We deeply value all forms of contribution. Contributors will be recognized in the following ways:
我们高度重视所有形式的贡献。贡献者将通过以下方式获得认可：

•   Contributor List: Significant contributors (those with merged PRs, substantive issue discussions, or major documentation improvements) will be acknowledged in the repository’s CONTRIBUTORS.md file (or similar) and in future publications/releases stemming from this project, subject to their consent.

•   贡献者名单：重要贡献者（其 PR 被合并、进行了实质性的议题讨论，或对文档有重大改进）将在仓库的 CONTRIBUTORS.md 文件（或类似文件）以及本项目未来的出版物/版本中获得致谢（需经其本人同意）。

•   Transparency: All contributions are publicly recorded in the commit history and issue/PR tracker.

•   透明度：所有贡献都公开记录在提交历史和议题/PR追踪器中。

By participating in this project, you agree to abide by these guidelines and to foster a collaborative and respectful environment for all.
通过参与本项目，您同意遵守本指南，并为所有人营造一个协作、尊重的环境。
