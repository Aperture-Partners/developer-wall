# Add yourself to Developer Wall

You will make one real contribution in your browser. This repository is public. Use only information you are comfortable publishing.

## 1. Create your branch

1. Open the [Developer Wall repository](https://github.com/Aperture-Partners/developer-wall) and sign in.
2. Select the branch button labeled **main**.
3. Type `add-YOUR-USERNAME-profile`, replacing `YOUR-USERNAME` with your lowercase GitHub username.
4. Choose **Create branch: add-YOUR-USERNAME-profile from main**.

A branch is your separate workspace. Check that your new branch name is visible before continuing.

## 2. Add your profile

1. Choose **Add file → Create new file**.
2. Name the file `_data/profiles/YOUR-USERNAME.json` using your lowercase GitHub username.
3. Paste this example and replace every value

```json
{
  "name": "Your name or nickname",
  "github": "your-github-username",
  "favorite_language": "Still learning!",
  "fun_fact": "Ask me later!"
}
```

JSON needs double quotes and commas between lines. Do not add a comma after the final value. Keep the same four field names.

4. Choose **Commit changes…**.
5. Use the message `Add YOUR-USERNAME profile`, confirm the commit is going to your branch, and choose **Commit changes**.

A commit is a saved snapshot.

## 3. Open a pull request

1. Choose **Compare & pull request**. If the banner is gone open **Pull requests → New pull request**. Set base to `main` and compare to your branch.
2. Title it `Add YOUR-USERNAME to Developer Wall`.
3. Complete the checklist and choose **Create pull request**.

A pull request asks to add your branch to `main`.

## 4. Pass the check

Open the PR checks. **validate-profiles** checks the filename and JSON. If it fails open **Details** and fix the same file on the same branch. The PR updates on its own. Do not open a second PR.

## 5. Swap reviews

Request your assigned partner under **Reviewers**. Then open your partner's PR and choose **Files changed**. Check that it changes only their profile and that the content is appropriate.

Leave one useful comment or question. When it is ready choose **Review changes → Approve → Submit review**. A normal comment is not a formal approval. You cannot approve your own PR.

## 6. Merge and find your card

When the check is green and a different participant has approved, choose **Merge pull request → Confirm merge**. Delete your finished branch if GitHub offers the button.

Open the [live Developer Wall](https://aperture-partners.github.io/developer-wall/) and refresh after Pages finishes deploying. Publishing may take a few minutes.

## Quick glossary

- **Repository** the shared project and its history
- **Branch** a separate workspace
- **Commit** a saved snapshot
- **Pull request** a request to add work to `main`
- **Review** another person's feedback and approval
- **Merge** adding approved work to `main`
- **Deploy** publishing `main` as the site

## Stuck?

- **No branch button** ask the organizer to check your Write access
- **Wrong target branch** the PR base must be `main`
- **Invalid JSON** check double quotes and commas
- **No approval** your reviewer must use **Review changes → Approve**
- **Check pending** wait and refresh
- **Filename taken** ask the organizer for help
- **Card missing** wait a few minutes for Pages
- **Merge conflict** stop and ask the organizer
