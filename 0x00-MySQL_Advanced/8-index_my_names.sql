-- creates an index idx_names_first on the table names and
-- first letter of the name
CREATE INDEX idx_name_first ON names(name(1));