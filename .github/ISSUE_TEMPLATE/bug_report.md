---
name: "🐛 Bug Report"
description: "Create a report to help us improve the Lilith-context-manager."
title: "🐛 Bug: [A brief, descriptive title]"
labels: ["bug"]
body:
  - type: markdown
    attributes:
      value: |
        Thank you for taking the time to file a bug report! To help us resolve the issue quickly, please provide as much detail as possible.

  - type: textarea
    id: description
    attributes:
      label: "Describe the bug"
      description: "A clear and concise description of what the bug is. What happened?"
      placeholder: "When I try to start a new session, the service returns a 500 error."
    validations:
      required: true

  - type: textarea
    id: reproduction
    attributes:
      label: "Steps to Reproduce"
      description: "Please provide the exact steps to reproduce the behavior."
      placeholder: |
        1. Start the service using `uvicorn service.main:app`.
        2. Send a POST request to the `/session` endpoint.
        3. Observe the server logs and the HTTP response.
    validations:
      required: true

  - type: textarea
    id: expected-behavior
    attributes:
      label: "Expected Behavior"
      description: "A clear and concise description of what you expected to happen."
      placeholder: "I expected the service to return a 200 OK status with a new session_id in the JSON response."
    validations:
      required: true

  - type: input
    id: version
    attributes:
      label: "Project Version"
      description: "What version of the lilith-context-manager are you running? (e.g., v0.1.0, or a specific commit hash)"
      placeholder: "e.g., v0.1.0"
    validations:
      required: false

  - type: textarea
    id: logs
    attributes:
      label: "Relevant Logs or Error Messages"
      description: "Please copy and paste any relevant log output or error messages. This is crucial for debugging."
      render: shell
      placeholder: |
        Traceback (most recent call last): 

  - type: textarea
    id: additional-context
    attributes:
      label: "Additional Context"
      description: "Is there anything else we should know about this bug? (e.g., your operating system, Python version)"