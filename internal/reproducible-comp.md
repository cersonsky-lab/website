---
layout: default
title: "Reproducible Computational Environments."
---

# Cersonsky Lab Commandments for Reproducible Computational Environments.

Creating reproducible environments is a longstanding challenge in computational sciences. Often, the diverse software tools and their complex interactions with various hardware makes it difficult to guarantee that software can work on multiple users' machines. In addition, future members of the lab may need to see or run your code, even if its dependencies are no longer being maintained. Thus having a framework for managing projects and their dependencies is important.

In our lab, we use [`git`](https://git-scm.com/), [`GitHub`](https://github.com/), and [`pixi`](https://pixi.sh/latest/) for managing projects on a per-project basis. Note that historically, we have used [`conda`](https://docs.conda.io/en/latest/) for environment management, but the Cersonsky Lab aims to be early adopters of the `pixi` tool, and we find it very promising and exciting.

Git is a tool for version control, which can be used for saving states of a project. We recommend going through the [git tutorial](https://education.molssi.org/python-package-best-practices/02-git.html) which covers the most important commands for git. Many popular IDEs, such as VSCode, also contain some sort of git integration.

GitHub is a web service that integrates with git. GitHub allows us to host repositories (projects made with git) online and share projects and code with others. Repositories hosted on GitHub should be kept private until ready to publish. Please see read the tutorials [on GitHub](https://education.molssi.org/python-package-best-practices/03-github.html) and [on code collaboration with GitHub](https://education.molssi.org/python-package-best-practices/07-collaboration.html).

Pixi is a tool that aims to simplify environment management and create reproducible setups. It combines many of the best features of older package managers like `conda` or `pip`, and is faster than both. Notable aspects include:

1. Seamless integration and installation from different package indices (e.g. `conda-forge`, `PyPi`), and can quickly and automatically resolve complex dependency trees. 
2. Creating and updating a lockfile that enables reproducible workflows.
3. Easy reproducibility on systems of different architectures, including CHTC workflows.

Please follow these steps for [`pixi` installation and documentation](https://pixi.sh/latest).

**Note**: If you are adding Pixi to an existing python software project with a `pyproject.toml`, running the usual `pixi init` command in your root directory will append Pixi related tables to the end of `pyproject.toml`. This is fine.

It is recommended that multiple collaborators working on the same project use the same Pixi environment. This eliminates the chance of issues arising from differing dependencies between machines, thus making it easier to collaborate and reproduce code.

A useful template for some `pixi` commands to set up a multiplatform, multienvironment `pixi` config files is show below. Specifically, this config file allows one to install either CPU or GPU versions of the same environment, depending on the available hardware and platform. This material is taken from the [Reproducible Machine Learning Workflows for Scientists Workshop](https://indico.global/event/14982/), held at UW Madison August 12-14, 2025. Specifically, what's shown below is the solution to the challenge in the [CUDA use with Pixi](https://carpentries-incubator.github.io/reproducible-ml-workflows/cuda-conda-pacakges.html#cuda-use-with-pixi) portion of the workshop. The commands are meant to run in a unix shell (e.g. `bash`, `zsh`, ...) and contain comments with the action they perform.

```
pixi init ~/pixi-cuda-lesson/cuda-exercise    # Create a new project that supports cpu or CUDA
cd ~/pixi-cuda-lesson/cuda-exercise
pixi workspace platform add linux-64 osx-arm64 win-64       # Add platform support for linux, mac, windows.
pixi add python     # Install python into this pixi project.
pixi add --feature cpu pytorch-cpu      # Add a _feature_ called "cpu" that contains `pytorch-cpu` as a dependency
pixi workspace environment add --feature cpu cpu        # Add an _environment_ called "cpu" that installs the dependencies listed in the _feature_ cpu.
pixi upgrade --feature cpu pytorch-cpu      # Resolve the specific version of this dependency.
pixi workspace system-requirements add --feature gpu cuda 12    # Specify that cuda 12 is a system requirement for the _feature_ gpu. This implicitly creates the _feature_ gpu as well.
pixi workspace environment add --feature gpu gpu    # Add an _environment_ called "gpu" that installs the dependencies listed in the _feature_ gpu.
pixi add --platform linux-64 --platform win-64 --feature gpu pytorch-gpu    # Specify that these GPU dependencies are only available on linux and windows.
```


The final `.toml` file should look like this:

```
[workspace]
channels = ["conda-forge"]
name = "cuda-exercise"
platforms = ["linux-64", "osx-arm64", "win-64"]
version = "0.1.0"

[tasks]

[dependencies]
python = ">=3.13.5,<3.14"

[feature.cpu.dependencies]
pytorch-cpu = ">=2.7.1,<3"

[feature.gpu.system-requirements]
cuda = "12"

[feature.gpu.target.linux-64.dependencies]
pytorch-gpu = ">=2.7.1,<3"

[feature.gpu.target.win-64.dependencies]
pytorch-gpu = ">=2.7.1,<3"

[environments]
cpu = ["cpu"]
gpu = ["gpu"]
```

And specific environments can be invoked on target platforms by running either
* `pixi run -e gpu *command*` or
* `pixi run -e cpu *command*`

A few other tips:

1. If using python, you should generally not use `pip install` to install packages when working in a pixi environment, as the `pixi.toml` file will not update to account for the new dependency. Instead, use `pixi add <package>` or, if the package if only available on `PyPi`, `pixi add --pypi <package>`.

2. Pixi environments are compatible with VSCode - if you create a pixi environment using `pixi init` and add python using `pixi add python`, the python version that you installed as a part of your pixi environmnet will show up as the recommended interpreter. It will be called "default" by default. If using a Python notebook in VSCode, go to the notebook, hit "Select Kernel" in the top right corner, then "Python Environments". You should see your python environment as the recommended environment.

3. Sending a pixi environment to a friend is easy. Just make sure that your pixi.toml and pixi.lock files are being tracked in git. Then, if your friend clones your repository, they can reproduce your environment bit-for-bit with just `pixi install`.