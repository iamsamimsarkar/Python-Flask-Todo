$(document).ready(function(){
  $("#search").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $(".table tbody tr").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});
$(".upload-btn").on("click",function(){
  const props = ["name","tel","address"]
  const opts = {multiple:false}
  const contacts = navigator.contacts.select(props,opts)
  contacts.then((res)=>{
    $("#fname").val(res[0].name[0])
    $("#number").val(res[0].tel[0])
    $("#address").val(res[0].address[0].addressLine[0])
  })
})
$(".print-btn").on("click",function(){
  html2canvas($(".table")[0]).then((canvas)=>{
    canvas.toBlob((blob)=>{
      filename = "database_"+Math.floor(Math.random()*69495984)+".jpg";
      let a =document.createElement("a")
      a.href = URL.createObjectURL(blob)
      a.download = filename
      a.click()
      a.remove()
    })
  })
})
$(".delete-btn").on("click",function(){
  let name = $(this).attr("data-name")
  if(confirm("Are you sure, you want to delete "+name+"?")){
    let link = $(this).attr("data-link")
    window.location.replace(link)
  }
})