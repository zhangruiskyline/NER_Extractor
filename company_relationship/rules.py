# Write here your rules
# RELATION = 'your relation here'


# -*- coding: utf-8 -*-

from refo import Star, Any
from iepy.extraction.rules import rule, Token, Pos, Lemma

RELATION = "buy"

@rule(True,priority=1)
def company_buy_company(Subject, Object):
    anything = Star(Any())
    return  Subject + Lemma("buy")+ Object + anything


@rule(True,priority=1)
def company_buy_company_2(Subject, Object):
    anything = Star(Any())
    return  Subject + anything + Lemma("buy")+ Object

@rule(False,priority=1)
def company_buy_company_2(Subject, Object):
    anything = Star(Any())
    return  Subject + Lemma("compete")+ Object