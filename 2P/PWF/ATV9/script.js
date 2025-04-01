document.addEventListener("DOMContentLoaded", async () => {
    const timeline = document.getElementById("timeline");
    const postsResponse = await fetch("https://jsonplaceholder.typicode.com/posts");
    const posts = await postsResponse.json();
    
    for (let post of posts) {
        const userResponse = await fetch(`https://jsonplaceholder.typicode.com/users/${post.userId}`);
        const user = await userResponse.json();

        const postElement = document.createElement("div");
        postElement.classList.add("post");
        postElement.innerHTML = `
            <h5>${post.title}</h5>
            <p>${post.body}</p>
            <small>Autor: <strong>${user.username}</strong> (${user.email})</small>
            <br>
            <a href="#" class="btn btn-link" data-post-id="${post.id}">Ver Comentários</a>
            <div class="comments" id="comments-${post.id}"></div>
        `;
        
        timeline.appendChild(postElement);
    }

    document.addEventListener("click", async (event) => {
        if (event.target.matches("[data-post-id]")) {
            event.preventDefault();
            const postId = event.target.getAttribute("data-post-id");
            const commentsDiv = document.getElementById(`comments-${postId}`);

            if (commentsDiv.style.display === "none" || commentsDiv.innerHTML === "") {
                const commentsResponse = await fetch(`https://jsonplaceholder.typicode.com/comments?postId=${postId}`);
                const comments = await commentsResponse.json();
                
                commentsDiv.innerHTML = comments.map(comment => `
                    <div class="border p-2 rounded bg-light mt-2">
                        <strong>${comment.name}</strong> (${comment.email})
                        <p>${comment.body}</p>
                    </div>
                `).join("");
                commentsDiv.style.display = "block";
            } else {
                commentsDiv.style.display = "none";
            }
        }
    });
});