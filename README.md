## Adding your page to the website
1. Begin by cloning the repository to your local computer. You can do this by clicking the green `<> code` button above, copying the URL to your clipboard, and then executing `git clone link` in the terminal in which you paste the link in place of the word `link` in your desired local directory.
2. In the terminal, travel to the website directory. Remain there for the rest of the instructions. Create a new branch by executing `git checkout -b your_name_branch` in the terminal.
3. Add your name to `members.txt` (by running `nano members.txt` in the terminal) under the appropriate category in alphabetic order by last name. Type your name _exactly_ how you would like it to show up in the directory.
4. Execute `cp members/example_student.md members/your_name.md` in terminal where `your_name` is the name you wrote in (3), but lowercase and with '_' instead of spaces. This will create a file `members/your_name.md` that is an exact copy of `members/example_student.md`.
5. Fill out `members/your_name.md`! Access the file by executing `nano members/your_name.md` and make sure to replace all instances of `example student` with your name. 
6. Add a professional photo (preferably square aspect ratio) at `assets/img/your_name.png`. This can be done manually on the cumputer desktop or by executing `cp /path/to/source/your_name.png ./assets/img`, where `/path/to/source` is the path to where the image is on your computer.
7. Add any extra photos (research, hobbies, etc.) at `assets/img/your_name_#.png`, where `#` is a number 1-3. If you choose not to do this, comment out the table in `members/your_name.md`.
8. Run `make_member_page.py` and check that there are no errors.
9. Preview your webpage using Docker (recommended):
    * If you don't have Docker, install it from [https://docs.docker.com/get-started/get-docker/](https://docs.docker.com/get-started/get-docker/).
    * Run `rm -f Gemfile.lock` to clear any stale lockfile.
    * Build the image once: `docker build -t jekyll:latest .`
    * Serve the site (pick your OS):
      * Linux/Mac: `docker run --rm -it -v $(pwd):/website -p 4000:4000 jekyll:latest`
      * Windows Powershell: `docker run --rm -it -v ${PWD}:/website -p 4000:4000 jekyll:latest`
      * Windows Command Prompt: `docker run --rm -it -v %cd%:/website -p 4000:4000 jekyll:latest`
    * Open [http://localhost:4000](http://localhost:4000) in your browser. Changes hot-reload automatically.
    * **Alternative (native Ruby)**: If you prefer not to use Docker, install Ruby 2.6.10 via `rbenv` (`brew install rbenv`, `rbenv install 2.6.10`, `rbenv global 2.6.10`) and run `bundle install; bundle exec jekyll serve`.
10. Commit your branch and push it to the repository with `git add *; git commit -m "Making a page for your name"; git push origin your_name_branch`.
11. Create a pull request on `https://github.com/cersonsky-lab/website/pulls` and check that all tests run.
12. Request one of your group members and Rosy (@rosecers) as a reviewer.    
