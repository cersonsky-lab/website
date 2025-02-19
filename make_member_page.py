import os

with open("members/index.md", "w") as outf:
    outf.write("---\nlayout: default\n---\n# Cersonsky Lab Members\n\n")
    outf.write("<head>\n<style>\n.profile-container {\n display: flex;\n flex-direction: row;\n flex-wrap: wrap;\n"
               " justify-content: center;\n align-items: center;\n gap: 25px 10px;\n max-width: 700px;\n"
               " margin-left: auto;\n margin-right: auto;\n margin-top: 20px;\n margin-bottom: 20px;\n}\n"
               ".profile {\n text-align: center;\n width: 210px;\n}\n\n"
               "ul {\n list-style-type: none;\n padding: 0\n}\n\n"
               "li {\n text-align: center;\n font-size: 24px;\n}\n\n"
               "@media print, screen and (max-width: 1100px) {\n .profile-container {\n  max-width: 450px\n }\n"
               " .profile{\n  width: 47%;\n }\n\n"
               "@media print, screen and (max-width: 960px) {\n .profile-container {\n  max-width: 700px\n }\n"
               " .profile{\n  width: 31%;\n }\n\n"
               "@media print, screen and (max-width: 720px) {\n .profile-container {\n  max-width: 450px\n }\n"
               " .profile{\n  width: 47%;\n }\n\n"
               "</style>\n</head>\n\n")

    n = 0
    subtitle = ""
    peeps = []
    peepcodes = []
    for line in open("members.txt"):
        if line in [
            "principal investigator\n",
            "postdoctoral researchers\n",
            "graduate researchers\n",
            "undergraduate researchers\n",
            "visitors and collaborators\n",
            "alumni\n",
            #"end\n"
        ]:
            if n > 0:
                s = f'\n\n<h2 style="text-align: center;"> {subtitle.title()}</h2>\n\n'
                skip = n
                outf.write(s)
                outf.write('<div class="profile-container">\n')
                images = ""
                for j in range(len(peeps)):
                    if j < len(peeps):
                        ext = "png"
                        if not os.path.exists(
                            f"assets/img/{peepcodes[j]}.png"
                        ):
                            if not os.path.exists(
                                f"assets/img/{peepcodes[j]}.jpg"
                            ):
                                raise FileNotFoundError(
                                    f"File assets/img/{peepcodes[j]}.png does not exist."
                                )

                            else:
                                ext = "jpg"
                        if not os.path.exists(
                            f"./members/{peepcodes[j]}.md"
                        ):
                            raise FileNotFoundError(
                                f"./members/{peepcodes[j]}.md does not exist."
                            )
                        images += f'<div class="profile">\n<a href="/members/{peepcodes[j]}"><img src="/assets/img/{peepcodes[j]}.{ext}" style="width:200px; height:200px; object-fit:cover;"></a><br><a href="/members/{peepcodes[j]}">{peeps[j]}</a>\n</div>\n'
                images += "</div>\n"
                outf.write(images)
                outf.write("\n\n------\n")
            n = 0
            subtitle = line
            peeps = []
            peepcodes = []
        elif line in [
            "end\n"
        ]:
            if n > 0:
                s = f'\n\n<h2 style="text-align: center;"> {subtitle.title()}</h2>\n\n'
                skip = n
                outf.write(s)
                outf.write('<div class="container">\n<ul>\n')
                images = ""
                for j in range(len(peeps)):
                    if j < len(peeps):
                        images += f'\t<li>{peeps[j]}</li>\n'
                        #images += f'<div class="profile">\n<a href="/members/{peepcodes[j]}"></a><br><a href="/members/{peepcodes[j]}">{peeps[j]}</a>\n</div>\n'
                #images += 
                images += "</ul>\n</div>\n"
                outf.write(images)
                outf.write("\n\n------\n")
            n = 0
            subtitle = line
            peeps = []
            peepcodes = []
        elif line != "\n":
            line = line.strip("\n").strip(" - ")
            peeps.append(line)
            peepcodes.append(line.lower().replace(" ", "_"))
            n += 1
