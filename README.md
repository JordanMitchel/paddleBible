<div align="left">
  <img src="paddle-logo-dark.svg" align="right" width="30%" style="margin: -20px 0 0 20px;">
  <h1>PADDLEBIBLE</h1>
  <p align="left">
    <em><code>❯ Charting Knowledge, One Page at a Time 📚🌊</code></em>
  </p>
  <p align="left">
    <img src="https://img.shields.io/github/license/JordanMitchel/paddleBible?style=for-the-badge&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
    <img src="https://img.shields.io/github/last-commit/JordanMitchel/paddleBible?style=for-the-badge&logo=git&logoColor=white&color=0080ff" alt="last-commit">
    <img src="https://img.shields.io/github/languages/top/JordanMitchel/paddleBible?style=for-the-badge&color=0080ff" alt="repo-top-language">
    <img src="https://img.shields.io/github/languages/count/JordanMitchel/paddleBible?style=for-the-badge&color=0080ff" alt="repo-language-count">
  </p>
  <p align="left">Built with the tools and technologies:</p>
  <p align="left">
    <img src="https://img.shields.io/badge/FastAPI-009688.svg?style=for-the-badge&logo=FastAPI&logoColor=white" alt="FastAPI">
    <img src="https://img.shields.io/badge/spaCy-09A3D5.svg?style=for-the-badge&logo=spaCy&logoColor=white" alt="spaCy">
    <img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=for-the-badge&logo=Pytest&logoColor=white" alt="Pytest">
    <img src="https://img.shields.io/badge/Docker-2496ED.svg?style=for-the-badge&logo=Docker&logoColor=white" alt="Docker">
    <img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=for-the-badge&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions">
    <img src="https://img.shields.io/badge/pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white" alt="pandas">
    <img src="https://img.shields.io/badge/Pydantic-E92063.svg?style=for-the-badge&logo=Pydantic&logoColor=white" alt="Pydantic">
  </p>
</div>


<br clear="right">

