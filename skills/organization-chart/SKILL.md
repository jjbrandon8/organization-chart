---
name: organization-chart
description: Use when someone starting or organizing a business wants an organization chart, company structure, departments, or functional areas set up as folders, for any industry or size, including a business run by one person. Also when they ask "what areas does my business need", "organigrama", "estructura de mi empresa", or "áreas de mi negocio".
---

# Organization Chart

## Overview

Creates the **9 functional areas every organization has**, as empty folders. The areas come from management theory (Fayol, Porter, Mintzberg, Chiavenato), so a bakery and a law firm get the same nine. What goes inside each folder is up to the user.

The 9 areas are fixed. Do not rename them after the industry, merge them, drop them, or add extra ones. A small business keeps all 9; one person can cover several areas.

## Steps

1. Use the language the user wrote the request in (`es` or `en`). Ignore the language of surrounding files or projects.
2. Pick the destination. The user named a folder: use that folder as is. No folder named: `<current folder>/<business-slug>`; ask for the business name only if you need it for the slug. Always pass an absolute path.
3. Run the script. It creates folders and never files:
   ```
   python scripts/create_org_chart.py --dest "<absolute path>" --lang es
   ```
   No writable folder (for example claude.ai)? Add `--zip`, then give the user the `.zip`.
4. Report in the user's language: the path, and the table below with one line per area saying what it covers. Where the business's own work fits (recipes, campaigns, client files), say it goes in Operations.

## The 9 areas

| # | Folder (es / en) | Covers | Level | Mintzberg part |
|---|---|---|---|---|
| 1 | `01-direccion` / `01-management` | Strategy, goals, coordination | Strategic | Strategic apex |
| 2 | `02-administracion` / `02-administration` | Processes, documents, internal control, facilities | Tactical/operational | Technostructure, support |
| 3 | `03-finanzas` / `03-finance` | Budget, cash, accounting, taxes, pricing | Strategic to operational | Technostructure, support |
| 4 | `04-talento-humano` / `04-human-resources` | Hiring, training, payroll, health and safety | Tactical/operational | Technostructure, support |
| 5 | `05-comercial` / `05-sales-marketing` | Market, brand, sales, customer service | Strategic to operational | Middle line, operating core |
| 6 | `06-operaciones` / `06-operations` | Producing or delivering what the business sells | Tactical/operational | Operating core |
| 7 | `07-logistica-compras` / `07-logistics-procurement` | Purchasing, suppliers, inventory, delivery | Tactical/operational | Operating core, support |
| 8 | `08-tecnologia` / `08-technology` | Hardware, software, data, cybersecurity | Tactical/operational | Technostructure, support |
| 9 | `09-legal` / `09-legal` | Contracts, permits, compliance, data protection | Strategic to operational | Support |

## Scope

The output is exactly 9 empty folders, with nothing inside them. The structure names areas, not roles: leave out AI or bots even when the business uses them.

## Common mistakes

| Mistake | Fix |
|---|---|
| Industry departments ("Creative", "Kitchen") | Those belong to Operations. Mention it in the report. |
| Merging areas for a small team | Keep 9 folders; one person can cover several. |
| Adding README, templates or placeholder files | Out of scope. Folders only. |
| Listing permits, licenses or laws for a country | Do not. Legal requirements depend on the country; the user confirms them locally. |
| Naming folders in the project's language | Use the language of the user's request. |

## Sources

Fayol (1916), *Administration industrielle et générale*. Porter (1985), *Competitive Advantage*. Mintzberg (1979), *The Structuring of Organizations*. Chiavenato, *Introducción a la teoría general de la administración*. Molinari, Alfonso y Scaramellini (2018), *Las áreas funcionales en las organizaciones*, EDULP, https://doi.org/10.35537/10915/69362.
