# Contributing to Lilith Context Manager

First off, thank you for considering contributing to the Lilith Context Manager! It’s people like you that make open source such a great community. We welcome any and all contributions, from bug reports and feature suggestions to documentation improvements and code patches.

To ensure a smooth and collaborative process, we have established a few guidelines that we ask you to follow.

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to the appropriate channel in our discord.

## How Can I Contribute?

There are many ways to contribute to the project. Here are some of the most common:

### 🐛 Reporting Bugs

Bugs are tracked as [GitHub Issues](https://github.com/Squirrelthug/lilith-context-manager/issues). If you find a bug, please create a new issue.

Before creating a new issue, please perform a quick search to see if the bug has already been reported. If it has, and the issue is still open, add a comment to the existing issue instead of opening a new one.

When creating a bug report, please include as many details as possible. Fill out the required template, which will help us resolve issues faster. A good bug report should include:

* **A clear and descriptive title.**
* **The version of the software you are using.**
* **A step-by-step description** of how to reproduce the problem.
* **What you expected to happen** vs. **what actually happened.**
* **Any relevant logs or error messages.**

### ✨ Suggesting Enhancements

Enhancements are also tracked as [GitHub Issues](https://github.com/your-username/lilith-context-manager/issues). If you have an idea for a new feature or an improvement to an existing one, we'd love to hear it.

When suggesting an enhancement, please provide:

* **A clear and descriptive title.**
* **A detailed description** of the proposed enhancement and why it would be valuable.
* **A step-by-step description of the desired behavior.**
* **(Optional) Any mockups or code examples** that might help illustrate your idea.

### 📝 Improving Documentation

Clear documentation is just as important as clean code. If you find a typo, a confusing sentence, or an area where the documentation could be improved, please don't hesitate to open an issue or submit a pull request.

### 💻 Submitting Code Changes (Pull Requests)

Ready to write some code? Great! Here’s how to set up your environment and submit a pull request.

#### Setting Up Your Development Environment

1.  **Fork the repository** on GitHub.
2.  **Clone your fork** locally:
    ```bash
    git clone [https://github.com/your-username-fork/lilith-context-manager.git](https://github.com/your-username-fork/lilith-context-manager.git)
    cd lilith-context-manager
    ```
3.  **Create a new branch** for your changes. Please choose a descriptive branch name (e.g., `feature/add-new-endpoint`, `fix/session-persistence-bug`).
    ```bash
    git checkout -b your-branch-name
    ```
4.  **Set up a virtual environment** and install the required dependencies. This ensures you are working in an isolated environment.
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r service/requirements.txt
    ```
    #### Making Your Changes

**Write clean, readable code.** This project's architecture is based on a clean separation of concerns. Please adhere to this principle.
**Ensure data integrity.** All data transfer uses Pydantic models for validation. If you add or modify data structures, update the corresponding models in `service/core/models.py`.
* **(Optional but Recommended) Write tests for your changes.** This helps ensure that your code works as expected and doesn't introduce any regressions.
    * **Update the documentation** if your changes affect it.
* **Format your code.**
    #### Submitting Your Pull Request

1.  **Commit your changes** with a clear and descriptive commit message.
    ```bash
    git commit -m "feat: Add a concise summary of your changes"
    ```
2.  **Push your branch** to your fork on GitHub:
    ```bash
    git push origin your-branch-name
    ```
3.  **Open a pull request** from your fork to the main `lilith-context-manager` repository.
4.  In the pull request description, **link to any relevant issues** (e.g., `Closes #123`).
5.  **Wait for a review.** One of the project maintainers will review your pull request, provide feedback, and merge it if everything looks good.

Thank you again for your contribution. We look forward to building something amazing together!