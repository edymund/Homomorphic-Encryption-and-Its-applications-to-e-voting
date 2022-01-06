$(document).ready(function(){
    $("#search_bar").on("keyup", function() {
      var value = $(this).val().toLowerCase();
      $(".all_ballots").filter(function() {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      });
    });
  });