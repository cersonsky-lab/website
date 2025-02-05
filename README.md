## Adding your page to the website
1. Create a new branch by executing `git checkout -b your_name_branch` in the terminal.
2. Add your name to `members.txt` under the appropriate category in alphabetic order by last name. Type your name _exactly_ how you would like it to show up in the directory.
3. Copy `members/example_student.md` to `members/your_name.md`, where `your_name` is the name you wrote in (1), but lowercase and with '_' instead of spaces.
4. Fill out `members/your_name.md`! Make sure to replace all instances of `example student` with your name. 
5. Add a professional photo (preferably square aspect ratio) at `assets/img/your_name.png`.
6. Add any extra photos (research, hobbies, etc.) at `assets/img/your_name_#.png`., where `#` is a number 1-3. If you choose not to do this, comment out the table in `members/your_name.md`.
7. Run `make_member_page.py` and check that there are no errors.
8. Preview your webpage by calling `bundle install; bundle exec jekyll serve`.
9. Commit your branch and push it to the repository with `git add *; git commit -m "Making a page for your name"; git push origin your_name_branch`.
10. Create a pull request on `https://github.com/cersonsky-lab/website/pulls` and check that all tests run.
11. Request one of your group members and Rosy (@rosecers) as a reviewer.    
