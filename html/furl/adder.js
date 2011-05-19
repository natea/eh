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
    $j = jQuery.noConflict();
	if ($j("#adder").length == 0) {
	            var src = 'http://{{request.META.SERVER_NAME}}/{{FURL_ROOT}}/add?url=' + escape(document.location) + '&title=' + document.title ;
    			$j("body").append("\
    			<div id='adder' style='display:none; width:100%; position:absolute; top: 0px; left: 0px; z-index: 99999'>\
    			    <iframe width=100% frameborder='0' border='0' height='60px'; src='" + src + "' </iframe>\
    			</div>\
    			");
    			
    			$j("#adder").slideDown(500);
    }
    else {
    	killAdder();
    }
}

function killAdder() {
    $j("#adder").slideUp(500);
	setTimeout("$j('#adder').remove()", 750);
}    
