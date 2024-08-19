# Multilanguage Invoice Extractor - README

## Overview

The **Multilanguage Invoice Extractor** is a Streamlit application that leverages Google's Gemini AI model (`gemini-1.5-pro`) to analyze and extract relevant information from invoices uploaded by the user. This app allows users to upload an invoice image, ask specific questions, and receive AI-generated insights and information from the uploaded document.

## Features

- **Multimodal Input**: Accepts both text input and image files (invoices) for analysis.
- **Advanced AI Processing**: Utilizes Google's Gemini `gemini-1.5-pro` model for understanding and extracting invoice details.
- **Streamlined Workflow**: A simple interface that allows users to upload an invoice, ask questions, and get responses.

## Technology Stack

- **Streamlit**: For building the interactive web app.
- **Google Generative AI SDK**: For interfacing with the Gemini model.
- **PIL (Python Imaging Library)**: For handling image uploads.
- **dotenv**: For securely loading environment variables.

## Prerequisites

- Python 3.x
- Streamlit
- Google Generative AI SDK
- PIL (Python Imaging Library)
- dotenv