console.log("loaded form handler");

// form validation
  $(function() {
    $('button#summary').bind('click', function(event) {
        var elements = document.forms['wordentry'].elements;
        var error_free=true;
        for (i=0; i<elements.length; i++){
          if(elements[i].value.length == 0){
            error_free = false;
            //alert("Fill All Fields!");
            break;
            }
          }
    if (!error_free){
      //event.preventDefault();
      console.log("but error!!! oh no")
      var s = document.getElementById('error');
      s.innerHTML = "Fill All Fields!";
     }
    else{
      $.post($SCRIPT_ROOT + '/_return_summary', {
        noun1: $('input[name="noun1"]').val(),
        adj1: $('input[name="adj1"]').val(),
        adj2: $('input[name="adj2"]').val(),
        adj3: $('input[name="adj3"]').val(),
        plnoun1: $('input[name="plnoun1"]').val(),
        plnoun2: $('input[name="plnoun2"]').val(),
        plnoun3: $('input[name="plnoun3"]').val(),
        verb1: $('input[name="verb1"]').val(),
        verb2: $('input[name="verb2"]').val(),
        verb3: $('input[name="verb3"]').val(),
        verb4: $('input[name="verb4"]').val()
      }, function(data) {
        $("#result").text(data.result);
      });
     }
   })});
