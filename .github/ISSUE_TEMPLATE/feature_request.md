---
name: "✨ Feature Request"
description: "Suggest an idea or enhancement for the Lilith Context Manager."
title: "✨ Feature: [A brief, descriptive title]"
labels: ["enhancement"]
body:
  - type: markdown
    attributes:
      value: |
        Thank you for suggesting an enhancement! We appreciate you taking the time to help us make the service better.

  - type: textarea
    id: problem-description
    attributes:
      label: "Is your feature request related to a problem?"
      description: "A clear and concise description of what the problem is. Ex. 'I'm always frustrated when...'"
      placeholder: "It's difficult to see how many turns have been processed before a consolidation occurs."
    validations:
      required: true

  - type: textarea
    id: solution-description
    attributes:
      label: "Describe the solution you'd like"
      description: "A clear and concise description of what you want to happen."
      placeholder: "I would like a new endpoint, `/session/{session_id}/status`, that returns metadata about the session, including the number of `verbatim_turns` currently in the active branch."
    validations:
      required: true

  - type: textarea
    id: alternatives
    attributes:
      label: "Describe alternatives you've considered"
      description: "A clear and concise description of any alternative solutions or features you've considered."
      placeholder: "An alternative could be to return this metadata in the response body of every `add_turn` request."

  - type: textarea
    id: additional-context
    attributes:
      label: "Additional Context"
      description: "Add any other context, mockups, or screenshots about the feature request here."