# Use an official Python runtime as a parent image
FROM python:3.13-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the MkDocs configuration file from the project root (build context is project root)
COPY mkdocs.yml mkdocs.yml

# Copy the requirements file from the docs directory into the container's WORKDIR
COPY docs/requirements.txt requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the documentation content (markdown files, assets, etc.) from the local 'docs' directory
# into a 'docs' subdirectory within the WORKDIR (/usr/src/app/docs)
COPY docs/ ./docs/

# Expose port 8001 for MkDocs
EXPOSE 8001

# Run mkdocs when the container launches
# mkdocs.yml is in WORKDIR (/usr/src/app/mkdocs.yml)
# docs_dir in mkdocs.yml points to 'docs', which will resolve to /usr/src/app/docs
CMD ["mkdocs", "serve", "-a", "0.0.0.0:8001"]
