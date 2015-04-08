# -*- coding: utf-8 -*-

import time

from openerp.osv import fields, osv
from openerp.tools.translate import _
from openerp import workflow
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT


class res_partner(osv.osv):
    _name = 'res.partner'
    _inherit = 'res.partner'
    _columns = {
        'pdg_contract': fields.one2many('pdg.contract', 'partner_id', 'Contractos'),
    }
