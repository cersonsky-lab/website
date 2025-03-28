---
layout: default
---

# **Welcome to the webpage of the Cersonsky Lab!**

The Cersonsky group is interested in leveraging data science and molecular simulation to explore molecular systems with changing and complex phase behavior. This research aims to address pertinent fundamental and applied open problems in computational chemical and materials sciences, all to better our world. Our group is committed to conducting research that upholds the principles of open science and adheres to FAIR data standards.

While you're here, check out <a href="/members">our fantastic members</a>!

<!-- The following is the style code for the news bulletin objects-->
<style>
.news-bulletin {
    max-width: 700px;
    max-height: 1000px;  /* Set the maximum height */
    margin-right: auto;
    padding: 20px;
    background-color: #f9f9f9;
    border-radius: 10px;
    box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
    overflow-y: auto; /* Enables vertical scrolling if content exceeds max height */
  }
  
  .news-item {
    margin-bottom: 20px;
    padding-bottom: 10px;
    border-bottom: 1px solid #ddd;
  }
  
  .news-item img {
    display: block;
    max-height: 200px;
    max-width: 400px;
    height: auto;
    margin-top: 10px;
    border-radius: 8px;
    box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
  }
  </style>

<!-- This code displays the news bulletin itself:
* To add posts to the news bulletin, add a new section to internal/newsposts.json
* To add an image to the post, add your image to assests/news and link it appropriately in the newspost.json post
* The .json is a little annoying but I could not figure out a better way to do it-->

<div class="news-bulletin">
  <h1>Lab News!</h1>
  <ul id="news-list"></ul>
</div>

<script>
  fetch('/internal/newsposts.json')
    .then(response => response.json())
    .then(data => {
      const newsList = document.getElementById('news-list');
      data.forEach(post => {
        const listItem = document.createElement('li');
        listItem.className = 'news-item';
        listItem.innerHTML = `<strong>${post.title}</strong> - <em>${post.date}</em>
          <p>${post.content}</p>
          ${post.image ? `<img src="${post.image}" alt="${post.title}">` : ''}`;
        newsList.appendChild(listItem);
      });
    })
    .catch(error => console.error('Error loading news:', error));
</script>