$(document).ready(function() {
  var oTable = $('#example1').DataTable({
      "paging": true,
      "lengthChange": true,
      "searching": true,
      "ordering": false,
      "info": true,
      "autoWidth": true
    });

  $("#datepicker_from").datepicker({
    showOn: "button",
    autoclose: true,
    buttonImage: "images/calendar.gif",
    buttonImageOnly: false,
    "onSelect": function(date) {
      minDateFilter = new Date(date).getTime();
      oTable.draw();
      
    }
  }).keyup(function() {
    minDateFilter = new Date(this.value).getTime();
    oTable.draw();  
  });

  $("#datepicker_to").datepicker({
    showOn: "button",
    autoclose: true,
    buttonImage: "images/calendar.gif",
    buttonImageOnly: false,
    "onSelect": function(date) {
      maxDateFilter = new Date(date).getTime();
      oTable.draw();
      
    }
  }).keyup(function() {
    maxDateFilter = new Date(this.value).getTime();
    oTable.draw();
    
  });

  $('#btn-reload').click(function(){
     oTable.draw();
  });

});


minDateFilter = "";
maxDateFilter = "";


$.fn.dataTableExt.afnFiltering.push(
  function(oSettings, aData, iDataIndex) {
    console.log(aData)
    maxDateFilter = new Date($('#datepicker_from').val()).getTime();
    maxDateFilter = new Date($('#datepicker_to').val()).getTime();
    var d = new Date(aData[5]).getTime();
    if (minDateFilter && !isNaN(minDateFilter)) {
      if (d < minDateFilter) {
        return false;
      }
    }

    if (maxDateFilter && !isNaN(maxDateFilter)) {
      if (d > maxDateFilter) {
        return false;
      }
    }

    return true;
  }
);




