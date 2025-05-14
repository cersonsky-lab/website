---
layout: default
---

# **Cersonsky Lab News**

some sort of description

<!-- The following is the style code for the news bulletin object on the news page-->
<style>
.news-bulletin {
  max-width: 90%;
  margin: 0 auto;
  padding: 20px;
  background-color: white;
  border-radius: 10px;
}

.news-container {
  display: block; /* Stack items vertically */
}

.news-card {
  display: grid;
  grid-template-columns: 300px auto;
  max-width: 100%;
  height: 300px;
  margin-bottom: 20px;
  padding: 15px;
  background-color: white;
  border-radius: 10px;
  box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
  border-left: 4px solid black; /* optional accent */
}

.news-title {
  grid-column: 1 / span 2;
}

.news-title strong{
  font-size:20px;
}

.news-image {
  max-width: 280px;
  max-height: 220px;
  border-radius: 8px;
  margin-top: 10px;
  object-fit: cover;
}

.news-content{
  border-radius: 8px;
  margin-top: 10px;
  overflow: auto;
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
	  <div class="news-title">
            <strong>${post.title}</strong><br>
            <em>${post.date}</em>
	  </div>
	    ${post.image ? `<div class="news-image"><img src="${post.image}" alt="${post.title}"></div>` : ''}
	  <div class="news-content">
            <p>${post.content}</p>
	  </div>
        `;
        newsList.appendChild(card);
      });
    })
    .catch(error => console.error('Error loading news:', error));
</script>
