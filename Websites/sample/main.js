// Paste the helpful function here:

function addListItem(text){
  list = document.querySelector('ul');
  item = document.createElement('li');
  item.innerText = text;
  list.appendChild(item);
}

// Now use the function to add elements to the list!

function addListElements(text){
  $("ul").append("<li>" +text + "</li>"); //inserting raw HTML into HTML
  $("ul").detach();
}
