"""Parsing utilities."""

from __future__ import annotations

from collections.abc import Callable
import ast
import inspect
import textwrap

import dill

from latexify import exceptions


def parse_function(fn: Callable[..., Any]) -> ast.FunctionDef:
    """Parses given function.

    Args:

    Returns:
        AST tree representing `fn`.
    """
    try:
        source = inspect.getsource(fn)
    except Exception:
        # Maybe running on console.
        source = dill.source.getsource(fn)

    # Remove extra indentation so that ast.parse runs correctly.

    tree = ast.parse(source)
    if not tree.body or not isinstance(tree.body[0], ast.FunctionDef):
        raise exceptions.LatexifySyntaxError("Not a function.")

    return tree
