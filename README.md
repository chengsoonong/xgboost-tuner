**xgboost-tuner is a Python library for automating the tuning of XGBoost parameters.**

Due to XGBoost's large number of parameters and the size of their possible parameter spaces, doing an ordinary GridSearch over all of them isn't computationally feasible.

The excellent article [Complete Guide to Parameter Tuning in XGBoost](https://www.analyticsvidhya.com/blog/2016/03/complete-guide-parameter-tuning-xgboost-with-codes-python/) offers an alternative approach to tuning XGBoost by tuning parameters incrementally.

This library offers two strategies to automate this tuning - an incremental approach as laid out in the article above and an alternative approach using a more computationally efficient randomized search.

In both strategies, the user can configure the parameter space of interest through keyword arguments.

## Installing xgboost-tuner

#### PyPI

To install xgboost-tuner, execute  

```bash
pip install xgboost-tuner  
```

Alternatively, you could download the package manually from the Python Package Index [https://pypi.python.org/pypi/xgboost-tuner](https://pypi.python.org/pypi/xgboost-tuner), unzip it, navigate into the package, and use the command:

```bash
python setup.py install
```

## Examples

#### Tuning XGBoost parameters through an incremental grid search

```python
from sklearn.datasets import load_svmlight_file
from xgboost_tuner.tuner import tune_xgb_params

train, label = load_svmlight_file('data/agaricus.txt.train')
train = train.toarray()

# Tune the parameters incrementally and limit the range for colsample_bytree and subsample
best_params, history = tune_xgb_params(
    cv_folds=3,
    label=label,
    metric_sklearn='accuracy',
    metric_xgb='error',
    n_jobs=4,
    objective='binary:logistic',
    random_state=2017,
    strategy='incremental',
    train=train,
    colsample_bytree_min=0.8,
    colsample_bytree_max=1.0,
    subsample_min=0.8,
    subsample_max=1.0,
    dry_run=True,
)
```

#### Tuning XGBoost parameters through randomized search

```python
from sklearn.datasets import load_svmlight_file
from xgboost_tuner.tuner import tune_xgb_params

train, label = load_svmlight_file('data/agaricus.txt.train')
train = train.toarray()

# Tune the parameters in a randomized fashion and control the distributions for colsample_bytree and subsample
best_params, history = tune_xgb_params(
    cv_folds=3,
    label=label,
    metric_sklearn='accuracy',
    metric_xgb='error',
    n_jobs=4,
    objective='binary:logistic',
    random_state=2017,
    strategy='randomized',
    train=train,
    colsample_bytree_loc=0.5,
    colsample_bytree_scale=0.2,
    subsample_loc=0.5,
    subsample_scale=0.2,
    n_iter=3,
)
```
