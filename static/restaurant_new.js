let numTabType = document.querySelector('#numTabType');

numTabType.addEventListener('onchange', e=> {
  let number = document.getElementById("member").value;
  const container = document.getElementById("container");
    while (container.hasChildNodes()) {
      container.removeChild(container.lastChild);
      }
    for (i=0;i<number;i++){
      container.appendChild(document.createTextNode("Member " + (i+1)));
      let input1 = document.createElement("input");
      input1.type = "text";
      input1.name = "tableType" + i;
      let inp
      container.appendChild(input);
      container.appendChild(document.createElement("br"));
    }
  }
