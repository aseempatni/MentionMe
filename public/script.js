$(document).ready(function(){
    $("#getreco").click(function(){
        tweet = $("#tweet").val();
        ip = "http://10.105.71.202:8080/";
        url = 'proxy.php';
        $.ajax({url:url,
        data:{"tweet":tweet,
        "url":ip},
        headers:{"Accept": "application/json"},
        success: function(result){
            result = (result);
            x = "<ul>";
            recommendations = result["message"]["recommendations"]
            for (user in recommendations) {
                x+="<li>"+recommendations[user]+"</li>";
            }
            x+="</ul>";
            $("#recommendations").html(x);
        }});
    });
});
