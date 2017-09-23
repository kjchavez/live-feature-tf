# LiveFeature

A lightweight framework for adding features fetched from the Web to TensorFlow models.
Ensures consistency between training and inference time.

This is the package to use during training time. It includes the base `livefeature` package
plus a few extra utilities that depend on TensorFlow.

> NOTE: At serving time, you probably don't need the TensorFlow dependency if hosting model
> on Cloud ML Engine.

## Training API

Suppose you have your LiveFeatures defined in the python module `my_live_features`.

```python
# my_live_features.py
@lf.feature("wiki_summary", str)
def fetch_wiki_summary(idx):
  # do stuff…
  return str(summary)
```

Then somewhere in your model definition...

```python

# In tensorflow training file.
import my_live_features
import livefeature_tf as lftf

def input_fn():
  d = tf.contrib.data.Dataset...
  expander = lftf.Expander('id', my_live_features, cache_fn=lftf.FrozenCache)
  dataset = expander.transform(dataset)
  ...
```
