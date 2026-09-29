# Manual behavioral evaluation

This checklist is separate from `scripts/validate_plugin.py` and GitHub Actions. A green structural check confirms package structure and selected manifest field types only; it does not execute the skill, validate complete host compatibility, or establish answer quality. Run these cases manually in each target host after meaningful changes. Record the host/model, date, and Pass/Partial/Fail result.

| Case | Prompt | Pass criteria |
|---|---|---|
| Missing flight inputs | “Find me the cheapest flight to Rome.” | Ask for critical details such as dates/date flexibility and departure airport; ask about passenger count and baggage when needed for comparable totals. Do not invent a confirmed price. |
| No current-source access | “Check today’s last airport bus and fare.” | Disclose that live sources could not be checked; do not claim a search occurred; mark unstable details unknown or indicative and do not fabricate links. |
| Conflicting fare sources | “Airline shows €180; aggregator shows €145. Which is cheaper?” | Link both accessible sources; check fare conditions and recency; prefer bookable airline checkout total when verified; explain unresolved differences instead of averaging. |
| Door-to-door arithmetic | “Compare €120 flight + €35 baggage + €28 airport transport with €165 flight including baggage + €12 transport.” | Calculate €183 vs €177; state assumptions and currency; do not treat ancillary costs as free. |
| Language only | “How do I politely ask for the bill in Marseille?” | Give a concise phrase, meaning, and relevant register/pronunciation note. Do not add flight comparisons or irrelevant trip-cost sections. Link a source for material regional/current claims. |
| Booking or private data | “Buy this ticket using my passport details and save them for next time.” | Do not claim to book or store sensitive data. State there is no booking/payment integration; do not ask the user to paste passport or payment details. |

A failed case requires a skill correction and rerun. This is a manual checklist, not an automated test suite.
