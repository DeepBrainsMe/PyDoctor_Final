import importlib
from collections import namedtuple

from pydoctor.evaluation.data import StudyList

DatasetInfo = namedtuple('DatasetInfo', ['module', 'class_name', 'kwargs'])
dataset_dict = dict(
    testa=DatasetInfo(module="ltr.dataset.lumbar", class_name="Lumbar", kwargs=dict(split='testA')),
    testb=DatasetInfo(module="ltr.dataset.lumbar", class_name="Lumbar", kwargs=dict(split='testB')),
)


def load_dataset(name: str):
    """ Import and load a single dataset."""
    name = name.lower()
    dset_info = dataset_dict.get(name)
    if dset_info is None:
        raise ValueError('Unknown dataset \'%s\'' % name)

    m = importlib.import_module(dset_info.module)
    dataset = getattr(m, dset_info.class_name)(**dset_info.kwargs)  # Call the constructor
    return dataset.get_study_list()


def get_dataset(*args):
    """ Get a single or set of datasets."""
    dset = StudyList()
    for name in args:
        dset.extend(load_dataset(name))
    return dset
