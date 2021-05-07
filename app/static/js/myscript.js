$('.plus-cart').click(function(){
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2]
    //console.log(id)
    $.ajax({
        type:"GET",
        url:"/pluscart",
        data:{
            pid: id
        },
        success:function(data){
            eml.innerText = data.quantity;
            document.getElementById("amount").innerText=data.amount;
            document.getElementById("totalamount").innerText.data.totalamount;
            document.location = '/showcart/';

        }
    })
})




$('.minus-cart').click(function(){
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2];
    //console.log(id)
    $.ajax({
        type:"GET",
        url:"/minuscart",
        data:{
            pid: id
        },
        success:function(data){
            eml.innerText = data.quantity;
            document.getElementById("amount").innerText=data.amount;
            document.getElementById("totalamount").innerText.data.totalamount;
            document.location = '/showcart/';
        }
    })
})


$('.remove-cart').click(function(){
    var id = $(this).attr("pid").toString();
    var eml = this
    //console.log(id)
    $.ajax({
        type:"GET",
        url:"/removecart",
        data:{
            pid: id
        },
        success:function(data){
            //console.log("Delete")
            document.getElementById("amount").innerHtml=data.amount
            document.getElementById("totalamount").innerHtml.data.totalamount
        }
    })
})