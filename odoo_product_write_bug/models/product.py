from odoo import models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    def write(self, vals):
        """Inherit method for call update_pricelist_item() method."""
        res = super(ProductTemplate, self).write(vals)
        # Loop over all product template.
        for template in self:
            template.update_pricelist_item()
        return res

    def update_pricelist_item(self):
        """ New method for write values in product_pricelist_item. """
        pricelist_item = self.env["product.pricelist.item"].search([])
        pricelist_item.write(
            {
                "fixed_price": 122,
            }
        )
