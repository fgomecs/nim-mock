# 🧠 Mock NVIDIA NIM Microservice

This project simulates the structure and behavior of an NVIDIA Inference Microservice (NIM) using Docker and Flask — built from scratch by Francisco Gomez to demystify the process of deploying GPU-ready AI APIs, even on modest local hardware.

It’s not an LLM — it’s a **learning-first microservice scaffold** designed to help others:
- Understand containerized API services
- Interact with model-style POST endpoints
- Lay the groundwork for real inference pipelines

---

## 🚀 What It Does

- 🧱 Spins up a lightweight Flask app inside a Docker container
- 🌐 Exposes a REST API endpoint at `/v1/mock`
- 📩 Accepts a `POST` request with a `"prompt"` in JSON
- 🧠 Returns a simple JSON acknowledgment as a mock inference response

It mirrors the basic structure of real NIMs like `/v1/completions` and `/v1/embeddings`, minus the model overhead.

---

## 🛠️ Getting Started

### Prerequisites
- Docker Desktop installed with WSL2 enabled
- Git (optional, but preferred)

---

### Clone the Repo

```bash
git clone https://github.com/fgomecs/nim-mock.git
cd nim-mock
```

### Or if using Docker
```
docker run --rm -p 8800:8000 fgomecs/mock-nim:latest
```
---

### Build the Docker Image

```bash
docker build -t mock-nim .
```
---

### Run the Mock NIM Container

```bash
docker run --rm -p 8800:8000 mock-nim
```

Now the service is live at:

```
http://localhost:8800/v1/mock
```

---

### Test the API

```bash

curl -X POST http://localhost:8800/v1/mock -H "Content-Type: application/json" -d "{\"prompt\": \"What is NIM?\"}"

```

✅ Response:

```json
{
  "response": "Mock NIM received: What is NIM?"
}
```

---

## 💡 Why This Exists

Francisco wanted a hands-on way to learn and teach:

- How modern AI microservices work
- How to simulate endpoints locally using Docker
- How to move from “zero to API” on a Windows machine with a GTX 1060

This project serves as **a foundation for real NIM deployments** — with minimal hardware, no hype, and full transparency.

---

## 📦 Coming in Version 2

- `/v1/completions` and `/v1/embeddings` endpoints
- Fake AI behavior (return text or embeddings)
- Containerized logging
- Cloud deployment (Azure / AWS / Fly.io)
- Postman & Python client examples

---

## 🧾 License

MIT – use it, extend it, share it. No permission needed.

---

## ✌️ Author

Francisco Gomez – [LinkedIn](https://www.linkedin.com/in/fgomecs)  
=======

Atlanta-based TPM | Builder | Tinkerer | AI Explorer
