import os

# 项目根目录
PROJECT_DIR = "gomoku_ai"

# 定义目录结构
DIRS = [
    os.path.join(PROJECT_DIR, "data", "raw"),
    os.path.join(PROJECT_DIR, "data", "processed"),
    os.path.join(PROJECT_DIR, "data", "external"),
    os.path.join(PROJECT_DIR, "notebooks"),
    os.path.join(PROJECT_DIR, "src", "data"),
    os.path.join(PROJECT_DIR, "src", "models"),
    os.path.join(PROJECT_DIR, "src", "training"),
    os.path.join(PROJECT_DIR, "src", "utils"),
    os.path.join(PROJECT_DIR, "src", "inference"),
    os.path.join(PROJECT_DIR, "tests"),
    os.path.join(PROJECT_DIR, "scripts"),
    os.path.join(PROJECT_DIR, "models", "checkpoints"),
    os.path.join(PROJECT_DIR, "models", "logs"),
    os.path.join(PROJECT_DIR, "models", "saved_models"),
    os.path.join(PROJECT_DIR, "outputs", "figures"),
    os.path.join(PROJECT_DIR, "outputs", "results"),
]

# 创建所有目录
for directory in DIRS:
    os.makedirs(directory, exist_ok=True)

# 定义需要创建的 __init__.py 文件
init_files = [
    os.path.join(PROJECT_DIR, "src", "__init__.py"),
    os.path.join(PROJECT_DIR, "src", "data", "__init__.py"),
    os.path.join(PROJECT_DIR, "src", "models", "__init__.py"),
    os.path.join(PROJECT_DIR, "src", "training", "__init__.py"),
    os.path.join(PROJECT_DIR, "src", "utils", "__init__.py"),
    os.path.join(PROJECT_DIR, "src", "inference", "__init__.py"),
    os.path.join(PROJECT_DIR, "tests", "__init__.py"),
]

for file in init_files:
    open(file, 'a').close()

# 定义需要创建的 README.md 文件
readmes = [
    os.path.join(PROJECT_DIR, "data", "README.md"),
    os.path.join(PROJECT_DIR, "notebooks", "README.md"),
    os.path.join(PROJECT_DIR, "outputs", "README.md"),
]

for file in readmes:
    with open(file, 'w') as f:
        f.write(f"# {os.path.basename(os.path.dirname(file))}\n")

# 定义示例文件
sample_files = [
    os.path.join(PROJECT_DIR, "data", "raw", "README.md"),
    os.path.join(PROJECT_DIR, "data", "processed", "README.md"),
    os.path.join(PROJECT_DIR, "data", "external", "README.md"),
    os.path.join(PROJECT_DIR, "notebooks", "data_exploration.ipynb"),
    os.path.join(PROJECT_DIR, "notebooks", "model_training.ipynb"),
    os.path.join(PROJECT_DIR, "notebooks", "README.md"),
    os.path.join(PROJECT_DIR, "src", "data", "data_loader.py"),
    os.path.join(PROJECT_DIR, "src", "data", "preprocess.py"),
    os.path.join(PROJECT_DIR, "src", "data", "augment.py"),
    os.path.join(PROJECT_DIR, "src", "models", "base_model.py"),
    os.path.join(PROJECT_DIR, "src", "models", "resnet_transfer.py"),
    os.path.join(PROJECT_DIR, "src", "models", "custom_model.py"),
    os.path.join(PROJECT_DIR, "src", "training", "train.py"),
    os.path.join(PROJECT_DIR, "src", "training", "validate.py"),
    os.path.join(PROJECT_DIR, "src", "training", "utils.py"),
    os.path.join(PROJECT_DIR, "src", "utils", "logger.py"),
    os.path.join(PROJECT_DIR, "src", "utils", "metrics.py"),
    os.path.join(PROJECT_DIR, "src", "utils", "helpers.py"),
    os.path.join(PROJECT_DIR, "src", "inference", "predict.py"),
    os.path.join(PROJECT_DIR, "src", "inference", "deploy.py"),
    os.path.join(PROJECT_DIR, "tests", "test_data_loader.py"),
    os.path.join(PROJECT_DIR, "tests", "test_model.py"),
    os.path.join(PROJECT_DIR, "tests", "test_training.py"),
    os.path.join(PROJECT_DIR, "scripts", "prepare_data.sh"),
    os.path.join(PROJECT_DIR, "scripts", "train_model.sh"),
    os.path.join(PROJECT_DIR, "scripts", "evaluate_model.sh"),
    os.path.join(PROJECT_DIR, "models", "checkpoints", "README.md"),
    os.path.join(PROJECT_DIR, "models", "logs", "README.md"),
    os.path.join(PROJECT_DIR, "models", "saved_models", "README.md"),
    os.path.join(PROJECT_DIR, "outputs", "figures", "README.md"),
    os.path.join(PROJECT_DIR, "outputs", "results", "README.md"),
    os.path.join(PROJECT_DIR, "outputs", "figures", "loss_curve.png"),
    os.path.join(PROJECT_DIR, "outputs", "results", "evaluation_results.csv"),
    os.path.join(PROJECT_DIR, "models", "checkpoints", "checkpoint_epoch_10.pth"),
    os.path.join(PROJECT_DIR, "models", "logs", "training.log"),
    os.path.join(PROJECT_DIR, "models", "saved_models", "gomoku_ai_final.pth"),
]

for file in sample_files:
    if file.endswith('.ipynb'):
        with open(file, 'w') as f:
            f.write('{ "cells": [], "metadata": {}, "nbformat": 4, "nbformat_minor": 5 }')
    elif file.endswith('.sh'):
        with open(file, 'w') as f:
            f.write('#!/bin/bash\n')
        os.chmod(file, 0o755)
    elif file.endswith('.py'):
        with open(file, 'w') as f:
            f.write('# Python script\n')
    elif file.endswith('.md'):
        with open(file, 'w') as f:
            f.write(f"# {os.path.basename(file)}\n")
    else:
        open(file, 'a').close()

# 创建根目录文件
with open(os.path.join(PROJECT_DIR, "requirements.txt"), 'w') as f:
    pass

with open(os.path.join(PROJECT_DIR, "environment.yml"), 'w') as f:
    pass

with open(os.path.join(PROJECT_DIR, "setup.py"), 'w') as f:
    pass

with open(os.path.join(PROJECT_DIR, "README.md"), 'w') as f:
    f.write("# Gomoku AI 项目\n")

with open(os.path.join(PROJECT_DIR, ".gitignore"), 'w') as f:
    f.write("__pycache__/\n*.pyc\nmodels/checkpoints/\nmodels/logs/\nmodels/saved_models/\noutputs/\n")

print("项目结构已成功创建！")
