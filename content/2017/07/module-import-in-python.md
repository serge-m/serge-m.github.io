Title: Module import in python
Author: SergeM
Date: 2017-07-09 23:07:00
Slug: module-import-in-python
Tags: python


## Import module by path/name
```python
import importlib
module = importlib.import_module(module_path)
```

## Find class implementing certain interface in a module

```python
def load_class_from_module(module_path: str, target_class: type) -> type:
    module = importlib.import_module(module_path)
    list_classes = get_all_classes_implementing_interface(module, target_class)
    if not list_classes:
        raise RuntimeError("Unable to find implemented interface {} in {}".format(target_class, module_path))
    if len(list_classes) > 1:
        raise RuntimeError("More then 1 implementation of {} was found in {}".format(target_class, module_path))
    return list_classes[0]


def get_all_classes_implementing_interface(module, target_class: type) -> List[type]:
    results = []
    for attr in dir(module):
        cls = getattr(module, attr)
        if isinstance(cls, type) and issubclass(cls, target_class):
            results.append(cls)
    return results

```

