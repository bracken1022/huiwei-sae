

GetQQData = function(){

    $.getJSON( $SCRIPT_ROOT + '/ajax_qq_data', '', function( data ){
        //$("#qq_data").text(data.content_qq);
        AppendQQData( data.content_qq );
      });

    AppendQQData = function( listData )
    {
        $("#qq_data").text("");
        $("#qq_data").append( "<ul>" );
        for (var i = 0; i <= listData.length; i++) {

            var result = "";

            if ( listData[i] == null ) {
                return;
            };

            if ( listData[i].hasOwnProperty('from') )
            {
                var from_str = listData[i].from;
                result += from_str + "<br>";
            }

            if ( listData[i].hasOwnProperty('from_url') )
            {
                var from_url = listData[i].from_url;
                result += from_url + "<br>";
            }

            if ( listData[i].hasOwnProperty('image') && listData[i].image != null )
            {
                var image_url = listData[i].image;
                result += "<img src=\"" + image_url +"\"><br>";
            }

            if ( listData[i].hasOwnProperty('location' )) 
            {
                var location = listData[i].location;
                result += location + "<br>";
            }

            if ( listData[i].hasOwnProperty('name') ) {
                var name = listData[i].name;
                result += name + "<br>";
            };

            if ( listData[i].hasOwnProperty('text') ) {
                var text = listData[i].text;
                result += text + "<br>";
            };
            
            $("#qq_data").append( "<li>" + result + "</li>" );
            
        };  
        $("#qq_data").append("</ul>");
    };

};