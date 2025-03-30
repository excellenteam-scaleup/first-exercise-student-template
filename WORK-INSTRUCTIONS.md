# DEVELOPMENT INSTRUCTIONS

This file presents a few guidelines you need to follow, so that your workflow in git will be smooth. 

## Workflow
 ### GitHub Flow
 In our project, we use a structured branching strategy involving `main`, and feature branches. The `main` branch serves as the primary development branch where all the feature development takes place. Contributors create feature branches off of `main` for each new feature or bug fix. After completing the development, the changes are merged back into `main` through pull requests.

#### Updating the main Branch:

 1. **Create a Feature Branch:**
    - From  `main` branch, create a new branch. This is where you'll work on your changes.
    ```bash
    git checkout main
    git pull origin main
    git checkout -b your-feature-branch
    ```

 2. **Develop Your Feature:**
    - Make your changes in this feature branch. Commit these changes to the branch.
    - The -p flag for the git add is used to pick the specific changes you want. Use h command in the
    - interactive shell that opens up after the usage of the command. 
    - make sure to add only the specific changes you want. 
    ```bash
    git add -p 
    git commit -m "Your commit message"
    ```

 3. **Create a Pull Request (PR):**
    - Push your branch to the remote repository and open a pull request to the `main` branch.
    - If you receive an error regarding upstream branches, follow the recommendation in the output using --set-upstream.
    ```bash
    git push origin your-feature-branch
    ```
    - On GitHub, create a new PR from `your-feature-branch` to `main` 

 4. **Merge the PR:**
    - After Pull Request review
    - Choose **"Rebase and merge"**.
    ``` 
#### Managing conflicts
Here's how to manage a scenario, with `feature/one` already rebased and merged into `main`, and now needing to add changes from `feature/two` into `main`.

##### Managing Conflicts on Master Branch:
**Update Your Local main Branch:**
Before attempting to merge `feature/two`, ensure your local `main` branch is up to date with the remote repository. This includes the changes from `feature/one` that were recently merged.

    git checkout main
    git pull origin main

**Rebase feature/two Against the Updated main:**
Switch to your `feature/two` branch and rebase it against the updated `main` branch. This step is crucial as it applies your `feature/two` changes on top of the latest `main`, helping to identify and resolve conflicts outside the `main` branch.

    git checkout feature/two
    git rebase main

During the rebase process, git may pause and alert you to conflicts that need to be resolved manually.

**Resolve Conflicts:**
If there are conflicts, git will stop the rebase and list the files that need manual intervention. Open these files in your code editor, and you'll see sections marked with <<<<<<<, =======, and >>>>>>>, indicating conflicting changes. Resolve each conflict by editing the file to your desired final state.

After resolving each conflict in a file, add it to the staging area:

    git add <filename>

Once all conflicts are resolved and the changes are staged, continue the rebase:

    git rebase --continue

Repeat this process until all conflicts are resolved and the rebase is complete. If at any point you decide that the rebase should be aborted, you can do so with `git rebase --abort`.

**Finalize the Merge:**
After successfully rebasing `feature/two` onto the latest `main`, push your changes to the remote feature branch (you might need to use force push due to the rebase, but be cautious as this can overwrite history on the remote branch):

    git push origin feature/two --force

Then, create a pull request for `feature/two` into `main` as you did with `feature/one`. Since `feature/two` has been rebased, the pull request should only contain the changes unique to `feature/two` and be free of conflicts with `main`.

**Review and Merge the Pull Request:**
Have your changes reviewed through the pull request process. If there are no additional conflicts or issues, merge `feature/two` into `main` using your project's preferred merge strategy - either squash and merge, or rebase and merge.
