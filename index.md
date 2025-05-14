---
layout: default
---

# **Welcome to the webpage of the Cersonsky Lab!**

The Cersonsky group is interested in leveraging data science and molecular simulation to explore molecular systems with changing and complex phase behavior. This research aims to address pertinent fundamental and applied open problems in computational chemical and materials sciences, all to better our world. Our group is committed to conducting research that upholds the principles of open science and adheres to FAIR data standards.

While you're here, check out <a href="/members">our fantastic members</a>!

<!-- The following is the style code for the news bulletin object on the landing page-->
<style>
.news-bulletin {
  max-width: 100%;
  padding: 10px;
  background-color: white;
  overflow-x: auto;
}

.news-container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  justify-content: space-around;
}

.news-card {
  flex-shrink: 0;
  width: 250px;
  height: 380px;
  padding: 15px;
  background-color: white;
  border-radius: 10px;
  box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
}

.news-card img {
  width: 100%;
  height: 200px;
  border-radius: 8px;
  margin-top: 10px;
  object-fit: cover;
</style>

<!-- This code displays the news bulletin itself:
* To add posts to the news bulletin, add a new section to news/newsposts.json file, preferably at the top (though order does not matter)
* To add an image to the post, add your image to assets/news and link it appropriately in the newspost.json section
* The posts in the .json file are loaded by date, so the correct dating of the posts matters!-->

<div class="news-bulletin">
  <h1><a href="/news">Recent News:</a></h1>
  <div id="news-list" class="news-container"></div>
</div>

<script>
  fetch('/news/newsposts.json')
    .then(response => response.json())
    .then(data => {
      const newsList = document.getElementById('news-list');

      // Sort by date (most recent first)
      data.sort((a, b) => new Date(b.date) - new Date(a.date));

      // Slice top 4 posts, here is where you can change the number of posts to be featured
      const latestNews = data.slice(0, 4);

      latestNews.forEach(post => {
        const card = document.createElement('div');
        card.className = 'news-card';
        card.innerHTML = `
          <strong>${post.title}</strong><br>
          <em>${post.date}</em>
          ${post.image ? `<img src="${post.image}" alt="${post.title}">` : ''}
          <p style="display: -webkit-box; -webkit-line-clamp: 6; -webkit-box-orient: vertical;overflow: hidden;">${post.content}</p>
        `;
        newsList.appendChild(card);
      });
    })
    .catch(error => console.error('Error loading news:', error));
</script>
