# Copyright 2013 semantics GmbH
# Written by Marcus Brinkmann <m.brinkmann@semantics.de>

from __future__ import print_function, absolute_import, division

from lxml import etree

from . mw import mwParser as Parser
from . semantics import mwSemantics as Semantics
from . semantics import SemanticsTracer

class MediaWiki(object):
    """MediaWiki parser.

    Parses the provided MediaWiki-style wikitext and renders it to HTML."""

    def __init__(self, wikitext):
        """Construct a new MediaWiki object for the given wikitext."""

        parser = Parser(parseinfo=False,  whitespace='', nameguard=False)
        ast = parser.parse(wikitext, "document", filename="wikitext",
                           semantics=SemanticsTracer(Semantics(), trace=False),
                           trace=False, nameguard=False, whitespace='')
        self.ast = ast

    def as_string(self):
        """Return the rendered output as HTML string."""
        return etree.tostring(self.ast)

    def as_tree(self):
        """Return the rendered output as element tree."""
        return self.ast

def mediawiki(wikitext):
    """Render the wikitext and return output as HTML string."""
    mw = MediaWiki(wikitext)
    return mw.as_string()