$(document).ready(function(){
    $("#getreco").click(function(){
        $.ajax({url: "response.json", success: function(result){
            x = "<ul>";
            for (reco in result["recommendations"]) {
                x+="<li>"+result["recommendations"][reco]["id"]+"</li>";
            }
            x+="</ul>";
            $("#recommendations").html(x);
        }});
    });
});
