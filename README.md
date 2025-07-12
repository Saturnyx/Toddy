# Toddy 📝

A Discord bot that helps you manage your to-do list directly in your Discord server! Keep track of tasks, organize them with tags, and collaborate with your team members.

## ✨ Features

- **Add Tasks**: Create new tasks with optional tags for better organization
- **List Tasks**: View all your tasks with their status, tags, and creator information
- **Mark Complete**: Mark tasks as done when completed
- **Edit Tasks**: Update task descriptions when needed
- **Remove Tasks**: Delete individual tasks or clear all tasks
- **Tag System**: Organize tasks with custom tags
- **User Tracking**: See who created each task and when
- **Clean Interface**: Uses emoji reactions for quick feedback

## 🚀 Commands

All commands use the `\` prefix:

| Command    | Usage                                | Description                                     |
| ---------- | ------------------------------------ | ----------------------------------------------- |
| `\hello`   | `\hello`                             | Greets you with a wave reaction                 |
| `\todo:`   | `\todo: <task> tags: <tag1, tag2>`   | Add a new task to the list (tags are optional)  |
| `\list`    | `\list`                              | Display all tasks with their status and details |
| `\done:`   | `\done: <task_number>`               | Mark a task as completed                        |
| `\remove:` | `\remove: <task_number>`             | Remove a specific task from the list            |
| `\edit:`   | `\edit: <task_number> <new_message>` | Update the description of a task                |
| `\clear`   | `\clear`                             | Remove all tasks from the list                  |
| `\cls`     | `\cls`                               | Clear all messages in the channel               |

## 📋 Usage Examples

```
# Add a simple task
\todo: Review the project documentation

# Add a task with tags
\todo: Fix login bug tags: urgent, backend

# List all tasks
\list

# Mark task #2 as done
\done: 2

# Edit task #1
\edit: 1 Review and update project documentation

# Remove task #3
\remove: 3

# Clear all tasks
\clear
```

## 🛠️ Setup

### Prerequisites

- Python 3.8 or higher
- A Discord bot token
- Required Python packages (see requirements.txt)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Saturnyx/Toddy.git
   cd Toddy
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Create a Discord Bot**

   - Go to the [Discord Developer Portal](https://discord.com/developers/applications)
   - Create a new application and bot
   - Copy the bot token

4. **Configure Environment Variables**
   Create a `.env` file in the project root:

   ```env
   DISCORD_TOKEN=your_bot_token_here
   ```

5. **Invite the Bot to Your Server**

   - In the Discord Developer Portal, go to OAuth2 > URL Generator
   - Select "bot" scope and necessary permissions:
     - Send Messages
     - Read Message History
     - Add Reactions
     - Manage Messages (for `\cls` command)
   - Use the generated URL to invite the bot

6. **Run the Bot**
   ```bash
   python main.py
   ```

## 🔧 Configuration

The bot uses the following intents:

- `message_content`: Required to read message content
- Default intents for basic bot functionality

## 📦 Dependencies

- **discord.py**: Main Discord API wrapper
- **python-dotenv**: Environment variable management
- **aiohttp**: Asynchronous HTTP client/server

## 🤝 Contributing

Contributions are welcome! Here are some ways you can help:

1. **Report Issues**: Found a bug? Open an issue!
2. **Feature Requests**: Have an idea? We'd love to hear it!
3. **Code Contributions**:
   - Fork the repository
   - Create a feature branch
   - Make your changes
   - Submit a pull request

## 📝 License

This project is open source. Feel free to use, modify, and distribute as needed.

## 🙋‍♂️ Support

If you encounter any issues or have questions:

- Check the existing issues on GitHub
- Create a new issue with detailed information
- Join our Discord server for community support

Made with ❤️ for Discord communities who want to stay organized!
