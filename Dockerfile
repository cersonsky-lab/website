FROM ubuntu:latest

# install app dependencies
RUN apt-get update && apt-get install -y ruby-full build-essential zlib1g-dev git 
RUN echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
RUN echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
RUN echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
RUN . ~/.bashrc

RUN gem install jekyll bundler
RUN mkdir /website
WORKDIR /website 
# If just a branch from main, clone then switch to branch (defaults to main, but you can change!)
RUN git clone https://github.com/cersonsky-lab/website.git .
RUN git checkout main 
# If forked, clone the fork:
# RUN git clone https://github.com/Tejas7007/website.git .
# RUN git checkout tejas_dahiya_branch
RUN bundle install

CMD ["bundle", "exec", "jekyll", "serve", "--host", "0.0.0.0"]

EXPOSE 4000

# To build the docker image from this Dockerfile, run: `docker build -t jekyll:latest .` without the backticks. This will take a few min the first time as it installs a bunch of stuff.
# To run a container from this image, run `docker run -p 4000:4000 -it jekyll` The ports should forward to your local computer.