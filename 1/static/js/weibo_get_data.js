
$(document).ready(function(){
   
      
      fetchItems_from_place_photos();
      

    });




    
    fetchItems = function () { 

        var url = '/weibodata';
        $.ajax({
            url: url,
            type: "GET",
            dataType: "json",
            context: this,
          success:fetchCallback
        });
    }; 
    
    fetchCallback = function(obj, textStatus, xhr) {
        xhr = null;
        
        var lat1 = obj.weiboDict[0].geo.coordinates[0];
        var lng1 = obj.weiboDict[0].geo.coordinates[1];
        
        map = new GMaps({
        div: '#map',
        lat: lat1,
        lng: lng1,
        height: '600px'
      });
      

        
        
    };
    
    fetchItems_from_place_photos = function()
    {
        var url = '/weibo_poi_data';
      $.ajax({
        url: url,
        type: "GET",
        dataType: "json",
        context: this,
        success:fetchCallback_place_photos
      });
      

    };
    
    fetchCallback_place_photos = function(obj, textStatus, xhr) {
        xhr = null;
        var i = 0;
        var lat1 = obj.data[0].geo.coordinates[0];
        var lng1 = obj.data[0].geo.coordinates[1];
        
        map = new GMaps({
        div: '#map',
        lat: lat1,
        lng: lng1,
        height: '675px'
        
        
        
        });
      
      

     $("#info").tmpl(obj.data).appendTo("#container1");
      
        
    for ( i = 0; i < obj.data.length; i++ ) 
    {

        var text = obj.data[i].text
        var img_url = obj.data[i].original_pic

        
        map.addMarker({
            lat: obj.data[i].geo.coordinates[0],
            lng: obj.data[i].geo.coordinates[1],
            title: 'Marker with InfoWindow',
            infoWindow: {
              content: '<p>'+text+'</p>'+'</br><img src='+img_url+'>'
            }
          });
    }
    

    
        
    };
    
   fetchCallback_place_photos1 = function(obj, textStatus, xhr) {
        xhr = null;
        var i = 0;
        var lat1 = obj.data[0].geo.coordinates[0];
        var lng1 = obj.data[0].geo.coordinates[1];
        
        window.img_data = obj.data[0].original_pic;
        
       
    

    
        
    };