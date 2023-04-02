
--Here we have to get the old data for the field stock_quant_package.gram_weight after the update of the field type from float to integer
UPDATE stock_quant_package SET gram_weight=gram_weight_moved0;





