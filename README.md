# Rbg

![Lang](https://img.shields.io/badge/Language-Python-orange)
![License](https://img.shields.io/github/license/AlfredUFY/rbg)
![Issues](https://img.shields.io/github/issues/AlfredUFY/rbg?color=red)

Rbg is a simple flask website to remove images background by [Rembg](https://github.com/danielgatis/rembg).

## Installation

`pip install -r requirements.txt`

## Models

You should download models to a folder under the project root dir named `.u2net` by yourself.

The available models are:

u2net (download - alternative, source): A pre-trained model for general use cases.

u2netp (download - alternative, source): A lightweight version of u2net model.

u2net_human_seg (download - alternative, source): A pre-trained model for human segmentation.

u2net_cloth_seg (download - alternative, source): A pre-trained model for Cloths Parsing from human portrait. Here clothes are parsed into 3 category: Upper body, Lower body and Full body.

## Launch
`flask run`