## 🔗 Table of Contents

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [📁 Project Structure](#-project-structure)
  - [📂 Project Index](#-project-index)
- [🚀 Getting Started](#-getting-started)
  - [☑️ Prerequisites](#-prerequisites)
  - [⚙️ Installation](#-installation)
  - [🤖 Usage](#🤖-usage)
  - [🧪 Testing](#🧪-testing)
- [📌 Project Roadmap](#-project-roadmap)
- [🔰 Contributing](#-contributing)
- [🎗 License](#-license)
- [🙌 Acknowledgments](#-acknowledgments)

---

##  📖  Overview

<code>❯ ✨ _PaddleBible is designed to integrate scripture with AI-driven insights and location-based studies._ ✨</code>

---

## 👾 Features  

### 🌍 Location & Historical Context  
- **Biblical Map Integration:** Identifies real-world locations of biblical events using geospatial AI.  

### 🔗 Graph-Based Genealogy & Bible Traversal  
- **Family Tree of Biblical Figures:** Uses a graph-based AI model to visualize relationships between people in the Bible.  
- **Genealogy Explorer:** Navigate through lineages (e.g., from Adam to Jesus) with interactive nodes.  
- **Ancestry-Based Scripture Discovery:** See how biblical figures are connected across different books and contexts.  

### 📏 Dimensional & Object Analysis  
- **Biblical Object Measurements:** AI-powered 3D reconstructions of the Ark, Solomon’s Temple, and other key structures.  
- **Size Comparisons:** Compare ancient measurements to modern equivalents (e.g., cubits to meters).  
- **Material & Symbolism Analysis:** Insights into the significance of materials used in biblical artifacts (gold, wood, linen, etc.).  

### 🏛️ Word Usage & Etymology Over Time  
- **Biblical Word Evolution:** AI-powered etymology tracker showing how words changed over time.  
- **Contextual Meaning Analysis:** Discover how a word’s meaning varies in different books and translations.  
- **Hebrew & Greek Lexicon Insights:** AI-powered deep dives into original scriptural languages.  

### 👥 Group Study & Interactive Scripture Rooms  
- **Leader-Driven Study Rooms:** A host (pastor, teacher, or study leader) controls which scripture or feature all members view in real-time.  
- **Topic-Based Group Studies:** Suggests study groups based on shared interests or themes.  
- **AI Moderation for Discussions:** Enhances and filters user-generated Bible discussions.  


---

## 📁 Project Structure

```sh
└── paddleBible/
    ├── .github
    │   └── workflows
    │       └── pylint.yml
    ├── LICENSE
    ├── README.md
    ├── bff
    │   ├── Dockerfile
    │   ├── __init__.py
    │   ├── requirements.txt
    │   ├── src
    │   │   ├── __init__.py
    │   │   ├── app.py
    │   │   ├── controllers
    │   │   ├── routes
    │   │   └── services
    │   └── tests
    │       ├── README.md
    │       ├── __init__.py
    │       └── search_test
    ├── docker-compose-paddle.yml
    ├── domain
    │   ├── README.md
    │   ├── __init__.py
    │   ├── data
    │   │   ├── csv
    │   │   ├── delimitedBiblicalData
    │   │   ├── geolocation
    │   │   ├── json
    │   │   ├── student.xml
    │   │   └── xml
    │   ├── requirements.txt
    │   ├── src
    │   │   ├── __init__.py
    │   │   ├── db
    │   │   ├── models
    │   │   └── services
    │   └── tests
    │       └── db_test
    ├── main.py
    ├── ml_service
    │   ├── Dockerfile
    │   ├── README.md
    │   ├── __init__.py
    │   ├── requirements.txt
    │   ├── src
    │   │   ├── __init__.py
    │   │   ├── app.py
    │   │   ├── models
    │   │   └── services
    │   └── tests
    │       ├── __init__.py
    │       ├── test_sentiment_search.py
    │       └── test_strip_locations.py
    ├── pytest.ini
    ├── requirements.txt
    ├── scripts
    │   └── background_tasks
    │       ├── __init__.py
    │       └── start_up_tasks.py
    └── shared
        ├── __init__.py
        ├── src
        │   ├── ServiceBus
        │   ├── __init__.py
        │   └── models
        ├── tests
        │   ├── __init__.py
        │   └── test_data
        └── utils
            ├── __init__.py
            └── config.py
```


### 📂 Project Index
<details open>
	<summary><b><code>PADDLEBIBLE/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/JordanMitchel/paddleBible/blob/master/docker-compose-paddle.yml'>docker-compose-paddle.yml</a></b></td>
				<td><code>❯ Docker Compose Configuration to run project via Docker</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/JordanMitchel/paddleBible/blob/master/main.py'>main.py</a></b></td>
				<td><code>❯ Main for testing file location</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/JordanMitchel/paddleBible/blob/master/pytest.ini'>pytest.ini</a></b></td>
				<td><code>❯ Pytest Configuration</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/JordanMitchel/paddleBible/blob/master/requirements.txt'>requirements.txt</a></b></td>
				<td><code>❯ Dependencies list</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- shared Submodule -->
		<summary><b>shared</b></summary>
		<blockquote>
			<details>
				<summary><b>src</b></summary>
				<blockquote>
					<details>
						<summary><b>ServiceBus</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/JordanMitchel/paddleBible/blob/master/shared/src/ServiceBus/producer.py'>producer.py</a></b></td>
								<td><code>❯ Message Producer</code></td>
							</tr>
							</table>
						</blockquote>
					</details>
					<details>
						<summary><b>models</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/JordanMitchel/paddleBible/blob/master/shared/src/models/scripture_result.py'>scripture_result.py</a></b></td>
								<td><code>❯ Models for bible objects</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/JordanMitchel/paddleBible/blob/master/shared/src/models/FileType.py'>FileType.py</a></b></td>
								<td><code>❯ File input type</code></td>
							</tr>
							</table>
						</blockquote>
					</details>
				</blockquote>
			</details>
			<details>
				<summary><b>utils</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/JordanMitchel/paddleBible/blob/master/shared/utils/config.py'>config.py</a></b></td>
						<td><code>❯ Getting configuration details from env file</code></td>
					</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<details> <!-- .github Submodule -->
		<summary><b>.github</b></summary>
		<blockquote>
			<details>
				<summary><b>workflows</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/JordanMitchel/paddleBible/blob/master/.github/workflows/pylint.yml'>pylint.yml</a></b></td>
						<td><code>❯ Github actions file</code></td>
					</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<details> <!-- scripts Submodule -->
		<summary><b>scripts</b></summary>
		<blockquote>
			<details>
				<summary><b>background_tasks</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/JordanMitchel/paddleBible/blob/master/scripts/background_tasks/start_up_tasks.py'>start_up_tasks.py</a></b></td>
						<td><code>❯ Start Kombu and DB ingestion</code></td>
					</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<details> <!-- bff Submodule -->
		<summary><b>bff</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/JordanMitchel/paddleBible/blob/master/bff/requirements.txt'>requirements.txt</a></b></td>
				<td><code>❯  Dependencies List in BFF</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/JordanMitchel/paddleBible/blob/master/bff/Dockerfile'>Dockerfile</a></b></td>
				<td><code>❯ Dockerfile in BFF</code></td>
			</tr>
			</table>
			<details>
				<summary><b>src</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/JordanMitchel/paddleBible/blob/master/bff/src/app.py'>app.py</a></b></td>
						<td><code>❯ Python Entry Point in BFF</code></td>
					</tr>
					</table>
					<details>
						<summary><b>routes</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/JordanMitchel/paddleBible/blob/master/bff/src/routes/router_ws.py'>router_ws.py</a></b></td>
								<td><code>❯ WebSocket Route Handler</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/JordanMitchel/paddleBible/blob/master/bff/src/routes/router_scripture.py'>router_scripture.py</a></b></td>
								<td><code>❯ Scripture API Route</code></td>
							</tr>
							</table>
						</blockquote>
					</details>
					<details>
						<summary><b>services</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/JordanMitchel/paddleBible/blob/master/bff/src/services/BibleService.py'>BibleService.py</a></b></td>
								<td><code>❯ Scripture Data Service</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/JordanMitchel/paddleBible/blob/master/bff/src/services/ProducerServiceContainer.py'>ProducerServiceContainer.py</a></b></td>
								<td><code>❯ Service Bus Producer Container</code></td>
							</tr>
							</table>
							<details>
								<summary><b>ServiceBus</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/JordanMitchel/paddleBible/blob/master/bff/src/services/ServiceBus/ResultService.py'>ResultService.py</a></b></td>
										<td><code>❯ Handles Message Results</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/JordanMitchel/paddleBible/blob/master/bff/src/services/ServiceBus/BFFKombuConsumer.py'>BFFKombuConsumer.py</a></b></td>
										<td><code>❯ Kombu Message Consumer</code></td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>search</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/JordanMitchel/paddleBible/blob/master/bff/src/services/search/search_locations.py'>search_locations.py</a></b></td>
										<td><code>❯ Location Search Service</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/JordanMitchel/paddleBible/blob/master/bff/src/services/search/search_bible_books_list.py'>search_bible_books_list.py</a></b></td>
										<td><code>❯ Bible Books Search</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/JordanMitchel/paddleBible/blob/master/bff/src/services/search/search_scripture.py'>search_scripture.py</a></b></td>
										<td><code>❯ Scripture Search Service</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/JordanMitchel/paddleBible/blob/master/bff/src/services/search/search_for_location_by_scripture.py'>search_for_location_by_scripture.py</a></b></td>
										<td><code>❯ Location Lookup by Scripture</code></td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>analysis</b></summary>
								<blockquote>
									<details>
										<summary><b>preProcessing</b></summary>
										<blockquote>
											<table>
											<tr>
												<td><b><a href='https://github.com/JordanMitchel/paddleBible/blob/master/bff/src/services/analysis/preProcessing/convert_to_csv.py'>convert_to_csv.py</a></b></td>
												<td><code>❯ Convert Data to CSV</code></td>
											</tr>
											</table>
										</blockquote>
									</details>
									<details>
										<summary><b>postProcessing</b></summary>
										<blockquote>
											<table>
											<tr>
												<td><b><a href='https://github.com/JordanMitchel/paddleBible/blob/master/bff/src/services/analysis/postProcessing/forward_geo_coding.py'>forward_geo_coding.py</a></b></td>
												<td><code>❯ Forward Geocoding Processing</code></td>
											</tr>
											<tr>
												<td><b><a href='https://github.com/JordanMitchel/paddleBible/blob/master/bff/src/services/analysis/postProcessing/find_extra_lat_longs.py'>find_extra_lat_longs.py</a></b></td>
												<td><code>❯ Find Missing Latitude & Longitude</code></td>
											</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
						</blockquote>
					</details>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<details> <!-- ml_service Submodule -->
		<summary><b>ml_service</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/JordanMitchel/paddleBible/blob/master/ml_service/requirements.txt'>requirements.txt</a></b></td>
				<td><code>❯ ML Service Dependencies</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/JordanMitchel/paddleBible/blob/master/ml_service/Dockerfile'>Dockerfile</a></b></td>
				<td><code>❯ ML Service Docker Configuration</code></td>
			</tr>
			</table>
			<details>
				<summary><b>src</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/JordanMitchel/paddleBible/blob/master/ml_service/src/app.py'>app.py</a></b></td>
						<td><code>❯ML Service API Endpoint and Kombu startpoint</code></td>
					</tr>
					</table>
					<details>
						<summary><b>services</b></summary>
						<blockquote>
							<details>
								<summary><b>service_bus</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/JordanMitchel/paddleBible/blob/master/ml_service/src/services/service_bus/ProcessService.py'>ProcessService.py</a></b></td>
										<td><code>❯ Message Processing Logic</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/JordanMitchel/paddleBible/blob/master/ml_service/src/services/service_bus/MLKombuConsumer.py'>MLKombuConsumer.py</a></b></td>
										<td><code>❯ Kombu Consumer for Message Queue</code></td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<details> <!-- domain Submodule -->
		<summary><b>domain</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/JordanMitchel/paddleBible/blob/master/domain/requirements.txt'>requirements.txt</a></b></td>
				<td><code>❯ Domain Service Dependencies</code></td>
			</tr>
			</table>
			<details>
				<summary><b>src</b></summary>
				<blockquote>
					<details>
						<summary><b>services</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/JordanMitchel/paddleBible/blob/master/domain/src/services/db_connector.py'>db_connector.py</a></b></td>
								<td><code>❯ Database Connection Handler</code></td>
							</tr>
							</table>
						</blockquote>
					</details>
					<details>
						<summary><b>db</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/JordanMitchel/paddleBible/blob/master/domain/src/db/add_bible_to_mongo.py'>add_bible_to_mongo.py</a></b></td>
								<td><code>❯ Insert Bible Data into MongoDB</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/JordanMitchel/paddleBible/blob/master/domain/src/db/add_coordinates_to_mongo.py'>add_coordinates_to_mongo.py</a></b></td>
								<td><code>❯ Insert Location Coordinates into MongoDB</code></td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/JordanMitchel/paddleBible/blob/master/domain/src/db/update_coordinates.py'>update_coordinates.py</a></b></td>
								<td><code>❯ Update Location Coordinates in MongoDB</code></td>
							</tr>
							</table>
						</blockquote>
					</details>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

---
## 🚀 Getting Started

### ☑️ Prerequisites

Before getting started with paddleBible, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Pip
- **Container Runtime:** Docker


### ⚙️ Installation

Install paddleBible using one of the following methods:

**Build from source:**

1. Clone the paddleBible repository:
```sh
❯ git clone https://github.com/JordanMitchel/paddleBible
```

2. Navigate to the project directory:
```sh
❯ cd paddleBible
```

3. Install the project dependencies:


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r requirements.txt, bff/requirements.txt, ml_service/requirements.txt, domain/requirements.txt
```


**Using `docker`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker build -t JordanMitchel/paddleBible .
```




### 🤖 Usage
Run paddleBible using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python {entrypoint}
```


**Using `docker`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker run -it {image_name}
```


### 🧪 Testing
Run the test suite using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pytest
```


---
## 📌 Project Roadmap

- [X] **`Task 1`**: <strike>Implement APIs to query the bible and locations</strike>
- [X] **`Task 2`**: <strike>Implement microservice architecture to speed up development time and imrpove work at 
  scale.</strike>
- [X] **`Task 3`**: <strike>Implement websocket communication to allow for real time development.</strike>
- [ ] **`Task 4`**: Implement logging and monitoring for the application.
- [ ] **`Task 5`**: Implement UI to connect to app
- [ ] **`Task 6`**: Implement login feature
- [ ] **`Task 7`**: Implement gunicorn instead of unicorn for scale and speed


---

## 🔰 Contributing

- **💬 [Join the Discussions](https://github.com/JordanMitchel/paddleBible/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/JordanMitchel/paddleBible/issues)**: Submit bugs found or log feature requests for the `paddleBible` project.
- **💡 [Submit Pull Requests](https://github.com/JordanMitchel/paddleBible/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/JordanMitchel/paddleBible
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/JordanMitchel/paddleBible/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=JordanMitchel/paddleBible">
   </a>
</p>
</details>

---

## 🎗 License

This project is protected under the [GNU Affero General Public License v3.0](https://choosealicense.com/licenses/agpl-3.0/#).

---

## 🙌 Acknowledgments

### Joshua 1:7-9
- #### 7 “Be strong and very courageous. Be careful to obey all the law my servant Moses gave you; do not turn from it to the right or to the left, that you may be successful wherever you go. 
- #### 8 Keep this Book of the Law always on your lips; meditate on it day and night, so that you may be careful to do everything written in it. Then you will be prosperous and successful. 
- #### 9 Have I not commanded you? Be strong and courageous. Do not be afraid"
---
