import setuptools

setuptools.setup(
  name="cells_selector",
  version="0.1.0",
  packages=["cells_selector"],
  install_requires=[
    'numpy',
    'tkinter>=3',
    'Pillow>=4'
  ],
  entry_points = {}
)
