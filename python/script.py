# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------------
#
# TITLE   :
# AUTHOR  :
# PROJECT :
#
# ----------------------------------------------------------------------------

"""**DOCSTRING**.

This script can be run from the command line with the following parameters:

Parameters
----------

"""

__author__ = ""
# __copyright__ = "Copyright 2019, "
# __credits__ = [""]
# __license__ = ""
# __version__ = "0.0.0"
# __maintainer__ = ""
# __email__ = ""
# __status__ = "Production"

# __all__ = [
#     ""
# ]


##############################################################################
# IMPORTS

# BUILT-IN
import argparse
import typing as T
import warnings

##############################################################################
# PARAMETERS

# General
_PLOT: bool = True  # Whether to plot the output

# Log file
_VERBOSE: int = 0  # Degree of logfile verbosity

##############################################################################
# CODE
##############################################################################


class ClassName(object):
    """Docstring for ClassName."""

    def __init__(self, arg):
        """Initialize class."""
        super().__init__()
        self.arg = arg

    # /def


# /class


# -------------------------------------------------------------------


def function():
    """Docstring."""
    pass


# /def


##############################################################################
# Command Line
##############################################################################


def make_parser(
    *, inheritable: bool = False, plot: bool = _PLOT, verbose: int = _VERBOSE
) -> argparse.ArgumentParser:
    """Expose ArgumentParser for ``main``.

    Parameters
    ----------
    inheritable: bool, optional, keyword only
        whether the parser can be inherited from (default False).
        if True, sets ``add_help=False`` and ``conflict_hander='resolve'``

    plot : bool, optional, keyword only
        Whether to produce plots, or not.

    verbose : int, optional, keyword only
        Script logging verbosity.

    Returns
    -------
    parser: |ArgumentParser|
        The parser with arguments:

        - plot
        - verbose

    ..
      RST SUBSTITUTIONS

    .. |ArgumentParser| replace:: `~argparse.ArgumentParser`

    """
    parser = argparse.ArgumentParser(
        description="",
        add_help=~inheritable,
        conflict_handler="resolve" if ~inheritable else "error",
    )

    # plot or not
    parser.add_argument("--verbose", action="store", default=_PLOT, type=bool)

    # script verbosity
    parser.add_argument("-v", "--verbose", action="store", default=0, type=int)

    return parser


# /def


# ------------------------------------------------------------------------


def main(
    args: T.Union[list, str, None] = None,
    opts: T.Optional[argparse.Namespace] = None,
):
    """Script Function.

    Parameters
    ----------
    args : list or str or None, optional
        an optional single argument that holds the sys.argv list,
        except for the script name (e.g., argv[1:])
    opts : `~argparse.Namespace`| or None, optional
        pre-constructed results of parsed args
        if not None, used ONLY if args is None

    """
    if opts is not None and args is None:
        pass
    else:
        if opts is not None:
            warnings.warn("Not using `opts` because `args` are given")
        if isinstance(args, str):
            args = args.split()

        parser = make_parser()
        opts = parser.parse_args(args)

    # /if


# /def


# ------------------------------------------------------------------------

if __name__ == "__main__":

    # call script
    main(args=None, opts=None)  # all arguments except script name


# /if


##############################################################################
# END
