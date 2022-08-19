"use strict";
var submitButton = document.querySelector(".btn-send");

submitButton.addEventListener("click", () => {
  var table = $("#table-body");
  $("tr td").remove();
  var page = document.querySelector("#page").value;
  var pagesize = document.querySelector("#pagesize").value;
  var fromdate = document.querySelector("#fromdate").value;
  var todate = document.querySelector("#todate").value;
  var order = document.querySelector("#order").value;
  var min = document.querySelector("#min").value;
  var max = document.querySelector("#max").value;
  var sort = document.querySelector("#sort").value;
  var tagged = document.querySelector("#tagged").value;
  var nottagged = document.querySelector("#nottagged").value;
  var intitle = document.querySelector("#intitle").value;

  $.ajax({
    url: `http://127.0.0.1:8000/stackReq?page=${page}&pagesize=${pagesize}&fromdate=${fromdate}&todate=${todate}&order=${order}&min=${min}&max=${max}&sort=${sort}&tagged=${tagged}&nottagged=${nottagged}&intitle=${intitle}&site=stackoverflow"`,
    method: "GET",
    timeout: 0,
    headers: {},
    success: function (response) {
      try {
        var res = JSON.parse(response);
        for (let i = 0; i < res.length; i++) {
          // console.log("response------->", res[i]);
          var row = `<tr>
                  <td style="word-wrap: break-word">${res[i]["title"]}</td>
                  <td style="word-wrap: break-word">${JSON.stringify(
                    res[i]["owner"]
                  )}</td>
                  <td style="word-wrap: break-word">${res[i]["tags"]}</td>
                  <td style="word-wrap: break-word"><a href="${
                    res[i]["link"]
                  }">${res[i]["link"]}</a></td>
                  <td style="word-wrap: break-word">${
                    res[i]["is_answered"]
                  }</td>
                  `;
          table.append(row);
        }
      } catch (err) {
        console.log("error-------->", err);
        alert("There was some error");
      }
    },
    error: function (data) {
      alert("Request Exceeds");
    },
  });
});
