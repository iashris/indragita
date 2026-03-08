// Indragita Book Template
// ========================
// An elegant, book-quality template for philosophical dialogue
// Supports both light and dark modes

// ============================================
// COLOR SCHEMES
// ============================================

// Light mode (default)
#let light-bg = white
#let light-primary = rgb("#D96D4B")      // Warm coral/terracotta
#let light-text = rgb("#2D2D2D")
#let light-muted = rgb("#666666")

// Dark mode - Night sky with golden fire
#let dark-bg = rgb("#0D1117")            // Deep night sky
#let dark-primary = rgb("#D4A853")        // Indra's gold/lightning
#let dark-text = rgb("#E6DCC8")           // Warm cream
#let dark-muted = rgb("#9CA3AF")          // Muted silver

// Active color scheme (set by dark-mode variable)
#let dark-mode = state("dark-mode", false)

#let get-bg() = context { if dark-mode.get() { dark-bg } else { light-bg } }
#let get-primary() = context { if dark-mode.get() { dark-primary } else { light-primary } }
#let get-text() = context { if dark-mode.get() { dark-text } else { light-text } }
#let get-muted() = context { if dark-mode.get() { dark-muted } else { light-muted } }

// Static colors for immediate use (will be overridden in setup)
#let primary-color = light-primary
#let text-color = light-text
#let light-text = light-muted
#let bg-color = light-bg

// Book metadata
#let book-title = "INDRAGITA"
#let book-subtitle = "What Indra Taught Krishna"
#let author = "Ashris Choudhury"
#let year = "2026"

// ============================================
// BOOK SETUP
// ============================================
#let book-setup(is-dark: false, doc) = {
  // Set the mode
  dark-mode.update(is-dark)

  // Define colors based on mode
  let bg = if is-dark { dark-bg } else { light-bg }
  let primary = if is-dark { dark-primary } else { light-primary }
  let txt = if is-dark { dark-text } else { light-text }
  let muted = if is-dark { dark-muted } else { light-muted }
  let separator-color = if is-dark { rgb("#3D4450") } else { luma(180) }

  set document(
    title: book-title,
    author: author,
  )

  set page(
    paper: "a5",
    fill: bg,
    margin: (
      top: 2cm,
      bottom: 2.5cm,
      inside: 2.2cm,
      outside: 1.8cm,
    ),
  )

  // Modern yet ancient fonts - 2026 Indraprastha aesthetic
  // Body: refined serif for readability
  // Headings: geometric sans for modernity
  // HYPHENATION OFF - prevents broken artifacts like "con￾sciousness"
  set text(
    font: ("Palatino", "Times New Roman", "Georgia", "Charter", "Baskerville"),
    size: 10pt,
    fill: txt,
    hyphenate: false,
  )

  set par(
    justify: true,
    leading: 0.78em,
  )

  // Prevent widow/orphan lines
  set block(breakable: true)
  show heading: set block(breakable: false, above: 1.5em, below: 0.8em)

  // Footnote styling
  set footnote.entry(
    separator: line(length: 30%, stroke: 0.5pt + separator-color),
    indent: 0em,
    gap: 0.5em,
  )

  show footnote.entry: it => {
    let loc = it.note.location()
    let num = counter(footnote).at(loc).first()
    set text(size: 8pt, fill: muted)
    set par(hanging-indent: 1em)
    super[#num]
    h(0.3em)
    it.note.body
  }

  // Heading styling
  show heading.where(level: 1): set text(fill: primary, weight: "bold")
  show heading.where(level: 2): set text(fill: primary, weight: "bold", size: 12pt)

  // Emphasis styling for dark mode visibility
  show emph: set text(fill: if is-dark { rgb("#F0E6D2") } else { txt })

  doc
}

// ============================================
// COVER PAGE
// ============================================
#let cover-page(is-dark: false) = {
  let bg = if is-dark { dark-bg } else { light-bg }
  let primary = if is-dark { dark-primary } else { light-primary }
  let muted = if is-dark { dark-muted } else { light-muted }

  set page(header: none, footer: none, margin: (x: 2cm, y: 2cm), fill: bg)

  v(4fr)

  align(center)[
    #text(
      size: 10pt,
      tracking: 0.3em,
      weight: "medium",
      fill: muted,
      font: ("Avenir Next", "Avenir", "Futura", "Helvetica Neue")
    )[#upper[#author]]
  ]

  v(1.5cm)

  align(center)[
    #text(
      size: 48pt,
      weight: "bold",
      fill: primary,
      tracking: 0.2em,
      font: ("Avenir Next", "Avenir", "Futura", "Helvetica Neue")
    )[INDRA]
    #v(-0.2cm)
    #text(
      size: 48pt,
      weight: "bold",
      fill: primary,
      tracking: 0.2em,
      font: ("Avenir Next", "Avenir", "Futura", "Helvetica Neue")
    )[GITA]
  ]

  v(1.5cm)

  align(center)[
    #text(
      size: 9pt,
      tracking: 0.25em,
      weight: "medium",
      fill: muted,
      font: ("Avenir Next", "Avenir", "Futura", "Helvetica Neue")
    )[#upper[What Indra Taught Krishna]]
  ]

  if is-dark {
    v(3cm)
    align(center)[
      #text(fill: primary, size: 24pt)[⚡]
    ]
    v(2fr)
  } else {
    v(5fr)
  }

  pagebreak()
}

