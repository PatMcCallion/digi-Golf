<h1>DigiGolf</h1>
<p>DigiGolf is a web application built to help golf enthusiasts track, score, and update their rounds from different courses in their area. The website uses <strong>Python</strong> and <strong>Flask</strong> to provide users with a seamless experience, while also utilizing APIs to track local weather and golf courses in the user's area.</p>
<h2>Getting Started</h2>
<p>These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.</p>
<h3>Prerequisites</h3>
<p>To run this application on your local machine, you will need to have <strong>Python 3</strong> and <strong>pip</strong> installed.</p>
<h3>Installing</h3>
<p>To get started, follow these steps:</p>
<ol>
<li>Clone the repository to your local machine using the command:</li>
<pre>
git clone https://github.com/yourusername/digigolf.git
</pre>
<li>Navigate to the project directory:</li>
<pre>
cd digigolf
</pre>
<li>Install the required Python packages:</li>
<pre>
pip install -r requirements.txt
</pre>
<li>Run the server:</li>
<pre>
pipenv shell
</pre>
<pre>
python server.py
</pre>
<p>The application should now be running at <a href="http://localhost:5000/">http://localhost:5000/</a></p>
</ol>
<h2>Features</h2>
<p>DigiGolf offers the following features:</p>
<ul>
<li><strong>User authentication:</strong> Users can create an account and log in to track their golf rounds.</li>
<li><strong>Round tracking:</strong> Users can create, view, and edit rounds, including the course played, date, and score.</li>
<li><strong>Weather integration:</strong> DigiGolf integrates with a weather API to provide users with local weather conditions for each round.</li>
<li><strong>Course search:</strong> Users can search for golf courses in their area using a golf API, and select the course they played for each round.</li>
</ul>
<h2>Built With</h2>
<ul>
<li>Python</li>
<li>Flask</li>
<li>HTML</li>
<li>CSS</li>
</ul>
<h2>APIs Used</h2>
<ul>
<li>OpenWeatherMap API (https://openweathermap.org/api)</li>
<li>Golf Courses API (https://golf-courses-api.herokuapp.com)</li>
</ul>
<h2>Authors</h2>
<p>Your Name - <a href="https://www.yourwebsite.com/">Your Website</a></p>
<h2>License</h2>
<p>This project is licensed under the <strong>MIT</strong> license.</p>
