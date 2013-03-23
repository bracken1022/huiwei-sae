

    GetWeiboData = function()
    {

    $.getJSON( $SCRIPT_ROOT + '/ajax_weibo_data', '', function( data ){

        AppendWeiboData( data.content_weibo );
        } );


    };

    AppendWeiboData = function( listData )
    {
        var result = ""

        $("#weibo_data").append( "<ul>" );
        for (var i = 0; i <= listData.length; i++) {

            var result = "";

            if ( listData[i] == null ) {
                return;
            };

            if ( listData[i].hasOwnProperty('user') )
            {
                var user = listData[i].user.name;
                result += user + "<br>";
                result += "<img src=\"" + listData[i].user.profile_image_url +"\">" + "<br>";

            }

            if ( listData[i].hasOwnProperty('retweeted_status') )
            {
                var retweeted_pic = listData[i].retweeted_status.original_pic;
                result += "<img src=\"" + retweeted_pic +"\">" + "<br>";

                var text = listData[i].retweeted_status.text;
                result += "<p>" + text + "</p>";
            }



            
            $("#weibo_data").append( "<li>" + result + "</li>" );
            
        };  
        $("#weibo_data").append("</ul>");
    };