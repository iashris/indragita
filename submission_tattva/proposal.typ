// Indragita - Penguin Tattva Submission Proposal
// Designed in the visual register of the manuscript itself

#let primary = rgb("#D96D4B")
#let text-color = rgb("#2D2D2D")
#let muted = rgb("#666666")
#let rule-color = rgb("#E5DDD3")

#let body-font = ("Palatino", "Times New Roman", "Georgia", "Charter", "Baskerville")
#let display-font = ("Avenir Next", "Avenir", "Futura", "Helvetica Neue")

#set document(title: "Indragita - Book Proposal", author: "Ashris Choudhury")

#set page(
  paper: "a4",
  margin: (top: 2.4cm, bottom: 2.4cm, left: 2.6cm, right: 2.6cm),
  footer: context [
    #set text(size: 8pt, fill: muted, font: display-font)
    #grid(
      columns: (1fr, auto, 1fr),
      align: (left, center, right),
      [Indragita], [#counter(page).display()], [Penguin Tattva Submission],
    )
  ],
)

#set text(font: body-font, size: 10.5pt, fill: text-color, hyphenate: false)
#set par(justify: false, leading: 0.72em, first-line-indent: 0pt, spacing: 0.85em)

// Heading styles
#show heading.where(level: 1): it => {
  set text(font: display-font, fill: primary, weight: "medium", size: 18pt, tracking: 0.05em)
  v(0.4em)
  it.body
  v(0.2em)
  line(length: 100%, stroke: 0.6pt + primary)
  v(0.6em)
}

#show heading.where(level: 2): it => {
  v(1.2em)
  set text(font: display-font, fill: primary, weight: "medium", size: 12pt, tracking: 0.04em)
  upper(it.body)
  v(0.4em)
}

#show heading.where(level: 3): it => {
  v(0.8em)
  set text(font: body-font, fill: text-color, weight: "bold", size: 11pt, style: "italic")
  it.body
  v(0.1em)
}

// List styling
#set list(indent: 0.6em, body-indent: 0.5em, marker: ([•], [◦]))
#set enum(indent: 0.6em, body-indent: 0.5em)

// Emphasis - keep italics in body color
#show emph: set text(fill: text-color)

// =====================================================
// TITLE PAGE
// =====================================================

#v(2cm)

#align(left)[
  #text(font: display-font, size: 9pt, fill: muted, tracking: 0.3em)[BOOK PROPOSAL]
]

#v(1.5cm)

#align(left)[
  #text(font: display-font, size: 42pt, fill: primary, weight: "medium", tracking: 0.04em)[Indragita]
]

#v(0.4cm)

#align(left)[
  #text(font: display-font, size: 18pt, fill: primary, weight: "regular")[What Indra Taught Krishna]
]

#v(1.2cm)

#align(left)[
  #text(size: 11pt, style: "italic", fill: text-color)[
    A Philosophical Dialogue
  ] \
  #v(0.1cm)
  #text(size: 10pt, fill: muted, style: "italic")[
    Drawn from the Rigveda, the Mahabharata, the Upanishads, and the Bhagavad Gita
  ]
]

#v(2cm)

#align(left)[
  #text(size: 10pt)[
    By *Ashris Choudhury* \
    #text(fill: muted)[Creator, India in Pixels] \
    #v(0.5em)
    #text(fill: muted, size: 9.5pt)[Manuscript complete - approx. 40,000 words - 12 adhyayas]
  ]
]

#v(1fr)

#line(length: 100%, stroke: 0.6pt + primary)

#v(0.4cm)

#align(left)[
  #text(font: display-font, size: 9pt, fill: muted, tracking: 0.15em)[
    SUBMITTED TO PENGUIN TATTVA \
    #v(0.2em)
    SHIVANI PANDEY, EDITOR
  ]
]

#pagebreak()

// =====================================================
// THE BOOK IN ONE PAGE
// =====================================================

= 1. The Book in One Page

*Indragita: What Indra Taught Krishna* is a philosophical dialogue, set at the close of the Dvapara Yuga, between Indra, the king of the Devas, and Krishna in the last hours before the hunter Jara's arrow ends his avatar. Across twelve adhyayas, the two figures speak about the long arc of the Gita's reception, about the older Vedic strand of agency and engagement that Indra represents, and about how the two together can shape a fuller philosophical inheritance for the modern Indian reader.

