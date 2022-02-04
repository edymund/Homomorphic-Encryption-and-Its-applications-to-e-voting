$(document).ready(function(){
    $("#search_bar").on("keyup", function() {
      var value = $(this).val().toLowerCase();
      $(".all_ballots").filter(function() {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      });
    });
  });

function showimg(){
  var modal = document.getElementById("myModal");
    var img = document.getElementById("myImg");
    var modalImg = document.getElementById("imgManual");
    var captionText = document.getElementById("caption");
    modal.style.display = "block";
    modalImg.src = img.src;
    captionText.innerHTML = "User manual";
}

// When the user clicks on <span> (x), close the modal
function spanclose() {
  var modal = document.getElementById("myModal");
  modal.style.display = "none";
}