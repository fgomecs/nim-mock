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
