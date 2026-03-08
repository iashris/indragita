// Indragita: What Indra Taught Krishna
// By Ashris Choudhury
// =====================================
// LIGHT MODE EDITION - V7

#import "template.typ": *

#show: book-setup.with(is-dark: false)

// ============================================
// FRONT MATTER
// ============================================

// Cover with image
#image-cover-page("cover-light.png", is-dark: false)

// Table of Contents
#toc-page(is-dark: false, (
  (label: "Preface", title: "Preface", page: "4"),
  (label: "Introduction", title: "Introduction", page: "6"),
  (label: "Adhyaya 1", title: "The Descent", page: "9"),
  (label: "Adhyaya 2", title: "The Wound of Time", page: "14"),
  (label: "Adhyaya 3", title: "The Fire on Your Own Soil", page: "22"),
  (label: "Adhyaya 4", title: "The Estranged Cousins", page: "31"),
  (label: "Adhyaya 5", title: "On Karma and the Instant Rebirth", page: "38"),
  (label: "Adhyaya 6", title: "On Sincerity and the Culture of Hiding", page: "46"),
  (label: "Adhyaya 7", title: "On Love, Loss, and Consciousness", page: "54"),
  (label: "Adhyaya 8", title: "On Excellence and the Fruit of Action", page: "65"),
  (label: "Adhyaya 9", title: "On Death, Beauty, and the Shape of a Life", page: "73"),
  (label: "Adhyaya 10", title: "On Joy and the Soma of Living", page: "80"),
  (label: "Adhyaya 11", title: "On Power and the Responsibility of the Strong", page: "87"),
  (label: "Adhyaya 12", title: "The Question", page: "94"),
  (label: "Afterword", title: "On the Society Indra Imagines", page: "102"),
  (label: "Glossary", title: "Glossary", page: "105"),
))

// Half-title page
#set page(header: none, footer: none)
#v(4cm)
#align(center)[
  #text(size: 14pt, fill: light-primary, weight: "medium")[What Indra Taught Krishna]
  #v(1cm)
  #text(style: "italic", size: 10pt)[By Ashris Choudhury]
]
#pagebreak()

// ============================================
// MAIN CONTENT
// ============================================

// Preface
#include "chapters/02-preface.typ"

// Introduction
#include "chapters/03-introduction.typ"

// Adhyaya 1: The Descent
#include "chapters/04-adhyaya-01.typ"

// Adhyaya 2: The Wound of Time
#include "chapters/05-adhyaya-02.typ"

// Adhyaya 3: The Fire on Your Own Soil
#include "chapters/06-adhyaya-03.typ"

// Adhyaya 4: The Estranged Cousins
#include "chapters/07-adhyaya-04.typ"

// Adhyaya 5: On Karma and the Instant Rebirth
#include "chapters/08-adhyaya-05.typ"

// Adhyaya 6: On Sincerity and the Culture of Hiding
#include "chapters/09-adhyaya-06.typ"

// Adhyaya 7: On Love, Loss, and the Nature of Consciousness
#include "chapters/10-adhyaya-07.typ"

// Adhyaya 8: On Excellence and the Fruit of Action
#include "chapters/11-adhyaya-08.typ"

// Adhyaya 9: On Death, Beauty, and the Shape of a Life
#include "chapters/12-adhyaya-09.typ"

// Adhyaya 10: On Joy and the Soma of Living
#include "chapters/13-adhyaya-10.typ"

// Adhyaya 11: On Power and the Responsibility of the Strong
#include "chapters/14-adhyaya-11.typ"

// Adhyaya 12: The Question
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
    By Ashris Choudhury \
    First Edition, 2026
  ]
]
#v(2cm)
