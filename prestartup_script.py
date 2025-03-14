import importlib.metadata
import folder_paths
import os
import pathlib

if importlib.util.find_spec("basicsr"):
    path = pathlib.Path(importlib.util.find_spec("basicsr").origin).parent.joinpath("data/degradations.py")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        if "from torchvision.transforms.functional_tensor import rgb_to_grayscale" in content:
            print(f"Patching basicsr with fix from https://github.com/XPixelGroup/BasicSR/pull/650 for PMRF...")
            content = content.replace(
                "from torchvision.transforms.functional_tensor import rgb_to_grayscale",
                "from torchvision.transforms.functional import rgb_to_grayscale",
            )
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
