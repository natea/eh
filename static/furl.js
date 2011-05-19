if (typeof jQuery == 'undefined') {
	var jQ = document.createElement('script');
	jQ.type = 'text/javascript';
	jQ.onload=runthis;
	jQ.src = 'http://ajax.googleapis.com/ajax/libs/jquery/1.6.0/jquery.min.js';
	document.body.appendChild(jQ);
} else {
	runthis();
}
function runthis() {
	if ($("#furl").length == 0) {
    			$("body").append("\
    			<div id='furl'>\
    				<div id='furl_veil' style=''>\
    					<p>Loading...</p>\
    				</div>\
    				<iframe src='http://localhost/f/add' onload=\"$('#furl iframe').slideDown(500);\">Enable iFrames.</iframe>\
    				<style type='text/css'>\
    					#furl_veil { display: none; position: fixed; width: 100%; height: 100%; top: 0; left: 0; background-color: rgba(255,255,255,.25); cursor: pointer; z-index: 900; }\
    					#furl_veil p { color: black; font: normal normal bold 20px/20px Helvetica, sans-serif; position: absolute; top: 50%; left: 50%; width: 10em; margin: -10px auto 0 -5em; text-align: center; }\
    					#furl iframe { display: none; position: fixed; top: 10%; left: 10%; width: 80%; height: 80%; z-index: 999; border: 10px solid rgba(0,0,0,.5); margin: -5px 0 0 -5px; }\
    				</style>\
    			</div>");
    			$("#furl_veil").fadeIn(750);
    		}
    	} else {
    		$("#furl_veil").fadeOut(750);
    		$("#furl iframe").slideUp(500);
    		setTimeout("$('#furl').remove()", 750);
    	}
    	$("#furl_veil").click(function(event){
    		$("#furl_veil").fadeOut(750);
    		$("#furl iframe").slideUp(500);
    		setTimeout("$('#furl').remove()", 750);
    	});
    }