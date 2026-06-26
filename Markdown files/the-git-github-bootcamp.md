# The Git & Github Bootcamp

## What You Will Learn

- Understand how Git works behind the scenes
- Explain the difference Git objects: trees, blobs, commits, and annotated tags
- Master the essential Git workflow: adding & committing
- Work with Git branches
- Perform Git merges and resolve merge conflicts
- Use Git diff to reveal changes over time
- Master Git stashing
- Undo changes using git restore, git revert, and git reset
- Work with local and remote repositories
- Master collaboration workflows: pull requests, "fork & clone", etc.
- Squash, clean up, and rewrite history using interactive rebase
- Retrieve "lost" work using git reflogs
- Write custom and powerful Git aliases
- Mark releases and versions using Git tags
- Host static websites using Github Pages
- Create markdown READMEs
- Share code and snippets using Github Gists

---

## Section 1: Course Orientation

### Welcome To The Course!

### Join Our Community!

### What The Course Covers

### A Note On The Exercises

### Accessing The Slides & Diagrams
Access slides and diagrams for GitHub bootcamp from first video titled what really matters in this section, where topics are prioritized and slides are linked in section resources.

### IMPORTANT NOTE: About The Slides Links

## Section 2: Introducing...Git!

### What Really Matters In This Section

### What Exactly Is Git?

### Visualizing Git

### A Quick History Of Git

### Who Uses Git?

### Git Vs. Github: What's The Difference?

## Section 3: Installation & Setup

### What Really Matters In This Section

### Installing Git: Terminal Vs. GUIs

### WINDOWS Git Installation

### MAC Git Installation

### Configuring Your Git Name & Email

### Installing GitKraken (Our GUI)

### Terminal Crash Course: Introduction

### Terminal Crash Course: Navigation

### Terminal Crash Course: Creating Files & Folders

### Terminal Crash Course: Deleting Files & Folders

### OPTIONAL: VS Code Color Theme

## Section 4: The Very Basics Of Git: Adding & Committing

### What Really Matters In This Section

### What Is A Git Repo?

### Our First Commands: Git Init and Git Status

### The Mysterious .Git Folder

### A Common Early Git Mistake

### The Committing Workflow Overview

### Staging Changes With Git Add

### Finally, The Git Commit Command!

### The Git Log Command (And More Committing)

### Committing Exercise

## Section 5: Commits In Detail (And Related Topics)

### What Really Matters In This Section

### Navigating The Git Documentation

### Keeping Your Commits Atomic

### Commit Messages: Present Or Past Tense?

### Escaping VIM & Configuring Git's Default Editor

### A Closer Look At The Git Log Command

### Committing With A GUI

### Fixing Mistakes With Amend
Fix git mistakes by amending the previous commit to include files. Use git commit --amend to update the message or include files; this applies only to the last commit.

### Ignoring Files w/ .gitignore

## Section 6: Working With Branches

### What Really Matters In This Section

### Introducing Branches

### The Master Branch (Or Is It Main?)

### What On Earth Is HEAD?

### Viewing All Branches With Git Branch

### Creating & Switching Branches

### More Practice With Branching
Explore creating and switching branches with git branch and git switch, based on the current head, and see how commits on diverging branches like oldies and georges affect history.

### Another Option: Git Checkout Vs. Git Switch

### Switching Branches With Unstaged Changes?

### Deleting & Renaming Branches

### How Git Stores HEAD & Branches

### Branching Exercise

## Section 7: Merging Branches, Oh Boy!

### What Really Matters In This Section

### An Introduction To Merging

### Performing A Fast Forward Merge

### Visualizing Merges

### Generating Merge Commits

### Oh No! Merge Conflicts!
Resolve merge conflicts in Git by editing conflicted files, removing conflict markers (head and branch), and committing the final resolution after choosing edits to keep.

### Resolving Merge Conflicts

### Using VSCode To Resolve Conflicts

### Merging Exercise

## Section 8: Comparing Changes With Git Diff

### What Really Matters In This Section

### Introducing The Git Diff Command

### A Guide To Reading Diffs

### Viewing Unstaged Changes
Learn to use git diff to compare the working directory, staging area, and HEAD, including file-name variations, and see how changes move from unstaged to staged.

### Viewing Working Directory Changes

### Viewing Staged Changes

### Diffing Specific Files

### Comparing Changes Across Branches

### Comparing Changes Across Commits

### Visualizing Diffs With GUIs

### Diff Exercise

## Section 9: The Ins and Outs of Stashing

### What Really Matters In This Section

### Why We Need Git Stash

### Stashing Basics: Git Stash Save & Pop

### Practicing With Git Stash

### Git Stash Apply
Explore git stash apply to reuse stash changes across branches, contrast it with git stash pop, and resolve conflicts while keeping stashed changes available.

### Working With Multiple Stashes

### Dropping & Clearing The Stash

### Stashing Exercise

## Section 10: Undoing Changes & Time Traveling

### What Really Matters In This Section

### Checking Out Old Commits

### Re-Attaching Our Detached HEAD!
Explore how to navigate a detached HEAD, inspect old commits, switch back to master, and create a new branch to preserve different versions.

### Referencing Commits Relative to HEAD

### Discarding Changes With Git Checkout

### Un-Modifying With Git Restore

### Un-Staging Changes With Git Restore

### Undoing Commits With Git Reset

### Reverting Commits With...Git Revert

### Undoing Changes Exercise
