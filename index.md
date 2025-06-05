---
layout: default
---

# **Welcome to the webpage of the Cersonsky Lab!**

The Cersonsky group is interested in leveraging data science and molecular simulation to explore molecular systems with changing and complex phase behavior. This research aims to address pertinent fundamental and applied open problems in computational chemical and materials sciences, all to better our world. Our group is committed to conducting research that upholds the principles of open science and adheres to FAIR data standards.

**This website is fully-built by our group at UW-Madison, in order to give it a personality and provide opportunities for our group to practice their skills in version control (via Git) and software collaboration.** Every person in the lab, from undergraduates to PI, are responsible for making and updating their own page, reviewing edits, and making suggestions about how to improve this public-facing resource. We hope you enjoy what we've come up with!

<style>
.image-hover-container {
  display: inline-block;
  max-width: 100%;
}

.image-hover-container img {
  width: 100%;
  height: auto;
  transition: opacity 0.3s ease-in-out;
}

.image-hover-container img.hover-image {
  position: absolute;
  top: 0;
  left: 0;
  opacity: 0;
}

.image-hover-container:hover img.hover-image {
  opacity: 1;
}

.image-hover-wrapper {
  position: relative;
  display: inline-block;
  width: 100%;
  max-width: 400px; /* Adjust as needed */
}
</style>

<div class="image-hover-wrapper">
  <div class="image-hover-container">
    <img src="{{ site.baseurl }}/assets/imgs/group_photo_06_2025.jpg" alt="Default Image">
    <img class="hover-image" src="{{ site.baseurl }}/assets/imgs/group_photo_06_2025-02.jpg" alt="Hover Image">
  </div>
</div>