The book belongs to the same lineage as the Gita itself: a philosophical dialogue embedded in a mythic setting. Its closest formal cousins are the Upanishadic samvadas (Yajnavalkya and Gargi, Uddalaka and Svetaketu) and the Platonic dialogues. It is non-fiction philosophical literature in the Indian dialogic tradition, drawing throughout on primary scripture: the Rigveda for its portrait of Indra, the Mahabharata and Bhagavata Purana for the setting of Krishna's last hours, the Upanishads and the Karma Kanda for its treatment of desire and action, and the Bhagavad Gita as the text whose teachings the dialogue meets and complements.

The argument the book makes, in one sentence: there is a strand of Indian philosophical tradition, older than the literature of renunciation and equally Vedic, that affirms agency, owned desire, and full-hearted engagement with the world; and the householder, the builder, the artist, and the parent of our own century deserve to hear it again.

The dialogue does not refute the Gita. It ends with Krishna and Indra parting as brothers who serve different children.

= 2. The Form

The Gita is a dialogue. The Upanishads are dialogues. Yajnavalkya speaks with Gargi in the court of Janaka. Uddalaka teaches Svetaketu in nine answers. The Buddha speaks with his questioners. Adi Shankara debates Mandana Mishra. Every age of Indian philosophy that mattered to us produced its own conversation, in its own voice, and added a room to the house we still live in.

*Indragita* is offered in that same form. It is a single sustained conversation, broken into twelve adhyayas, each on a distinct philosophical theme. It uses the formal devices of the older dialogue tradition: speakers named in the script, action and stage descriptions in the manner of the Mahabharata's narrative passages, footnotes for terms drawn from the Sanskrit, and a glossary at the end.

Crucially, this form lets the book do something direct exposition cannot: it lets two opposed positions sit in the same room, listen to one another, and end as friends. The reader is not told who is right. The reader is given the conversation and trusted to inherit it.

#pagebreak()

= 3. Structure

#v(0.4em)

#let toc-row(label, title) = (
  text(font: display-font, size: 9pt, fill: primary, weight: "medium", tracking: 0.04em)[#upper(label)],
  text(size: 10pt)[#title],
)

#table(
  columns: (4cm, 1fr),
  align: (left, left),
  stroke: none,
  inset: (x: 0pt, y: 6pt),
  ..toc-row("Preface", "The author's framing of the book and its lineage"),
  ..toc-row("Introduction", "The setting, the philosophical stakes, and a note on Indra"),
  ..toc-row("Adhyaya 1", "The Descent. Indra arrives at Prabhasa"),
  ..toc-row("Adhyaya 2", "The Wound of Time. What later ages did with Krishna's teaching"),
  ..toc-row("Adhyaya 3", "The Fire on Your Own Soil. The Vedic ethic of engagement"),
  ..toc-row("Adhyaya 4", "The Estranged Cousins. Indra and Krishna's shared lineage"),
  ..toc-row("Adhyaya 5", "On Karma and the Instant Rebirth. Karma as mechanism, not destiny"),
  ..toc-row("Adhyaya 6", "On Sincerity and the Culture of Hiding. The gap between word and act"),
  ..toc-row("Adhyaya 7", "On Love, Loss, and Consciousness. Fierce attachment as a path"),
  ..toc-row("Adhyaya 8", "On Excellence and the Fruit of Action. Re-reading nishkama karma"),
  ..toc-row("Adhyaya 9", "On Death, Beauty, and the Shape of a Life. The householder's measure"),
  ..toc-row("Adhyaya 10", "On Joy and the Soma of Living. Celebration as a sacred act"),
  ..toc-row("Adhyaya 11", "On Power and the Responsibility of the Strong. The kshatriya's burden"),
  ..toc-row("Adhyaya 12", "The Question. The parting bargain, and Krishna walks toward the arrow"),
  ..toc-row("Afterword", "On the Society Indra Imagines"),
  ..toc-row("Glossary", "Sanskrit terms and Vedic / Mahabharatan references"),
)

#pagebreak()

= 4. Why this Book Belongs at Tattva

Penguin Tattva's stated mandate is to publish books rooted in Indian spiritual and philosophical traditions, made resonant for the modern reader, with clarity and depth, in editions that match the seriousness of the texts in their visual and editorial care.

*Indragita* is, by its nature, a Tattva book.

#v(0.4em)

#let principle(title, body) = block(below: 0.9em)[
  #text(font: display-font, size: 9.5pt, fill: primary, weight: "medium", tracking: 0.05em)[#upper(title)] \
  #v(0.1em)
  #text(size: 10pt)[#body]
]

