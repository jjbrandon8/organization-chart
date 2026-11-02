# organization-chart

A Claude skill that sets up the 9 functional areas every business has, as empty folders. You fill them in.

[Español](#español) · [English](#english)

---

## Español

### Qué hace

Le pides a Claude "crea el organigrama de mi negocio" y te crea estas 9 carpetas vacías:

```
01-direccion
02-administracion
03-finanzas
04-talento-humano
05-comercial
06-operaciones
07-logistica-compras
08-tecnologia
09-legal
```

Son las mismas para una panadería o un estudio jurídico. Lo que cambia es lo que guardas dentro, sobre todo en `06-operaciones`. Si tu negocio es pequeño, una persona puede llevar varias áreas, pero las 9 siguen ahí.

Las carpetas salen en el idioma en que le escribas a Claude: español o inglés.

### Instalar

**Claude Code:**

```
/plugin marketplace add jjbrandon8/organization-chart
/plugin install organization-chart@jjbrandon8
```

**claude.ai:** descarga este repositorio, comprime la carpeta `skills/organization-chart` en un `.zip` y súbela en [Customize > Skills](https://claude.ai/customize/skills). Necesitas activar code execution en Settings > Capabilities. En claude.ai recibes las carpetas en un `.zip`.

### Usar

Escribe algo como "organiza mi cafetería por áreas" o "crea el organigrama de mi empresa en esta carpeta". También puedes llamarla con `/organization-chart`.

---

## English

### What it does

Ask Claude "set up my business's organization chart" and it creates these 9 empty folders:

```
01-management
02-administration
03-finance
04-human-resources
05-sales-marketing
06-operations
07-logistics-procurement
08-technology
09-legal
```

A bakery and a law firm get the same nine. What changes is what you keep inside, mostly in `06-operations`. In a small business one person can cover several areas, and all 9 stay.

Folder names follow the language you write to Claude in: English or Spanish.

### Install

**Claude Code:**

```
/plugin marketplace add jjbrandon8/organization-chart
/plugin install organization-chart@jjbrandon8
```

**claude.ai:** download this repository, zip the `skills/organization-chart` folder and upload it in [Customize > Skills](https://claude.ai/customize/skills). Code execution must be on in Settings > Capabilities. On claude.ai you get the folders as a `.zip`.

### Use

Write something like "organize my coffee shop by areas" or "create my company's org chart in this folder". You can also call it with `/organization-chart`.

---

## Sources

- Fayol, H. (1916). *Administration industrielle et générale*.
- Porter, M. E. (1985). *Competitive Advantage*.
- Mintzberg, H. (1979). *The Structuring of Organizations*.
- Chiavenato, I. *Introducción a la teoría general de la administración*.
- Molinari, G. E., Alfonso, A. M. y Scaramellini, N. (2018). *Las áreas funcionales en las organizaciones*. EDULP. https://doi.org/10.35537/10915/69362

## License

MIT
