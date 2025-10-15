FROM ubuntu:latest

# install app dependencies
RUN apt-get update && apt-get install -y ruby-full build-essential zlib1g-dev git 
RUN echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
RUN echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
RUN echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
RUN . ~/.bashrc

RUN gem install jekyll bundler

# We will mount our current local directory (my/path/to/website) to the docker container, so we set this as our working directory.
WORKDIR /website 

# Copy over the Gemfile and gemspec so we can run install.
COPY ./Gemfile /Gemfile 
COPY ./jekyll-theme-minimal.gemspec /jekyll-theme-minimal.gemspec
RUN bundle install

# This command runs when the docker container starts, and will run the localhost server.
CMD ["bundle", "exec", "jekyll", "serve", "--host", "0.0.0.0"]

EXPOSE 4000

# To build the docker image from this Dockerfile, run: `docker build -t jekyll:latest .` without the backticks. This will take a few min the first time as it installs a bunch of stuff, but you only have to build the image once.
# To run a container from this image, run `docker run --rm -it -v $(pwd):/website -p 4000:4000 jekyll:latest` This will mount the current folder into /website in the docker container, run the server, and forward the port so the webpage can be viewed locally.