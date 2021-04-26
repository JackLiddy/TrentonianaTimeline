CREATE VIEW chronological_view AS
SELECT * FROM AudioFiles
ORDER BY Date;
SELECT * FROM chronological_view;

CREATE VIEW admin_view AS
SELECT * FROM users
WHERE privileges='admin';
SELECT * FROM admin_view;

CREATE VIEW guest_view AS
SELECT * FROM users
WHERE privileges='guest';
SELECT * FROM guest_view;

/* subquery */
SELECT * FROM Views
WHERE username IN (SELECT username FROM Views WHERE TimelineName='Jewish History');

CREATE VIEW user_bookmarks_view AS
SELECT * FROM Bookmark
WHERE username='chrissmith42';
SELECT * FROM user_bookmarks_view;