// ============================================
// TABLE OF CONTENTS
// ============================================
#let toc-page(entries, is-dark: false) = {
  let bg = if is-dark { dark-bg } else { light-bg }
  let primary = if is-dark { dark-primary } else { light-primary }
  let txt = if is-dark { dark-text } else { light-text }
  let muted = if is-dark { dark-muted } else { light-muted }

  set page(header: none, footer: none, fill: bg)

  v(1.5cm)

  text(
    size: 32pt,
    weight: "bold",
    fill: primary,
    tracking: 0.15em,
    font: ("Avenir Next", "Avenir", "Futura", "Helvetica Neue")
  )[CONTENTS]

  v(2cm)

  set text(size: 9pt, fill: txt)

  // Keep all TOC entries together
  block(breakable: false)[
    #for entry in entries {
      grid(
        columns: (2.8cm, 1fr, 1cm),
        column-gutter: 0.5em,
        row-gutter: 0.3em,
        text(weight: "semibold", size: 7.5pt, tracking: 0.08em, fill: muted, font: ("Avenir Next", "Avenir", "Futura"))[#upper[#entry.label]],
        text(fill: txt, size: 9pt)[#entry.title],
        align(right)[#text(fill: primary, weight: "bold")[#entry.page]],
      )
      v(0.5em)
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

  context {
    let is-dark = dark-mode.get()
    let primary = if is-dark { dark-primary } else { light-primary }

    if title != none and title != [] {
      text(
        size: 22pt,
        weight: "bold",
        fill: primary,
        tracking: 0.15em,
        font: ("Avenir Next", "Avenir", "Futura", "Helvetica Neue")
      )[#upper[#label]]
      v(0.4cm)
      text(
        size: 16pt,
        weight: "medium",
        fill: primary,
        tracking: 0.05em,
        font: ("Avenir Next", "Avenir", "Futura", "Helvetica Neue")
      )[#title]
    } else {
      text(
        size: 26pt,
        weight: "bold",
        fill: primary,
        tracking: 0.15em,
        font: ("Avenir Next", "Avenir", "Futura", "Helvetica Neue")
      )[#upper[#label]]
    }
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
  context {
    let is-dark = dark-mode.get()
    let primary = if is-dark { dark-primary } else { light-primary }
    text(
      size: 11pt,
      weight: "semibold",
      fill: primary,
      tracking: 0.03em,
      font: ("Avenir Next", "Avenir", "Futura", "Helvetica Neue")
    )[#title]
  }
  v(0.8em)
}

// ============================================
// DIALOGUE FORMATTING
// ============================================
#let speaker(name) = {
  v(1em)
  context {
    let is-dark = dark-mode.get()
    let primary = if is-dark { dark-primary } else { light-primary }
    text(
      weight: "bold",
      fill: primary,
      size: 9pt,
      tracking: 0.1em,
      font: ("Avenir Next", "Avenir", "Futura", "Helvetica Neue")
    )[#upper[#name]:]
  }
  h(0.5em)
}

// Stage direction (inline)
#let stage(content) = {
  context {
    let is-dark = dark-mode.get()
    let muted = if is-dark { dark-muted } else { rgb("#666666") }
    text(style: "italic", fill: muted)[(#content)]
  }
}

// Action/narrative description (block)
#let action(content) = {
  v(0.8em)
  context {
    let is-dark = dark-mode.get()
    let muted = if is-dark { dark-muted } else { rgb("#666666") }
    text(style: "italic", fill: muted)[#content]
  }
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
  context {
    let is-dark = dark-mode.get()
    let primary = if is-dark { dark-primary } else { light-primary }
    par(hanging-indent: 1em, first-line-indent: 0em)[
      #text(fill: primary, weight: "bold")[--] #content
    ]
  }
}

#let bullet-bold(term, desc) = {
  context {
    let is-dark = dark-mode.get()
    let primary = if is-dark { dark-primary } else { light-primary }
    par(hanging-indent: 1em, first-line-indent: 0em)[
      #text(fill: primary, weight: "bold")[--] #strong[#term]: #desc
    ]
  }
}

// ============================================
// GLOSSARY
// ============================================
#let gloss-term(term, definition) = {
  v(0.5em)
  context {
    let is-dark = dark-mode.get()
    let primary = if is-dark { dark-primary } else { light-primary }
    par(first-line-indent: 0em)[
      #text(weight: "bold", fill: primary)[#term]
      #linebreak()
      #h(1em)--- #definition
    ]
  }
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
