document.querySelector('#add_item').addEventListener('click', function () {
  const ul = document.querySelector('.my_list');     // Sélectionne la liste ul
  const li = document.createElement('li');           // Crée un nouvel élément li
  li.textContent = 'Item';                            // Ajoute le texte "Item"
  ul.appendChild(li);                                 // Ajoute le li à la fin de la liste ul
});
