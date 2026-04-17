# Vulnerable Docker Container - Security Research
# Intentional vulnerabilities introduced for educational purposes

# VULNERABILITY 1: Using outdated base image with known CVEs
FROM ubuntu:18.04

# VULNERABILITY 2: Running as root user
USER root

# VULNERABILITY 3: Exposing sensitive build arguments
ARG API_TOKEN=mock-token-12345-thousandeyes
ENV API_TOKEN=${API_TOKEN}
ENV BASE_URL=https://api.thousandeyes.com/v6
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

# VULNERABILITY 4: No version pinning on system packages
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    curl \
    wget \
    net-tools \
    && apt-get clean

# VULNERABILITY 5: Wide open permissions on app directory
RUN mkdir -p /app
WORKDIR /app

# Copy application files
COPY requirements.txt .
COPY app.py .

# VULNERABILITY 6: Installing packages without integrity check
RUN pip3 install -r requirements.txt

# VULNERABILITY 7: Exposing unnecessary port info in ENV
ENV APP_PORT=5000

# VULNERABILITY 8: No health check defined
# VULNERABILITY 9: No resource limits set

# Expose application port
EXPOSE 5000

# VULNERABILITY 10: Running app directly as root with debug mode on
CMD ["python3", "app.py"]