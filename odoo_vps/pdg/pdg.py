# -*- coding: utf-8 -*-

import time

from openerp.osv import fields, osv
from openerp.tools.translate import _
from openerp import workflow
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT

class pdg_contract(osv.osv):
    _name = 'pdg.contract'
    _columns = {
        #'order_id': fields.many2one('sale.order', 'Order Reference'),
        'partner_id': fields.many2one('res.partner', 'Cliente'),
        'name': fields.char('Nombre', size=120),
        'date_start': fields.date('Inicio'),
        'date_end': fields.date('Fin'),

        'vps_online': fields.boolean('Online'),
        'vps_server': fields.many2one('pdg.vps', 'VPS'),
        'vps_access': fields.many2one('pdg.vps.access', 'VPS Access'),

        'cms_name': fields.many2one('pdg.cms', 'CMS'),
        'cms_access': fields.many2one('pdg.cms.access', 'CMS Access'),
        'cms_version': fields.char('CMS Version', size=10)
    }

class pdg_vps(osv.osv):
    _name = 'pdg.vps'
    _columns = {
        'name': fields.char('Nombre', size=30),
        'ip': fields.char('Ip', size=30),
    }

class pdg_vps_access(osv.osv):
    _name = 'pdg.vps.access'
    _columns = {
        'username': fields.char('User', size=30),
        'password': fields.char('Password', size=30),
    }


class pdg_cms(osv.osv):
    _name = 'pdg.cms'
    _columns = {
        'name': fields.char('Nombre', size=30),
        'web': fields.char('Web', size=30),
    }

class pdg_cms_access(osv.osv):
    _name = 'pdg.cms.access'
    _columns = {
        'database': fields.char('Database', size=30),
        'name': fields.char('Nombre', size=30),
        'password': fields.char('Password', size=30),
        'prefix': fields.char('Prefix', size=30),
    }

