---
layout: default
title: "Reproducible Computational Environments."
---

# Cersonsky Lab Commandments for Reproducible Computational Environments.

Creating reproducible environments is a longstanding challenge in computational sciences. Often, the diverse software tools and its complex interactions with various hardware makes it difficult to guarantee that software can work on multiple users' machines. In addition, future members of the lab may need to see or run your code, even if its dependencies are no longer being maintained. Thus having a framework for managing projects and their dependencies is important.

In our lab, we use [`git`](https://git-scm.com/), [‘GitHub’], and [`pixi`](https://pixi.sh/latest/) for managing projects on a per-project basis. Git is a tool for version control, which can be used for saving states of a project. We recommend going through the tutorial [‘here’], which covers the most important commands for git. Many popular IDEs, such as VSCode, also contain some sort of git integration.

GitHub is a web service that integrates with git. GitHub allows us to host repositories (projects made with git) online and share projects and code with others. Repositories hosted on GitHub should be kept private until ready to publish.

Pixi is a tool that aims to simplify environment management and create reproducible setups. It combines many of the best features of older package managers like `conda` or `pip`, and is faster than both. Notable aspects include:

1. Seamless integration and installation from different package indices (e.g. `conda-forge`, `PyPi`), and can automatically resolve the dependency tree. 
2. Pixi creates and updates a lockfile that enables reproducible workflows.
3. Pixi environments are easy to reproduce on systems of different architectures, including CHTC workflows.

Please follow these steps for [installation and documentation](https://pixi.sh/latest).

**Note**: If you are adding Pixi to an existing python software project with a `pyproject.toml`, running the usual `pixi init` command in your root directory will append Pixi related tables to the end of `pyproject.toml`. This is fine.

It is recommended that multiple collaborators working on the same project use the same Pixi environment. This eliminates the chance of issues arising from differing dependencies between machines, thus making it easier to collaborate and reproduce code.
