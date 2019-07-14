$(document).ready(function() {
  let btn = $("#start");
  btn.click(function() {
    btn.toggleClass("paused");
    return false;
  });
});