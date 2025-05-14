---
layout: default
---

# **Cersonsky Lab News**

some sort of description

<!-- The following is the style code for the news bulletin object on the news page-->
<style>
.news-bulletin {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  background-color: white;
  border-radius: 10px;
}

.news-container {
  display: block; /* Stack items vertically */
}

.news-card {
  margin-bottom: 20px;
  padding: 15px;
  background-color: white;
  border-radius: 10px;
  box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
  border-left: 4px solid black; /* optional accent */
}

.news-card img {
  max-width: 100%;
  height: auto;
  border-radius: 8px;
  margin-top: 10px;
}
</style>

<!-- This code displays the news bulletin itself:
* To add posts to the news bulletin, add a new section to news/newsposts.json file, preferably at the top (though order does not matter)
* To add an image to the post, add your image to assets/news and link it appropriately in the newspost.json section
* The posts in the .json file are loaded by date, so the correct dating of the posts matters!-->

<div class="news-bulletin">
  <!--<h1>Recent News:</h1>-->
  <div id="news-list" class="news-container"></div>
</div>

<script>
  fetch('/news/newsposts.json')
    .then(response => response.json())
    .then(data => {
      const newsList = document.getElementById('news-list');

      // Sort by most recent date
      data.sort((a, b) => new Date(b.date) - new Date(a.date));
      const latestNews = data;

      latestNews.forEach(post => {
        const card = document.createElement('div');
        card.className = 'news-card';
        card.innerHTML = `
          <strong>${post.title}</strong><br>
          <em>${post.date}</em>
          <p>${post.content}</p>
          ${post.image ? `<img src="${post.image}" alt="${post.title}">` : ''}
        `;
        newsList.appendChild(card);
      });
    })
    .catch(error => console.error('Error loading news:', error));
</script>
