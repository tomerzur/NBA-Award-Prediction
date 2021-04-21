# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rbo']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.18,<2.0']

setup_kwargs = {
    'name': 'rbo',
    'version': '0.1.2',
    'description': 'Simple library to calculate Rank-biased Overlap between two lists',
    'long_description': '# Rank-biased Overlap (RBO)\n[![CircleCI](https://circleci.com/gh/changyaochen/rbo/tree/master.svg?style=svg)](https://circleci.com/gh/changyaochen/rbo/tree/master)\n\nThis project contains a Python implementation of Rank-Biased Overlap (RBO) from: Webber, William, Alistair Moffat, and Justin Zobel. "A similarity measure for indefinite rankings." ACM Transactions on Information Systems (TOIS) 28.4 (2010): 20." ([Download][paper]).\n\n\n## Introduction\n\nRBO compares two ranked lists, and returns a numeric value between zero and one to quantify their similarity.\nA RBO value of zero indicates the lists are completely different, and a RBO of one means completely identical. The terms \'different\' and \'identical\' require a little more clarification.\n\nGiven two ranked lists:\n\n    A = ["a", "b", "c", "d", "e"]\n    B = ["e", "d", "c", "b", "a"]\n\nWe can see that both of them rank 5 items ("a", "b", "c", "d" and "e"), but with completely opposite order. In this case the similarity between `A` and `B` should (and will) be 0. But here we are ranking the 5 same items, hence they are conjoint. If there is third ranked list\n\n    C = ["f", "g", "h", "i", "j"]\n\nwhich ranks 5 totally different items, then if we ask for the similarity between `A` and `C`, we should expect a value of 0 as well. In such non-conjoint case, we need to be able to calculate a similarity as well.\n\nThe RBO measure can handle ranked lists with different lengths as well, with proper extrapolation. For example, the RBO between the list `A` and list\n\n    D = ["a", "b", "c", "d", "e", "f", "g"]\n\nwill be 1.\n\n\n## Usage\n\n### Installation using Pip\n\nTo install the RBO module to the current interpreter with Pip:\n\n    pip install rbo\n\n\n### Computing RBO\n\nThe `RankingSimilarity` class contains the calculation for the different flavours of RBO, with clear reference to the corresponding equations in the paper.\nBelow shows how to compute the similarity of two ranked lists S and T:\n\n```python\nIn [1]: import rbo\n\nIn [2]: S = [1, 2, 3]; T = [1, 3, 2]\n\nIn [3]: rbo.RankingSimilarity(S, T).rbo()\nOut[3]: 0.8333333333333334\n```\n\nAccepted datatypes are Python lists and Numpy arrays.\nUsing Pandas series is possible using the underlying Numpy array as shown below. This restriction is necessary, because using `[]` on a Pandas series queries the index, which might not number items contiguously, or might even be non-numeric.\n\n```python\nIn [4]: import pandas as pd\n\nIn [5]: U = pd.Series([1, 3, 2, 4, 5, 6])\n\nIn [6]: rbo.RankingSimilarity(T, U.values).rbo()\nOut[6]: 1.0\n```\n\n\n# Development\n\nRefer to the Makefile for supplementary tasks to development, e.g., executing unit tests, or checking for proper packaging.\nPlease let [me][contact] know if there is any issue.\n\n[contact]: mailto:changyao.chen@gmail.com\n[paper]: http://w.codalism.com/research/papers/wmz10_tois.pdf\n',
    'author': 'Changyao Chen',
    'author_email': 'changyao.chen@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/changyaochen/rbo',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
