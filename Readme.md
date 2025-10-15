# Ubuntu_Requests

## Image Downloader Script

A Python script by Fortune Akioya for fetching and saving images from specified URLs. It creates a dedicated directory for downloaded content, handles common network errors gracefully, and reflects Ubuntu principles of community, respect, sharing, and practicality.

---

### Features

*   **URL Input:** Prompts the user to enter a URL for the image to be downloaded.
*   **Directory Management:** Automatically creates a `Fetched_Images` directory if it doesn't already exist.
*   **Image Download:** Fetches the image content using the `requests` library.
*   **Intelligent Naming:** Extracts a filename from the URL or generates one based on content type, with basic sanitization.
*   **Error Handling:** Catches and reports various network and HTTP errors (e.g., connection issues, timeouts, 404s) without crashing.
*   **Ubuntu Principles:**
    *   **Community:** Connects to the wider web community to fetch resources.
    *   **Respect:** Handles errors gracefully, providing user-friendly feedback.
    *   **Sharing:** Organizes downloaded images into a single directory for easy access and sharing.
    *   **Practicality:** Provides a real-world tool for basic image downloading.

---

### Getting Started

#### Prerequisites

Before running the script, ensure you have Python installed (version 3.6 or higher recommended).
You also need the `requests` library. If you don't have it, install it via pip:

```bash
pip install requests
