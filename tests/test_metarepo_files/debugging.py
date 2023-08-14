#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This script contains functions for the mere purpose of triggering a particular action to debug it in you favourite
debugger. Feel free to add functions and to hardcode paths to your system since this is an auxiliary file where,
the moment something is considered, it is considered obsolete.
"""

from ms3 import Parse
from ms3.logger import get_logger


def ignoring_warning():
    p = Parse("~/unittest_metacorpus/mixed_files")
    p.parse_scores()
    t = get_logger("ms3.Parse.mixed_files.Did03M-Son_regina-1762-Sarti.mscx")
    filt = t.filters[0]
    print("IGNORED_WARNINGS")
    print(filt.ignored_warnings)
    t.warning("This should be a DEBUG message.", extra={"message_id": (2, 94)})
    _ = p.get_dataframes(expanded=True)


def extraction():
    """Created by executing an ms3 command and coping the object initializing from the output."""
    p = Parse(
        r"C:\Users\hentsche\all_subcorpora\liszt_pelerinage",
        recursive=True,
        only_metadata_pieces=True,
        include_convertible=False,
        exclude_review=True,
        file_re="160.06",
        folder_re=None,
        exclude_re=None,
        file_paths=None,
        labels_cfg={"positioning": False, "decode": True},
        ms=None,
        **{"level": "i", "path": None}
    )
    p.parse_scores()


if __name__ == "__main__":
    extraction()