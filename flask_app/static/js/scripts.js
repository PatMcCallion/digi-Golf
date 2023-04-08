async function randomQuote() {

    var randomQuoteArr = [
        '“I have a tip that can take five strokes off anyone’s game: it’s called an eraser.” Arnold Palmer', '“It took me 17 years to get 3,000 hits in baseball. It took one afternoon on the golf course.” Hank Aaron', ' “They call it golf because all the other four letter words were taken.” Raymond Floyd', '  “I know I am getting better at golf because I am hitting fewer spectators.” Gerald R. Ford', '“Sex and golf are the two things you can enjoy even if you’re not good at them.” Roy McAvoy', ' “If you drink, don’t drive. Don’t even putt.” Dean Martin', '“The only sure rule in golf is he who has the fastest golf cart never has to play the bad lie.” Mickey Mantle', '“Golf is a game in which you yell fore, shoot six, and write down five.” Paul Harvey', ' “It’s good sportsmanship to not pick up lost golf balls while they are still rolling.” Mark Twain', '“Golf?! You hit down to make the ball go up. You swing left and the ball goes right. The lowest score wins. And, on top of that, the winner buys the drinks.”', ' “If you think it’s hard to meet new people, try picking up the wrong golf ball.” Jack Lemmon', '“The difference in golf and government is that in golf you can’t improve your lie.” George Deukmejian', '“You don’t know what pressure is until you play for five bucks with only two bucks in your pocket.” Lee Trevino ', '  “The most important shot in golf is the one at the pub.” Ben Hogan', '"A good golf partner is always slightly worse than you are – and that’s why I get so many calls to play with friends."', '"Golf is a game where the ball always lies poorly and the player always lies well."', '"Golf is a lot of walking, broken up by disappointment and bad arithmetic."', '"Golf is a good walk spoiled" Mark Twain', '"If you get caught on the course during a storm and are afraid of lightning, then hold up your one-iron; even god cannot hit a one-iron." Lee Trevino', '"If profanity influenced the flight of the ball, the game of golf would be played far better than it is."', '"The reason the pro tells you to keep your head down is so that you cant see him laughing."', '"The people who gave us golf and called it a game are the same people who gave us bag pipes and called it music."', '"A gimme can be best defined as an agreement between two golfers, neither of whom can putt very well"', '"A good drive on the 18th hole has stopped many a golfer from giving up the game."']
    document.querySelector('.quotes').innerText = randomQuoteArr[Math.floor(Math.random() * (randomQuoteArr.length - 1))];
}

function getCardinalDirection(angle) {
    const directions = ['↑ N', '↗ NE', '→ E', '↘ SE', '↓ S', '↙ SW', '← W', '↖ NW'];
    return directions[Math.round(angle / 45) % 8];
}

var date1 = document.querySelector('.date1')
var date2 = document.querySelector('.date2')
var date3 = document.querySelector('.date3')
var temp1 = document.querySelector('.temp1')
var temp2 = document.querySelector('.temp2')
var temp3 = document.querySelector('.temp3')
var weather1 = document.querySelector('.weather1')
var weather2 = document.querySelector('.weather2')
var weather3 = document.querySelector('.weather3')
var windSpeed1 = document.querySelector('.windSpeed1')
var windSpeed2 = document.querySelector('.windSpeed2')
var windSpeed3 = document.querySelector('.windSpeed3')


async function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(getWeather);
    } else {
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}

async function getWeather(pos) {
    var response = await fetch("https://api.openweathermap.org/data/3.0/onecall?lat=" + pos.coords.latitude + "&lon=" + pos.coords.longitude + "&appid=52fca7625d261baf628ba9820e81d57d&units=imperial");
    var weatherData = await response.json();
    var newDate1 = new Date(weatherData.daily[0].dt * 1000);
    var newDate2 = new Date(weatherData.daily[1].dt * 1000);
    var newDate3 = new Date(weatherData.daily[2].dt * 1000);
    var properDate1 = newDate1.toDateString();
    var properDate2 = newDate2.toDateString();
    var properDate3 = newDate3.toDateString();
    date1.innerHTML = properDate1;
    date2.innerHTML = properDate2;
    date3.innerHTML = properDate3;
    temp1.innerHTML = weatherData.daily[0].temp.day + " " + "&#xb0;" + "F";
    temp2.innerHTML = weatherData.daily[1].temp.day + " " + "&#xb0;" + "F";
    temp3.innerHTML = weatherData.daily[2].temp.day + " " + "&#xb0;" + "F";
    weather1.innerHTML = weatherData.daily[0].weather[0].main;
    weather2.innerHTML = weatherData.daily[1].weather[0].main;
    weather3.innerHTML = weatherData.daily[2].weather[0].main;
    windSpeed1.innerHTML = weatherData.daily[0].wind_speed + "mph" + "   " + getCardinalDirection(weatherData.daily[0].wind_deg);
    windSpeed2.innerHTML = weatherData.daily[1].wind_speed + "mph" + "   " + getCardinalDirection(weatherData.daily[1].wind_deg);
    windSpeed3.innerHTML = weatherData.daily[2].wind_speed + "mph" + "   " + getCardinalDirection(weatherData.daily[2].wind_deg);
}

