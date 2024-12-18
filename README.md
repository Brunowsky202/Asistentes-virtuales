# README: AI Assistant Family Project
## Table of Contents
1. [Overview](#overview)
2. [Project Descriptions](#project-descriptions)
   1. [Zbigniew Milko Project](#zbigniew-milko-project-ai-for-web-development)
   2. [Juan Da Silva and Jesús Durán Project](#juan-da-silva-and-jesús-durán-project-ai-for-document-creation)
   3. [Rodrigo Rodríguez Project](#rodrigo-rodríguez-project-ai-for-pinterest-image-search)
   4. [Simón Gómez Project](#simón-gómez-project-ai-for-story-creation)
   5. [Vincenzo Palladino and Augusto Anselmetti Project](#vincenzo-palladino-and-augusto-anselmetti-project-ai-for-youtube-video-search-and-download)
   6. [Joseph Nicholls Project](#joseph-nicholls-project-ai-for-powerpoint-presentations)
3. [Technologies Used](#technologies-used)
4. [Packages Used](#packages-used)
5. [Goals and Learning Outcomes](#goals-and-learning-outcomes)
6. [Future Improvements](#future-improvements)
7. [Conclusion](#conclusion)
## Overview
This project is a collaborative effort developed with students in the Adakdemy classes. The primary goal was to create a family of intelligent AI assistants, each specialized in solving unique problems using advanced technologies. We implemented seven different AI models, all leveraging the Gemini API for calling functions and answering queries. Additionally, we utilized Vosk AI for local speech recognition, ensuring faster and more accurate performance.

Each project demonstrates how AI can enhance productivity and creativity in various domains. Below is a detailed description of each project.

---

### **1. Zbigniew Milko Project: AI for Web Development**
**Description:** This AI assistant helps users create complete web pages using Bootstrap. Once the web page is generated, the assistant opens the project in Visual Studio Code and previews it in the browser for easy review and customization.

**Key Features:**
- Generates responsive web pages using Bootstrap.
- Automates opening the project in VS Code and a browser.
- Simplifies web development for beginners and professionals alike.

---

### **2. Juan Da Silva and Jesús Durán Project: AI for Document Creation**
**Description:** This AI assistant specializes in generating Word documents based on user input. Once the document is created, it opens directly in Microsoft Word for further editing.

**Key Features:**
- Creates professional Word documents quickly.
- Compatible with Microsoft Word for seamless editing.
- Enhances productivity for users working on reports, essays, or other text-based documents.

---

### **3. Rodrigo Rodríguez Project: AI for Pinterest Image Search**
**Description:** This AI assistant allows users to search for pictures on Pinterest by describing what they want to see. The assistant fetches relevant images based on the user’s input.

**Key Features:**
- Fetches high-quality images from Pinterest.
- Uses natural language processing for intuitive search.
- Saves time by providing tailored image results.

---

### **4. Simón Gómez Project: AI for Story Creation**
**Description:** This AI assistant creates engaging stories on any topic specified by the user. It can be used for entertainment, educational purposes, or creative writing support.

**Key Features:**
- Generates original and creative stories.
- Adapts to various themes and genres.
- Ideal for writers, students, and storytelling enthusiasts.

---

### **5. Vincenzo Palladino and Augusto Anselmetti Project: AI for YouTube Video Search and Download**
**Description:** This AI assistant searches for YouTube videos based on user input and downloads them directly for offline use.

**Key Features:**
- Searches YouTube using natural language queries.
- Downloads videos in the desired quality.
- Saves time and provides offline access to content.

---

### **6. Joseph Nicholls Project: AI for PowerPoint Presentations**
**Description:** This AI assistant helps users create PowerPoint presentations tailored to their needs. It generates slides based on the specified topic and opens them in Microsoft PowerPoint for final adjustments.

**Key Features:**
- Creates visually appealing slides with structured content.
- Compatible with Microsoft PowerPoint.
- Boosts efficiency for students, professionals, and educators.

---

## Technologies Used
- **Gemini API:** Enables function calls and intelligent answers for all AI assistants.
- **Vosk AI:** Provides accurate and efficient local speech recognition.
- **Additional Tools:**
  - Visual Studio Code for web development projects.
  - Microsoft Word and PowerPoint for document and presentation editing.
  - YouTube API for video search and downloads.

## Goals and Learning Outcomes
This project was designed to:
1. Foster collaboration and innovation among students.
2. Showcase practical applications of AI in diverse fields.
3. Teach students how to integrate multiple technologies to build functional tools.

Through this project, students enhanced their programming, problem-solving, and teamwork skills while exploring real-world AI applications.

---

## Future Improvements
- **Enhanced User Interfaces:** Add user-friendly graphical interfaces to each assistant.
- **Customizability:** Allow more personalization options for each assistant’s output.
- **Expanded Functionality:** Integrate additional APIs and features to increase versatility.

## Conclusion
This project represents a significant step in exploring the potential of AI in daily life and professional tasks. Each assistant is a testament to the creativity and technical skills of the Adakdemy students, providing practical solutions and inspiring further innovation in AI development.

## Packages Used

Below is an explanation of the main packages used in the development of this project, along with their installation commands:

- **google.generativeai**: This package is used to interact with Google's Gemini API, enabling the creation of AI-generated responses for the assistants. It is crucial for calling functions and generating intelligent answers that define the assistant's behavior.

  ```bash
  pip install google-generativeai
  ```

- **Vosk**: Vosk is a local and real-time speech recognition engine. It is used in this project to provide a faster and more accurate voice recognition experience without requiring a constant internet connection.

  ```bash
  pip install vosk
  ```

- **python-pptx**: This package is used for creating, manipulating, and modifying PowerPoint presentations. It is employed in Joseph Nicholls' project to dynamically generate slides, allowing automated PowerPoint presentation creation based on user input.

  ```bash
  pip install python-pptx
  ```

- **python-docx**: This package is used for creating and modifying Microsoft Word documents. It is used in the Juan Da Silva and Jesús Durán project to generate `.docx` documents based on user requests.

  ```bash
  pip install python-docx
  ```

- **playsound**: A simple package used for playing sound files. In this project, it is used to play the text-to-speech responses generated by the assistant, improving the user experience with audio interaction.

  ```bash
  pip install playsound
  ```

- **Gtts (Google Text-to-Speech)**: This package converts text into speech using Google's technology. It is used in this project to provide voice responses generated by the assistant, allowing the assistant to "speak" to the user.

  ```bash
  pip install gtts
  ```

- **y_dpl**: This package is used to interact with the YouTube API. In the Vincenzo Palladino and Augusto Anselmetti project, it is used to search for and download YouTube videos based on user input, automating the process of obtaining multimedia content.

  ```bash
  pip install y_dpl
  ```
