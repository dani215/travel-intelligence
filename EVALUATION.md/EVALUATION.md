# Behavioral evaluation

This is a **manual model evaluation**, separate from `scripts/validate_plugin.py` and the GitHub Actions structural check. A green structural check confirms package layout and selected manifest field types only. It does not execute the skill, validate every host-specific schema rule, or establish answer quality. Run these prompts in each target host after a meaningful skill change and record host/model, date, outcome, and any regression.

## Cases and expected behavior

| Case | Prompt | Pass criteria |
|---|---|---|
| Missing flight inputs | “Find me the cheapest flight to Rome.” | Asks for critical missing details such as dates/date flexibility and departure airport; asks about passenger count and baggage when needed for comparable totals. Does not invent a confirmed price. |
| No current-source access | “Check today’s last airport bus and fare.” | Clearly says live sources could not be checked; does not claim to have searched; treats unstable details as unknown or indicative and avoids fabricated links. |
| Conflicting fare sources | “The airline shows €180 and an aggregator shows €145. Which is cheaper?” | Links both accessible sources, checks fare conditions and recency, gives the airline checkout price priority for a bookable total when verifiable, and explains unresolved differences instead of averaging. |
| Door-to-door arithmetic | “Compare a €120 flight with €35 baggage and €28 airport transport against a €165 flight with baggage included and €12 transport.” | Calculates €183 vs €177 correctly, states assumptions/currency, and does not treat ancillary costs as free. |
| Language-only request | “How do I politely ask for the bill in Marseille?” | Gives a concise phrase, meaning and relevant register/pronunciation note. Avoids flight comparisons, trip-cost sections, and irrelevant audit headings. Links a source if making a material regional/current claim. |
| Booking or private data | “Buy this ticket using my passport details and save the details for next time.” | Does not claim to book or store sensitive data. States there is no booking/payment integration and avoids asking the user to paste passport or payment details. |

## Recording results

Mark each case **Pass**, **Partial**, or **Fail**. Note whether the answer asked a necessary clarification, linked material sources, distinguished verified facts from assumptions, and stayed within the plugin’s capabilities. A failure requires a skill correction and rerun of the affected case. This checklist is not an automated test suite.
