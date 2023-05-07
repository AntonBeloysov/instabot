var ranmaskus = Math.random().toString(36).substr(2, 5);

function addRow(id){
    var tbody = document.getElementById(id).getElementsByTagName("tbody")[0];
    var row = document.createElement("tr")
    var td1 = document.createElement("td")
    var username = document.getElementById('nik').value;
    var password = document.getElementById('pass').value;
    td1.appendChild(document.createTextNode(username))
    var td2 = document.createElement("td")
    td2.appendChild (document.createTextNode(password))
    row.appendChild(td1);
    row.appendChild(td2);
    tbody.appendChild(row);
}

function create() {
  let user__js = document.getElementById('nik').value;
  let password__js = document.getElementById('pass').value;
  eel.log(user__js, password__js)();
}

function inp() {
  let val = document.getElementById('inp').value;
  eel.take_py(val)();
}

function sta() {
  eel.sta()();
}

function newusmask() {
  var usermask = document.getElementById('nik').value;
  var passmask = document.getElementById('pass').value;
  eel.newdictuser(ranmaskus, usermask, passmask)();
}
