import numpy as np

import torch

from scipy.sparse import load_npz, save_npz

from imputation_dgm.cuda import to_cuda_if_available


def load(features_path, features_format, to_tensor=True, to_cuda=True):
    loader = loaders[features_format]
    features = loader(features_path)
    if to_tensor:
        features = torch.from_numpy(features)
        if to_cuda:
            features = to_cuda_if_available(features)
    return features


def load_dense(features_path, transform=True):
    features = np.load(features_path)
    if transform:
        features = features.astype(np.float32)
    return features


def load_sparse(features_path, transform=True):
    features = load_npz(features_path)
    if transform:
        features = np.asarray(features.todense()).astype(np.float32)
    return features


def save_dense(features_path, features):
    np.save(features_path, features)


def save_sparse(features_path, features):
    save_npz(features_path, features)


loaders = {
    "dense": load_dense,
    "sparse": load_sparse,
}

savers = {
    "dense": save_dense,
    "sparse": save_sparse,
}

extensions = {
    "dense": "npy",
    "sparse": "npz",
}

data_formats = loaders.keys()
