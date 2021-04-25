CREATE VIEW chronological_view AS
SELECT * FROM AudioFiles
ORDER BY Date;
SELECT * FROM chronological_view;
