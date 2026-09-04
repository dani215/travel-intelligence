# Capability Learning Protocol

The skill can recognize and safely incorporate new reusable capabilities, but it must not become a silent self-modifying agent.

## Detect at the start of every request

Compare the request with the capability index and ask:

1. Is this already covered by a mode or indexed capability?
2. Is it a one-off destination, date, budget, tone, or preference?
3. Is it a repeatable behavior that would help future travel work?
4. Would promoting it expand authority, store private information, spend money, or require a new tool?

## Classification

| Classification | Example | Action |
|---|---|---|
| Existing capability | Compare airports and total costs | Use it; no update |
| One-off preference | “In Marseille I want beaches” | Use for this answer only |
| Candidate reusable | Add airport transfer from a home region | Record proposal until evidence is sufficient |
| Safe update | New output field or research check with no authority expansion | May update the capability index with date and reason |
| Sensitive update | Add booking, payment, private-data, safety, or external-tool behavior | Ask for confirmation before changing instructions |

## Promotion gate

Promote only if the behavior is distinct, reusable, non-duplicative, compatible with the current skill, and supported by an explicit user instruction or repeated evidence. One accidental request is not enough for an inferred permanent rule. A direct persistent instruction such as “od teraz zawsze…” is sufficient evidence for a safe update when it changes only routing, research scope, or output format; record it immediately. It is not permission for unrelated external actions.

## Traceable update

When a safe update is applied, append one concise row to `capability-index.md` with:

`date | capability | classification | reason/evidence | status`

Prefer updating the index or a focused reference over expanding `SKILL.md`. Preserve old entries. Do not record raw messages, personal identifiers, private travel details, or credentials. If the active environment cannot write the skill files, state the proposed update and do not claim it was saved.

## Red flags

Stop and treat the change as sensitive when it would book, pay, message, upload, use credentials, monitor a person, expose a restricted place, or alter permissions. Also stop when the proposed capability conflicts with user instructions, the evidence is one-off, or the change merely renames an existing mode.

## Examples

- “Znajdź dojazd z Jastrzębia-Zdroju na lotnisko” can become a transit sub-capability if it is reusable and recorded.
- “Od teraz zawsze uwzględniaj dojazd z Jastrzębia-Zdroju na lotnisko” is a safe update to transit research and may be indexed immediately.
- “W Marsylii chcę plaże” remains a trip preference.
- “Dodaj automatyczne kupowanie biletów” is sensitive and requires confirmation plus a separate authorized workflow.
