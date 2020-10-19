<<<<<<< HEAD
window.weatherWidgetConfig = window.weatherWidgetConfig || [];
window.weatherWidgetConfig.push({
  selector: ".weatherWidget",
  apiKey: "K8E8GMWKCRT7R9T2MUI056VN9", //lots of usage? Sign up for your personal key
  location: "Indianapolis, IN", //enter an addres
  unitGroup: "us", //"us" or "metric"
  forecastDays: 7, //how many days forecast to show
  title: "Indianapolis, IN", //optional title to show in the
  showTitle: true,
  showConditions: true,
});

(function () {
  var d = document,
    s = d.createElement("script");
  s.src =
    "https://www.visualcrossing.com/widgets/forecast-simple/weather-forecast-widget-simple.js";
  s.setAttribute("data-timestamp", +new Date());
=======


window.weatherWidgetConfig =  window.weatherWidgetConfig || [];
  window.weatherWidgetConfig.push({
      selector:".weatherWidget",
      apiKey = process.env.apiKey, //lots of usage? Sign up for your personal key
      location:"Halsey, OR",//enter an addres
      unitGroup:"us", //"us" or "metric"
      forecastDays:5, //how many days forecast to show
      title:"Halsey, OR",//optional title to show in the 
      showTitle:true, 
      showConditions:true
  });
 
  (function() {
  var d = document, s = d.createElement('script');
  s.src = "https://www.visualcrossing.com/widgets/forecast-simple/weather-forecast-widget-simple.js";
  s.setAttribute('data-timestamp', +new Date());
>>>>>>> 97a8f107eafe08b8172a1f1df71274a779d9362f
  (d.head || d.body).appendChild(s);
})();
