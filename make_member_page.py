import os

with open("members/index.md", "w") as outf:
    outf.write("---\nlayout: default\n---\n# Cersonsky Lab Members\n")

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
        ]:
            if n > 0:
                skip = n
                if n >= 3:
                    s = '\n\n<h2 style="text-align: center;"> {}</h2>\n\n|      |      |      |\n|:----:|:----:|:----:|\n'.format(
                        subtitle.title()
                    )
                    skip = 3
                elif n == 2:
                    s = '\n\n<h2 style="text-align: center;"> {}</h2>\n\n|      |      |\n|:----:|:----:|\n'.format(
                        subtitle.title()
                    )
                else:
                    s = '\n\n<h2 style="text-align: center;"> {}</h2>\n\n|      |\n|:----:|\n'.format(
                        subtitle.title()
                    )
                outf.write(s)
                for i in range(len(peeps))[::skip]:
                    my_peeps = peeps[i : i + skip]
                    my_peepcodes = peepcodes[i : i + 3]
                    images = ""
                    names = ""
                    for j in range(skip):
                        if j < len(my_peeps):
                            ext = "png"
                            if not os.path.exists(
                                "assets/img/{}.png".format(my_peepcodes[j])
                            ):
                                if not os.path.exists(
                                    "assets/img/{}.jpg".format(my_peepcodes[j])
                                ):
                                    raise FileNotFoundError(
                                        "File assets/img/{}.png does not exist.".format(
                                            my_peepcodes[j]
                                        )
                                    )

                                else:
                                    ext = "jpg"
                            if not os.path.exists(
                                "./members/{}.md".format(my_peepcodes[j])
                            ):
                                raise FileNotFoundError(
                                    "./members/{}.md does not exist.".format(
                                        my_peepcodes[j]
                                    )
                                )
                            images += "|<a href='/members/{}'><img src='/assets/img/{}.{}' style='max-height:200px'></a>".format(
                                my_peepcodes[j], my_peepcodes[j], ext
                            )
                            names += '|<a href="/members/{}">{}</a>'.format(
                                my_peepcodes[j], my_peeps[j]
                            )
                        else:
                            images += "| "
                            names += "| "
                    images += "|\n"
                    names += "|\n"
                    outf.write(images)
                    outf.write(names)
                outf.write("{:.custom-table}\n\n------\n")
            n = 0
            subtitle = line
            peeps = []
            peepcodes = []
        elif line != "\n":
            line = line.strip("\n").strip(" - ")
            peeps.append(line)
            peepcodes.append(line.lower().replace(" ", "_"))
            n += 1
