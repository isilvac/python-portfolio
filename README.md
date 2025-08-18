# Python Portfolio

A comprehensive collection of Python projects demonstrating various programming concepts, APIs integration, automation, and GUI development.

## 📁 Project Structure

### 🤖 **APIs & External Services**
Projects that integrate with external APIs and services:

- **[Flight Deals](./apis/flight_deals/)** - Flight price monitoring and alerts using Amadeus API, Twilio SMS, and Google Sheets
- **[Stock Alerts](./apis/stock_alerts/)** - Real-time stock monitoring with Alpha Vantage API, news integration, and WhatsApp alerts
- **[Spotify Playlist](./apis/spotify_playlist/)** - Billboard Top 100 scraper and Spotify playlist creation
- **[NutriTracker](./apis/nutritracker/)** - Exercise tracking and nutrition logging with Nutritionix API and Google Sheets
- **[Kanye Quotes](./apis/kanye_quotes/)** - Interactive quote generator using Kanye West quotes API with Tkinter GUI

### 🔧 **Automation**
Automated tasks and workflows:

- **[Birthday Wisher](./automation/birthday_wisher/)** - Automated birthday email sender with personalized messages and quotes
- **[Mail Merger](./automation/mail_merger/)** - Bulk email personalization tool for mass communications
- **[Selenium WebDriver](./automation/selenium_webdriver/)** - Web automation projects including Python.org events scraper
- **[YCombinator News](./automation/ycombinator_news/)** - Automated news aggregator that scrapes top stories and sends daily email summaries

### 📊 **Data Projects**
Data processing and analysis projects:

- **[NATO Phonetic Alphabet](./data_projects/nato_phonetic_alphabet/)** - Interactive NATO phonetic alphabet converter

### 🎮 **Games & Interactive Projects**
Fun and educational games built with Python:

- **[Snake Game](./games/snake/)** - Classic snake game with score tracking and food mechanics
- **[Pong](./games/pong/)** - Two-player Pong game with paddle controls and scoring system
- **[Quiz Brain](./games/quiz_brain/)** - Interactive quiz application with question models and scoring
- **[Quizzler App](./games/quizzler_app/)** - Enhanced quiz app with true/false questions and visual feedback
- **[US States Game](./games/us_states_game/)** - Educational game for learning US states geography
- **[Cookie Clicker](./games/cookie_clicker/)** - Automated cookie clicking game using Selenium WebDriver

### 🖥️ **GUI Applications**
Desktop applications with graphical user interfaces:

- **[Flashcard App](./gui-apps/flashcard_app/)** - Language learning flashcard application with French vocabulary
- **[Password Manager](./gui-apps/password_manager/)** - Secure password generator and manager with JSON storage
- **[Pomodoro Timer](./gui-apps/pomodoro_timer/)** - Productivity timer with work/break cycles

### 🏗️ **Object-Oriented Programming Projects**
Projects demonstrating OOP concepts:

- **[Coffee Machine OOP](./oop_projects/coffee_machine/)** - Coffee machine simulation using classes and objects
- **[Turtle Race](./oop_projects/race/)** - Street crossing game with car management and scoring system

### 🔤 **Basic Projects**
Fundamental Python concepts and utilities:

- **[Coffee Machine Basic](./basics/coffee_machine/)** - Basic coffee machine program with procedural programming
- **[Dots Picture](./basics/dots/)** - Image processing and manipulation with dots
- **[Tkinter Projects](./basics/tkinter/)** - Basic GUI applications including miles to kilometers converter and turtle race betting
- **[Top Movies Scraper](./basics/top_movies_scraper/)** - Web scraper for extracting top movie lists from Empire Online

## 🚀 **Technologies & APIs Used**

- **APIs**: Amadeus, Twilio, Spotify, Alpha Vantage, News API, Nutritionix, Sheety, Kanye Quotes API
- **GUI**: Tkinter, Turtle Graphics
- **Data Processing**: Pandas, CSV, JSON
- **Web Scraping**: BeautifulSoup, Selenium WebDriver
- **Authentication**: OAuth2, API Keys
- **Communication**: SMS, Email, WhatsApp
- **Game Development**: Turtle graphics, Pygame concepts
- **Web Automation**: Selenium for browser automation

## 📋 **Features by Project**

### APIs
- **Flight Deals**: Real-time flight price monitoring, SMS alerts, Google Sheets integration
- **Stock Alerts**: Stock price tracking, news aggregation, WhatsApp notifications
- **Spotify Playlist**: Web scraping, playlist creation, music API integration
- **NutriTracker**: Exercise logging, nutrition tracking, spreadsheet automation
- **Kanye Quotes**: Interactive quote generator with modern GUI design

### Automation
- **Birthday Wisher**: Email automation, template personalization, quote integration
- **Mail Merger**: Bulk email processing, template customization
- **Selenium WebDriver**: Web scraping automation, browser control
- **YCombinator News**: Automated news aggregation and email delivery

### Games
- **Snake**: Classic arcade gameplay with score tracking
- **Pong**: Two-player competitive gameplay with AI opponent
- **Quiz Apps**: Interactive learning with various question types
- **US States Game**: Educational geography learning
- **Cookie Clicker**: Web automation and game bot development

### GUI Apps
- **Flashcard App**: Language learning interface, progress tracking
- **Password Manager**: Secure password generation, encrypted storage
- **Pomodoro Timer**: Productivity timer with visual feedback

### OOP Projects
- **Coffee Machine**: Class-based coffee machine simulation
- **Turtle Race**: Object-oriented game development with multiple classes

### Basic Projects
- **Coffee Machine Basic**: Procedural programming fundamentals
- **Top Movies Scraper**: Web scraping and data extraction
- **Tkinter Projects**: Basic GUI development concepts

## 🔧 **Setup & Installation**

**Prerequisites:**
- Python 3.12 or higher

**Installation:**
1. Clone the repository
2. Install required dependencies:  
   - Básico: `pip install -r requirements.txt`  
   - O con dependencias de desarrollo: `pip install -e .[dev]`
3. También puedes usar el archivo `pyproject.toml` para instalar el entorno con herramientas modernas de Python.
4. Set up environment variables for API integrations
5. Run individual projects as needed

**Note:**  
The file `pyproject.toml` specifies the minimum Python version and project metadata.  
If usas herramientas como Poetry o pip >= 23.1, puedes instalar con:
```bash
pip install .
```
o para desarrollo:
```bash
pip install -e .[dev]
```

## 📝 **Note on Security**

This repository contains example projects with API integrations. For production use:
- Use environment variables for sensitive data
- Implement proper authentication
- Follow security best practices
- Never commit API keys or credentials

## 🎯 **Learning Objectives**

These projects demonstrate:
- API integration and authentication
- GUI development with Tkinter and Turtle graphics
- Data processing and manipulation
- Web scraping techniques with BeautifulSoup and Selenium
- Automation and workflow optimization
- File I/O and data persistence
- Error handling and user input validation
- Object-oriented programming concepts
- Game development fundamentals
- Web automation and browser control
- Email automation and communication systems

---

*Built with Python 3.12+ | Last updated: 2025-08-18
