setTimeout(function(){
	window.location.reload(1);
}, 30000);

var g1, g2;
document.addEventListener("DOMContentLoaded", function(event) {
	g1 = new JustGage({
		id: "g1",
		value: {{temp}},
		valueFontColor: "black",
		titleFontColor: "black",
		min: -10,
		max: 50,
		title: "Temperature",
		label: "Celcius"
	});

	g2 = new JustGage({
		id: "g2",
		value: {{hum}},
		valueFontColor: "black",
		titleFontColor: "black",
		min: 0,
		max: 100,
		title: "Humidity",
		label: "%"
	});

});