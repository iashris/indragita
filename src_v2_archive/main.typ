// Indragita: What Indra Taught Krishna
// By Ashris Choudhury
// =====================================

#import "template.typ": *

#show: book-setup

// ============================================
// FRONT MATTER
// ============================================

// Cover
#cover-page()

// Table of Contents
#toc-page((
  (label: "Preface", title: "Preface", page: "4"),
  (label: "Introduction", title: "Introduction", page: "6"),
  (label: "Adhyaya 1", title: "The Descent", page: "9"),
  (label: "Adhyaya 2", title: "The Worlds Beyond", page: "13"),
  (label: "Adhyaya 3", title: "On Karma and the Instant Rebirth", page: "17"),
  (label: "Adhyaya 4", title: "On Sincerity and the Culture of Hiding", page: "20"),
  (label: "Adhyaya 5", title: "On Love, Loss, and the Nature of Consciousness", page: "24"),
  (label: "Adhyaya 6", title: "On Excellence and the Fruit of Action", page: "28"),
  (label: "Adhyaya 7", title: "On Death, Beauty, and the Shape of a Life", page: "31"),
  (label: "Adhyaya 8", title: "On Joy and the Soma of Living", page: "34"),
  (label: "Adhyaya 9", title: "On Power and the Responsibility of the Strong", page: "36"),
  (label: "Adhyaya 10", title: "The Question", page: "39"),
  (label: "Afterword", title: "On the Society Indra Imagines", page: "42"),
  (label: "Glossary", title: "Glossary", page: "44"),
))

// Half-title page
#set page(header: none, footer: none)
#v(4cm)
#align(center)[
  #text(size: 14pt, fill: primary-color, weight: "medium")[What Indra Taught Krishna]
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

// Adhyaya 2: The Worlds Beyond
#include "chapters/05-adhyaya-02.typ"

// Adhyaya 3: On Karma and the Instant Rebirth
#include "chapters/06-adhyaya-03.typ"

// Adhyaya 4: On Sincerity and the Culture of Hiding
#include "chapters/07-adhyaya-04.typ"

// Adhyaya 5: On Love, Loss, and the Nature of Consciousness
#include "chapters/08-adhyaya-05.typ"

// Adhyaya 6: On Excellence and the Fruit of Action
#include "chapters/09-adhyaya-06.typ"

// Adhyaya 7: On Death, Beauty, and the Shape of a Life
#include "chapters/10-adhyaya-07.typ"

// Adhyaya 8: On Joy and the Soma of Living
#include "chapters/11-adhyaya-08.typ"

// Adhyaya 9: On Power and the Responsibility of the Strong
#include "chapters/12-adhyaya-09.typ"

// Adhyaya 10: The Question
#include "chapters/13-adhyaya-10.typ"

// Afterword
#include "chapters/14-afterword.typ"

// Glossary
#include "chapters/15-glossary.typ"

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
