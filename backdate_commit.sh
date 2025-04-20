#!/bin/bash

# Set the backdate (yesterday's date)
BACKDATE="2025-04-20T11:32:00"

# Add and commit each file separately
git add backdate_commit.sh
GIT_AUTHOR_DATE="$BACKDATE" GIT_COMMITTER_DATE="$BACKDATE" git commit -m "Add comment functionality (backdated --W0ow!)"

# git add add_comment.php
# GIT_AUTHOR_DATE="$BACKDATE" GIT_COMMITTER_DATE="$BACKDATE" git commit -m "Add comment functionality "

# git add add_post.php
# GIT_AUTHOR_DATE="$BACKDATE" GIT_COMMITTER_DATE="$BACKDATE" git commit -m "Implement post creation feature (backdated)"

# git add admin.css
# GIT_AUTHOR_DATE="$BACKDATE" GIT_COMMITTER_DATE="$BACKDATE" git commit -m "Style improvements for admin panel (backdated)"

# git add admin.php
# GIT_AUTHOR_DATE="$BACKDATE" GIT_COMMITTER_DATE="$BACKDATE" git commit -m "Build admin dashboard functionality (backdated)"

# git add admin_login.php
# GIT_AUTHOR_DATE="$BACKDATE" GIT_COMMITTER_DATE="$BACKDATE" git commit -m "Implement admin login system (backdated)"

# git add database.sqlite
# GIT_AUTHOR_DATE="$BACKDATE" GIT_COMMITTER_DATE="$BACKDATE" git commit -m "Update SQLite database (backdated)"

# git add db.php
# GIT_AUTHOR_DATE="$BACKDATE" GIT_COMMITTER_DATE="$BACKDATE" git commit -m "Database connection and queries (backdated)"

# git add edit_post.php
# GIT_AUTHOR_DATE="$BACKDATE" GIT_COMMITTER_DATE="$BACKDATE" git commit -m "Enable post editing (backdated)"

# git add global.css
# GIT_AUTHOR_DATE="$BACKDATE" GIT_COMMITTER_DATE="$BACKDATE" git commit -m "Global styles for consistency (backdated)"

# git add index.php
# GIT_AUTHOR_DATE="$BACKDATE" GIT_COMMITTER_DATE="$BACKDATE" git commit -m "Homepage with posts and pagination (backdated)"

# git add login.php
# GIT_AUTHOR_DATE="$BACKDATE" GIT_COMMITTER_DATE="$BACKDATE" git commit -m "User login implementation (backdated)"

# git add logout.php
# GIT_AUTHOR_DATE="$BACKDATE" GIT_COMMITTER_DATE="$BACKDATE" git commit -m "Logout system added (backdated)"

# git add profile_pictures/
# GIT_AUTHOR_DATE="$BACKDATE" GIT_COMMITTER_DATE="$BACKDATE" git commit -m "Profile pictures storage (backdated)"

# git add reg.css
# GIT_AUTHOR_DATE="$BACKDATE" GIT_COMMITTER_DATE="$BACKDATE" git commit -m "Styles for registration page (backdated)"

# git add register.php
# GIT_AUTHOR_DATE="$BACKDATE" GIT_COMMITTER_DATE="$BACKDATE" git commit -m "User registration system (backdated)"

# git add style.css
# GIT_AUTHOR_DATE="$BACKDATE" GIT_COMMITTER_DATE="$BACKDATE" git commit -m "General website styles (backdated)"

# git add uploads/
# GIT_AUTHOR_DATE="$BACKDATE" GIT_COMMITTER_DATE="$BACKDATE" git commit -m "Media upload folder (backdated)"

# Push all commits
git push origin main  # Change 'main' to your branch name if different -- wahala
