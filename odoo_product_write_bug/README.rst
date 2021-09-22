======================
Odoo Product Write Bug
======================

**Author**
**********
* BizzAppDev Systems Pvt. Ltd.

**Installation**
****************
* Under applications, the application odoo_product_write_bug can be installed/uninstalled.

**Description**
***************
* Technical explanation:
    - We have inherit write() method of product.template.
    - Call update_product_code() method of product.product from the write() method of product.template.
    - In the update_product_code() method, write data of product.pricelist.item.

* Steps to Reproduce an issue:
    - Create a new product variant(product.product) and save it.
    - Edit newly created product, update Income Account and Expense Account field at the same time.
    - Save the records, after saving Expense Account field get false.

**Configuration**
*****************
* #N/A

**Known issues/Roadmap**
************************

* #N/A

**Changelog**
*************
* 22/09/2021 - Created new module.