var course1 = document.querySelector('.course1')
var course2 = document.querySelector('.course2')
var course3 = document.querySelector('.course3')
var course4 = document.querySelector('.course4')
var course5 = document.querySelector('.course5')
var course6 = document.querySelector('.course6')
var course7 = document.querySelector('.course7')
var course8 = document.querySelector('.course8')
var course9 = document.querySelector('.course9')
var course10 = document.querySelector('.course10')
var zip1 = document.querySelector('.zip1')
var zip2 = document.querySelector('.zip2')
var zip3 = document.querySelector('.zip3')
var zip4 = document.querySelector('.zip4')
var zip5 = document.querySelector('.zip5')
var zip6 = document.querySelector('.zip6')
var zip7 = document.querySelector('.zip7')
var zip8 = document.querySelector('.zip8')
var zip9 = document.querySelector('.zip9')
var zip10 = document.querySelector('.zip10')
var dist1 = document.querySelector('.dist1')
var dist2 = document.querySelector('.dist2')
var dist3 = document.querySelector('.dist3')
var dist4 = document.querySelector('.dist4')
var dist5 = document.querySelector('.dist5')
var dist6 = document.querySelector('.dist6')
var dist7 = document.querySelector('.dist7')
var dist8 = document.querySelector('.dist8')
var dist9 = document.querySelector('.dist9')
var dist10 = document.querySelector('.dist10')

const options = {
    method: 'GET',
    headers: {
        'X-RapidAPI-Key': '0a593067a0msh98c38d311ca515ap1c7789jsn7ea799c0b29d',
        'X-RapidAPI-Host': 'golf-course-finder.p.rapidapi.com'
    }
};

async function getCourseLoc() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(getCourse);
    } else {
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}

async function getCourse(pos) {
    var response = await fetch('https://golf-course-finder.p.rapidapi.com/courses?radius=30&lat=' + pos.coords.latitude + '&lng=' + pos.coords.longitude + '', options);
    var courseData = await response.json();
    course1.innerHTML = courseData.courses[0].name;
    course2.innerHTML = courseData.courses[1].name;
    course3.innerHTML = courseData.courses[2].name;
    course4.innerHTML = courseData.courses[3].name;
    course5.innerHTML = courseData.courses[4].name;
    course6.innerHTML = courseData.courses[5].name;
    course7.innerHTML = courseData.courses[6].name;
    course8.innerHTML = courseData.courses[7].name;
    course9.innerHTML = courseData.courses[8].name;
    course10.innerHTML = courseData.courses[9].name;
    zip1.innerHTML = courseData.courses[0].zip_code;
    zip2.innerHTML = courseData.courses[1].zip_code;
    zip3.innerHTML = courseData.courses[2].zip_code;
    zip4.innerHTML = courseData.courses[3].zip_code;
    zip5.innerHTML = courseData.courses[4].zip_code;
    zip6.innerHTML = courseData.courses[5].zip_code;
    zip7.innerHTML = courseData.courses[6].zip_code;
    zip8.innerHTML = courseData.courses[7].zip_code;
    zip9.innerHTML = courseData.courses[8].zip_code;
    zip10.innerHTML = courseData.courses[9].zip_code;
    dist1.innerHTML = courseData.courses[0].distance + " Miles";
    dist2.innerHTML = courseData.courses[1].distance + " Miles";
    dist3.innerHTML = courseData.courses[2].distance + " Miles";
    dist4.innerHTML = courseData.courses[3].distance + " Miles";
    dist5.innerHTML = courseData.courses[4].distance + " Miles";
    dist6.innerHTML = courseData.courses[5].distance + " Miles";
    dist7.innerHTML = courseData.courses[6].distance + " Miles";
    dist8.innerHTML = courseData.courses[7].distance + " Miles";
    dist9.innerHTML = courseData.courses[8].distance + " Miles";
    dist10.innerHTML = courseData.courses[9].distance + " Miles";
}