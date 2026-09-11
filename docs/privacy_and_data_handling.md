# Privacy And Data Handling

- No names, emails, payment information, loyalty numbers, or external identity data are collected.
- The prompt and extracted preferences live only in the active application process.
- `DELETE /sessions/{session_id}` removes the session immediately.
- Feedback and aggregate events are held in memory in this prototype; production deployments should use an explicitly documented retention policy and anonymized aggregates.
- User preferences are supplied directly by the traveler and are not inferred from external sources.
- Do not add analytics identifiers or persistent profiles without a privacy review.
