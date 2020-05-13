FROM library/python:3.7-alpine

# Create the palylister directory
RUN mkdir /playlister
WORKDIR /playlister

# Install requirements and libraries.
#   --no-cache allows users to install packages with an index that is updated and used on-the-fly and not cached locally
RUN apk --no-cache --quiet add gcc make g++ bash git openssh \
        sqlite curl build-base libffi-dev python-dev py-pip \
        jpeg-dev zlib-dev libsass-dev

# Add needed requirements
COPY requirements.txt /playlister/
RUN pip3 install -r requirements.txt

# Copy to directory
COPY ./ /playlister/

# Open traffic
EXPOSE 8080 80 443

# Run the directory
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8080"]