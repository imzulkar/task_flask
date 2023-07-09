# Document Uploader and Worker Service

This repository contains an example implementation of a document uploader service and a worker service using Flask. The document uploader service allows users to upload documents, and the worker service asynchronously processes the uploaded documents by counting the number of words with a specified length.

## Prerequisites

Make sure you have the following dependencies installed:

- Python 3.x
- Flask
- Redis

You can install the required Python packages by running the following command:

```
pip install Flask redis
```

## Getting Started

1. Clone this repository to your local machine or download the source code.

2. Start a Redis server on your local machine. You can download Redis from the official website: [Redis](https://redis.io/)

3. Open two terminal windows.

4. In the first terminal, navigate to the repository's directory and start the document uploader service:

   ```bash
   python uploader_service.py
   ```

   The uploader service will start running on `http://localhost:5000`.

5. In the second terminal, navigate to the repository's directory and start the worker service:

   ```bash
   python worker_service.py
   ```

   The worker service will start processing uploaded documents.

## Uploading Documents

To upload a document, you can use tools like cURL or Postman. Make sure you have a file ready to upload.

Using cURL, you can run the following command to upload a document:

```bash
curl -X POST -F 'file=@/path/to/your/file.txt' http://localhost:5000/upload
```

Replace `/path/to/your/file.txt` with the actual path to the file you want to upload.

## Customizing Word Length

By default, the worker service counts words with a length of 5. If you want to change the word length, you can modify the `k` variable in the `process_documents` function in `worker_service.py`:

```python
k = 5  # Specify the desired word length here
```

Change the value of `k` to the desired word length.
