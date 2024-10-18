const APIURL = 'https://api.github.com/users/';

// Task 1: Reference the HTML elements with their respective IDs (main, form and search)
let mainRef = document.getElementById("main");
let formRef = document.getElementById("form");
let searchRef = document.getElementById("search");



initUserCard();

function initUserCard(){
    let cardHTML = `
        <div class="card">
            <h2>Please type a Github username</h2>
        </div>
    `
    mainRef.innerHTML = cardHTML    
}

async function getUser(username) {
    try {
        // Task 2: Use fetch API to fetch github user data. The URL format is APIURL + username
        let response = await fetch(APIURL + username);
        let data = await response.json();

        createUserCard(data)
        getRepos(username)
    } catch(err) {
        if(err.response.status == 404) {
            createErrorCard('No profile with this username')
        }
    }
}

async function getRepos(username) {
    try {
        // Task 3: Use fetch API to fetch github user repo. 
        // The URL format is APIURL + username + '/repos?sort=created'
        let response = await fetch(APIURL + username + '/repos?sort=created');
        let data = await response.json();

        addReposToCard(data)
    } catch(err) {
        createErrorCard('Problem fetching repos')
    }
}

function createUserCard(user) {
    let userID = user.name || user.login
    let userBio = user.bio ? `<p>${user.bio}</p>` : ''
    let numFollowers = user.followers;
    let numFollowing = user.following;
    let numRepos = user.public_repos;
    let userAvatar = user.avatar_url;

    /*
      Task 4: Inject user avatar_url, user name, user ID, user bio, 
      user followers, user following, user public repos to the template literals below
    */
    let cardHTML = `
    <div class="card">
    <div>       
      <img src="${userAvatar}" alt="${userBio}" class="avatar"> 
    </div>
    <div class="user-info">
      <h2>${userID}</h2>
      ${userBio}
      <ul>
        <li>${numFollowers} <strong>Followers</strong></li>
        <li>${numFollowing} <strong>Following</strong></li>
        <li>${numRepos} <strong>Repos</strong></li>
      </ul>

      <div id="repos"></div>
    </div>
  </div>
    `
    mainRef.innerHTML = cardHTML
    
}

function createErrorCard(msg) {
    const cardHTML = `
        <div class="card">
            <h1>${msg}</h1>
        </div>
    `

    mainRef.innerHTML = cardHTML
}

function addReposToCard(repos) {
    let reposRef = document.getElementById('repos')

    repos.slice(0, 5).forEach(repo => {
            let repoEl = document.createElement('a')
            repoEl.classList.add('repo')
            repoEl.href = repo.html_url
            repoEl.target = '_blank'
            repoEl.innerText = repo.name

            reposRef.appendChild(repoEl)
        })
}

formRef.addEventListener('submit', (e) => {
    e.preventDefault()

    let user = searchRef.value

    if(user) {
        getUser(user)

        searchRef.value = ''
    }
})

