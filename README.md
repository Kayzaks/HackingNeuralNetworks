# Hacking Neural Networks: A Short Introduction
 
<span style="color:red">**Disclaimer: This article and all the associated exercises are for educational purposes only.**</span>


This is a short introduction on methods that use neural networks in an offensive manner (bug hunting, shellcode obfuscation, etc.) and how to exploit neural networks found in the wild (information extraction, malware injection, backdooring, etc.).

Most of the methods presented are accompanied by an exercise found in this repo. The full article can be found here in '[Article.pdf](Article.pdf)' or on arXiv ([arXiv:1911.07658](https://arxiv.org/pdf/1911.07658.pdf)). 


---

## Setup

### Python and pip

Download and install Python3 and its package installer pip using a package manager or directly from the website https://www.python.org/downloads/. 

### Editor 

An editor is required to work with the code, preferably one that allows code highlighting for Python. Vim/Emacs will do. As a reference, all exercises were prepared using Visual Studio Code https://code.visualstudio.com/docs/python/python-tutorial.

### Packages 

- **Keras**: Installing Keras can be tricky. We refer to the official installation guide at https://keras.io/#installation and suggest TensorFlow as a backend (using the GPU-enabled version, if one is available on the machine). 
- **NumPy**, **SciPy** and **scikit-image**: NumPy and SciPy are excellent helper packages, which are used throughout all exercises. Following the official SciPy instructions should also install NumPy https://www.scipy.org/install.html. We will also need to install scikit-image for image loading and saving: https://scikit-image.org/docs/stable/install.html.
- **PyCuda**: PyCuda is required for the GPU-based attack exercise. If no nVidia GPU is available on the machine, this can be skipped. https://wiki.tiker.net/PyCuda/Installation
- **NLTK**: NLTK provides functionalities for natural language processing and is very helpful for some of the exercises. https://www.nltk.org/install.html

---
## The exercises

- *0 - Last Layer Attack*
- *1 - Backdooring*
- *2 - Extracting Information*
- *3 - Brute Forcing*
- *4 - Neural Overflow*
- *5 - Malware Injection*
- *6 - Neural Obfuscation*
- *7 - Bug Hunting*
- *8 - GPU Attack*

For instructions, please read the 'README.md' file in each of the exercise directories.

---

## Further Reading / Watching

Check out:
- Isao Takaesu's course on [Security and Machine Learning](https://github.com/13o-bbr-bbq/machine_learning_security/tree/master/Security_and_MachineLearning) 
- Will Pearce and Nick Landers' [Talk at Derbycon 2019](https://www.youtube.com/watch?v=CsvkYoxtexQ) on Offensive Machine Learning techniques.

---

## What else?

The neural networks found in the exercises are based on the examples provided by [keras](https://keras.io/). 

If you find that there are errors or missing references, feel free to make a PR or contact me.