# Python Portfolio

A comprehensive collection of Python projects demonstrating various programming concepts, APIs integration, automation, and GUI development.

## 📁 Project Structure

### 🤖 **APIs & External Services**
Projects that integrate with external APIs and services:

- **[Flight Deals](./apis/flight_deals/)** - Flight price monitoring and alerts using Amadeus API, Twilio SMS, and Google Sheets
- **[Stock Alerts](./apis/stock_alerts/)** - Real-time stock monitoring with Alpha Vantage API, news integration, and WhatsApp alerts
- **[Spotify Playlist](./apis/spotify_playlist/)** - Billboard Top 100 scraper and Spotify playlist creation
- **[NutriTracker](./apis/nutritracker/)** - Exercise tracking and nutrition logging with Nutritionix API and Google Sheets

### 🔧 **Automation**
Automated tasks and workflows:

- **[Birthday Wisher](./automation/birthday_wisher/)** - Automated birthday email sender with personalized messages and quotes
- **[Mail Merger](./automation/mail_merger/)** - Bulk email personalization tool for mass communications

### 📊 **Data Projects**
Data processing and analysis projects:

- **[NATO Phonetic Alphabet](./data_projects/nato_phonetic_alphabet/)** - Interactive NATO phonetic alphabet converter

### 🖥️ **GUI Applications**
Desktop applications with graphical user interfaces:

- **[Flashcard App](./gui-apps/flashcard_app/)** - Language learning flashcard application with French vocabulary
- **[Password Manager](./gui-apps/password_manager/)** - Secure password generator and manager with JSON storage
- **[Pomodoro Timer](./gui-apps/pomodoro_timer/)** - Productivity timer with work/break cycles

## 🚀 **Technologies & APIs Used**

- **APIs**: Amadeus, Twilio, Spotify, Alpha Vantage, News API, Nutritionix, Sheety
- **GUI**: Tkinter
- **Data Processing**: Pandas, CSV, JSON
- **Web Scraping**: BeautifulSoup
- **Authentication**: OAuth2, API Keys
- **Communication**: SMS, Email, WhatsApp

## 📋 **Features by Project**

### APIs
- **Flight Deals**: Real-time flight price monitoring, SMS alerts, Google Sheets integration
- **Stock Alerts**: Stock price tracking, news aggregation, WhatsApp notifications
- **Spotify Playlist**: Web scraping, playlist creation, music API integration
- **NutriTracker**: Exercise logging, nutrition tracking, spreadsheet automation

### Automation
- **Birthday Wisher**: Email automation, template personalization, quote integration
- **Mail Merger**: Bulk email processing, template customization

### Data Projects
- **NATO Phonetic**: Interactive alphabet conversion, user input validation

### GUI Apps
- **Flashcard App**: Language learning interface, progress tracking
- **Password Manager**: Secure password generation, encrypted storage
- **Pomodoro Timer**: Productivity timer with visual feedback

## 🔧 **Setup & Installation**

**Prerequisites:**
- Python 3.12 or higher

**Installation:**
1. Clone the repository
2. Install required dependencies: `pip install -r requirements.txt`
   - Or install with development dependencies: `pip install -e .[dev]`
3. Set up environment variables for API integrations
4. Run individual projects as needed

## 📝 **Note on Security**

This repository contains example projects with API integrations. For production use:
- Use environment variables for sensitive data
- Implement proper authentication
- Follow security best practices
- Never commit API keys or credentials

## 🎯 **Learning Objectives**

These projects demonstrate:
- API integration and authentication
- GUI development with Tkinter
- Data processing and manipulation
- Web scraping techniques
- Automation and workflow optimization
- File I/O and data persistence
- Error handling and user input validation

---

*Built with Python 3.12+ | Last updated: 2024*
