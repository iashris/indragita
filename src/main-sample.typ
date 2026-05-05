// Indragita: What Indra Taught Krishna
// A Philosophical Dialogue Drawn from the Rigveda, the Mahabharata, the Upanishads, and the Bhagavad Gita
// By Ashris Choudhury
// =====================================
// SAMPLE READING PACK for Penguin Tattva submission
// Includes: Preface, Introduction, Adhyaya 1 (The Descent),
//           Adhyaya 5 (On Karma and the Instant Rebirth),
//           Adhyaya 12 (The Question), Afterword, Glossary

#import "template.typ": *

#show: book-setup.with(is-dark: false)

// ============================================
// FRONT MATTER
// ============================================

// Cover with image
#image-cover-page("cover-light.png", is-dark: false)

// Sample-reading note page
#set page(header: none, footer: none)
#v(2.5cm)
#align(center)[
  #text(size: 9pt, fill: light-muted, weight: "regular")[
    A Sample Reading Pack
  ]
  #v(0.4cm)
  #text(size: 18pt, fill: light-primary, weight: "medium")[Indragita]
  #v(0.3cm)
  #text(size: 12pt, fill: light-primary, weight: "medium")[What Indra Taught Krishna]
  #v(0.6cm)
  #text(size: 9pt, style: "italic")[A Philosophical Dialogue]
  #v(0.2cm)
  #text(size: 8.5pt, style: "italic", fill: light-muted)[Drawn from the Rigveda, the Mahabharata, the Upanishads, and the Bhagavad Gita]
  #v(2cm)
  #box(width: 75%)[
    #align(left)[
      #text(size: 9.5pt)[
        This pack contains the complete framing material of the book, three of its twelve adhyayas, and the closing afterword. The chapters chosen, *The Descent*, *On Karma and the Instant Rebirth*, and *The Question*, give the editor the opening of the dialogue, its single clearest philosophical statement, and the parting bargain between Krishna and Indra with which the book closes.

        The full manuscript runs to twelve adhyayas and roughly forty thousand words. The full designed editions (light, dark, and print-ready) are available alongside this sample.
      ]
    ]
  ]
  #v(2cm)
  #text(size: 9pt, style: "italic")[By Ashris Choudhury]
  #v(0.3cm)
  #text(size: 8pt, fill: light-muted)[Submitted to Penguin Tattva · 2026]
]
#pagebreak()

// Table of Contents (sample-only)
#toc-page(is-dark: false, (
  (label: "Preface", title: "Preface", page: ""),
  (label: "Introduction", title: "Introduction", page: ""),
  (label: "Adhyaya 1", title: "The Descent", page: ""),
  (label: "Adhyaya 3", title: "The Fire on Your Own Soil", page: ""),
  (label: "Adhyaya 5", title: "On Karma and the Instant Rebirth", page: ""),
  (label: "Adhyaya 12", title: "The Question", page: ""),
  (label: "Afterword", title: "On the Society Indra Imagines", page: ""),
  (label: "Glossary", title: "Glossary", page: ""),
))

// Half-title page
#set page(header: none, footer: none)
#v(3.5cm)
#align(center)[
  #text(size: 20pt, fill: light-primary, weight: "medium")[Indragita]
  #v(0.4cm)
  #text(size: 14pt, fill: light-primary, weight: "medium")[What Indra Taught Krishna]
  #v(1.2cm)
  #text(size: 10pt)[A Philosophical Dialogue]
  #v(0.2cm)
  #text(size: 9pt, style: "italic")[Drawn from the Rigveda, the Mahabharata, the Upanishads, and the Bhagavad Gita]
  #v(1.5cm)
  #text(style: "italic", size: 10pt)[By Ashris Choudhury]
]
#pagebreak()

// ============================================
// SAMPLE CONTENT
// ============================================

// Preface
#include "chapters/02-preface.typ"

// Introduction
#include "chapters/03-introduction.typ"

// Adhyaya 1: The Descent
#include "chapters/04-adhyaya-01.typ"

// ---- elision marker between Adhyaya 1 and Adhyaya 3 ----
#pagebreak()
#set page(header: none)
#v(1fr)
#align(center)[
  #text(size: 9pt, style: "italic", fill: light-muted)[
    Adhyaya 2 is omitted in this sample pack.
    #linebreak()
    It develops the conversation through *The Wound of Time*.
    #linebreak() #linebreak()
    The sample resumes with Adhyaya 3.
  ]
]
#v(1fr)
#pagebreak()

// Adhyaya 3: The Fire on Your Own Soil (cites Rigveda 10.129.4, 10.129.6-7, and 1.9.7)
#include "chapters/06-adhyaya-03.typ"

// ---- elision marker between Adhyaya 3 and Adhyaya 5 ----
#pagebreak()
#set page(header: none)
#v(1fr)
#align(center)[
  #text(size: 9pt, style: "italic", fill: light-muted)[
    Adhyaya 4 is omitted in this sample pack.
    #linebreak()
    It develops the conversation through *The Estranged Cousins*.
    #linebreak() #linebreak()
    The sample resumes with Adhyaya 5.
  ]
]
#v(1fr)
#pagebreak()

// Adhyaya 5: On Karma and the Instant Rebirth
#include "chapters/08-adhyaya-05.typ"

// ---- elision marker between Adhyaya 5 and Adhyaya 12 ----
#pagebreak()
#set page(header: none)
#v(1fr)
#align(center)[
  #text(size: 9pt, style: "italic", fill: light-muted)[
    Adhyayas 6 through 11 are omitted in this sample pack.
    #linebreak()
    They take the dialogue through sincerity, love, excellence, death, joy, and power.
    #linebreak() #linebreak()
    The sample resumes with Adhyaya 12, the closing dialogue.
  ]
]
#v(1fr)
#pagebreak()

// Adhyaya 12: The Question (the closing dialogue)
#include "chapters/15-adhyaya-12.typ"

// Afterword
#include "chapters/16-afterword.typ"

// Glossary
#include "chapters/17-glossary.typ"

// ============================================
// COLOPHON
// ============================================
#pagebreak()
#set page(header: none)
#v(1fr)
#align(center)[
  #text(style: "italic", size: 9pt)[
    Indragita: What Indra Taught Krishna \
    A Philosophical Dialogue \
    Sample Reading Pack for Penguin Tattva \
    By Ashris Choudhury \
    Manuscript, 2026
  ]
]
#v(2cm)