#principle("Rooted in scripture", [Every philosophical move the book makes is anchored in primary text: the Rigveda's hymns to Indra, the Mahabharata's account of Krishna's last hours, the Upanishadic dialogue tradition, the householder ethics of the Dharmashastras, the Bhagavad Gita itself.])

#principle("Accessible to the modern reader", [The form is conversational. The language is plain English, with Sanskrit terms introduced and glossed. No prior knowledge of Vedic philosophy is required. A reader meeting the Gita for the first time can read this beside it and understand both more fully.])

#principle("Forward-looking, not iconoclastic", [The book does not break with tradition. It extends it. It puts back into circulation a strand of the Vedic inheritance, the Indra-strand of action and engagement, that has been quieter in the popular telling but is just as authentically ours.])

#principle("Visually finished", [The manuscript is fully typeset and designed in three editions (light, dark, and a print-ready dark-cover/light-interior version) using a custom Typst template. The author would expect to work closely with Tattva's design team for the published edition, but the existing design demonstrates the visual register the book is reaching for.])

#principle("Two-track ready", [#emph[Indragita] sits naturally in Tattva's "simplified editions for Gen Z and the spiritual explorer" track, with potential later for a collector's edition that pairs it with selected Rigvedic hymns and Mahabharatan source passages.])

= 5. The Reader

The book is written for several overlapping audiences, all of whom are visible in Tattva's stated readership:

- *The young Indian reader (20-35) who has read or heard the Gita* and felt that, for all its depth, something in their own life - their ambition, their love, their grief, their wanting to build something in the world - has not yet been addressed by it. They are looking for a philosophical vocabulary that affirms engagement, not only renunciation.

- *The builder, founder, artist, professional, parent.* The reader for whom #emph[karma yoga] is a lived question, not an academic one. The reader who wants to know what their tradition has to say about ambition, sincerity, fierce love, and the carrying of consequences.

- *The general reader of modern Indic non-fiction.* Readers who have moved through Devdutt Pattanaik, Sanjeev Sanyal, Amartya Sen on argumentative India, Sheldon Pollock, Wendy Doniger, Bibek Debroy's translations. #emph[Indragita] meets them at the level of seriousness they expect, while opening a register (the philosophical dialogue) that is currently underrepresented on the modern Indic shelf.

- *The collector* of beautifully made books on Indian thought. The Tattva reader who buys the Gita Press edition, the Penguin Black Classics, the Aleph hardcovers, and would value a designed companion text in the same register.

The book is also designed to be read by readers in Mumbai and Gorakhpur with equal access. The English is plain. The Sanskrit terms are introduced gently. The form is the form our tradition has always trusted: two people talking.

#pagebreak()

= 6. The Market

The Indian non-fiction market in spirituality and philosophy is large, growing, and currently dominated either by traditional commentaries (Gita Press, Chinmaya, Iskcon) or by contemporary popular re-tellings (Pattanaik, Amish on the mythic side; Sadhguru, Jaggi Vasudev, Gaur Gopal Das on the spiritual instruction side).

What is comparatively rare is the *textually grounded, accessible, modern philosophical dialogue* in the Indic tradition. Tattva itself is being built precisely to occupy this gap.

== Comparable Titles

For shelf placement and audience overlap, not as direct equivalents.

#let comp(name, works, note) = block(below: 0.7em)[
  *#name.* #text(style: "italic", fill: muted)[#works] \
  #v(0.05em)
  #text(size: 9.5pt)[#note]
]

#comp(
  "Devdutt Pattanaik",
  "Jaya, My Gita, The Pregnant King",
  [Closest in audience and accessibility. #emph[Indragita] differs in form (sustained dialogue rather than retelling) and in argument (a single, focused philosophical case).],
)

#comp(
  "Amish Tripathi",
  "Immortal India, The Liberation of Sita",
  [Overlapping readership of mythic-philosophical non-fiction.],
)

#comp(
  "Sanjeev Sanyal",
  "The Ocean of Churn, Land of the Seven Rivers",
  [Audience overlap among readers of civilisational non-fiction; the #emph[India in Pixels] viewership is heavily co-extensive with this readership.],
)

#comp(
  "Eknath Easwaran / Stephen Mitchell",
  "The Bhagavad Gita for Daily Living, Bhagavad Gita",
  [Comparable in accessibility and tone, though those are translations.],
)

#comp(
  "Sheldon Pollock and the Murty Classical Library",
  "A Rasa Reader",
  [The collector-grade end of the audience.],
)

