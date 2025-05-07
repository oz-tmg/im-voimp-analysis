# im-voimp-analysis
Transcribes voice and video messages into text to analyze chat conversations from apps that allow for downloadable backups of chats.  Mainly built for WhatsApp conversations.

# Requirements
Uses Python and R simultaneously.
    - R, for it's better data visualization and presentation tools.
    - Python, for data import, APIs that transcribe audio messages and sentiment analysis of images.

Used VS Code to run both.  

# Setup

## Pyenv
Using pyenv is a must since given the high degree of dependency between python versions and libraries able to transcribe audio files and describe images in python.  

```
{ 
# Install pyenv
curl https://pyenv.run | bash

# Add pyenv to your shell
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc

# Restart your shell
exec "$SHELL"

pyenv install 3.11.9  # or latest stable version

# Create new virtualenv
pyenv virtualenv 3.11.9 whatsapp-chat-analysis-env
pyenv activate whatsapp-chat-analysis-env

# Set the Python version for the current directory
pyenv local whatsapp-chat-analysis-env

# Audio transcription
pip install openai faster-whisper ffmpeg-python

# Google Drive access
pip install gdown pydrive

# R interface
pip install rpy2

# Image captioning
pip install torch torchvision transformers

# Reading local .env files 
pip install python-dotenv

# Set up environment variables for GDrive login (optional)
echo 'export SNOWSQL_ACCOUNT="<your_account>"' >> ~/.bashrc
echo 'export SNOWSQL_USER="<your_username>"' >> ~/.bashrc
echo 'export SNOWSQL_PWD="<your_password>"' >> ~/.bashrc
echo 'export SNOWSQL_DATABASE="<your_database>"' >> ~/.bashrc
echo 'export SNOWSQL_SCHEMA="<your_schema>"' >> ~/.bashrc
echo 'export SNOWSQL_WAREHOUSE="<your_warehouse>"' >> ~/.bashrc
echo 'export SNOWSQL_ROLE="<your_role>"' >> ~/.bashrc

# Restart your shell to apply changes
exec "$SHELL"
}
```

### Migration Guide for OpenAI
First, update the package:
`pip install --upgrade openai`

Then run the terminal code below.  It will automatically migrate your codebase using grit, either online or with the following CLI command on Mac or Linux:
`openai migrate`
