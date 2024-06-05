# Python-Whisper-Webservice

## 项目简介
本项目提供基于Whisper服务的Web Service，默认使用CPU进行运算。

## 安装
1. `pip install -r requirements.txt`
2. `fastapi dev server.py`
3. open [docs](http://127.0.0.1:8000/docs)

### 模型本地化安装
1. open [openai/whisper-large-v3](https://huggingface.co/openai/whisper-large-v3)
2. mkdir models
3. git clone https://huggingface.co/openai/whisper-large-v3
4. cd whipser-large-v3 && git lfs install
5. git lfs pull

## 许可证
### MIT License

Copyright (c) 2024 Deer404

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE