# Contributing to Toddy 🤝

Thank you for your interest in contributing to Toddy! We welcome contributions from everyone, whether you're fixing bugs, adding features, improving documentation, or suggesting enhancements.

## 📋 Table of Contents

- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Code Guidelines](#code-guidelines)
- [Submitting Changes](#submitting-changes)
- [Issue Guidelines](#issue-guidelines)
- [Community Guidelines](#community-guidelines)

## 🚀 Getting Started

### Prerequisites

Before contributing, make sure you have:

- Python 3.8 or higher
- Git installed on your system
- A Discord account and basic understanding of Discord bots
- Familiarity with Python and the discord.py library

### First Time Setup

1. **Fork the repository**
   ```bash
   # Click the "Fork" button on GitHub, then clone your fork
   git clone https://github.com/YOUR_USERNAME/Toddy.git
   cd Toddy
   ```

2. **Add the original repository as upstream**
   ```bash
   git remote add upstream https://github.com/Saturnyx/Toddy.git
   ```

3. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up your environment**
   - Create a `.env` file with your Discord bot token
   - Create a test Discord server for development

## 💡 How to Contribute

### Types of Contributions

We welcome several types of contributions:

- 🐛 **Bug Reports**: Help us identify and fix issues
- ✨ **Feature Requests**: Suggest new functionality
- 🔧 **Bug Fixes**: Submit fixes for existing issues
- 🎨 **New Features**: Add new commands or capabilities
- 📚 **Documentation**: Improve README, comments, or guides
- 🧪 **Tests**: Add or improve test coverage
- 🎯 **Performance**: Optimize existing code

### Good First Issues

Look for issues labeled:
- `good first issue` - Perfect for newcomers
- `help wanted` - We'd love community help on these
- `documentation` - Great for non-code contributions

## 🛠️ Development Setup

### Environment Configuration

1. **Create a test Discord server** where you can safely test the bot
2. **Set up a development bot** separate from any production instance
3. **Configure your `.env` file**:
   ```env
   DISCORD_TOKEN=your_development_bot_token_here
   ```

### Testing Your Changes

1. **Run the bot locally**:
   ```bash
   python main.py
   ```

2. **Test all affected commands** in your test server
3. **Verify edge cases** and error handling
4. **Check that existing functionality** still works

## 📝 Code Guidelines

### Python Style

- Follow [PEP 8](https://pep8.org/) style guidelines
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions focused and concise

### Code Quality

```python
# Good example
@bot.command("todo:")
async def todo(ctx, *, message: str):
    """Adds a task to the to-do list with optional tags.
    
    Args:
        ctx: The command context
        message: The task message with optional tags
    """
    # Implementation here
```

### Comments and Documentation

- Add clear comments for complex logic
- Update docstrings when modifying functions
- Include usage examples in command docstrings
- Document any new configuration options

### Error Handling

- Always handle potential errors gracefully
- Provide helpful error messages to users
- Log errors appropriately for debugging

```python
# Good error handling example
try:
    # Bot operation
    await ctx.send("Task added successfully!")
except discord.Forbidden:
    await ctx.send("I don't have permission to perform this action.")
except Exception as e:
    print(f"[ERROR] Unexpected error: {e}")
    await ctx.send("An unexpected error occurred. Please try again.")
```

## 📤 Submitting Changes

### Pull Request Process

1. **Create a new branch** for your feature or fix:
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/issue-description
   ```

2. **Make your changes** following the code guidelines

3. **Test thoroughly** in your development environment

4. **Commit your changes** with clear, descriptive messages:
   ```bash
   git add .
   git commit -m "Add task priority feature with urgent/normal/low levels"
   ```

5. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request** on GitHub

### Pull Request Guidelines

#### Title Format
- Use clear, descriptive titles
- Prefix with type: `feat:`, `fix:`, `docs:`, `refactor:`
- Example: `feat: add task priority levels`

#### Description Template
```markdown
## Description
Brief description of the changes made.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Refactoring
- [ ] Other (please describe)

## Testing
- [ ] Tested locally
- [ ] All existing commands still work
- [ ] New functionality works as expected

## Screenshots (if applicable)
Include screenshots of new features or UI changes.

## Checklist
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Documentation updated (if needed)
- [ ] No breaking changes (or clearly documented)
```

## 🐛 Issue Guidelines

### Bug Reports

When reporting bugs, please include:

1. **Clear title** describing the issue
2. **Steps to reproduce** the bug
3. **Expected behavior** vs actual behavior
4. **Environment details**:
   - Python version
   - discord.py version
   - Operating system
5. **Screenshots or logs** if helpful

### Feature Requests

For feature requests, please provide:

1. **Clear description** of the proposed feature
2. **Use case** - why would this be useful?
3. **Proposed implementation** (if you have ideas)
4. **Examples** of how it would work

### Issue Labels

We use these labels to organize issues:
- `bug` - Something isn't working
- `enhancement` - New feature or improvement
- `good first issue` - Good for newcomers
- `help wanted` - Community help needed
- `documentation` - Documentation related
- `question` - General questions

## 🌟 Community Guidelines

### Code of Conduct

- Be respectful and inclusive
- Welcome newcomers and help them learn
- Provide constructive feedback
- Focus on the code, not the person
- Assume good intentions

### Communication

- Use clear, professional language
- Ask questions if something is unclear
- Provide context in discussions
- Be patient with review processes

### Recognition

Contributors will be recognized in:
- Release notes for significant contributions
- README acknowledgments
- GitHub contributor graphs

## 🔄 Keeping Your Fork Updated

```bash
# Fetch upstream changes
git fetch upstream

# Switch to main branch
git checkout main

# Merge upstream changes
git merge upstream/main

# Push updates to your fork
git push origin main
```

## 📞 Getting Help

If you need help or have questions:

1. **Check existing issues** - your question might be answered
2. **Open a new issue** with the `question` label
3. **Join our Discord server** for real-time discussion
4. **Review the documentation** in the README

## 🎉 Thank You!

Every contribution, no matter how small, helps make Toddy better for everyone. We appreciate your time and effort in contributing to this project!

---

Happy coding! 🚀
