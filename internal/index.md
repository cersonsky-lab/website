---
layout: default
---

# Internal Wiki

## Administrative stuff

- [On-boarding steps](/internal/onboard)
- [Group guidelines](https://docs.google.com/document/d/1Z-WA_A9c1kzol6xR3PqYmwi2-I_M_S8DDMXS7CykKc8/edit?usp=sharing)
- [Reproducible Computational Environments](/internal/reproducible-comp)
- [Paper publication checklist](/internal/paperpub-todo)
- [Off-boarding steps](/internal/offboard)

## Presentations and Slides

- [Rosy's Previous Presentations](https://drive.google.com/drive/folders/1EUrJ_0fvkSWEr2CMPQIp7MU7AXsFlrjW?usp=sharing)
- [Group Meeting Presentations](https://drive.google.com/drive/folders/1dYHTgyDiGY05MSSJpxTmCZ1JyGJ2_ca6?usp=sharing)

## Useful Links

- [scikit-matter](https://scikit-matter.readthedocs.io/en/latest/): a repository of scikit-learn compatible methods for chemical and materials research
- [AniSOAP](https://github.com/cersonsky-lab/anisoap): a software suite for representing anisotropic particles in machine learning feature spaces
- [Kernel tutorials](https://github.com/lab-cosmo/kernel-tutorials): a set of pedagogical notebooks for learning non-linear machine learning methods

## Group Member Blogposts

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.date | date: "%B %d, %Y: " }}{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>
