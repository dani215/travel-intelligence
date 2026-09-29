# Travel Intelligence

An evidence-led travel-planning plugin for compatible AI agents. It helps compare trips using current local sources, practical transport, realistic door-to-door costs, affordable food, regional language, and candid risk audits.

## What it does

- finds less-obvious places using local-language and local-source evidence;
- compares city transport, airport transfers, parking, walking, and door-to-door costs;
- researches affordable local food, current menus, and useful phrases for ordering;
- compares flights across nearby airports, flexible dates, airlines, and self-transfers;
- explains regional language, register, etiquette, and local vocabulary;
- stress-tests itineraries, budgets, routes, and recommendations;
- distinguishes confirmed facts, corroborated evidence, indicative information, inference, and unknowns.

## Install

This repository follows Agent Plugins 1.0. Use your agent's plugin installation flow to install this repository or its packaged folder. Plugin installation commands and supported sources vary by client; the standard defines the package layout, not a universal installer.

The plugin root is this directory, containing `plugin.json` and `skills/travel-intelligence/SKILL.md`. Clients that support Agent Skills can discover the skill from that location.

## Example requests

- “Compare flights from Katowice, Kraków, and Ostrava to Marseille for these dates, including bags and all ground transport.”
- “Plan four days in Marseille with local food and a relaxed pace, avoiding generic tourist recommendations.”
- “Audit this itinerary for weak assumptions, hidden costs, late-night transfers, and fallback options.”
- “Find an affordable local dinner and teach me natural phrases to order in the local language.”

## Reality-first policy

Every final answer passes a risk-scaled reality audit. Prices, schedules, opening hours, fares, safety rules, and local conditions are checked against current sources when possible. Material claims should link to direct sources; high-risk claims should use primary sources where possible. If sources conflict or cannot be accessed, the answer explains the limitation rather than inventing confirmation. The skill never claims personal local identity or claims to have searched when source access was unavailable.

For flights, “cheapest” is split into three decisions: absolute cheapest, cheapest sensible option, and best value. The comparison includes baggage, ground transport, parking or fuel, pre-flight lodging, airport transfers, and self-transfer risk. Critical missing details such as dates, origin, passenger count, or baggage trigger a clarifying question when they prevent a meaningful comparison.

## Project structure

```text
plugin.json
skills/travel-intelligence/SKILL.md
skills/travel-intelligence/references/
  capability-index.md
  capability-learning.md
  reality-audit.md
tests/behavioral-cases.md
scripts/validate_plugin.py
.github/workflows/validate.yml
```

## Validate locally

```bash
python scripts/validate_plugin.py .
```

The validator checks package structure and selected manifest field types. It does not validate complete host compatibility or the quality of model responses. GitHub Actions runs this structural check; use the manual scenarios in [tests/behavioral-cases.md](tests/behavioral-cases.md) to assess behavior in each target host.

## Scope

This plugin contains instructions and documentation. It does not include an airfare API, booking automation, payment credentials, hidden monitoring, or guarantees that every market fare has been found.

## License

MIT. See [LICENSE](LICENSE).
