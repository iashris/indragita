// Indragita Book Template
// ========================
// An elegant, book-quality template for philosophical dialogue

// Color palette matching the original PDF
#let primary-color = rgb("#D96D4B")  // Warm coral/terracotta
#let text-color = rgb("#2D2D2D")
#let light-text = rgb("#666666")

// Book metadata
#let book-title = "INDRAGITA"
#let book-subtitle = "What Indra Taught Krishna"
#let author = "Ashris Choudhury"
#let year = "2026"

// ============================================
// BOOK SETUP
// ============================================
#let book-setup(doc) = {
  set document(
    title: book-title,
    author: author,
  )

  set page(
    paper: "a5",
    margin: (
      top: 2cm,
      bottom: 2.5cm,
      inside: 2.2cm,
      outside: 1.8cm,
    ),
  )

  // Use elegant book fonts (system-available)
  // Palatino and Georgia are excellent for book typography
  set text(
    font: ("Palatino", "Georgia", "Times New Roman"),
    size: 10pt,
    fill: text-color,
  )

  set par(
    justify: true,
    leading: 0.78em,
  )

  // Prevent widow/orphan lines (min 2 lines at page break)
  set block(breakable: true)
  show heading: set block(breakable: false, above: 1.5em, below: 0.8em)

  // Footnote styling
  set footnote.entry(
    separator: line(length: 30%, stroke: 0.5pt + luma(180)),
    indent: 0em,
    gap: 0.5em,
  )

  show footnote.entry: it => {
    let loc = it.note.location()
    let num = counter(footnote).at(loc).first()
    set text(size: 8pt, fill: light-text)
    set par(hanging-indent: 1em)
    super[#num]
    h(0.3em)
    it.note.body
  }

  // Heading styling
  show heading.where(level: 1): set text(fill: primary-color, weight: "bold")
  show heading.where(level: 2): set text(fill: primary-color, weight: "bold", size: 12pt)

  doc
}

// ============================================
// COVER PAGE
// ============================================
#let cover-page() = {
  set page(header: none, footer: none, margin: (x: 2cm, y: 2cm))

  v(4fr)

  align(center)[
    #text(
      size: 11pt,
      tracking: 0.25em,
      weight: "medium",
      font: ("Helvetica Neue", "Helvetica", "Arial")
    )[#upper[#author]]
  ]

  v(1.5cm)

  align(center)[
    #text(
      size: 52pt,
      weight: "bold",
      fill: primary-color,
      tracking: 0.02em,
      font: ("Georgia", "Palatino", "Times New Roman")
    )[INDRA]
    #v(-0.3cm)
    #text(
      size: 52pt,
      weight: "bold",
      fill: primary-color,
      tracking: 0.02em,
      font: ("Georgia", "Palatino", "Times New Roman")
    )[GITA]
  ]

  v(1.5cm)

  align(center)[
    #text(
      size: 10pt,
      tracking: 0.2em,
      weight: "medium",
      font: ("Helvetica Neue", "Helvetica", "Arial")
    )[#upper[What Indra Taught Krishna]]
  ]

  v(5fr)

  pagebreak()
}

// ============================================
// TABLE OF CONTENTS
// ============================================
#let toc-page(entries) = {
  set page(header: none, footer: none)

  v(1.5cm)

  text(
    size: 36pt,
    weight: "bold",
    fill: primary-color,
    tracking: 0.02em,
    font: ("Georgia", "Palatino", "Times New Roman")
  )[TABLE OF]
  linebreak()
  text(
    size: 36pt,
    weight: "bold",
    fill: primary-color,
    tracking: 0.02em,
    font: ("Georgia", "Palatino", "Times New Roman")
  )[CONTENTS]

  v(2cm)

  set text(size: 9.5pt)

  // Keep all TOC entries together to avoid orphaned last entry
  block(breakable: false)[
    #for entry in entries {
      grid(
        columns: (3.5cm, 1fr, auto),
        row-gutter: 0.6em,
        text(weight: "bold", size: 8.5pt)[#upper[#entry.label]],
        entry.title,
        text(fill: primary-color, weight: "bold")[#entry.page],
      )
      v(0.4em)
    }
  ]

  pagebreak()
}

// ============================================
// CHAPTER TITLE
// ============================================
#let chapter-title(label, title) = {
  pagebreak(weak: true)
  set page(header: none)

  v(3cm)

  if title != none and title != [] {
    text(
      size: 26pt,
      weight: "bold",
      fill: primary-color,
      tracking: 0.02em,
      font: ("Georgia", "Palatino", "Times New Roman")
    )[#upper[#label]]
    v(0.2cm)
    text(
      size: 22pt,
      weight: "bold",
      fill: primary-color,
      tracking: 0.01em,
      font: ("Georgia", "Palatino", "Times New Roman")
    )[#upper[#title]]
  } else {
    text(
      size: 30pt,
      weight: "bold",
      fill: primary-color,
      tracking: 0.02em,
      font: ("Georgia", "Palatino", "Times New Roman")
    )[#upper[#label]]
  }

  v(2cm)
}

// Adhyaya (chapter) title
#let adhyaya(num, title) = {
  chapter-title([Adhyaya #num:], title)
}

// ============================================
// SECTION HEADINGS
// ============================================
#let section-heading(title) = {
  v(1.5em)
  text(
    size: 12pt,
    weight: "bold",
    fill: primary-color,
    font: ("Georgia", "Palatino", "Times New Roman")
  )[#title]
  v(0.8em)
}

// ============================================
// DIALOGUE FORMATTING
// ============================================
#let speaker(name) = {
  v(1em)
  text(
    weight: "bold",
    fill: primary-color,
    size: 9.5pt,
    tracking: 0.05em,
    font: ("Helvetica Neue", "Helvetica", "Arial")
  )[#upper[#name]:]
  h(0.5em)
}

// Stage direction (inline)
#let stage(content) = {
  text(style: "italic")[(#content)]
}

// Action/narrative description (block)
#let action(content) = {
  v(0.8em)
  text(style: "italic")[#content]
  v(0.5em)
}

// ============================================
// INDENTED PARAGRAPH
// ============================================
#let indent-para(content) = {
  pad(left: 1em)[#content]
}

// ============================================
// LIST ITEMS
// ============================================
#let bullet(content) = {
  par(hanging-indent: 1em, first-line-indent: 0em)[
    #text(fill: primary-color, weight: "bold")[--] #content
  ]
}

#let bullet-bold(term, desc) = {
  par(hanging-indent: 1em, first-line-indent: 0em)[
    #text(fill: primary-color, weight: "bold")[--] #strong[#term]: #desc
  ]
}

// ============================================
// GLOSSARY
// ============================================
#let gloss-term(term, definition) = {
  v(0.5em)
  par(first-line-indent: 0em)[
    #text(weight: "bold", fill: primary-color)[#term]
    #linebreak()
    #h(1em)--- #definition
  ]
}

// ============================================
// BLOCK QUOTE
// ============================================
#let quote-block(content) = {
  v(0.5em)
  pad(left: 1.5em, right: 1em)[
    #text(style: "italic")[#content]
  ]
  v(0.5em)
}

// ============================================
// PAGE UTILITIES
// ============================================
#let new-page() = {
  pagebreak()
}
