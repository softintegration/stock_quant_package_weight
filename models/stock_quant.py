# -*- coding: utf-8 -*- 

from odoo import models,fields,api,_
from odoo.exceptions import ValidationError


class QuantPackage(models.Model):
    """ Inherit stock package to add product dimensions to the package """
    _inherit = "stock.quant.package"

    gram_weight = fields.Float(string='Weight',related='product_id.gram_weight',store=True)
    gram_weight_uom_id = fields.Many2one('uom.uom', string="Weight unit of Measure",
                                         default=lambda self: self.env.ref('uom.product_uom_gram'),
                                         related='product_id.gram_weight_uom_id',store=True)




