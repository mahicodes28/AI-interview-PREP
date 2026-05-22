# AI Interview Simulator

A multimodal mock interview system that records your webcam and audio, 
analyzes non-verbal behavior in real time, and delivers a timestamped 
feedback dashboard — so you can review exactly where you lost eye contact 
or said "um" for the fourth time.

Built as a hackathon project. Deployed via Docker on Render.

---

## What it actually does

**During the interview**
- Records webcam feed + audio simultaneously
- Runs facial landmark detection (OpenCV) to track eye contact in real time
- Captures audio in raw chunks and feeds them to a Whisper STT engine

**After the interview**
- Detects and counts filler words (um, uh, like, basically, you know)
- Syncs every filler word event to a precise video timestamp
- Clicking a filler word in the dashboard jumps the video to that exact moment

**The hard part**
Raw audio chunking without word loss was the core engineering problem. 
STT engines drop words at chunk boundaries if you split naively. 
Built a pipeline that handles boundary overlap so no speech is lost 
between chunks, then re-aligns the transcription timeline to the 
original video clock for accurate timestamp sync.

---

## Tech Stack

| Layer | Stack |
|---|---|
| Backend | Python, FastAPI |
| Video Analysis | OpenCV, facial landmark detection |
| Speech-to-Text | OpenAI Whisper |
| Frontend | React.js |
| Containerization | Docker, docker-compose |
| Deployment | Render (backend), Vercel (frontend) |

---

## Architecture