#comp(
  "Internationally",
  "Stephen Greenblatt's The Swerve, Robert Wright's Why Buddhism is True, Anthony de Mello's dialogues",
  [Reference points for the kind of accessible philosophical book this is.],
)

#v(0.6em)

The platform behind the book (700,000+ subscribers on a research-driven Indic civilisation channel, a growing podcast presence) gives Tattva an unusually large warm-launch audience for a debut philosophical non-fiction title.

#pagebreak()

= 7. The Author

*Ashris Choudhury* is the creator of #emph[India in Pixels], a YouTube channel with over 700,000 subscribers that produces research-driven Hinglish video essays on Indian civilisation, Vedic literature, and comparative mythology. His four-part Vedas series, covering the Rigveda, Atharvaveda, Yajurveda, and Samaveda, was built from primary Sanskrit scholarship and is among the most-watched English-language treatments of the Vedas online.

He recently appeared on #emph[The Ranveer Show], one of India's largest English-language podcasts; the episode performed well enough that a second has been commissioned. The connection that brought #emph[Indragita] to Tattva began with that episode.

He holds a B.Tech from IIT Kharagpur and a Master's from the MIT Media Lab. He lives and writes in Jharsuguda, Odisha.

His broader project, both on screen and on the page, is to make the primary-source seriousness of Indic scholarship available to readers in their own register, in their own time, without dilution and without academic gatekeeping. #emph[Indragita] is the first book-length expression of that project.

= 8. The Author Platform

#let platform-row(label, body) = (
  text(font: display-font, size: 9pt, fill: primary, weight: "medium", tracking: 0.05em)[#upper(label)],
  text(size: 10pt)[#body],
)

#table(
  columns: (3.6cm, 1fr),
  align: (left, left),
  stroke: none,
  inset: (x: 0pt, y: 5pt),
  ..platform-row("YouTube", [#emph[India in Pixels], 700,000+ subscribers. Audience skews 18-35, urban and tier-2/3 Indian readers, with strong interest in civilisational non-fiction, primary-source scholarship, and Indic philosophy. Average video views in the hundreds of thousands.]),
  ..platform-row("Podcast", [Recent feature on #emph[The Ranveer Show.] Second episode commissioned. Open conversations with several other major Indian podcasts.]),
  ..platform-row("Prior release", [#emph[Indragita] was previously made available in self-published form on Gumroad and Kindle Direct Publishing. Initial reader response was strong; readers asked for a print edition. Penguin Tattva is the first traditional publisher being approached for the formal first edition.]),
  ..platform-row("Launch reach", [A coordinated launch through #emph[India in Pixels], the next #emph[Ranveer Show] episode, and a podcast tour can reasonably be expected to put the book in front of well over a million potential readers in its first month.]),
)

= 9. Editorial Notes

- The manuscript is *finished and designed*. It is ready for editorial review in its current form. The author is open to and expects substantive editorial collaboration.

- The *visual treatment* is part of the reading. The book has been typeset with care in three editions. The author would value working with Tattva's design team to bring this into the imprint's house style without losing the typographic qualities that distinguish a designed philosophical text from a generic trade paperback.

- A potential *collector's edition.* If commercially attractive to Tattva, the manuscript can be paired in a later edition with selected Rigvedic hymns to Indra (in Sanskrit and translation) and key passages from the Mahabharata's account of Krishna's last hours, as a deluxe companion volume in the Tattva collector's track.

- A *Hindi edition* of an earlier draft has already been produced in working form. A full Hindi translation, prepared in conversation with Tattva, would significantly extend the book's reach to the readership the imprint is built to serve.

= 10. Sample Reading Order

For the first read of the manuscript, the author recommends:

+ Preface
+ Introduction
+ Adhyaya 1, #emph[The Descent]
+ Adhyaya 5, #emph[On Karma and the Instant Rebirth] - the cleanest single statement of the book's central re-reading
+ Adhyaya 12, #emph[The Question] - the parting bargain between Krishna and Indra
+ Afterword

This sequence, around fifty pages, gives the editor the form, the argument, and the resolution. The remaining adhyayas extend the dialogue thematically and can be read in order thereafter. The accompanying *sample pack* contains exactly this reading.

#v(2cm)

#line(length: 30%, stroke: 0.5pt + primary)

#v(0.4cm)

#text(size: 9pt, style: "italic", fill: muted)[
  Submitted with gratitude to Shivani Pandey and Penguin Tattva. \
  Ashris Choudhury, 2026.
]
