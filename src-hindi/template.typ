// Indragita Book Template - Hindi Edition
// ========================================
// इंद्रगीता - हिंदी संस्करण
// Supports Devanagari script with elegant typography

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

// Book metadata
#let book-title = "इंद्रगीता"
#let book-subtitle = "इंद्र ने कृष्ण को क्या सिखाया"
#let author = "आश्रिस चौधरी"
#let year = "२०२६"

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
    author: "Ashris Choudhury",
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

  // Hindi/Devanagari fonts
  // Body: Elegant Devanagari serif
  // Headings: Clean Devanagari sans
  // HYPHENATION OFF
  set text(
    font: ("Kohinoor Devanagari", "Noto Serif Devanagari", "Devanagari MT", "Noto Sans Devanagari"),
    size: 11pt,
    fill: txt,
    hyphenate: false,
    lang: "hi",
  )

  set par(
    justify: true,
    leading: 0.85em,
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
    set text(size: 9pt, fill: muted)
    set par(hanging-indent: 1em)
    super[#num]
    h(0.3em)
    it.note.body
  }

  // Heading styling
  show heading.where(level: 1): set text(fill: primary, weight: "bold")
  show heading.where(level: 2): set text(fill: primary, weight: "bold", size: 13pt)

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
      size: 11pt,
      tracking: 0.2em,
      weight: "medium",
      fill: muted,
    )[आश्रिस चौधरी]
  ]

  v(1.5cm)

  align(center)[
    #text(
      size: 52pt,
      weight: "bold",
      fill: primary,
      tracking: 0.1em,
    )[इंद्र]
    #v(-0.3cm)
    #text(
      size: 52pt,
      weight: "bold",
      fill: primary,
      tracking: 0.1em,
    )[गीता]
  ]

  v(1.5cm)

  align(center)[
    #text(
      size: 10pt,
      tracking: 0.15em,
      weight: "medium",
      fill: muted,
    )[इंद्र ने कृष्ण को क्या सिखाया]
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
    tracking: 0.1em,
  )[विषय-सूची]

  v(2cm)

  set text(size: 10pt, fill: txt)

  block(breakable: false)[
    #for entry in entries {
      grid(
        columns: (3cm, 1fr, 1cm),
        column-gutter: 0.5em,
        row-gutter: 0.3em,
        text(weight: "semibold", size: 8pt, fill: muted)[#entry.label],
        text(fill: txt, size: 10pt)[#entry.title],
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
        size: 24pt,
        weight: "bold",
        fill: primary,
        tracking: 0.1em,
      )[#label]
      v(0.4cm)
      text(
        size: 17pt,
        weight: "medium",
        fill: primary,
      )[#title]
    } else {
      text(
        size: 28pt,
        weight: "bold",
        fill: primary,
        tracking: 0.1em,
      )[#label]
    }
  }

  v(2cm)
}

// Adhyaya (chapter) title
#let adhyaya(num, title) = {
  chapter-title([अध्याय #num:], title)
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
      size: 12pt,
      weight: "semibold",
      fill: primary,
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
      size: 10pt,
    )[#name:]
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
      #text(fill: primary, weight: "bold")[—] #content
    ]
  }
}

#let bullet-bold(term, desc) = {
  context {
    let is-dark = dark-mode.get()
    let primary = if is-dark { dark-primary } else { light-primary }
    par(hanging-indent: 1em, first-line-indent: 0em)[
      #text(fill: primary, weight: "bold")[—] #strong[#term]: #desc
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
      #h(1em)— #definition
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
