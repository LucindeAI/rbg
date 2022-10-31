# Rbg

![Lang](https://img.shields.io/badge/Language-Python-orange)
![License](https://img.shields.io/github/license/AlfredUFY/rbg)
![Issues](https://img.shields.io/github/issues/AlfredUFY/rbg?color=red)

Rbg is a simple flask website to remove images background by [Rembg](https://github.com/danielgatis/rembg).

## Project Tree
```bash
.
├── app.py
├── LICENSE
├── __pycache__
│   └── app.cpython-310.pyc
├── README.md
├── requirements.txt
├── templates
│   └── index.html
├── .u2net                   # Download models to this folder by yourself
└── uploads                  # folder as `UPLOAD_FOLDER` folder in app.py
```

## Installation

`pip install -r requirements.txt`

## Models

You should download models to a folder under the project root dir named `.u2net` by yourself.

The available models are:

-   u2net ([download](https://drive.google.com/uc?id=1tCU5MM1LhRgGou5OpmpjBQbSrYIUoYab) - [alternative](http://depositfiles.com/files/ltxbqa06w), [source](https://github.com/xuebinqin/U-2-Net)): A pre-trained model for general use cases.
-   u2netp ([download](https://drive.google.com/uc?id=1tNuFmLv0TSNDjYIkjEdeH1IWKQdUA4HR) - [alternative](http://depositfiles.com/files/0y9i0r2fy), [source](https://github.com/xuebinqin/U-2-Net)): A lightweight version of u2net model.
-   u2net_human_seg ([download](https://drive.google.com/uc?id=1ZfqwVxu-1XWC1xU1GHIP-FM_Knd_AX5j) - [alternative](http://depositfiles.com/files/6spp8qpey), [source](https://github.com/xuebinqin/U-2-Net)): A pre-trained model for human segmentation.
-   u2net_cloth_seg ([download](https://drive.google.com/uc?id=15rKbQSXQzrKCQurUjZFg8HqzZad8bcyz) - [alternative](http://depositfiles.com/files/l3z3cxetq), [source](https://github.com/levindabhi/cloth-segmentation)): A pre-trained model for Cloths Parsing from human portrait. Here clothes are parsed into 3 category: Upper body, Lower body and Full body.

## Launch
`flask run`
