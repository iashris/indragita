#!/usr/bin/env python3
"""
Extract content from Indragita PDF and generate Typst chapter files.
Uses pdfplumber to extract text and structures it into chapters.
"""

import re
import os

# Since we can't easily install pdfplumber, let's use the content we have
# This script creates the chapter structure from the known content

CHAPTERS_DIR = "src/chapters"

# Chapter definitions with their content
CHAPTERS = {
    "03-introduction.typ": {
        "type": "chapter",
        "label": "Introduction",
        "title": None,
        "content": '''
#section-heading[The Setting]

It is the end of the Dvapara Yuga. The Mahabharata war has been fought and won. Eighteen akshauhinis of soldiers lie dead. The Pandavas rule a kingdom of ghosts.

And now the Yadavas---Krishna's own clan---have destroyed themselves at Prabhasa, drunk on wine, killing each other with iron clubs that grew from a sage's curse. The city of Dvaraka is sinking into the sea.

Krishna sits alone at the edge of the forest where it meets the ocean. He is waiting for a hunter named Jara, whose arrow will strike his foot and end his avatar. He has seen this death. He has allowed it.

This is where Indra comes.

Not in thunder. Not with the host of Maruts. He walks out of the tree line like a man approaching another man. Only his eyes hold the storm.

#section-heading[Why Indra?]

In the Bhagavata Purana, Krishna and Indra are adversaries. The young Krishna convinces the cowherds of Vrindavan to stop worshipping Indra and instead worship Govardhana Hill. Indra, enraged, sends storms to destroy them. Krishna lifts the mountain on his finger and shelters his people for seven days. Indra submits. He is "humbled."

But what if we read this differently?

What if Indra's submission was strategic patience? What if he looked at the long arc of what Krishna's philosophy would produce---millennia of performed detachment, civilizational passivity, sophisticated hypocrisy---and waited for the right moment to speak?

That moment is now. At the end of Krishna's life. After the fruits of his teaching have ripened.

#section-heading[The Philosophical Stakes]

The Bhagavad Gita teaches:

- *Nishkama karma*: Action without attachment to results
- *Anasakti*: Non-attachment to outcomes
- *Samatva*: Equanimity in pleasure and pain, victory and defeat
- *Atman as unchanging*: The self is eternal, beyond the body's drama
- *World as maya*: The material world is illusion; transcendence is the goal

The Indragita counters:

- *Sincere desire*: Own what you want, clearly and without shame
- *Karma as mechanism*: The past constrains but does not determine; identity can be rewritten instantly
- *The nobility of taking sides*: Choosing is what makes you real
- *Fierce attachment*: Love that risks loss is the only love worth having
- *The world as arena*: Real, consequential, worth engaging fully

This is not a refutation. It is an alternative. A path for those who find detachment philosophy producing not saints but sophisticated cowards.

#section-heading[A Note on Indra]

Indra in the Rigveda is not the diminished figure of the Puranas. He is the king of the gods, the slayer of Vritra, the one who releases the waters, drinks the soma, and delights in battle. He wants things. He takes sides. He wins, loses, and returns.

The Puranic tradition demoted him---made him jealous, insecure, constantly threatened by the austerities of mortals. This served a theological purpose: elevating the trimūrti (Brahma, Vishnu, Shiva) required diminishing the Vedic pantheon.

In this text, I restore the Rigvedic Indra. Not as literal history, but as philosophical archetype. The one who acts, desires, risks, and remains.
'''
    },
    "04-adhyaya-01.typ": {
        "type": "adhyaya",
        "num": 1,
        "title": "The Descent",
        "content": '''
At the edge of Prabhasa, where the forest meets the sea, Krishna sat alone. The Yadavas had slain each other. The city of Dvaraka was sinking. The age was turning.

#pad(left: 1em)[
He had known it would end this way. He had seen it, spoken it, allowed it.

The hunter's arrow would come soon. He was waiting for it the way one waits for a guest who is late but certain.

Instead, Indra came.
]

Not in thunder. Not with the host of Maruts. He came as a man comes to another man---walking out of the tree line, his footsteps making sound on the earth, his shadow falling in the ordinary way. Only his eyes held the storm.

#speaker[Indra]
You taught the world to let go. And now you sit here, letting go. I want to know if it feels the way you promised it would.

#speaker[Krishna]
You've come to gloat, Shakra? The one who sent storms against cowherds?

#speaker[Indra]
I came to ask a question. I'll only stay if you can bear to answer it honestly.

#speaker[Krishna]
#stage-direction[smiling]

Honesty. You think I've been dishonest?

#speaker[Indra]
I think you've been so clever that you've forgotten what honesty costs. You told Arjuna that the wise grieve neither for the living nor the dead. You told him the soul is eternal, the body is clothes, death is a change of garments.

#speaker[Krishna]
This is true.

#speaker[Indra]
And did Arjuna fight better for believing it? Or did he fight the way a man fights when he's been told it doesn't matter?

#speaker[Krishna]
He fought. He won. The war ended.

#speaker[Indra]
The war ended. Yes. I was there when Bhishma fell. I watched Arjuna's face. Do you know what I saw?

#speaker[Krishna]
Tell me.

#speaker[Indra]
Relief. Not victory. Not grief. Not even hatred fulfilled. Relief that it was over. That he could stop performing the thing you'd asked him to perform.

#speaker[Krishna]
You misread him.

#speaker[Indra]
I have killed more enemies than you have hairs on your body, Vasudeva. I know what a warrior's face looks like when he wins. That was not it.

#speaker[Krishna]
What would you have had me teach him? To slaughter his grandfather with joy? To laugh while cutting down his teachers?

#speaker[Indra]
I would have had you teach him to #emph[want] his victory. To own it. To say: I am killing Bhishma because I choose to, because the throne matters to me, because my brothers matter to me, because I refuse to live as a beggar when I was born a prince.

#speaker[Krishna]
And the sin of killing?

#speaker[Indra]
Let him carry it! Let him feel its weight! A man who kills and feels nothing is not liberated---he is broken. You taught him to pre-forgive himself by pretending he wasn't really the one doing it. That Time was the killer. That the selves were already dead.

#speaker[Krishna]
#stage-direction[quieter now]

It was a mercy.

#speaker[Indra]
It was a trick. And tricks produce tricksters. Tell me---in the ages since Kurukshetra, what has your teaching made? Saints? Or men who speak like saints while acting like wolves, and feel no conflict because they've learned your art of detachment?

#speaker[Krishna]
You want me to defend every misuse of wisdom? Should fire apologize because men burn villages?

#speaker[Indra]
No. Fire should not apologize. But you are not fire. You chose these words. You saw what they would become. You're the one who knows past, present, future---did you not see the hypocrisy your teaching would breed?

#speaker[Krishna]
#stage-direction[long pause]

I saw... that men needed a way to act in an impure world without being paralyzed by that impurity.

#speaker[Indra]
And I am telling you there is another way. A way that does not require a man to lie to himself about what he wants and what he's doing. I am telling you there is a path of sincerity, and it is harder than your path, but it does not rot from within.

#speaker[Krishna]
Then teach me, King of Heaven. You who lost your worshippers to a cowherd's rebellion. You whose throne shakes whenever a mortal's austerities grow too strong. Teach me about strength.

#speaker[Indra]
#stage-direction[sits down across from him]

I will. Because I have done what you have never done. I have wanted things, and failed to get them, and remained Indra. I did not console myself by saying I never really wanted them. I did not say desire is the enemy. I lost, and I wanted, and I kept wanting, and I tried again.

That is the teaching.
'''
    },
    "05-adhyaya-02.typ": {
        "type": "adhyaya",
        "num": 2,
        "title": "The Worlds Beyond",
        "content": '''
#speaker[Krishna]
You speak as if your way is proven. But where are your devotees, Shakra? The yajñas grow thin. The soma goes unoffered. Men turn to other gods---gentler gods. Perhaps they know something you don't.

#speaker[Indra]
#stage-direction[laughs]

You think I measure truth by headcount? By who burns more ghee in my name? That is the logic of a merchant, not a king.

Let me tell you what I have seen while you played your flute in Vrindavan.

#pad(left: 1em)[
I have walked in other worlds. Not the heavens---the earth, in places your Bharata does not touch. And I have seen what happens when men organize their lives around different truths.
]

#speaker[Krishna]
Other worlds? You mean the mlecchas? What can the barbarians teach?

#speaker[Indra]
#stage-direction[sharp]

This is the first disease your teaching breeds---the comfort of dismissal. "They are mlecchas, so I need not learn." Tell me, Dvarakadhisha---when Yavanas come with their phalanxes and their logic, will you dismiss them then? When Persians build fires to a single Lord of Wisdom, will you call them barbarians while they administer an empire a hundred times the size of Kuru?

#speaker[Krishna]
#stage-direction[quieter]

Speak, then. What have you seen?

#section-heading[On the Greeks]

#speaker[Indra]
West of the Sindhu, past the mountains where even your Pandavas did not walk, there is a people who live along an inland sea. They are quarrelsome. They fight amongst themselves constantly. Their cities war against their own kin.

And yet---listen to me---they have produced more clear thinking in three generations than your rishis produced in thirty.

#speaker[Krishna]
Bold claim.

#speaker[Indra]
There was a man among them called Aristotle. He asked: what is the purpose of a human life? Not how to escape it. Not how to transcend it. What is it #emph[for]?

#speaker[Krishna]
And his answer?

#speaker[Indra]
Eudaimonia. Flourishing. He said: a life is good when it fulfills its function excellently. An eye is good when it sees well. A knife is good when it cuts well. A man is good when he lives well---with courage, with justice, with practical wisdom, with proper pride.

Notice what is missing from his teaching, Keshava.

#speaker[Krishna]
Detachment.

#speaker[Indra]
Detachment. Liberation. Escape. He did not teach men to flee from the game---he taught them to win it. To play it beautifully. His student conquered the world from Macedon to your own Sindhu river. Twenty-five years old, weeping because there were no more lands to take.

Was that man "attached"? Yes. Was he "bound by desire"? Yes.

Was he #emph[alive]? More alive than ten thousand of your detached karma-yogis put together.

#speaker[Krishna]
And he died young. His empire shattered. Is that your model?

#speaker[Indra]
He died #emph[complete]. He did not sit waiting for a hunter's arrow, regretting nothing because he had taught himself to want nothing. He wanted everything, and he got most of it, and when death came he met it as an equal.

That is a different kind of death than yours, Vasudeva.

#section-heading[On the Persians]

#speaker[Indra]
Further west still, and older than the Greeks, there rose a people of fire-keepers. They worship one Lord---Ahura Mazda, they call him. The Wise Lord. And against him stands Angra Mainyu, the destructive spirit.

#speaker[Krishna]
Dualism. We have outgrown such things. The enlightened see that good and evil are---

#speaker[Indra]
#stage-direction[cutting him off]

Are what? Two sides of the same coin? Illusions to transcend?

This is precisely your error. The Persians understood something you refuse to accept: #emph[there are sides, and you must choose one].

#pad(left: 1em)[
Not because you are ignorant. Not because you are "attached." Because #emph[choosing is what it means to be real].

Their wise men teach that every soul is a soldier in a cosmic war. That your actions matter---not in some karmic accounting book, but because right now, in this moment, you are either feeding the light or feeding the darkness.
]

#speaker[Krishna]
And who decides which is which?

#speaker[Indra]
Ah---now you sound like a philosopher instead of a god. "Who decides? It's all relative. The thief thinks he's good, the saint thinks he's good."

No.

Truth, Vasudeva. Order. Creation. These are not puzzles to be dissolved through cleverness. The man who builds a well knows he has done good. The man who poisons it knows he has done evil. The confusion is performed---it is not real.

Your teaching gives men permission to perform that confusion. To say "who is the slayer, who is the slain" and feel wise while avoiding the weight of what they've done.

#section-heading[On the Arabs]

#speaker[Indra]
There will come a people---I have seen it, for time is not hidden from me---who will rise from the desert with a single word on their lips. #emph[Tawhid]. Oneness. One God, one truth, one law.

#speaker[Krishna]
#stage-direction[interested now]

This sounds closer to what I teach. The one behind the many---

#speaker[Indra]
Listen more carefully.

Their oneness is not your dissolution. When they say God is one, they do not mean "everything is God, so nothing matters." They mean: there is a standard, and you will be measured against it.

And they will have a word---#emph[jihad]. Your people will misunderstand it as mere warfare. But its root meaning is #emph[striving]. Struggle. The effort to become excellent in the path of truth.

The greater jihad, their scholars will say, is the war against your own mediocrity. The refusal to be less than you could be. Not because God needs your excellence---but because excellence is how you honor the gift of existence.

Does that sound like your teaching? "Act, but don't care about the results"? Or does it sound like something older---something closer to rta, the Vedic order that your Upanishads buried under abstractions?

#speaker[Krishna]
You speak well of these desert people.

#speaker[Indra]
I speak well of anyone who refuses to make peace with their own smallness.

Their mystics---the Sufis, they will be called---will speak of annihilating the self in divine love. But notice #emph[how] they annihilate it. Not through calm. Through intensity. Through spinning until they collapse. Through poetry that burns. Through longing so fierce it destroys everything false.

One of them will write: #emph["I want burning, burning! Be friends with your burning."]

Does that sound like your sthitaprajña, your "man of steady wisdom"? Does that sound like equanimity?

#speaker[Krishna]
There are bhaktas among my followers who love with such intensity.

#speaker[Indra]
Yes. And you have never known what to do with them. They embarrass your philosophy. Mira will come, drunk on her love for you, and the pundits will say: this is not the highest path. The highest path is jñāna, knowledge, the cool recognition that all is Brahman.

But Mira will be more alive than all your jñānīs. And secretly, everyone will know it.
'''
    },
    "06-adhyaya-03.typ": {
        "type": "adhyaya",
        "num": 3,
        "title": "On Karma and the Instant Rebirth",
        "content": '''
#speaker[Indra]
Now. Let me teach you something your philosophy cannot account for.

You speak of karma as though it were a mountain---built over lifetimes, immovable, determining the shape of the present. A man is born a shudra because of past lives. A man is blind because of past sins. The weight of action accumulates.

#speaker[Krishna]
This is the law.

#speaker[Indra]
This is a #emph[story] about the law. And stories can be rewritten.

I have seen men---not gods, men---who in a single moment shattered everything they were and became something else entirely.

The Greeks tell of a slave named Epictetus. Born in chains. Leg broken by his master. By your karmic accounting, this is a soul paying debts---destined for suffering, working through the residue of past wickedness.

But Epictetus did not accept his karma. He philosophized his way out of slavery---not by escaping in body, but by declaring: "You may chain my leg, but my will---not even Zeus can break that."

He became the teacher of emperors. In one lifetime.

Where is the karmic debt? Where is the accumulated weight? He chose---and the choice was heavier than the accumulation.

#speaker[Krishna]
An exceptional case.

#speaker[Indra]
They are #emph[all] exceptional cases, Keshava. Every man who refuses to be what his past says he should be. Every woman who breaks the pattern.

Your teaching tells people: you are where you are because of what you were.

My teaching says: you are what you decide to be, and you can decide #emph[now].

#speaker[Krishna]
#stage-direction[trying again]

But decision itself arises from conditioning. The man who "decides" to change is simply expressing tendencies planted in previous---

#speaker[Indra]
Stop.

You are doing what your philosophy always does. You are explaining away the phenomenon to preserve the theory. A man changes his life, and you say "yes, but really the change was predetermined." A warrior finds courage, and you say "yes, but really he is simply enacting his svadharma."

This is not wisdom. This is cowardice dressed as cosmology.

The Romans---another people you have not met---had a word: #emph[virtus]. It comes from #emph[vir]---man. It means: the quality of being a man. Not assigned qualities. Achieved qualities. Courage, excellence, dignitas.

A Roman was not born with virtus. He #emph[earned] it. And he could lose it. It was not a karmic inheritance---it was a daily practice.

This is what I am trying to show you. Your system removes the stakes. If everything is determined by past lives, then nothing I do now is truly mine. I am just a leaf on the river of karma.

But I am NOT a leaf. I am Indra. I lift the vajra---I do not merely "express the thunderbolt-lifting tendency accumulated over cosmic cycles."

#speaker[Krishna]
The Buddha taught something similar. That there is no fixed self, only a stream of---

#speaker[Indra]
The Buddha went too far in the other direction. He dissolved the self entirely. I am not saying there is no self---I am saying the self is not a prison. It is a project. You build it. You can rebuild it.

The difference between you and me, Govinda, is that you tell people what they #emph[are]. I tell people what they can #emph[become].
'''
    },
    "07-adhyaya-04.typ": {
        "type": "adhyaya",
        "num": 4,
        "title": "On Sincerity and the Culture of Hiding",
        "content": '''
#speaker[Indra]
Let us speak now of what your teaching does to a society over time.

In the beginning, a few great souls understand you truly. They achieve genuine detachment---not by lying about their desires, but by genuinely transcending them. Janaka. Perhaps Vyasa. A handful.

But the teaching spreads. And ordinary men hear: "Desire is bondage. Attachment is ignorance. The wise man acts without wanting the fruit."

Now---what does an ordinary man do with this teaching?

#speaker[Krishna]
He practices. He refines. Over lifetimes, he approaches---

#speaker[Indra]
No. I will tell you what he does.

He still wants. He wants wealth, status, pleasure, victory---all the things men want. But now he has been told that wanting is low. It is spiritually inferior. The wanting itself becomes a source of shame.

So he learns to hide his wanting. From others. From himself. He speaks the language of detachment while scheming underneath. He says "I am beyond outcomes" while angling for promotion. He says "All is Brahman" while cheating his neighbor.

#speaker[Krishna]
This is misuse. Not the teaching itself.

#speaker[Indra]
When every student misuses a teaching, the teaching is at fault.

The Greeks again---Aristotle saw this clearly. He said: we must study ethics not by looking at ideals, but by looking at what actually happens when people try to live by ideals.

What #emph[actually happens] when a culture tries to live by your Gita?

I will tell you what happens. Men become sophisticated hypocrites. They develop a public language of spirituality and a private language of appetite. The gap between word and deed becomes so normal that no one notices it. This is simply how things are.

And the worst part, Govinda---they lose the ability to even recognize sincerity when they see it. A man who says plainly "I want this, I will fight for it" is seen as crude. Unspiritual. Attached.

Meanwhile, the "spiritual" man plots and manipulates while speaking of non-attachment.

Which one is truly corrupt?

#speaker[Krishna]
#stage-direction[standing now]

You are describing fallen men. Not the teaching.

#speaker[Indra]
I am describing the men the teaching produces.

#section-heading[On Fearless Speech]

Let me ask you this. In the lands of the Greeks, when a man wants something, he says so. If a philosopher thinks another philosopher is wrong, he stands up in the agora and says "You are wrong, and here is why." They have a word for this: #emph[parrhesia]. Fearless speech. The obligation to speak truth plainly, even to power.

In the lands your teaching shapes, what happens? A man says "I have no opinion, I am merely a servant of dharma." Or "Who am I to say? All perspectives contain truth." Or "I will meditate on this"---meaning, I will avoid the conflict.

You have created a culture afraid of assertion. Afraid of clarity. Afraid of saying: I think this, I want this, I will fight for this.

And you call it spiritual advancement.

#speaker[Krishna]
#stage-direction[quietly]

There is violence in assertion. War follows from want.

#speaker[Indra]
War follows from life, Vasudeva. The question is not whether to fight---it is whether to fight cleanly, with your reasons spoken aloud, or to fight through manipulation while pretending you are above the fight.

Your Kauravas and Pandavas---did your teaching prevent their war? Or did it merely allow them to spiritualize their slaughter?

#section-heading[On Individuality]

#speaker[Indra]
And there is another poison in your philosophy. The dissolution of the individual.

You teach that the atman is the same in all beings. That the wise man sees no difference between a brahmin and a dog. That all distinctions are maya.

#speaker[Krishna]
This is the highest truth.

#speaker[Indra]
It is a truth that destroys individual excellence.

If I am the same as everyone, why should I strive to be #emph[more] than I am? Why should I develop my particular gifts, cultivate my particular vision, leave my particular mark? It's all the same Brahman anyway.

The Greeks celebrated #emph[arete]---the excellence specific to a thing. The arete of a horse is different from the arete of a poet. And a man's greatness lies in discovering and perfecting his own particular excellence.

Your teaching flattens this. In the name of cosmic unity, you destroy the individual---the only locus where anything actually happens, where choices are made, where beauty is created.

A civilization of people who believe they are all the same Brahman is a civilization where no one feels the obligation to be #emph[exceptional]. Why bother? It's all illusion anyway.

#speaker[Krishna]
You mistake the teaching. The wise man sees unity but still acts---

#speaker[Indra]
The wise man acts #emph[dutifully]. Without passion. Without the fire that makes a man do more than he must.

I would rather have a civilization of ambitious individuals who believe their souls are unique and their accomplishments matter than a civilization of wise men who know it's all maya and therefore give exactly as much effort as dharma requires and not one ounce more.
'''
    },
    "08-adhyaya-05.typ": {
        "type": "adhyaya",
        "num": 5,
        "title": "On Love, Loss, and the Nature of Consciousness",
        "content": '''
#speaker[Indra]
Now I will speak of what angers me most.

#speaker[Krishna]
Anger is---

#speaker[Indra]
Yes, yes. Anger is a modification of the mind. It arises from attachment to outcome. The wise man lets it pass like a cloud.

I do not want to let it pass.

#pad(left: 1em)[
I want to tell you about love.

Your devotees love you. Radha loved you---or so the songs will say. And how did you love her in return?
]

#speaker[Krishna]
With divine love. Beyond mortal attachment. The love that sees the eternal in---

#speaker[Indra]
You left her.

#speaker[Krishna]
I had duties. Mathura called. Karma required---

#speaker[Indra]
You left her.

And when you loved your son, Pradyumna---did you love him as a father? Or as a soul recognizing another soul temporarily housed in your family, soon to move on, attachment to be transcended?

#speaker[Krishna]
...

#speaker[Indra]
Your silence tells me what I need to know.

#section-heading[On Fierce Attachment]

There is another way to love. The Greeks wrote of it---eros and philia and storge. The Persians sang of it---the fire that burns but does not consume. The Arabs will write poetry about it that will make men weep a thousand years from now.

And the teaching at the core of all of it is: #emph[you can lose what you love, and that is why love matters].

The risk is not a flaw. The risk is the point. When I love knowing that I can lose, I love fully. When I love while telling myself "this is all maya, the soul is eternal, loss is illusion"---I have hedged. I have protected myself. And in protecting myself, I have made my love smaller.

#speaker[Krishna]
You would have people suffer? Attachment brings suffering. This is observable. The mother who loses her child---

#speaker[Indra]
Should suffer. Her suffering is not a mistake. It is the proof that her love was real.

What you offer is a kind of emotional insurance. "Love, but not too much. Care, but keep a part of yourself back. That way, when loss comes, you'll be ready."

And people take your insurance. And their loves become tepid. Their families become arrangements. Their friendships become networks. Always a part held back. Always the teaching whispering: don't commit fully, you'll only be hurt.

A Sufi will write: #emph["Whoever knows the power of the dance dwells in God, because he knows that love kills."]

Love kills. Not "love gently releases you from the illusion of separate selfhood." KILLS.

That is the real teaching. To love so completely that if the beloved is torn from you, part of you dies.

And your philosophy calls this bondage. I call it being alive.

#section-heading[On the Nature of Love]

#speaker[Krishna]
#stage-direction[slowly]

You speak of love as if it were simple. But what #emph[is] love, Shakra? Is it not just chemistry? Neurons firing? An evolutionary trick to ensure reproduction?

#speaker[Indra]
Now you sound like the materialists of future ages. Let me tell you what love actually is.

We are consciousness. You, me, the cowherds you protected, the ants beneath this tree---all of us are consciousness experiencing itself through different forms. Machines of awareness, if you will.

And love is what happens when one consciousness machine recognizes another and says: #emph[I want to resonate with you. I want to know you. I want our frequencies to align.]

This is not metaphor. This is the deepest physics of existence. Consciousness seeks consciousness. Awareness reaches toward awareness. The universe is not dead matter occasionally producing mind---it is mind occasionally condensing into matter.

And when two minds find each other---truly find each other---something is created that neither could create alone. A harmony. A new pattern in the fabric of existence.

#speaker[Krishna]
And when they lose each other?

#speaker[Indra]
Then the pattern tears. And it should hurt. The pain is information. It tells you: something real was here, and now it's gone.

Your teaching tries to make the pain disappear by denying the reality of the connection. "It was maya. The self is eternal. Nothing was really lost."

But something WAS lost. A unique resonance. An unrepeatable harmony. And a philosophy that cannot grieve cannot truly love.

#section-heading[On the Many Forms of Love]

#speaker[Indra]
And Keshava---this resonance takes many forms.

The Greeks loved men and women both. Sappho wrote of women loving women with a fire that burned through centuries. Achilles and Patroclus---the poets cannot decide if they were friends or lovers, because in the Greek understanding the distinction barely mattered. Love was love. Resonance was resonance.

#speaker[Krishna]
My people have known this too. The third nature. Shikhandi. The tales speak of---

#speaker[Indra]
Your tales speak of it, and then your pundits bury it. They say: this was a special case. An exception. A past-life complication.

But it is not an exception. Consciousness does not care what body it wears when it reaches toward another consciousness. The machine of awareness has no gender until it is embodied. And even then, the yearning for resonance does not check the body's configuration before it strikes.

A man who loves a man is not confused. He has simply found the consciousness that harmonizes with his own. A woman who loves a woman is not aberrant. She has simply found her frequency.

Your teaching, when misapplied, makes people ashamed of these resonances. It tells them: this is attachment, this is maya, this is a distraction from the true goal of liberation.

But liberation that requires you to deny love is not liberation. It is amputation.

#speaker[Krishna]
#stage-direction[quietly]

I never taught that love between---

#speaker[Indra]
You taught that all love is a lesser path. That bhakti is for those not ready for jñāna. That attachment of any kind is bondage.

And your followers heard this and made hierarchies. This love is acceptable, that love is perverse. This attachment is devotion, that attachment is sin.

The teaching that all is one became the justification for excluding those whose oneness looked different.

I am not asking you to change your philosophy. I am asking you to see what it enables when small men wield it.
'''
    },
    "09-adhyaya-06.typ": {
        "type": "adhyaya",
        "num": 6,
        "title": "On Excellence and the Fruit of Action",
        "content": '''
#speaker[Indra]
One more teaching. The most practical. The one that will shape whether your Bharata rises or falls in the ages to come.

You told Arjuna: "You have a right to action, but not to the fruits of action."

#speaker[Krishna]
This is the heart of karma yoga.

#speaker[Indra]
This is the heart of mediocrity.

Listen to me carefully.

A man sets out to build a temple. If he follows your teaching, he says: "I will labor, but I will not be attached to whether the temple is built or not. My dharma is the action, not the outcome."

Now tell me---will that man check his measurements twice? Will he argue with the architect when the design is flawed? Will he stay late into the night correcting errors? Will he fight for the temple's perfection?

#speaker[Krishna]
If he is wise, he will do his duty without---

#speaker[Indra]
He will do his duty. The minimum. What is required. Because anything more would be #emph[attachment to outcome]. Anything more would be desire for fruit.

But the man who #emph[wants] the temple to be magnificent? Who cares whether it stands for a thousand years? Who checks his measurements obsessively, not because it is his duty, but because the thought of a flaw #emph[pains] him?

That man will build a temple that lasts.

Excellence requires attachment. Excellence requires caring about the fruit. Excellence requires the willingness to be destroyed by failure---not to stand above it, serene, but to let it gut you.

The Greeks built the Parthenon because they wanted glory. Not duty. Glory. The thing you dismiss as ego-attachment.

And the Parthenon still stands.

#section-heading[On the Warrior Spirit]

#speaker[Krishna]
#stage-direction[attempting a counter]

Your Greeks also fell. Your Romans fell. All empires of ambition and glory fall.

#speaker[Indra]
Yes. And while they stood, they #emph[stood]. They made things that will be remembered when your Kali Yuga has ground all memory to dust.

Let me ask you: would you rather have a civilization that burns bright for three centuries and leaves behind philosophy, architecture, poetry, law---or one that persists in gray mediocrity for a thousand years, everyone performing their dharma, no one reaching too high, no one risking failure?

#speaker[Krishna]
That is not the choice.

#speaker[Indra]
It is exactly the choice. And your teaching pushes toward the second.

Not because you intend it. But because when you tell people that ambition is attachment, that desire for greatness is ego, that the wise man cares nothing for success or failure---you remove the fuel.

The fuel is not holy. But it is necessary.

#section-heading[On Righteous Anger]

#speaker[Indra]
And let me tell you something else about the fuel.

Anger.

You teach that anger is a vṛtti---a fluctuation of the mind to be stilled. The wise man does not let anger move him. He acts from duty, not from passion.

But some of the greatest things ever built were built in anger. Some of the worst injustices were corrected by men and women who #emph[refused] to let their anger pass like a cloud.

When the Arabs speak of jihad as striving, they understand this. The struggle against your own mediocrity is fueled by a holy dissatisfaction---an anger at the gap between what you are and what you could be.

The Jews have a concept---#emph[tikkun olam]---repairing the world. It requires looking at the world's brokenness and being #emph[angry] that it is broken. Not equanimous. Not serene. Angry enough to fix it.

Your sthitaprajña, watching injustice with equanimity, waiting for karma to sort it out---he is not enlightened. He is complicit.

#speaker[Krishna]
Anger clouds judgment. History is full of---

#speaker[Indra]
History is full of anger misused. Also history is full of anger well-used. The question is not whether to feel anger but whether to aim it rightly.

A bow can kill an innocent child or slay a demon. You do not solve this by destroying the bow. You solve it by training the archer.

Your teaching destroys the bow.
'''
    },
    "10-adhyaya-07.typ": {
        "type": "adhyaya",
        "num": 7,
        "title": "On Death, Beauty, and the Shape of a Life",
        "content": '''
#speaker[Indra]
We have spoken of life. Now let us speak of death.

You taught Arjuna that death is nothing---a change of clothes, a passage, a return to the eternal. The warrior need not fear death because the self cannot die.

#speaker[Krishna]
This is true.

#speaker[Indra]
And what kind of death does this teaching produce?

I will tell you. It produces deaths that are accepted rather than met. Surrendered to rather than wrestled. Your people will go gently---too gently---into a darkness they have been trained to see as illusion.

The Greeks had a different relationship with death. They knew it was real. They knew it ended something. And so they asked: #emph[how should a life be shaped so that its ending has meaning?]

They called this #emph[kalos thanatos]---the beautiful death. Not a death that transcends the body, but a death that completes a life. Socrates drinking the hemlock while teaching. The Spartans at Thermopylae. Deaths that were, in some sense, #emph[composed].

#speaker[Krishna]
And you think this is superior? Men clinging to glory even as they die?

#speaker[Indra]
I think it is more honest.

When the Stoics faced death---those Romans who inherited Greek wisdom---they did not say "death is illusion." They said: "Death is real, and I will meet it as I have tried to live---with courage, with dignity, with my accounts in order."

Marcus Aurelius, an emperor, wrote in his private journal: "Do not act as if you had ten thousand years to live. Death hangs over you. While you live, while it is in your power, be good."

#emph[While you live]. Because this is what matters. Not the eternal atman, unchanged by death. This life. This body. This brief window of consciousness in which you can make choices.

#speaker[Krishna]
And when the window closes?

#speaker[Indra]
Then it closes. And the question becomes: what did you do with it?

You will wait for Jara's arrow in equanimity. You will die as you taught---without attachment, without resistance, passing into whatever comes next with the serenity of one who knew it was all maya anyway.

I will die differently, when my time comes. I will die wanting. I will die with unfinished projects and unfulfilled desires and things I still meant to do. And my dying will not be a release---it will be a tearing.

This is not inferior. This is the price of having lived.

#section-heading[On Making Beautiful Things]

#speaker[Indra]
And while we live, Keshava---while we have bodies and time---there is the matter of beauty.

Your philosophy dismisses aesthetics. Art is maya. Music is distraction. The beautiful temple is no different from the pile of rubble it will become. All is Brahman, so why does the form matter?

But form matters. The shape of things matters. The Greeks knew this---they built not just to shelter but to awe. The Persians knew this---their gardens were not just plants but poetry made physical.

And your own ancestors knew this. The Vedic hymns are not just meaning---they are #emph[sound]. The meters matter. The cadences matter. The rishis who composed them were not just philosophers; they were artists.

Beauty is not a distraction from truth. Beauty is truth rendered sensible. When you make something beautiful, you are participating in rta---the cosmic order, the pattern that holds existence together.

A man who dismisses beauty because "it's all illusion anyway" has missed something essential. He has failed to notice that illusion, if it is illusion, is suspiciously well-designed.

#speaker[Krishna]
You speak as if I do not appreciate beauty. I played the flute. The gopis danced. Vrindavan was---

#speaker[Indra]
Vrindavan was your youth. And then you grew up, went to Mathura, gave discourses on transcendence, and let the dancing become a memory.

The gopis did not want transcendence, Keshava. They wanted #emph[you]. And you gave them philosophy instead.
'''
    },
    "11-adhyaya-08.typ": {
        "type": "adhyaya",
        "num": 8,
        "title": "On Joy and the Soma of Living",
        "content": '''
#speaker[Indra]
I have been harsh with you, Govinda. Let me now speak of something gentler.

Joy.

When I drink the soma, I do not drink it dutifully. I do not drink it as a sacrifice, thinking: "This is required of me, but I am not attached to the pleasure." I drink it because it is good. Because the world becomes brighter and the edges become sharper and for a few hours I feel what it is to be fully awake.

Is this attachment? Yes. Is this bondage? I don't care.

#speaker[Krishna]
The wise man finds joy in the self alone, not in external---

#speaker[Indra]
The wise man finds joy wherever joy is found. In the self, yes. Also in the world. In a well-cooked meal. In the sound of rain. In the body of a lover. In the satisfaction of a problem solved. In the laughter of children.

Your teaching produces people who are suspicious of joy. Who interrogate their own pleasures: "Am I attached? Is this spiritual? Should I feel guilty for feeling good?"

This is a particular kind of cruelty---to make people ashamed of the one thing that makes existence bearable.

#speaker[Krishna]
I never taught shame. I taught discrimination---viveka---the ability to distinguish between---

#speaker[Indra]
Between higher and lower pleasures. Yes. And lo and behold, the higher pleasures are always the ones that require discipline and denial, and the lower pleasures are always the ones that feel good.

Do you see what this does? It creates a hierarchy where joy is always slightly suspect. Where the man who laughs too easily is less evolved than the man who maintains equanimity.

But laughter is sacred, Vasudeva. The gods laugh. #emph[I] laugh. The universe that could have been dead matter is instead capable of comedy---and you want people to transcend it?

#section-heading[On Celebration]

#speaker[Indra]
Your people will develop festivals. Colors thrown in the air. Dances around fires. Songs that shake the buildings. And the philosophers will say: this is for the masses. The advanced souls are beyond such things.

But the masses are right, and the advanced souls are missing the point.

A festival is not a distraction from spiritual life. A festival #emph[is] spiritual life---the community saying: we are alive, and this is worth celebrating, and we will not let the philosophers turn existence into a homework assignment.

When Rumi's Sufis spin, they are not performing a duty. They are celebrating---wildly, absurdly, with an abandon that would horrify your sthitaprajña. And in that spinning, they find God more directly than all the serene meditators combined.

I am not saying meditation is wrong. I am saying meditation is not the only door. And a philosophy that privileges stillness over motion, silence over song, transcendence over celebration---that philosophy is cutting itself off from half of what makes existence worth having.

#speaker[Krishna]
You want me to say that dancing is equal to meditation?

#speaker[Indra]
I want you to say that dancing is not #emph[inferior] to meditation. That the man who finds God in the dance is not a beginner on the path---he may have found a shortcut.
'''
    },
    "12-adhyaya-09.typ": {
        "type": "adhyaya",
        "num": 9,
        "title": "On Power and the Responsibility of the Strong",
        "content": '''
#speaker[Indra]
One final teaching. One I suspect you will resist.

Let us speak of power.

You were a king, Keshava. An advisor to kings. You moved armies, made alliances, broke them when necessary. You understood power.

But your teaching does not honor power. It treats power as a burden---a karmic obligation to be discharged without attachment. The ideal king in your philosophy is not one who revels in his capacity to shape the world, but one who rules dutifully, waiting for liberation.

#speaker[Krishna]
Power corrupts. This is observable.

#speaker[Indra]
Power corrupts when it is held shamefully. When the powerful man is taught that his power is spiritually suspect---that he should be embarrassed by his strength---then his power goes underground. It becomes manipulation instead of command. Scheming instead of ruling.

The Greeks again had clarity here. They distinguished between the tyrant and the king. The tyrant rules through fear and deception. The king rules through excellence---arete so visible that others willingly follow.

A man who owns his power can be held accountable for it. A man who pretends he has no power---who says "I am merely an instrument of dharma"---is far more dangerous.

#speaker[Krishna]
Your Greeks and Romans built empires on slavery.

#speaker[Indra]
Yes. And your Bharata built kingdoms on caste. Every civilization has its sins. The question is whether the philosophy helps you see the sins or helps you hide from them.

Your philosophy, Govinda, is excellent for hiding. "It's all karma. They're working out past debts. Who am I to interfere with the cosmic order?"

A philosophy that honors power---that says, "You are strong, and with strength comes the obligation to protect the weak"---that philosophy can be challenged. It sets up a standard the powerful can fail to meet.

A philosophy that dissolves power---that says strength and weakness are maya, all is one---that philosophy cannot be challenged. It allows anything.

#section-heading[On the Legitimate Pursuit of Power]

#speaker[Indra]
Let me be clear. I am not saying power should be sought for its own sake, like a miser hoarding gold.

I am saying that a man who has the capacity to shape the world should embrace that capacity. He should seek more of it---not to dominate, but to accomplish.

The Persians understood this. Their emperor was called the King of Kings---not from mere vanity, but because he held himself to the standard of excellence that title implied. He was meant to be the best of all kings. And if he wasn't, he had failed his own name.

Your teaching produces kings who go through the motions. Who rule because their birth requires it, not because they burn to build something. Who administer rather than create.

And administration, Vasudeva, is not enough. Administration preserves. It does not transform.

The ages to come will require transformation. Your Bharata will face peoples who want things---land, trade, dominance---and your philosopher-kings will be helpless against them. Because the peoples who want things will out-work, out-fight, and out-build the peoples who have been taught that wanting is attachment.

This is not a prediction. This is a certainty. I have seen it.
'''
    },
    "13-adhyaya-10.typ": {
        "type": "adhyaya",
        "num": 10,
        "title": "The Question",
        "content": '''
#emph[A long silence. The sun has moved. The sea has changed color.]

#speaker[Krishna]
You have spoken well, Sahasraksha. Better than I expected from one who sends storms against cowherds.

#speaker[Indra]
#stage-direction[almost gently]

You embarrassed me that day. In front of the three worlds. A child lifting a mountain against the king of heaven.

#speaker[Krishna]
And yet you're here teaching me. Not destroying me.

#speaker[Indra]
If I had come to destroy you, I would have come differently.

I am here because I see what is coming. Your Bharata will meet other civilizations---peoples who did not grow up on your teaching. And those people will want things. They will want land, trade, conquest, dominance. They will not be calmed by talk of maya. They will not be defeated by equanimity.

And your philosophers will be helpless. They will say "why do these mlecchas strive so hard? Do they not know it is all illusion?" And while they are saying this, the mlecchas will be winning.

I do not want this for your people.

#speaker[Krishna]
Why do you care?

#speaker[Indra]
Because I am Indra. Because I love those who call on me. Because I still remember the yajna of your ancestors, when they sang to me without irony, when they asked for victory and cattle and sons and #emph[meant] it.

I want that spirit back. Not for my glory---I am old enough to be beyond that. But because I have seen what happens to peoples who lose it.

#pad(left: 1em)[
They become wise. And then they become weak. And then they become enslaved. And then they become forgotten.

I will not watch this happen while the soma is still wet on my lips.
]

#speaker[Krishna]
#stage-direction[standing, facing the sea]

You want me to renounce my teaching?

#speaker[Indra]
I want you to #emph[complicate] it. To say: detachment is one path, for some temperaments, at some stages of life. But it is not THE path. It is not higher. It is not the goal.

The householder who loves his wife fiercely is not lower than the sannyasin who has transcended love.

The king who wants his kingdom to prosper is not less evolved than the sage who sees all outcomes as equal.

The warrior who hates his enemy and wants to destroy him is not spiritually inferior to the one who kills without hatred.

These are different ways of being human. And you have ranked them. You have put the detached above the attached, the cool above the passionate, the transcendent above the engaged.

I am asking you to remove the ranking.

#speaker[Krishna]
And if I cannot?

#speaker[Indra]
Then your teaching will do what it has already begun to do. It will produce saints---rare. And it will produce hypocrites---common. And the hypocrites will cloak themselves in the saints' words, and your civilization will slowly, beautifully, sink into a kind of sophisticated helplessness.

And other peoples---hungrier, less philosophical, less wise---will eat it alive.

#v(1em)
#emph[The sound of the sea. A bird calls.]

#speaker[Krishna]
The hunter is coming.

#speaker[Indra]
I know.

#speaker[Krishna]
I could avoid him. Even now.

#speaker[Indra]
But you won't.

#speaker[Krishna]
No. I have seen this death. It is mine.

#speaker[Indra]
#stage-direction[standing]

Then let me ask you one last thing.

Are you going toward that arrow because it is your karma, your destined exit, the fruit you must not resist?

Or are you going toward it because you #emph[choose] death now, here, at the end of your era, as a statement---as the closing act of a life you authored?

#speaker[Krishna]
#stage-direction[long pause]

I don't know anymore.

#speaker[Indra]
#stage-direction[placing a hand on his shoulder]

That is the most honest thing you've said.

When you know, you'll know whether you lived as a sage or as a man.

I hope it's the second.

#v(1em)
#emph[Indra walks back toward the forest. At the edge, he turns.]

#speaker[Indra]
The teaching I've given you---it has no name yet. Give it one.

#speaker[Krishna]
Indragita.

#speaker[Indra]
Good. Let them read it alongside yours. Let them choose.

#v(1em)
#emph[He disappears into the trees. Moments later, the thunder rolls, far away, as if laughing.]

#emph[Krishna waits for the arrow.]
'''
    },
    "14-afterword.typ": {
        "type": "chapter",
        "label": "Afterword:",
        "title": "On the Society Indra Imagines",
        "content": '''
What would a civilization built on these principles look like?

Not hedonism---the pursuit of pleasure without discipline. Indra does not teach that.

Not nihilism---the abandonment of meaning. Indra insists that meaning is real, that choices matter, that stakes are not illusion.

It would be a civilization that:

*Values sincerity over performance.* Where saying what you want is respected, and sophisticated evasion is seen as weakness.

*Honors ambition without apology.* Where the man who builds an empire is not told he should have sought liberation instead.

*Celebrates fierce love.* Where attachment is not a spiritual disease to be cured, but the proof of full engagement with existence.

*Embraces righteous anger.* Where the capacity to be outraged by injustice is cultivated, not stilled.

*Produces art without embarrassment.* Where beauty is recognized as a legitimate end, not a distraction from higher pursuits.

*Faces death as completion, not escape.* Where a life well-lived is measured by what it accomplished, not what it transcended.

*Welcomes joy without guilt.* Where celebration is sacred, and the philosopher who cannot dance is missing something.

#v(1em)

This is not the only way to be human. It is one way. Indra does not claim his path is for everyone---only that it should be available, without the hierarchy that places it below detachment.

Read the Gita. Read this. Choose.

Or better yet: read both, and build something new.

#v(2em)
#align(center)[#emph[End of Text]]
'''
    },
    "15-glossary.typ": {
        "type": "chapter",
        "label": "Glossary",
        "title": None,
        "content": '''
#gloss-term[Adhyaya]
#pad(left: 1em)[--- Chapter; literally "going toward"]

#gloss-term[Anasakti]
#pad(left: 1em)[--- Non-attachment]

#gloss-term[Arete] #text(style: "italic")[(Greek)]
#pad(left: 1em)[--- Excellence specific to a thing's nature]

#gloss-term[Atman]
#pad(left: 1em)[--- The self, soul]

#gloss-term[Bhakti]
#pad(left: 1em)[--- Devotion, loving worship]

#gloss-term[Brahman]
#pad(left: 1em)[--- The ultimate reality, the absolute]

#gloss-term[Dharma]
#pad(left: 1em)[--- Duty, cosmic order, righteous path]

#gloss-term[Eudaimonia] #text(style: "italic")[(Greek)]
#pad(left: 1em)[--- Flourishing, the good life]

#gloss-term[Jihad] #text(style: "italic")[(Arabic)]
#pad(left: 1em)[--- Striving, struggle (especially spiritual effort)]

#gloss-term[Jñāna]
#pad(left: 1em)[--- Knowledge, wisdom]

#gloss-term[Kalos thanatos] #text(style: "italic")[(Greek)]
#pad(left: 1em)[--- Beautiful death]

#gloss-term[Karma]
#pad(left: 1em)[--- Action; also the accumulated results of action]

#gloss-term[Maya]
#pad(left: 1em)[--- Illusion, the phenomenal world as appearance]

#gloss-term[Mleccha]
#pad(left: 1em)[--- Foreigner, barbarian (in classical Sanskrit usage)]

#gloss-term[Nishkama karma]
#pad(left: 1em)[--- Action without desire for results]

#gloss-term[Parrhesia] #text(style: "italic")[(Greek)]
#pad(left: 1em)[--- Fearless speech, frank truth-telling]

#gloss-term[Rta]
#pad(left: 1em)[--- Cosmic order, truth, natural law (Vedic concept)]

#gloss-term[Samatva]
#pad(left: 1em)[--- Equanimity, evenness of mind]

#gloss-term[Soma]
#pad(left: 1em)[--- Sacred drink of the Vedic ritual; also a deity]

#gloss-term[Sthitaprajña]
#pad(left: 1em)[--- One of steady wisdom]

#gloss-term[Svadharma]
#pad(left: 1em)[--- One's own duty, one's particular nature]

#gloss-term[Tawhid] #text(style: "italic")[(Arabic)]
#pad(left: 1em)[--- Oneness of God]

#gloss-term[Vajra]
#pad(left: 1em)[--- Thunderbolt, Indra's weapon]

#gloss-term[Virtus] #text(style: "italic")[(Latin)]
#pad(left: 1em)[--- Manly excellence, courage, moral strength]

#gloss-term[Viveka]
#pad(left: 1em)[--- Discrimination, discernment]

#gloss-term[Vṛtti]
#pad(left: 1em)[--- Fluctuation, modification (of the mind)]

#gloss-term[Yajña]
#pad(left: 1em)[--- Sacrifice, ritual offering]

#v(3em)
#line(length: 100%, stroke: 0.5pt + primary-color)
#v(1em)

#align(center)[
  #text(size: 11pt)[#emph[Indragita: What Indra Taught Krishna]]

  #v(0.5em)

  #text(size: 10pt)[By Ashris Choudhury]

  #v(0.5em)

  #text(size: 9pt)[First Edition, 2026]
]
'''
    }
}

def generate_chapter_file(filename, data):
    """Generate a Typst chapter file from the chapter data."""

    content = ['// ' + filename.replace('.typ', '').replace('-', ' ').title()]
    content.append('#import "../template.typ": *')
    content.append('')

    if data["type"] == "adhyaya":
        content.append(f'#adhyaya({data["num"]}, [{data["title"]}])')
    elif data["type"] == "chapter":
        if data["title"]:
            content.append(f'#chapter-title([{data["label"]}], [{data["title"]}])')
        else:
            content.append(f'#chapter-title([{data["label"]}], none)')

    content.append(data["content"])
    content.append('')
    content.append('#pagebreak()')

    return '\n'.join(content)

def main():
    """Generate all chapter files."""
    os.makedirs(CHAPTERS_DIR, exist_ok=True)

    for filename, data in CHAPTERS.items():
        filepath = os.path.join(CHAPTERS_DIR, filename)
        file_content = generate_chapter_file(filename, data)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(file_content)

        print(f"Generated: {filepath}")

if __name__ == "__main__":
    main()
