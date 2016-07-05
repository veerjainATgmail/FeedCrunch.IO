$(function() {
  $("#submit").click( function(){
    $.ajax({
      url : "ajax/",
      type : "POST",
      data: {
        title: $("#title").val(),
        link: $("#link").val(),
        csrfmiddlewaretoken: $('input[name^=csrfmiddlewaretoken]').val(),
        activated: $("#activated_radio").bootstrapSwitch('state'),
        twitter: $("#twitter_radio").bootstrapSwitch('state'),
        autoformat: $("#auto_format").bootstrapSwitch('state')
      },
      dataType : "json",

      success: function(data){
        if (data.status != "success") {
           $("#resultatUpload").attr('class', 'alert alert-warning show');
           $("#resultatUpload").html("Attention, cette action n'a pas pu être enregistrée.");
        }
        else
        {
          $("#resultatUpload").attr('class', 'alert alert-success show');
          $("#resultatUpload").html("Enregistrement effectué avec succès.");

          if (data.operation == "insert"){
            $("#title").val("");
            $("#link").val("");
            $("#activated_radio").bootstrapSwitch('state', true);
            $("#twitter_radio").bootstrapSwitch('state', true);
            $("#auto_format").bootstrapSwitch('state', true);
          }
          else if (data.operation == "modification") {
            window.location.href = "../";
          }
        }
      }
    });
  });
});

$(function() {
  $("#clear").click( function(){
    $("#title").val("");
    $("#link").val("");
    $("#activated_radio").bootstrapSwitch('state', true);
    $("#twitter_radio").bootstrapSwitch('state', true);
    $("#auto_format").bootstrapSwitch('state', true);
  });
});

$(function() {
  $("#reset").click( function(){
    $("#title").val($("#title").data("init"));
    $("#link").val($("#link").data("init"));
    $("#activated_radio").bootstrapSwitch('state', $("#activated_radio").data("init"));
    $("#twitter_radio").bootstrapSwitch('state', true);
    $("#auto_format").bootstrapSwitch('state', true);
  });
});