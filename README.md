# Travel Intelligence

Evidence-led travel planning for Codex and ChatGPT. It is designed for people who want local context, practical transport, realistic costs, affordable food, natural language, and honest recommendations instead of generic guidebook lists.

## What it covers

- less-obvious places grounded in local-language and local-source evidence;
- city transport, airport transfers, parking, walking, and door-to-door costs;
- affordable local food, current menus, and useful phrases for ordering;
- flight research across nearby airports, flexible dates, airlines, and self-transfers;
- regional language, pronunciation, register, etiquette, and local vocabulary;
- adversarial audits of itineraries, budgets, routes, and assumptions;
- controlled detection of new reusable capabilities.

## Reality-first policy

Every final answer passes a risk-scaled reality audit. Prices, schedules, opening hours, fares, safety rules, and local conditions are checked against current sources when possible. The skill distinguishes confirmed facts, corroborated evidence, indicative information, inference, and unknowns. It never claims to be a resident, Indigenous person, native speaker, or personal witness.

For flights, “cheapest” means three separate decisions: absolute cheapest, cheapest sensible option, and best value. The comparison includes baggage, ground transport, parking or fuel, pre-flight lodging, airport transfers, and self-transfer risk.

## Installation

Clone the repository and copy the skill files into the Codex skills directory:

```bash
git clone https://github.com/<YOUR_GITHUB_USERNAME>/travel-intelligence.git
mkdir -p ~/.codex/skills/travel-intelligence
cp -a travel-intelligence/SKILL.md travel-intelligence/agents travel-intelligence/references ~/.codex/skills/travel-intelligence/
```

The same structure can be used by other compatible agent runtimes that support `SKILL.md` skills.

## Invocation

Explicit invocation:

```text
$travel-intelligence /loty Katowice/Kraków/Ostrawa → Marsylia, 6–10 października 2026, 2 osoby, bagaż podręczny
$travel-intelligence /plan Zaplanuj 4 dni w Marsylii lokalnie i bez typowych atrakcji
$travel-intelligence /lokalnie Znajdź mniej oczywiste miejsca w Marsylii i sprawdź, czy są naprawdę lokalne
$travel-intelligence /transit Porównaj transport z lotniska Marsylia-Provence do centrum
$travel-intelligence /jedzenie Znajdź tanie lokalne jedzenie w Marsylii i naturalne zwroty po francusku
$travel-intelligence /jezyk Naucz mnie zwrotów używanych w konkretnym regionie Hiszpanii
$travel-intelligence /audyt Sprawdź mój plan i znajdź ukryte koszty oraz ryzyka
```

It can also be invoked naturally without the `$travel-intelligence` prefix when automatic skill discovery is enabled.

## Project structure

```text
SKILL.md
agents/openai.yaml
references/reality-audit.md
references/capability-learning.md
references/capability-index.md
scripts/validate_skill.py
.github/workflows/validate.yml
```

## Validate locally

```bash
python scripts/validate_skill.py .
```

## Scope

This repository contains instructions and documentation. It does not include an airfare API, booking automation, payment credentials, hidden monitoring, or guarantees that every market fare has been found.

## License

MIT. See [LICENSE](LICENSE).
