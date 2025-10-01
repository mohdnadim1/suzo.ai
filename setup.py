from setuptools import setup, find_packages

setup(
    name="suzo.ai",
    version="0.1.0",
    description="A modular AI framework for text generation, chatbot engines, and image classification.",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/your-username/suzo.ai",
    packages=find_packages(),
    install_requires=[
        "torch",
        "transformers",
        "fastapi",
        "uvicorn",
        "Pillow",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)