// इंद्रगीता: इंद्र ने कृष्ण को क्या सिखाया
// Indragita: What Indra Taught Krishna
// Hindi Edition - हिंदी संस्करण
// By Ashris Choudhury / आश्रिस चौधरी
// =====================================

#import "template.typ": *

#show: book-setup.with(is-dark: false)

// ============================================
// FRONT MATTER
// ============================================

// Cover
#cover-page(is-dark: false)

// Table of Contents
#toc-page(is-dark: false, (
  (label: "प्राक्कथन", title: "प्राक्कथन", page: "४"),
  (label: "भूमिका", title: "भूमिका", page: "६"),
  (label: "अध्याय १", title: "अवतरण", page: "९"),
  (label: "अध्याय २", title: "परलोक", page: "१३"),
  (label: "अध्याय ३", title: "कर्म और तत्काल पुनर्जन्म", page: "१७"),
  (label: "अध्याय ४", title: "सच्चाई और छिपाव की संस्कृति", page: "२०"),
  (label: "अध्याय ५", title: "प्रेम, विछोह, और चेतना", page: "२४"),
  (label: "अध्याय ६", title: "उत्कृष्टता और कर्मफल", page: "२८"),
  (label: "अध्याय ७", title: "मृत्यु, सौंदर्य, और जीवन का आकार", page: "३१"),
  (label: "अध्याय ८", title: "आनंद और जीवन का सोम", page: "३४"),
  (label: "अध्याय ९", title: "शक्ति और बलवान का दायित्व", page: "३६"),
  (label: "अध्याय १०", title: "प्रश्न", page: "३९"),
  (label: "उपसंहार", title: "इंद्र की कल्पना का समाज", page: "४२"),
  (label: "शब्दावली", title: "शब्दावली", page: "४४"),
))

// Half-title page
#set page(header: none, footer: none, fill: light-bg)
#v(4cm)
#align(center)[
  #text(size: 15pt, fill: light-primary, weight: "medium")[इंद्र ने कृष्ण को क्या सिखाया]
  #v(1cm)
  #text(style: "italic", size: 11pt, fill: light-muted)[आश्रिस चौधरी]
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
#set page(header: none, fill: light-bg)
#v(1fr)
#align(center)[
  #text(style: "italic", size: 10pt, fill: light-muted)[
    इंद्रगीता: इंद्र ने कृष्ण को क्या सिखाया \
    आश्रिस चौधरी \
    प्रथम संस्करण, २०२६ \
  ]
]
#v(2cm)
