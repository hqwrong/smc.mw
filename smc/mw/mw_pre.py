#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# CAVEAT UTILITOR
# This file was automatically generated by Grako.
#    https://bitbucket.org/apalala/grako/
# Any changes you make to it will be overwritten the
# next time the file is generated.
#

from __future__ import print_function, division, absolute_import, unicode_literals
from grako.parsing import * # @UnusedWildImport
from grako.exceptions import * # @UnusedWildImport

__version__ = '13.309.04.17.07'

class mw_preParser(Parser):
    def __init__(self, whitespace='', nameguard=False, **kwargs):
        super(mw_preParser, self).__init__(whitespace=whitespace,
            nameguard=nameguard, **kwargs)

    @rule_def
    def _blank_(self):
        with self._optional():
            self._pattern(r'[ \t]+')

    @rule_def
    def _end_of_open_tag_(self):
        self._pattern(r'(\s(.|\n)*?)?(?=>|/>)')

    @rule_def
    def _end_of_close_tag_(self):
        self._pattern(r'(\s(.|\n)*?)?(?=>)')

    @rule_def
    def _document_(self):
        def block1():
            self._element_()
            self._cut()
        self._closure(block1)
        self.ast['elements'] = self.last_node
        self._check_eof()

    @rule_def
    def _element_(self):
        with self._choice():
            with self._option():
                self._text_()
            with self._option():
                self._link_()
            with self._option():
                self._argument_()
            with self._option():
                self._template_()
            with self._option():
                self._heading_()
            with self._option():
                self._comment_()
            with self._option():
                self._noinclude_()
            with self._option():
                self._includeonly_()
            with self._option():
                self._onlyinclude_()
            with self._option():
                self._ignore_()
            with self._option():
                self._pattern(r'(.|\n)')
            self._error('expecting one of: (.|\n)')

    @rule_def
    def _text_(self):
        self._pattern(r'[^\n<{}|=\[\]]+')

    @rule_def
    def _link_(self):
        self._token('[[')
        self._link_content_()
        self.ast['content'] = self.last_node
        self._token(']]')

    @rule_def
    def _link_content_(self):
        def block0():
            with self._ifnot():
                self._token(']]')
            self._element_()
        self._closure(block0)

    @rule_def
    def _argument_(self):
        self._token('{{{')
        self._argument_content_()
        self.ast['name'] = self.last_node
        def block2():
            self._argument_default_()
        self._closure(block2)
        self.ast['defaults'] = self.last_node
        self._token('}}}')

    @rule_def
    def _argument_content_(self):
        def block0():
            with self._ifnot():
                with self._group():
                    with self._choice():
                        with self._option():
                            self._token('}}}')
                        with self._option():
                            self._token('|')
                        self._error('expecting one of: | }}}')
            self._element_()
        self._closure(block0)

    @rule_def
    def _argument_default_(self):
        self._token('|')
        self._argument_content_()
        self.ast['content'] = self.last_node

    @rule_def
    def _template_(self):
        with self._optional():
            self._pattern(r'(?<=^)|(?<=\n)')
            self.ast['bol'] = self.last_node
        self._token('{{')
        self._template_content_()
        self.ast['name'] = self.last_node
        def block3():
            self._template_arg_()
        self._closure(block3)
        self.ast['arguments'] = self.last_node
        self._token('}}')

    @rule_def
    def _template_content_(self):
        def block0():
            with self._ifnot():
                with self._group():
                    with self._choice():
                        with self._option():
                            self._token('}}')
                        with self._option():
                            self._token('|')
                        self._error('expecting one of: | }}')
            self._element_()
        self._closure(block0)

    @rule_def
    def _template_arg_(self):
        self._token('|')
        with self._group():
            with self._choice():
                with self._option():
                    self._template_named_arg_()
                with self._option():
                    self._template_unnamed_arg_()
                self._error('no available options')
        self.ast['@'] = self.last_node

    @rule_def
    def _template_named_arg_(self):
        self._template_arg_name_content_()
        self.ast['name'] = self.last_node
        self._token('=')
        self._template_content_()
        self.ast['content'] = self.last_node

    @rule_def
    def _template_arg_name_content_(self):
        def block0():
            with self._ifnot():
                with self._group():
                    with self._choice():
                        with self._option():
                            self._token('}}')
                        with self._option():
                            self._token('|')
                        with self._option():
                            self._token('=')
                        self._error('expecting one of: | }} =')
            self._element_()
        self._closure(block0)

    @rule_def
    def _template_unnamed_arg_(self):
        self._template_content_()
        self.ast['content'] = self.last_node

    @rule_def
    def _comment_(self):
        with self._choice():
            with self._option():
                self._comment_alone_()
            with self._option():
                self._comment_plain_()
            self._error('no available options')

    @rule_def
    def _comment_alone_(self):
        self._pattern(r'\n')
        self._blank_()
        self._comment_plain_()
        self._blank_()
        with self._if():
            self._pattern(r'\n')

    @rule_def
    def _comment_plain_(self):
        self._token('<!--')
        self._pattern(r'((?!-->).|\n)*')
        with self._group():
            with self._choice():
                with self._option():
                    self._token('-->')
                with self._option():
                    self._check_eof()
                self._error('expecting one of: -->')

    @rule_def
    def _noinclude_(self):
        self._token('<noinclude')
        self._end_of_open_tag_()
        self.ast['attr'] = self.last_node
        with self._group():
            with self._choice():
                with self._option():
                    self._token('/>')
                with self._option():
                    self._token('>')
                    self._noinclude_content_()
                    self.ast['content'] = self.last_node
                    with self._group():
                        with self._choice():
                            with self._option():
                                self._noinclude_end_()
                                self.ast['end'] = self.last_node
                            with self._option():
                                self._check_eof()
                            self._error('no available options')
                self._error('expecting one of: />')

    @rule_def
    def _noinclude_content_(self):
        def block0():
            with self._ifnot():
                self._noinclude_end_()
            self._element_()
        self._closure(block0)

    @rule_def
    def _noinclude_end_(self):
        self._token('</noinclude')
        self._end_of_close_tag_()
        self._token('>')

    @rule_def
    def _includeonly_(self):
        self._token('<includeonly')
        self._end_of_open_tag_()
        self.ast['attr'] = self.last_node
        with self._group():
            with self._choice():
                with self._option():
                    self._token('/>')
                with self._option():
                    self._token('>')
                    self._includeonly_content_()
                    self.ast['content'] = self.last_node
                    with self._group():
                        with self._choice():
                            with self._option():
                                self._includeonly_end_()
                                self.ast['end'] = self.last_node
                            with self._option():
                                self._check_eof()
                            self._error('no available options')
                self._error('expecting one of: />')

    @rule_def
    def _includeonly_content_(self):
        def block0():
            with self._ifnot():
                self._includeonly_end_()
            self._element_()
        self._closure(block0)

    @rule_def
    def _includeonly_end_(self):
        self._token('</includeonly')
        self._end_of_close_tag_()
        self._token('>')

    @rule_def
    def _onlyinclude_(self):
        self._token('<onlyinclude')
        self._end_of_open_tag_()
        self.ast['attr'] = self.last_node
        with self._group():
            with self._choice():
                with self._option():
                    self._token('/>')
                with self._option():
                    self._token('>')
                    self._onlyinclude_content_()
                    self.ast['content'] = self.last_node
                    with self._group():
                        with self._choice():
                            with self._option():
                                self._onlyinclude_end_()
                                self.ast['end'] = self.last_node
                            with self._option():
                                self._check_eof()
                            self._error('no available options')
                self._error('expecting one of: />')

    @rule_def
    def _onlyinclude_content_(self):
        def block0():
            with self._ifnot():
                self._onlyinclude_end_()
            self._onlyinclude_element_()
        self._closure(block0)

    @rule_def
    def _onlyinclude_end_(self):
        self._token('</onlyinclude')
        self._end_of_close_tag_()
        self._token('>')

    @rule_def
    def _onlyinclude_element_(self):
        with self._choice():
            with self._option():
                with self._ifnot():
                    self._onlyinclude_()
                self._element_()
            with self._option():
                self._pattern(r'(.|\n)')
            self._error('expecting one of: (.|\n)')

    @rule_def
    def _ignore_(self):
        self._token('</')
        with self._group():
            with self._choice():
                with self._option():
                    self._token('noinclude')
                with self._option():
                    self._token('includeonly')
                with self._option():
                    self._token('onlyinclude')
                self._error('expecting one of: onlyinclude noinclude includeonly')
        self._end_of_close_tag_()
        self._token('>')

    @rule_def
    def _heading_(self):
        self._pattern(r'^|(?<=\n)')
        with self._group():
            with self._choice():
                with self._option():
                    self._h6_()
                with self._option():
                    self._h5_()
                with self._option():
                    self._h4_()
                with self._option():
                    self._h3_()
                with self._option():
                    self._h2_()
                with self._option():
                    self._h1_()
                self._error('no available options')
        self.ast['@'] = self.last_node
        with self._if():
            with self._group():
                def block1():
                    self._blank_()
                    with self._optional():
                        self._comment_plain_()
                self._closure(block1)
                self._blank_()
                with self._group():
                    with self._choice():
                        with self._option():
                            self._pattern(r'\n')
                        with self._option():
                            self._check_eof()
                        self._error('expecting one of: \n')

    @rule_def
    def _h6_(self):
        self._token('======')
        self._push_no_h6_()
        self._heading_inline_()
        self.ast['@'] = self.last_node
        self._pop_no_()
        self._token('======')

    @rule_def
    def _h5_(self):
        self._token('=====')
        self._push_no_h5_()
        self._heading_inline_()
        self.ast['@'] = self.last_node
        self._pop_no_()
        self._token('=====')

    @rule_def
    def _h4_(self):
        self._token('====')
        self._push_no_h4_()
        self._heading_inline_()
        self.ast['@'] = self.last_node
        self._pop_no_()
        self._token('====')

    @rule_def
    def _h3_(self):
        self._token('===')
        self._push_no_h3_()
        self._heading_inline_()
        self.ast['@'] = self.last_node
        self._pop_no_()
        self._token('===')

    @rule_def
    def _h2_(self):
        self._token('==')
        self._push_no_h2_()
        self._heading_inline_()
        self.ast['@'] = self.last_node
        self._pop_no_()
        self._token('==')

    @rule_def
    def _h1_(self):
        self._token('=')
        self._push_no_h1_()
        self._heading_inline_()
        self.ast['@'] = self.last_node
        self._pop_no_()
        self._token('=')

    @rule_def
    def _push_no_h6_(self):
        pass

    @rule_def
    def _push_no_h5_(self):
        pass

    @rule_def
    def _push_no_h4_(self):
        pass

    @rule_def
    def _push_no_h3_(self):
        pass

    @rule_def
    def _push_no_h2_(self):
        pass

    @rule_def
    def _push_no_h1_(self):
        pass

    @rule_def
    def _heading_inline_(self):
        self._push_no_nl_()
        self._heading_content_()
        self.ast['@'] = self.last_node
        self._pop_no_()

    @rule_def
    def _heading_content_(self):
        def block0():
            self._check_no_()
            self._pattern(r'(.|\n)')
        self._closure(block0)

    @rule_def
    def _pop_no_(self):
        pass

    @rule_def
    def _check_no_(self):
        pass

    @rule_def
    def _push_no_nl_(self):
        pass



