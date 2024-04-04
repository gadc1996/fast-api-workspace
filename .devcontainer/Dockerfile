FROM python:3.11-slim-bullseye

# Set the working directory
WORKDIR /code

# Install apt-get workspace packages
RUN apt-get update && \
    apt-get install -y \
    git \
    sudo \
    wget \
    curl \
    unzip \
    groff \
    zsh

# Create user with permissions in folder /code
ARG USERNAME=devcontainer
RUN useradd -ms /bin/bash $USERNAME && \
    chown -R $USERNAME:$USERNAME /code

# Add user to sudoers
RUN echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Give full permissions to /usr/local to devcontainer user
RUN chown -R $USERNAME:$USERNAME /usr/local

# Set zsh as default shell for user
RUN chsh -s $(which zsh) $USERNAME
    
# Copy files
COPY . .

# Non root user configuration
USER $USERNAME

# Intall requirements
RUN pip install -r requirements.txt
