# ![Git](2color-lightbg@1x.png)

Run `git` without arguments to get a list of basic commands

| Workflow |
|----------|
| Pull changes only using fast forward |
| `git pull --ff-only` |
| Cherry-pick a commit |
| `git cherry-pick <commit>` |
| Push and set tracking information |
| `git push -u origin <branch>` |
| Show the working tree status incl. untracked files |
| `git status -u` |

| Explore Changes |
|-----------------|
| Compact view of commit history |
| `git log --oneline` |
| Look at a specific commit |
| `git show <commit>` |
| Look at changes in a range of commits |
| `diff <commit> <commit>` |
| Look at changes in staged files |
| `git diff --staged` |
| Look at changes using an external diff tool |
| `git difftool [<commit> [<commit>]] [--] [<path>...]` |

| Resolve Conflicts |
|-------------------------------------|
| Resolve conflicts using an external merge tool |
| `git mergetool` |
| Reset only merge related changes after cancelling |
| `git reset --merge` |

| Branching |
|-----------|
| List local branches with commit and tracking info |
| `git branch -vv` |
| Create and switch to new branch |
| `git checkout -b <branch-name>` |
| Create a new branch corresponding to a tag |
| `git checkout -b tags/<tag-name>` |
| Switch to a remote branch |
| `git checkout -t <remote>/<branch-name>` |
| Rename a branch |
| `git branch -m <new-branch-name>` |
| Delete a branch |
| `git branch -d <branch-name>` |
| Delete a remote branch |
| `git push <remote> --delete <branch-name>` |
| Propagate remote-deleted branches to your repo |
| `git fetch --all --prune` |

| Clean up & Reset |
|------------------|
| Clean up everything interactively, including ignored files and directories |
| `git clean -fx -d -i` |
| Reset local branch to remote HEAD |
| `git fetch <remote> && git reset FETCH_HEAD --hard` |

| Submodules |
|------------|
| Update all submodules |
| `git submodule update --init --recursive` |
| Add a submodule (also works if repo already exists) |
| `git submodule add <url> <path>` |
| Push commits including associated submodule revisions | 
| `git push --recurse-submodules=on-demand` |

| Stash work in progress |
|------------------------|
| Stash work in progress, incl. untracked files |
| `git stash save -u "Comment"` |
| Restore work in progress (also merge to stage) |
| `git stash pop --index` |

| Rewrite History |
|-----------------|
| Pull changes only using rebase |
| `git pull --rebase[=interactive] <remote> <branch-name>` |
| Amend the previous commit, using your original message |
| `git add --all && git commit --amend` |
| Regress HEAD by one commit without reverting changes |
| `git reset --soft HEAD^` |
| Regress HEAD by N commits without reverting changes |
| `git reset --soft HEAD~N` |
| Change previous N commits with an interactive rebase |
| `git rebase -i HEAD~N` |
| Marks your commit as a fix of a previous commit |
| `git commit --fixup <commit>` |
| Squash fixup commits to normal commits |
| `git rebase -i --autosquash <commit>` |
| Force push to Remote Repository |
| `git push -f <remote-name> <branch-name>` |

| Configuration |
| ------------- |
| Check configuration |
| `git config --list` |
| Setup your name |
| `git config --global user.name "John Doe"` |
| Setup your email |
| `git config --global user.email johndoe@example.com` |
| Cache your credentials for limited time |
| `git config credential.helper cache` |
| Edit [local/global] git config in editor |
| `git config [--global] --edit` |
| Use nano as the default editor |
| `git config --global core.editor "nano"` |
| Use nano as the default editor (Windows git bash) |
| `git config --global core.editor "winpty nano"` |
