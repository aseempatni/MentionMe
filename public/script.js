$(document).ready(function(){
    $("#getreco").click(function(){
        tweet = $("#tweet").val();
        ip = "http://10.5.30.132:8080/";
        url = 'proxy.php';
        $.ajax({url:url,
	timeout: 300000,
        data:{"tweet":tweet,
        "url":ip},
        headers:{"Accept": "application/json"},
        success: function(result){
            result = (result);
            x = "<ul>";
            recommendations = result["message"]["recommendations"]
            for (i in recommendations) {
                if (user["name"] !="error") {
                    user = recommendations[i];
                    x+="<li><a href = 'https://twitter.com/"+user["name"].substring(1)+"'>"+ user["name"] +"</a> ("+user["id"]+")</li>";
                }
            }
            x+="</ul>";
            $("#recommendations").html(x);
        }});
    });
});

function get_user_name_from(user_id) {
	var url = "http://tweeterid.com/ajax.php"
	$.ajax({
	url: url,
	data: {input:user_id},
	type: 'post',
	success: function (response) {//response is value returned from php
		console.log(response)
	}
});
}
