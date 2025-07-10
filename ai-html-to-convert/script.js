document.addEventListener("DOMContentLoaded", () => {
  const loadUsersBtn = document.getElementById("loadUsersBtn");
  const userList = document.getElementById("userList");
  const loadingMessage = document.getElementById("loadingMessage");
  const errorMessage = document.getElementById("errorMessage");

  loadUsersBtn.addEventListener("click", async () => {
    loadingMessage.classList.remove("hidden");
    errorMessage.classList.add("hidden");
    userList.innerHTML = ""; // Limpiar lista

    try {
      // Simulación de fetch con Axios (en React usaremos Axios directamente)
      const response = await fetch(
        "https://jsonplaceholder.typicode.com/users"
      );
      if (!response.ok) {
        throw new Error("Error al cargar los usuarios");
      }
      const users = await response.json();

      users.forEach((user) => {
        const li = document.createElement("li");
        li.innerHTML = `
                    <strong>${user.name}</strong>
                    <span>(${user.email})</span>
                `;
        userList.appendChild(li);
      });
    } catch (error) {
      console.error("Error fetching users:", error);
      errorMessage.classList.remove("hidden");
    } finally {
      loadingMessage.classList.add("hidden");
    }
  });
});
