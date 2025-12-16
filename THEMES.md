# Queen of Peace Messages – Themes v1.0

This document defines the official **theme taxonomy** used to categorize Medjugorje (Queen of Peace) messages.

The themes are designed to support:

* theological accuracy
* liturgical matching
* GPT-based semantic understanding
* meditation & media production (TTS / YouTube)

---

## 1. Usage Rules

### Mandatory Rules

* Each message MUST have **at least 1 theme**
* Recommended: **3–5 themes**
* Maximum: **7 themes**
* At least **one Core Theme** must be included

### Formatting

Themes are stored as lowercase strings in JSON:

```json
"themes": ["peace", "conversion", "prayer"]
```

---

## 2. Core Theological Themes (Mandatory)

These represent the **essence of Medjugorje messages**.

```json
[
  "peace",
  "conversion",
  "faith",
  "prayer",
  "repentance",
  "hope",
  "love"
]
```

| Theme      | Meaning                              |
| ---------- | ------------------------------------ |
| peace      | Inner and world peace through God    |
| conversion | Turning back to God                  |
| faith      | Trust and belief in God              |
| prayer     | Call to personal and communal prayer |
| repentance | Confession and return to grace       |
| hope       | Hope even in suffering               |
| love       | Divine and human love                |

---

## 3. Spiritual Practice Themes

Concrete spiritual actions requested by Our Lady.

```json
[
  "fasting",
  "rosary",
  "eucharist",
  "confession",
  "scripture",
  "obedience",
  "humility"
]
```

---

## 4. Ecclesial & Community Themes

Messages concerning the Church and community.

```json
[
  "church",
  "priests",
  "religious",
  "laity",
  "unity",
  "mission",
  "persecution"
]
```

---

## 5. Prophetic & Eschatological Themes

Warnings, signs, and global messages.

```json
[
  "warning",
  "signs",
  "tribulation",
  "suffering",
  "end_times",
  "atheism",
  "world_peace"
]
```

---

## 6. Pastoral & Consolation Themes

Themes for healing, encouragement, and tenderness.

```json
[
  "healing",
  "consolation",
  "trust",
  "fearlessness",
  "family",
  "children"
]
```

---

## 7. Best Practices

### Good Example

```json
"themes": ["faith", "signs", "peace", "trust"]
```

### Bad Example (no core theme)

```json
"themes": ["rosary", "fasting"]
```

---

## 8. Future Extensions (Reserved)

These themes are **not yet active**, but reserved:

* "marian_identity"
* "angelic_presence"
* "sacrifice"
* "martyrdom"

---

**Version:** 1.0
**Maintained by:** Queen of Peace Digital Liturgy Project
**Authority:** Consistent with Medjugorje message corpus (1981–present)

> “Peace, peace, peace – and only peace.”
> – Queen of Peace
