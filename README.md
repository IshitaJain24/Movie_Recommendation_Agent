# Movie Recommendation Agent

A LangChain-based ReAct agent that uses live TMDB data to recommend movies matching user-defined constraints.

The agent interprets natural language requests, converts them into structured search criteria, queries TMDB, and returns a recommendation based on the highest-ranked matching result.

---

# Architecture

The solution follows the ReAct (Reasoning + Acting) pattern.

### Flow

User Query

↓

Constraint Extraction

↓

Tool Invocation

↓

TMDB Search

↓

Result Analysis

↓

Movie Recommendation

### Example

Input:

```text
Recommend a horror movie from the 90s rated R
```

Extracted Constraints:

```json
{
  "genre": "horror",
  "year_range": {
    "start": 1990,
    "end": 1999
  },
  "rating": "R"
}
```

Tool:

```text
search_tmdb_movies
```

The tool queries TMDB using these filters and returns the highest-ranked matching movie.

---

# Installation

## 1. Create Virtual Environment

Windows:

```powershell
py -3.12 -m venv venv
```

Activate:

```powershell
venv\Scripts\activate
```

Verify:

```powershell
python --version
```

Expected:

```text
Python 3.12.x
```

---

## 2. Install Dependencies

```powershell
pip install -r requirements.txt
```

Contents of requirements.txt:

```text
python-dotenv
requests
pydantic
langchain==0.3.25
langchain-community==0.3.24
langchain-google-genai==2.1.4
```

---

# API Configuration

## Gemini API

Generate an API key from:

https://aistudio.google.com/

## TMDB API

Create an account and generate an API key from:

https://www.themoviedb.org/settings/api

---

## Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_gemini_api_key
TMDB_API_KEY=your_tmdb_api_key
```

---

# Execution

Run the application:

```powershell
python app.py
```

Example query:

```text
Recommend a horror movie from the 90s rated R
```

---

# Sample Output

```text
Question:
Recommend a horror movie from the 90s rated R

Thought:
The user wants a horror movie.

Thought:
The decade "90s" corresponds to 1990-1999.

Thought:
The required rating is R.

Action:
search_tmdb_movies

Observation:
Movie data returned from TMDB.

Final Answer:

Best Match Found

Title: Scream

Year: 1996

TMDB Score: 7.43

Reason:
Matches the horror genre, satisfies the R certification requirement,
and was released during the 1990s.

Overview:
A year after the murder of her mother, a teenage girl is terrorized
by a masked killer who targets her and her friends.
```

---

# Supported Constraints

The agent currently supports:

* Genre filtering
* Decade-based release filtering
* Certification filtering

Examples:

```text
Recommend an action movie from the 2000s rated PG-13
```

```text
Recommend a horror movie from the 90s rated R
```

```text
Recommend a drama from the 80s
```

---

# Limitations

* Limited genre mapping.
* Uses TMDB as the only data source.
* Returns a single recommendation.
* No conversation memory.
* No streaming platform filtering.

---

# Future Enhancements

Potential improvements include:

* Streaming provider filters
* Additional genre coverage
* Multi-movie recommendations
* User preference memory
* Retry and caching support
* Unit and integration tests

---

# Technologies Used

* Python 3.12
* LangChain
* Google Gemini
* TMDB API
* Requests
* Python Dotenv

---

# Notes

This project demonstrates how a ReAct agent can combine reasoning and tool usage to generate recommendations from live external data rather than relying solely on language model knowledge.
