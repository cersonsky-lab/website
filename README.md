## Adding your page to the website
1. Begin by cloning the repository to your local computer. You can do this by clicking the green `<> code` button above, copying the URL to your clipboard, and then executing `git clone link` in the terminal in which you paste the link in place of the word `link` in your desired local directory.
2. In the terminal, travel to the website directory. Remain there for the rest of the instructions. Create a new branch by executing `git checkout -b your_name_branch` in the terminal.
3. Add your name to `members.txt` (by running `nano members.txt` in the terminal) under the appropriate category in alphabetic order by last name. Type your name _exactly_ how you would like it to show up in the directory.
4. Execute `cp members/example_student.md members/your_name.md` in terminal where `your_name` is the name you wrote in (3), but lowercase and with '_' instead of spaces. This will create a file `members/your_name.md` that is an exact copy of `members/example_student.md`.
5. Fill out `members/your_name.md`! Access the file by executing `nano members/your_name.md` and make sure to replace all instances of `example student` with your name. 
6. Add a professional photo (preferably square aspect ratio) at `assets/img/your_name.png`. This can be done manually on the cumputer desktop or by executing `cp /path/to/source/your_name.png ./assets/img`, where `/path/to/source` is the path to where the image is on your computer.
7. Add any extra photos (research, hobbies, etc.) at `assets/img/your_name_#.png`, where `#` is a number 1-3. If you choose not to do this, comment out the table in `members/your_name.md`.
8. Run `make_member_page.py` and check that there are no errors.
9. Preview your webpage by calling `bundle install; bundle exec jekyll serve`.
    * This step may not work if you do not have _Jekyll_ installed correctly or installed in general on your computer. To fix this, the first step is to install _Ruby_ through a version manager. Do this by running `brew install rbenv`, then run `rbenv init`, and then restart your terminal and return to the website directory. The second step is to run `gem install jekyll`, and the problem will be solved.
    * Another reason this step may not work is because your version of _Ruby_ is not compatible with the bundler that generatreed the _Gemfile.loc_ file (`1.17.2`). Begin by seeing if this is the issue by executing `ruby -v` in the terminal. If any number is displayed that is higher than 2.6.10, then an older version of _Ruby_ must be downloaded. Do this by executing `rbenv install 2.6.10`, then `rbenv global 2.6.10`, and finally `ruby -v` to verify version 2.6.10 of _Ruby_ is now installed.
    * Once the command is succesfully ran, copy and paste the provided URL into your browser and verify everything on the website is how you want it to look.
    * **Update as of October 10, 2025**: If none of these commands work, you can use the provided Dockerfile to create an image and container. To get started, follow [these instructions](https://docs.docker.com/get-started/get-docker/) to download, install, and learn more about Docker.
      * Run `rm Gemfile.lock` to remove the Lockfile if it exists - it will be regenerated in later steps
      * After doing so, run `docker build -t jekyll:latest .`, which will build the image. This takes a few minutes, but building the image only needs to be done once.
      * Then, run 
        * Linux/Mac: `docker run --rm -it -v $(pwd):/website -p 4000:4000 jekyll:latest` or
        * Windows Powershell:  `docker run --rm -it -v ${PWD}:/website -p 4000:4000 jekyll:latest` or
        * Windows Command Prompt: `docker run --rm -it -v %cd%:/website -p 4000:4000 jekyll:latest`
        which will run the container and the server, mounting this directory to `/website` in the docker container. Things will be properly hot-reloaded, allowing for immediate feedback on updates to the webpage.
      * After about 30 seconds, it will present you with the url `http://0.0.0.0:4000`. This URL works for Linux and Mac, but not Windows. If you're on Windows, navigate to `http://localhost:4000`.
10. Commit your branch and push it to the repository with `git add *; git commit -m "Making a page for your name"; git push origin your_name_branch`.
11. Create a pull request on `https://github.com/cersonsky-lab/website/pulls` and check that all tests run.
12. Request one of your group members and Rosy (@rosecers) as a reviewer.    
