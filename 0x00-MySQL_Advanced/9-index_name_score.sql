-- Script to create an index on the first letter of 'name' and 'score'
DELIMITER $$

CREATE INDEX idx_name_first_score ON names ((LEFT(name, 1)), score)$$

DELIMITER ;
