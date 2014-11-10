"""Builds the project using py2exe with various, specified configurations"""
from distutils.core import setup
import py2exe

setup(windows=[{"script" : "../registry_edit.py"}],
      zipfile=None,
      options={"py2exe" : {"bundle_files" : 1,
                           "compressed" : 1,
                           "dist_dir" : "../release/_latest/bin"}})
