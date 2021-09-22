from odoo import models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    def write(self, vals):
        """ Inherit method for call update_product_code() method of
        product_product. """
        res = super(ProductTemplate, self).write(vals)
        # Loop over all variants.
        for product in self.product_variant_ids:
            product.update_product_code()
        return res


class ProductProduct(models.Model):
    _inherit = "product.product"

    def update_product_code(self):
        """ New method for update product_pricelist_item. """
        for product in self:
            search_ids = self.env["product.pricelist.item"].search(
                [
                    ("product_id", "=", product.id),
                ]
            )
            search_ids.write(
                {
                    "name": product.name,
                    "applied_on": "0_product_variant",
                    "product_id": product.id,
                    "fixed_price": 122,
                }
            )