class mw_preSemanticParser(CheckSemanticsMixin, mw_preParser):
    pass


class mw_preSemantics(object):
    def blank(self, ast):
        return ast

    def end_of_open_tag(self, ast):
        return ast

    def end_of_close_tag(self, ast):
        return ast

    def document(self, ast):
        return ast

    def element(self, ast):
        return ast

    def text(self, ast):
        return ast

    def link(self, ast):
        return ast

    def link_content(self, ast):
        return ast

    def argument(self, ast):
        return ast

    def argument_content(self, ast):
        return ast

    def argument_default(self, ast):
        return ast

    def template(self, ast):
        return ast

    def template_content(self, ast):
        return ast

    def template_arg(self, ast):
        return ast

    def template_named_arg(self, ast):
        return ast

    def template_arg_name_content(self, ast):
        return ast

    def template_unnamed_arg(self, ast):
        return ast

    def comment(self, ast):
        return ast

    def comment_alone(self, ast):
        return ast

    def comment_plain(self, ast):
        return ast

    def noinclude(self, ast):
        return ast

    def noinclude_content(self, ast):
        return ast

    def noinclude_end(self, ast):
        return ast

    def includeonly(self, ast):
        return ast

    def includeonly_content(self, ast):
        return ast

    def includeonly_end(self, ast):
        return ast

    def onlyinclude(self, ast):
        return ast

    def onlyinclude_content(self, ast):
        return ast

    def onlyinclude_end(self, ast):
        return ast

    def onlyinclude_element(self, ast):
        return ast

    def ignore(self, ast):
        return ast

    def heading(self, ast):
        return ast

    def h6(self, ast):
        return ast

    def h5(self, ast):
        return ast

    def h4(self, ast):
        return ast

    def h3(self, ast):
        return ast

    def h2(self, ast):
        return ast

    def h1(self, ast):
        return ast

    def push_no_h6(self, ast):
        return ast

    def push_no_h5(self, ast):
        return ast

    def push_no_h4(self, ast):
        return ast

    def push_no_h3(self, ast):
        return ast

    def push_no_h2(self, ast):
        return ast

    def push_no_h1(self, ast):
        return ast

    def heading_inline(self, ast):
        return ast

    def heading_content(self, ast):
        return ast

    def pop_no(self, ast):
        return ast

    def check_no(self, ast):
        return ast

    def push_no_nl(self, ast):
        return ast

def main(filename, startrule, trace=False):
    import json
    with open(filename) as f:
        text = f.read()
    parser = mw_preParser(parseinfo=False)
    ast = parser.parse(text, startrule, filename=filename, trace=trace)
    print('AST:')
    print(ast)
    print()
    print('JSON:')
    print(json.dumps(ast, indent=2))
    print()

if __name__ == '__main__':
    import argparse
    import sys
    class ListRules(argparse.Action):
        def __call__(self, parser, namespace, values, option_string):
            print('Rules:')
            for r in mw_preParser.rule_list():
                print(r)
            print()
            sys.exit(0)
    parser = argparse.ArgumentParser(description="Simple parser for mw_pre.")
    parser.add_argument('-l', '--list', action=ListRules, nargs=0,
                        help="list all rules and exit")
    parser.add_argument('-t', '--trace', action='store_true',
                        help="output trace information")
    parser.add_argument('file', metavar="FILE", help="the input file to parse")
    parser.add_argument('startrule', metavar="STARTRULE",
                        help="the start rule for parsing")
    args = parser.parse_args()

    main(args.file, args.startrule, trace=args.trace)
