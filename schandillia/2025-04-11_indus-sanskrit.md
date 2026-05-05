# The Case for Indus Sanskrit

*A Critical Examination of a Recent Paper by Yajnadevam*

- date: 2025-04-11
- audience: only_paid
- url: https://www.schandillia.com/p/indus-sanskrit
- slug: indus-sanskrit

---

Among the most enduring mysteries of the ancient world is the language of the Indus people. The most surefire way of learning a lost civilization’s language is through its writings. Back in the day, people left behind seals and inscriptions just as today we leave behind books and billboards. If an inscription is bilingual, one of the scripts being familiar, it makes the job of deciphering the unknown easier. The Rosetta Stone is arguably the most celebrated example of such an artifact. It helped us decipher Egyptian hieroglyphs a good 2,000 years after they were carved. Greek helped us there. But not all inscriptions offer that convenience.

The Indus civilization remains an odd mystery majorly because it has left behind very little writing. Everything we know so far is educated guesswork, logical extrapolation. But there’s a great deal we still don’t know even with such extrapolations. For instance, we’re yet to confidently ascertain what they imported. We know they exported carnelian, bronze, fowls, buffalos, and other exotic items to the Mesopotamians, but we don’t know much about that they got back in return. A correct decipherment of their script could help answer a long list of similar questions.

With over 4,000 inscriptions recovered so far, it’s hard to believe that they left behind insufficient writing. But while the volume of inscriptions is great, not so great is the average size of these inscriptions. The longest is about 30-35 characters, the shorted just one character. The average hovers around 5. That’s not a whole lot to work with. But that doesn’t mean attempts haven’t been made.

As is the case with the Aryans, the Harappans too come with immense political and ideological baggage. The Indus civilization is primordial India. Whoever gets to claim it, gets to claim India. Much ideological debate in the subcontinent revolves around the ethnic identity of the Meluhhans or Harappans with two major contentions—Dravidian or Aryan. South Indians want the civilization to be Proto-Dravidian so they could claim primacy over the country’s civilizational heritage. This ties in well with their notion that they are natives and the Aryans or North Indians, foreign invaders. The converse is claimed by North Indians.

This politics colors scholarship. Many scholars are also ideologues and enter the study not to find out the truth, but to confirm something they already hold as the truth. In the simplest terms, this debate boils down to language. South Indian ideologues want the Indus language to be some kind of a Proto-Dravidian dialect, so as to fortify their claims of nativity. North Indians, on the other hand, want the Indus language to be Sanskrit, for the exact opposite reasons. Who is right then?

This article does not answer that question. Hundreds of scholars and experts all over the world are working hard to crack this code, certainly not something an article like this could even begin to cover. What this article does endeavor is to pick one of the myriad hypotheses and examine it objectively for viability. We’re talking a 2024 paper titled “A Cryptanalytic Decipherment of the Indus Script” that makes a bold claim in favor of Sanskrit. The paper which is yet to be peer-reviewed and published in a journal, uses an impressive array of cryptographic novelties to arrive at its conclusions. Reading it thoroughly before proceeding is highly recommended even if not an absolute necessity.

This piece is going to be very different from all others on this site, because this one involves a good deal of math and a little bit of computers, in addition to linguistics and history. Cryptography is a math-intensive discipline and therefore hard to keep purely equation-free. As for computers, there’s only this concept of regex. Not the whole concept, but a couple of real-world examples. Nothing that should deter a sincere reader. The only caveat here is that the Indus glyphs are mentioned using their short English descriptions rather than the characters. This is because the Indus font is not supported on this platform yet, so the glyphs would render as unreadable blocks like this—. So, instead of typing out the jar character, we’ll just spell out “jar.” We’ll start with some elementary jargon and relevant math and then wiggle our way into the meat and potatoes of Yajnadevam’s decipherment.

## The Mathematics of Decipherment

Entropy is randomness. It measures the unpredictability in a system. The higher the predictability, the lower the entropy, and vice versa. This is not just some vague abstraction, but a tangible, quantifiable value that can be derived and expressed in real numbers. Mathematically, this randomness is expressed in bits. Why? Because it’s the lowest unit of information. For instance, the answer to a basic yes/no question only needs two states, and those can be expressed as either 0 or 1, i.e. using a single bit. If a question can be answered one of four ways, a single bit isn’t sufficient. Two are—00, 01, 10, and 11. The number of bits required to express a piece of information can be calculated as:

Where _i_ is the number of possible values in the information. So, for a yes/no question, _i_ is 2, which can be expressed using log2(2) = 1 bit. For a question that can be answered 10 different ways, log2(10) = 3.32 bits would be needed.

For languages, entropy tells us how much information is packed into each symbol (like letters). If a language is very predictable (e.g., “th_” often becomes “the”), its entropy is lower. In this context, the number of possible answers is the probability of a given letter. We know that all letters are not equally ubiquitous. “E” is far more frequent than, say, “X,” and so on. Thus, for a letter, its frequency or probability is what governs its entropy. This probability is a quantifiable value. Thus, the above entropy formula can be extended to calculate the overall entropy for an entire language system:

Where:

  * _p i_ = probability of the _i_ -th symbol (e.g., how often “A” appears in English)

  * _n_ = total number of symbols (e.g., 26 for English)




This formula sums up the contributions of all symbols based on their probabilities. Once again, the final value is expressed in bits. Let’s illustrate this with a calculation. English has 26 letters, but they don’t appear equally often. For simplicity, let’s use approximate probabilities for common letters:

  * “E” appears 13% of the time, hence _p E_ = 0.13, _H E_ = -_p E_ ⋅ log2(_p E_) ≈ 0.38 bits.

  * “T” appears 9% of the time, hence _p T_ = 0.09, _H T_ = -_p T_ ⋅ log2(_p T_) ≈ 0.31 bits.

  * Other letters have lower probabilities.




For “E” and “T” we get a total entropy of 0.69 bits. If we calculate this for all 26 letters in English, using their actual probabilities (which vary widely), we find that English has an average entropy of about 1.5 bits per letter. This means that each letter carries about 1.5 bits of information on average.

The next term of relevance here is redundancy. Language, it’s often said, is a Markov chain. A Markov chain is where the future value depends on the current value, i.e. any value is a function of the value just before it. In English terms, if we have “t_,” we can reasonably predict the word to be “to” because “ti,” “ta,” “tu,” or “te” don’t make sense as complete words. Nor does any consonant right next to “t.” But if we’re given “ti_,” we can be reasonably sure it’s “tin.” In other words, not all combinations weigh the same. Of all the combinations possible with “t” and one more letter, a total of 26 possible values, only one makes sense. The remaining 25 are meaningless. In this specific example, the maximum possible randomness is 26, but the actual or useful entropy is only 1, so to speak. Of course, these values ought to be expressed in bits, but this is the fundamental premise. The difference between the maximum number of possibilities and the maximum number of valid choices is what we call redundancy. In other words, redundancy measures how much less information a language carries compared to its maximum possible randomness. Its formula is:

For English,

  1. Maximum possible entropy (if all letters were equally likely):

log2(26) ≈ 4.7 bits per letter.

  2. Actual entropy (due to patterns):

_H_ = 1.5 bits per letter.

  3. Redundancy:

_D_ = 4.7 − 1.5 = 3.2 bits per letter.




This shows that English has 3.2 bits of predictable structure per letter, making it easier to analyze or crack.

In sum, For English letters, actual entropy (~1.5 bits) reflects predictable patterns, while redundancy (~3.2 bits) highlights how much structure exists in the language compared to maximum randomness (~4.7 bits). This redundancy is typically expressed as a percentage of maximum entropy.

An interesting implication of this derivation is that for the English language, one only needs to know 30% of the letters to guess everything written in the language with reasonable confidence. That’s how we’re able to guess, for example, “message” when we see “msg.” Of course, context matters too. Many other languages share a similar redundancy—70.2% for Russian, 67.3% for Greek, 71.6% for Spanish, 73.4% for Hindi, and so on.

Having thoroughly understood entropy and redundancy, we are now equipped to explore the concept of equivocation. Imagine you’re trying to guess the next letter in a word, but you’re not 100% sure what it will be. Equivocation is a fancy word for that uncertainty or ambiguity you feel when you’re making that guess. In the context of language (or even cryptography, as the snippets mention), equivocation measures how uncertain you are about the correct letter, word, or message, even after you’ve made some observations or guesses.

Say, there’s an obscure inscription we’re given to decipher and there’s no clue of any kind to work with. At this point, all we know is that it’s a word. But which word? Now, say some cleaning up reveals that it’s in the Latin script. Now our options narrow down to the English alphabet. Good progress but still in the wild because only the first letter is clear (“J”), and we still don’t know what the word could even be about. A little more study of the context and we learn that it’s the name of a month. Finally, we have something. Our choices now are down to January, June, and July. If we now learn that there are only four letters, we can safely rule out January, and so on. We started with infinite possibilities and zero knowledge. With each subsequent clue, our knowledge increased by a factor and the number of possibilities or total entropy decreased by a factor. That is, with each new piece of information, the number of possible solutions reduced. This gap between entropy and information gained is what we call equivocation. At first, its value is equal to the total entropy. Once we have made the right guess, its value becomes zero because there’s only one possibility and we have already guessed that. This too is measured in bits. There’s a formula to calculate equivocation but we won’t worry about that here.

Finally, we can now discuss unicity distance. This is the amount of ciphertext (encrypted message) needed to uniquely determine the correct plaintext. In simpler terms, it’s the minimum amount of encrypted text required to break the code. We’re talking in terms of cryptography here because that’s how we treat undeciphered writings, such as the Indus script. The idea here is that the longer the encoded text, the easier its decipherment.

For example, let’s say we have a cryptic message that reads “UC.” Just two letters. What could it mean? Could be “TO.” Could also be “OH.” Or “GO.” Or any of the several two-letter combinations in the English language that translate into something meaningful. It’s nearly impossible to determine the correct key. Now let’s say the ciphertext is “UCJJ.” This time we have more information. We know there’s a word of four letters with the last two positions taken by a double letter. In other words, three unique letters. Now our choices reduce. Now we can try “WELL,” “TELL,” “MESS,” or “TIFF,” but not “BEAT” or “PONY.” With longer ciphertext comes better accuracy and vice versa.

In cryptography, unicity distance is the point at which the amount of information in the encrypted message is just enough to guarantee that only one possible meaningful solution can exist for the decryption. Before this point, multiple valid answers could exist. After it, the chances of guessing wrong drop drastically. Before we get to its math, let’s understand the concept of key space, the total number of possible keys in a cipher. In a simple substitution cipher, where each letter of the plaintext is mapped to another letter, the number of possible keys (for English) is:

Which translates to:

A decipherment must extract at least this amount of information from the ciphertext to be considered reliable. If the amount of deciphered information is less than this, ambiguity remains, and multiple interpretations may still be possible.

A language consists of 𝑝 unique symbols (e.g., 26 letters in English). But not all sequences are equally probable. Languages have redundancy. In English, as we’ve already seen, that redundancy (𝜌) is about 0.7. The information content per symbol is:

This represents the effective bits of information per letter in a given language. The cipher most commonplace in the context of script decipherment is what we call a homophonic cipher. It’s a type of encryption where each plaintext symbol can be mapped to multiple different ciphertext symbols instead of just one. The goal of such a cipher is to obscure frequency patterns in the plaintext, making statistical attacks more difficult. In script decipherment, homophonic ciphers are commonplace. For instance, in English, the sound /i/ can be rendered with “i,” “ee,” “y,” “ea,” “ie,” and even “oe,” depending on the word. If these were independent symbols, we’d call them homophones.

In a homophonic cipher where:

  * _N_ is the number of ciphertext symbols

  *  _p_ is the number of plaintext symbols

  * Each ciphertext symbol maps to a plaintext symbol in 𝑝 different ways, adding log2 _p_ bits of information per symbol




The key space for a homophonic cipher is:

The use of multiple ciphertext symbols for each plaintext letter increases the complexity of decryption, effectively raising the unicity distance—more ciphertext is required before a unique decryption can be achieved. Since the information contained in the key space must be extracted from the ciphertext, the unicity distance is given by:

Substituting ∣ _K_ ∣ = _p N_:

Since log2 _p N_ = _N_ ⋅ log2 _​p_ , we simplify:

This shows that the unicity distance depends entirely on the ciphertext length _N_ and the redundancy _ρ_ of the language. This has following implications:

  * High redundancy (_ρ_) → lower unicity distance (_d_)

    * Languages with high redundancy (e.g., English) require fewer ciphertext symbols to reach the unicity distance.

    * This means a shorter message can still be deciphered reliably.

  * Larger key space (∣ _K_ ∣) → higher unicity distance (_d_)

    * Ciphers with a larger key space (such as homophonic ciphers) require longer ciphertexts to reach a reliable decryption.

  * More ciphertext (_N_) → easier decryption

    * The more ciphertext symbols available, the closer one gets to reaching the unicity distance, making decryption more accurate.




Unicity distance determines how much inscription length is needed for a unique decipherment. Scripts where symbols map to multiple sounds raise this threshold, complicating phonetic analysis. This explains why short inscriptions, like those of the Indus Valley, remain difficult to decrypt reliably, while longer texts, like those of the Egyptians, provide enough patterns to break even complex writing systems. With that, we have all the mathematics relevant to our investigation in place. Now, we’re sufficiently equipped to explore the various principles and methodologies of Indus decipherment so far.

## Why Existing Methods Fail

Although it’s quite the leap to declare that existing theories have necessarily failed, we’ll try to understand why the paper in question passes that verdict. To understand its arguments, let’s first familiarize ourselves with the concepts of _logographic_ and _logosyllabic_.

Imagine writing as a spectrum. On one end, we have writing systems where each symbol represents a complete word or idea, such as Egyptian hieroglyphics or emojis. A picture of a smiling face directly conveys the concept of happiness. Chinese characters are a classic example, where each character represents a distinct word or concept (e.g., 水 for water). We call such systems logographic.

On the other end of the spectrum, we have alphabetic systems like English, where each letter represents a sound, and we combine these sounds to form words. Somewhere in the middle lies the logosyllabic system. In this type of script, some symbols represent whole words while others represent syllables, which are the building blocks of words (e.g., “ba,” “ki,” “to”). Mayan hieroglyphs, for example, are logosyllabic. Some glyphs stand for entire words, while others represent syllables used to construct longer words. The key difference lies in the ratio of symbols to words and sounds. Logographic systems need a vast array of unique symbols—potentially thousands—to represent all the words in a language. Alphabetic systems, on the other hand, can represent virtually countless words with a relatively small set of letters. Logosyllabic systems fall somewhere in between, requiring more symbols than an alphabet but fewer than a purely logographic system.

Now, with that foundation laid, let’s circle back to the Indus script and why the paper argues against logographic and logosyllabic interpretations. The core of the argument is that decipherments based on these models suffer from an inherent flaw—the assumptions required to make them work are too numerous and arbitrary. Without a bilingual text (like the Rosetta Stone for Egyptian hieroglyphs), these interpretations rely on subjective assignments of meaning to signs. The method involves taking a sign and assigning it a meaning that seems plausible within a given cultural or linguistic context. However, as the paper points out, these assignments are often based on speculation rather than solid linguistic evidence.

For instance, Parpola’s interpretation assigns the intersecting circles sign to mean “bangles” and a three-stroke sign to mean “hearth.” But why these meanings specifically? The paper notes that these signs could just as easily stand for entirely different words—perhaps “nuts” or “wheels” or any number of other concepts. The lack of a reliable means to validate these readings results in an insurmountable unicity distance, where a given decipherment could be entirely arbitrary. Moreover, when multiple signs are combined, the supposed meanings often become nonsensical, forcing scholars to add further layers of interpretation, such as turning “hearth bangles” into “pregnancy bangles.” This continuous reinterpretation highlights the method’s fundamental weakness.

Another key issue the paper highlights is the explosion of possible meanings when trying to decipher the entire corpus. If each symbol can have multiple potential meanings, the number of possible readings increases exponentially, creating an unwieldy and impractical system. Essentially, the method allows for too many interpretations, making it impossible to determine which, if any, is correct. Genuine written languages tend to have some degree of regularity and constraint, whereas the Indus script, when analyzed through logographic and logosyllabic lenses, yields an excessive number of potential readings that lack coherence.

Another reason for ruling out logographic readings outright is the size of Indus character set. If each word or idea were to be represented by a separate character, the script would need thousands of glyphs. Just to write the most frequently used vocabulary, one would need upward of 2,000 characters. The Unicode Standard for Chinese, for instance, has as many as 100,000 characters. The oracle bone script, the precursor to modern Chinese writing, features more than 30,000 distinct symbols. The Egyptian hieroglyphics featured as many as 5,000 graphemes during the Ptolemaic period. But the Indus script, even by most generous of estimates, has been assigned no more than 500 characters.

So, if it’s not logosyllabic or logographic, what is it? There are three more systems that do not require an unwieldy character-set like Chinese or Egyptian— _alphabet_ , _abjad_ , and _abugida_. We are already familiar with alphabet. This is where each sound, vowel or consonant, gets a symbol. Abjad is where only consonants get symbols and vowels are either left out to be guessed from the context or indicated using optional diacritic marks. An example of such a system is Arabic where, for instance, book is called _kitāb_ but only rendered as _ktb_. Abugida writes consonants with a default inherent vowel and modifies them using diacritic marks or small additions to represent other vowel sounds. This system is common in scripts like Devanagari, used for Sanskrit and Hindi. For example, the character क (/kə/) represents the consonant sound /k/ with the inherent vowel /ə/. To render the /ki/ sound, a small diacritic is added (की), and for /ku/, a different mark is used (कु). Almost all Indic scripts including Tamil, Bengali, etc., belong to this class.

So, the Indus script, the paper argues, has to be one of these three types. Within this set, it then leans in favor of abjad. But more on that in a bit. First, let’s understand the basic steps involved, the algorithm if you will. The paper in question deploys Claude Shannon’s method for solving ciphers in its quest to read the Indus script. At first crack, this might sound illogical because languages are not cryptograms. In cryptography, we use keys to decode the encrypted message. In the context of script decipherment, that would mean choosing a known language as the key space and seeing if a text written in the script yields a meaningful message. In other words, we’re force-fitting a known language on to an unknown script. Which assumes that the unknown script is not in an unknown language. Before we look into the problems with this approach, let’s see how the paper approaches this and zeroes in on Sanskrit.

## Why Sanskrit

One of the most popular theories proposes Proto-Dravidian as the language of the Indus. The continued presence of a most unlikely Dravidian tongue, Brahui, in the region only makes the proposition more plausible. And yet the paper at hand dismisses it in favor of Sanskrit. Why? To answer that question, we must understand the concept of agglutinative languages.

Also sometimes called concatenative, agglutinative languages primarily form words by attaching separate pieces, called morphemes, each carrying its own distinct grammatical function (such as plural, past tense, or possession). These pieces, typically suffixes, are added to a stem in a fixed order, without altering their own form or the stem itself. Tamil, along with other Dravidian languages, exemplifies this type. This contrasts with inflection, where the root itself undergoes modification, and affixes may fuse with it in less separable ways.

While English and Sanskrit exhibit some agglutinative traits, Dravidian languages stand out because their affixes are bound morphemes—unable to stand alone as independent words—and must follow a strict sequence. For instance, in Tamil, the plural marker precedes the locative case marker, as the paper notes. These affixes rely on the stem for meaning, building complex words through systematic attachment. This does not seem to happen in the Indus script. How?

The paper notes five examples. In the first four, we have single symbols—H-1497 (three vertical strokes), H-1546 (a tapering U or a jar), H-1514 (a D with a single slash), H-1462 (a human stick figure). In the fifth, H-246, we have the four symbols in the following order right to left—three strokes, jar, slashed D, stick figure. If the Indus language were agglutinative and H-246 were an agglutinative compound, the three strokes symbol must be the root and the remaining three, the various affixes. But that can’t work because an agglutinative affix cannot survive as independent word as seems to be the case in H-1462, H-1514, and H-1546. Also, the order cannot flip in a different construction. If the order of affixes in H-246 is jar, slashed D, and stick figure, right to left, it must stay that way in all usage. But in H-894, the paper notes the same morphemes in a different order—slashed D, stick figure, and jar, right to left. Therefore, it’s evident that H-246 and H-894 are not agglutinative but inflective.

Another example is a Dholavira specimen that features a sectored circle, double apostrophes, four vertical strokes, and a crude trident, right to left. The last two of these symbols, the four strokes and the trident, also appear together and in the same order in the independent B-9. Again, the latter’s independent occurrence proves that it could not be an agglutinative affix. The paper further assumes the jar symbol to be a case marker when in a terminal position, as in H-1953 (fish, two vertical strokes, jar, right to left). In this example, that makes the combination fish and two strokes the root or stem. In M-1706 (wheel, two apostrophes, fish, two strokes, fish, trident in circle, and jar, right to left), the same combination appears without the jar, but a different combination (fish and trident-in-circle) keeps it.

The paper interprets M-1706 as a compound of three stems with the terminal jar declining the case for the whole compound, a feature not characteristic of Dravidian but commonplace in Sanskrit. Dravidian, being agglutinative, avoids compounds that involve more than two stems. Think of it as how English is okay with two-part compounds like schoolbag or horseback, but nothing more, whereas German can take something like _Lebensversicherungsgesellschaft_ (life insurance corporation) without a fuss.

Closer home, consider காட்டுமரம் (_kāṭṭumaram_). It’s a perfectly acceptable compound of காட்டு, meaning forest, and மரம், meaning tree—wild tree. But if we were to refer to a flower of a wild tree, காட்டுமரம்பூ would no longer work and we need three separate words, காட்டு மரம் பூ (_kāṭṭu maram pū_). On the other hand, Sanskrit is totally comfortable even with something like _nāgarājaputrakumāra_ or the “the prince son of the serpent king.”

The paper also contends that while Sanskrit is fine with repeat syllables, mostly double but sometimes even triple, Dravidian isn’t. Which is problematic for the latter because the Indus inscriptions are replete with repetitive signs, such as H-210 (two jars side-by-side) or H-1182 (two triple-strokes side-by-side).

The paper argues not only for Sanskrit but also Brahmi, the precursor to modern Devanagari. It posits that the Indus script was some kind of proto-Brahmi which makes sense if we admit the language being Sanskrit or anything Indo-Aryan. A most compelling support for this claim comes in the shape of a terracotta seal from the ancient city of Vaishali. Dated to the Śunga period (185–75 BC), the specimen bears three symbols with at least two readily identifiable as Indus script artifacts.

[![Book page image](https://substackcdn.com/image/fetch/$s_!w4IY!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff25aced2-a9b2-41d4-b904-8c001c759fd2_1231x1547.jpeg)](https://substackcdn.com/image/fetch/$s_!w4IY!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff25aced2-a9b2-41d4-b904-8c001c759fd2_1231x1547.jpeg)**Fig. 1** : Seals and tokens recovered from excavation sites in Vaishali, most going back almost 2,000 years; no. 24 bears three symbols reminiscent of the ancient Indus script. [courtesy B. P. Sinha and Sita Ram Roy in _Vaiśālī Excavations, 1958–1962_ , Directorate of Archaeology and Museums, Bihar, 1969, plate XXX.]

The appearance of Indus symbols more than 1,800 years after the purported decline of the civilization is a strong indicator of at least some kind of cultural continuity. Not to mention the geographical expanse of its influence. Could the Indus script be some kind of primordial Brahmi? A precursor? The paper certainly favors that conclusion. And if the script could be Brahmi, why couldn’t the language be Sanskrit?

## Methodology

So where does one begin? In the most simplistic of terms, one character at a time. Applying Shannon’s cryptographical methods to script decipherment, we start with a fundamental premise—when deciphering a sequence of symbols, it’s the arrangement thereof that matters and not the individual symbol’s shape, appearance, or history. For instance, if the inscription says “cbmm,” all that matters is that it’s composed of three letters with one being repeated for the last two places. It doesn’t matter whether it looks like “cbmm” or “bzkk.” The pattern matters. Because it’s the pattern that tells us that if the text were to be read in the English language, “ball” is a stronger possibility than “pin” or “gate.”

Let’s illustrate this concept and its application better with the famous “Aristocrat” cipher, named so by the American Cryptogram Association. It’s a simple substitution cipher and this is what it looks like:
    
    
    UTAK QYK UTYU SGGE RWESIAPU LGIAQ VDGI AJBADOAPLA, YPE AJBADOAPLA, HAXX UTYU LGIAQ VDGI ZYE RWESIAPU.

The solution we’re about to study appeared on an online Perl programming forum in 2007.1 The approach is straightforward. Identify a short segment with a distinctive pattern like a repeated letter or a specific sequence and compare it to a list of English words exhibiting the same pattern. This method narrows down potential matches efficiently by leveraging the structure of the text rather than guessing randomly.

The first pattern that stands out is HAXX—a four-letter sequence where the third and fourth letters are the same. Now this pattern needs to be looked up against a list of valid English words, a dictionary file named `Words.knu`. In programming, such lookups are performed using a technique called regular expressions or “regex,” a sequence of characters that forms a search pattern. It is used in programming to match, locate, or extract specific parts of text based on rules defined by the pattern. A tutorial on regex is beyond the scope of this discussion so we’ll just move on to the solution. This is what the expression for HAXX looks like:
    
    
    ^..(.)\1$

This tells the interpreter to match any four-letter word where the third and fourth letters are identical. The caret marks the start of the string, the two dots represent any two characters in the first and second positions (think wildcards), the parentheses and dot capture the third character, the “\1” ensures the next one character matches the third exactly. The dollar sign signals the end of the string, restricting the match to four letters total. When applied to `Words.knu`, this regex might return words like “ball,” “tree,” or “mitt,” which fit the HAXX pattern.

Used in a Perl statement:
    
    
    perl -ne "print if m/^..(.)\1$/;" Words.knu

An excellent place to test out expressions like this without writing computer programs is a website like <https://regex101.com>.

Now this regex returns all words that match the pattern, which significantly narrows down our search. Which can be further reduced if we eliminate options like “lull” because in the HAXX pattern, the first and second letters must be unique. We can further finetune our regex to exclude words like lull:
    
    
    ^([a-z])(?!\1.*)([a-z])(?!\2.*)([a-z])(?!\1)(?!\2)\3$

In a similar fashion, other expressions can be used to interpret other patterns. Results can continuously be refined until coherence is achieved. For example, we know YPE cannot be “toy” if HAXX is “tree” even if the pattern fits, because the first letters of the two words cannot be identical.

This is, at its essence, how dictionary lookup works. Of course, Perl is just one of several choices at our disposal. Such scripts could just as easily be written in, say, C++. Or Javascript. Or even PHP. In fact, scripting isn’t even a necessity, it just makes the job much faster. These lookups can grow impractically tedious very quickly.

So we now have the methodology, and we have the language—Sanskrit. The objective is simple. Use the methodology to look up Indus words in a Sanskrit dictionary like Monier-Williams and examine the result for coherence. If successful, admit Sanskrit as the language of the Indus and some kind of proto-Brahmi as the script. This is a perfectly acceptable way of deciphering a script without a “Rosetta stone.” It’s extremely unlikely for the same script to be coherent in two distinct languages. Yajnadevam makes the following assumptions for the purpose of his study:

  1. Sanskrit, like any natural language, has a redundancy of around 70%.

  2. The Indus people spoke a Sanskrit that was post-Vedic but not yet Classical.

  3. Indus consonants did not have the implicit /ə/ or _virāma_.

  4. The Indus script did not differentiate between aspirated and unaspirated sounds, as is still the case in Tamil where த represents both त or /t̪/ and थ or /t̪ʰ/ sounds.

  5. The Indus script did not differentiate between dental and retroflex sounds, as was once the case in Tamil where த represents both त and ट or /ʈ/ sounds, although modern Tamil prefers ட for the latter.

  6. The Indus script did not differentiate between voiced and unvoiced sounds, as is still the case in Tamil where க represents both क or /k/ and ट or /ʈ/ sounds, although modern Tamil prefers ட for the latter.

  7. The Indus script had a single symbol for all sibilants, as is still the case in core Tamil where ச represents both /s/, /t͡ʃ/, and /z/, with ஷ and ஸ being later Grantha additions.

  8. The Indus script uses single consonants for doubles, so for example, _bitter_ would be rendered as _biter_.




Inscriptions with repeat symbols are particularly useful. Remember the total entropy of an inscription reduces with each new piece of decipherment. Equivocation is a direct measurement of the gap between the falling entropy and the accumulating decipherment, and it’s effectively zero once the text has been fully deciphered. Naturally then, repeat symbols reduce the total amount of randomness possible in the system because there are fewer symbols to be decoded. The more the frequency of such repeats, the lower the equivocation. Thus, HAXX has a lower redundancy than HAXY, because there’s fewer possibilities with the former than with the latter.

Another crucial assumption Yajnadevam makes pertains to the size of the character-set itself. Since the inscriptions in question were handmade, it follows that no two renditions would be visually identical as is the case in print. Even the same individual can write the same letter slightly differently at different times. Thus, the assumption is that most symbols in the Indus script are but variants of the same letter and not different letters. For example, the fat jar symbol is the same thing as the slim jar symbol, which is the same as the jar symbol with any number of short vertical strokes. Similarly, the concave stroke is the same thing as the convex stroke, just flipped depending on the writing direction. This is mostly right to left, but sometimes also left to right or even boustrophedon. Some symbols are also organic simplification or abstraction of other more complex symbols.

## First Letter

Having established the ground rules, Yajnadevam proceeds to crack the code, one letter at a time. Each cracked symbol is a reduction of equivocation bringing us that much closer to a final solution to the Indus script. For obvious reasons, it makes sense to start with the symbol that has the highest frequency, in this case the jar, as first noted by G. R. Hunter who performed the first statistical analysis of the script nearly a hundred years ago.2 Hunter also noted that the sign is more likely to be in a terminal position than otherwise.3 Yajnadevam resolves it to the _anusvāra_ , a nasalization marker in Sanskrit and its descendants, when in terminal positions. In Devanagari, we represent the sound with a dot above the phoneme being nasalized. When the jar appears in non-terminal positions, he assigns it the sound of न or /n/. Thus, the three jars in H-764B are read as अननम् or /ananaṃ/, the accusative declension of अनन or /anana/, meaning “face.”

The jar symbol gives us a good jumpstart by automatically shaving off equivocation from a number of Indus inscriptions that contain the symbol. All we now need to do is plug the value wherever the symbol occurs and use regex to derive the rest. The more symbols we have guessed correctly, the fewer variables remain to be guessed with regex.

Keeping all caveats in mind, the algorithm ultimately reduces the entire Indus character-set to a total of just 24 glyph-sets. Down from hundreds. Earlier, Bryan Wells had counted almost 700 symbols and even a conservative Iravatham Mahadevan had kept it above 400. Yajnadevam’s algorithm flattens most of the symbols as variants of the same phoneme, either handwriting variant or evolutionary abstraction, to leave us with 24.

[![](https://substackcdn.com/image/fetch/$s_!wfC7!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F05cc677e-d9c3-4c5a-afee-ec91ee4aea40_680x723.png)](https://substackcdn.com/image/fetch/$s_!wfC7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F05cc677e-d9c3-4c5a-afee-ec91ee4aea40_680x723.png)**Fig. 2** : The entire Indus glyph-set is down to 24 distinct phonemes in Yajnadevam’s paper. [courtesy Sreenivasarao Vepachedu in “A Cryptanalytic Decipherment of the Indus Script,” November 2024, p. 20.]

Speaking of jars, the glyph has one more reading besides nasalization, in Yajnadevam’s theory—as a direction marker. Remember, Indus inscriptions, while mostly right to left, could also be sometimes left to right or even more confusingly, bidirectional. The latter, better known as boustrophedon, is quite common with ancient inscriptions including Linear B and Egyptian. So how does the reader know which way to read?

As Yajnadevam rightly posits, this is primarily a problem with shorter inscriptions rather than longer, because the longer the text, the less likelihood of its being meaningful in the wrong direction. Take “I go home,” for instance. Read in the wrong direction, “emoh og I” makes no sense whatsoever. But if we take a much shorter “tip,” we still have an equally meaningful “pit” when flipped. An even shorter “I” is impossible to misread in either direction. Therefore, the Indus script must have some kind of a direction marker, and these direction markers would be far more necessary in longer inscriptions than in shorter ones. So which glyph is that marker? Turns out, it’s the jar. So, depending on the context, the same jar can serve two completely unrelated functions.

As a direction marker, the jar sign comes with two or more strokes, either on the rim or within. If there’s two or more jars with varying number of strokes, the reading direction is from more strokes to less.

With these pieces in place, it’s possible to run the corpus through a series of regex matches to arrive at a viable solution, which is exactly what Yajnadevam has done for his paper. To demonstrate the success of his methods, he even presents us an exhaustive list of deciphered texts along with their Sanskrit equivalents. This includes both short and long specimens.

While this is remarkably meticulous work and deserves all the applause coming its way for scholarship and rigor, a whole host of issues put a dent on the paper’s conclusions. And the first such issue is the sheer volume of arbitrary assumptions necessary to maintain the intended reading.

## Unicity Distance for Indus Sanskrit

We know that a viable decryption demands a minimum number of ciphertext symbols, something known as unicity distance. We’ve already learned its calculation, but to refresh memory, it’s the redundancy of the assumed language (_ρ_) divided into the size of the ciphertext (_N_), i.e. the number of unique symbols in the specimen to be decrypted:

Yajnadevam assumes a blanket _ρ_ of 0.7 for all natural languages. For _N_ , he starts with Mahadevan’s 417—that’s the total number of symbols in the Indus glyph-set. Of these, he identifies 124 as ligatures or combinations of two or more symbols, such as æ in Latin and क्ष in Devanagari. Which leaves him with 293 unique symbols. Now since a number of symbols carry more than one sound, the need to be counted more than once. For instance, since the same cross symbol represents both क or /k/ and ख or /kʰ/, it ought to be counted twice. Similarly, the same symbol represents multiple sibilants. Or the same symbol gives us both aspirated and unaspirated variants of the associated phoneme. Considering these examples, the author adds another 37 to the original 293, for a final value of 330. With a redundancy of 0.7 for Sanskrit, we get a unicity distance of roughly 471.

Which means we need a corpus of at least 471 symbols in order to ascertain any decipherment for validity. The 50 longest inscriptions, each with a minimum length of ten glyphs, give us a total of 500 symbols. We have comfortably more than the required volume.

The calculation seems sound at first glance, but one ought to wonder whence the 37. The paper takes 30 unaspirated and 20 dental signs for a total of 50. That’d imply 30 aspirated counterparts and another 20 retroflex for a total of 50 corresponding modifications. Then the author calculates 10% of this to arrive at 5 additional glyphs. The paper does not explain the reasoning behind this assumption. Why 10%? We don’t know. Even the assumption that the same sign stood for both aspirated and unaspirated, or dental and retroflex is just that, an assumption.

Another inexplicable assumption is a redundancy of 0.7 for all natural languages including Sanskrit. Let’s see if the value holds. The total number of phonemes in Sanskrit is 48 which gives us a theoretical maximum entropy of 5.58 bits/letter:

for a redundancy of 0.7 or 70%, the actual entropy would have to be

For reference, we had earlier calculated a value of 1.5 bits per letter for English. The paper does not shed any light on how the value of 1.67 was arrived at for Sanskrit. This matters because even a slightly different value here can greatly alter our unicity distance for the Indus script. For example, keeping the character-count to Mahadevan’s 417 and changing actual entropy for Sanskrit to just 1.8, we get a unicity distance of 616. Which is more than just 50 longest inscriptions with 10 glyphs each, as stipulated by Yajnadevam.

## Glyph Reuse

As already noted, Yajnaveam starts off with the axiom that a large number of Indus glyphs render multiple phonemes. In 2.10.5, he places the Meluhhan dialect between Vedic Sanskrit and Classical Sanskrit. As for the script, he likens it to Tamil Brahmi, seeing the Indus script as some primordial form of what would eventually become Brahmi.

So, the first assumption is that of the same symbol serving both unaspirated and aspirated sounds. This is analogous to Tamil having a single த to represent both त or /t̪/ and थ or /t̪ʰ/ phonemes. But that’s because Tamil does not have the /t̪ʰ/ sound natively. So, it never needed to have a separate representation for it. Sanskrit, on the other hand, makes clear distinction between /t̪/ and /t̪ʰ/. This was the case in Vedic Sanskrit, and this is the case in Classical Sanskrit. In which case it only makes sense that should there be a script, the two sounds would have two distinct glyphs. Expectedly, Brahmi honors that distinction and represents /t̪/ with a vertically flipped “Y” symbol and /t̪ʰ/ with a circle that has a dot in the center. What Yajnadevam seems to be saying here, is that we first had a script that didn’t make that distinction (Indus), which evolved into a script that does make that distinction (Brahmi) and another that doesn’t (Tamil). Another interpretation would be that the language started off making that distinction in Vedic Sanskrit, then forgot it in Indus, and then returned to making the distinction in Classical Sanskrit. However one slices this, the Indus language cannot be post-Vedic Sanskrit on this ground with a script that aligns with Tamil.

Another reason the Indus script cannot be post-Vedic is that it’d make the Rigveda older than 3000 BC, something not supported by evidence. For more, refer to the article on Aryans.

* * *

* * *

But we won’t dwell on that and move on to other discrepancies with glyph reuse. One such occurs in the specimen labeled H-101a. Read right to left, it consists of three symbols—a left-facing hangman scaffold, a jar with a trident on either side, and a jar with two horizontal strokes on either side. In short, scaffold, jar with tridents, jar with strokes. As per his list (fig. 1), this should be p, r, and an or aṃ. The terminal jar, according to 2.12, is basically an anusvāra (rendered with a dot above the letter in Devanagari) if after a vowel and /an/ otherwise. The word should thus be either परं /paraṁ/ (if anusvāra), or परन् paran (if /an/). Neither of which make any sense in Sanskrit. One reading that does make sense is पर्ण /parṇa/, Sanskrit for “leaf.” This is what Yajnadevam posits. But his own list does not assign any glyph to ण, the reroflex /ṇ/, least of all the jar symbol. Of course, this is the only reading where the inscription makes any sense whatsoever in Sanskrit, but here’s the thing—it doesn’t have to. What we’re doing here is bending it to conform to Sanskrit, then using this conformation to prove that it’s Sanskrit. Somewhat of a circular reference.

Even if we accept his caveat of shared glyphs between retroflex and dental in Indus, the jar symbol does not feature as dental /n/. Again, a script meant for Sanskrit would have no reason to not distinguish between न and ण. Which is why Brahmi does it, as does modern Devanagari and even Tamil (ந vs. ண).

In the same vein, we have M-734 where Yajnadevam reads the standing hat symbol as ण instead of न because that’s the only way the text resolves to a valid Sanskrit word. Admitting glyph reuse between न and ण, as he spells out in 4.10, satisfies Yajnadevam’s अननं /ananaṁ/ for the three jars inH-764B, but makes one wonder why the same ण would be rendered as a completely unrelated standing hat glyph in M-734. Even if we were to make concessions for handwriting variations or evolutionary abstraction, no conceivable line can be drawn between the jar and the standing hat. They have nothing whatsoever in common.

In 4.9, he reiterates the glyph reuse for dental and retroflex consonants and offers as example, the Latin rendition of Sanskrit where the letter “t” stands for both त and ट. The analogy, however, is incorrect because Latin does not have the retroflex ट sound whereas Sanskrit does. Latin has no reason to invent a new character for a foreign sound, whereas Brahmi or Devanagari have no reason to use the same letter for both sounds when rendering Sanskrit. Tamil too makes that distinction with த for त and ட for ट.

Back in 2.10.5, Yajnadevam speaks of flattening all sibilants, i.e. using the same symbol for all s-related sounds—/s/, /t͡ʃ/, /z/, /ʃ/. But in the final list, he singles out च or /t͡ʃ/ with a separate glyph. But Old Tamil did not even have sibilants other than /t͡ʃ/, represented by ச. All the sibilants that we see today—ஸ, ஷ, ஶ, க்ஷ—entered the language with the post-Sangam extension under the influence of Sanskrit. We call this extension, Grantha. If the Indus script was a precursor to Tamil Brahmi, it would mean the language spoken by the Meluhhans started off with separately rendered sibilants as attested in Vedic Sanskrit, then reduced to a single rendition for all sibilants in the “post-Vedic” Indus Sanskrit, then again acquired separately rendered sibilants in the Brahmi of Classical Sanskrit while losing all of them in the Tamil Brahmi of pre-Grantha Old Tamil. This does not sound very organic. If the language never lost the sounds, why would the script stop rendering them, only to revert after a while? Is the Indus script analogous to Tamil Brahmi or is it not? We cannot entertain both possibilities at once. Let’s explore this deeper with a real Tamil Brahmi specimen.

## Keezhadi Potsherds

In 4.16, Yajnadevam calls Keezhadi Tamil Brahmi specimens an evolved form of Indus script without much in the way of evidence. The reference he cites for this claim is a document on the subject issued by the Tamil Nadu government’s Department of Archaeology in 2019.4 This pertains to a cache of potsherds recovered from the eponymous site bearing short post-firing inscriptions. The document identifies the script as Tamil Brahmi, a fact not disputed by anyone including Yajnadevam. Now, one of the inscriptions looks remarkably similar to and has been read as the following Tamil Brahmi letters:

𑀫𑀱𑀉𑀅

If read independently in accordance with the sound values listed by James Prinsep in his 1858 paper, the letters render _ma-ṣa-u-a_5 which makes no sense at least in Sanskrit. But what if we read it right to left, as if it were an Indus inscription? Then we get _a-u-ṣa-ma_ , which still means nothing. But this is what Yajnadevam does with a slight tweak—he reads 𑀉 as _ru_ instead of _u_ , and elides the terminal schwa turning _ma_ into _m_. This way he arrives at अरुषम् _aruṣam_ , a perfectly valid word in Sanskrit. It’s the accusative declination of अरुष, Sanskrit for “reddish.”

[![](https://substackcdn.com/image/fetch/$s_!8Ct4!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fef7f36b4-761e-4188-8c22-930cca715816_488x665.png)](https://substackcdn.com/image/fetch/$s_!8Ct4!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fef7f36b4-761e-4188-8c22-930cca715816_488x665.png)**Fig. 3** : A graphical rendition of some Tamil Brahmi inscriptions recovered from Keezhadi in Tamil Nadu, including a specimen (top row, center) read by Yajnadevam as _aruṣam_. [courtesy R. Sivanantham and M. Seran in _Keeladi: An Urban Settlement of Sangam Age on the Banks of River Vaigai_ , Department of Archaeology, Government of Tamil Nadu, 2019, p. 56.]

While अरुष makes perfect sense, Yajnadevam tells us nothing about how he came up with the र in an inscription where no symbol corresponds to the sound by any stretch of the imagination. Brahmi renders the rhotic sound with 𑀭, a simple squiggly staff with no horizontal tail. Only by 150 AD (Girnar inscription) we start seeing a tail but that too is in the opposite direction, much like the English “J.” In no rendition does the rhotic sound take the right turn as in 𑀉.

Many papers, including the one by Sivanantham and Seran, insist a continuity between the Indus script and Brahmi, something Yajnadevam too insists. But so far, every such claim has been extrapolated from an infinitesimally tiny handful of visual similarities. Sivanantham and Seran, for instance, list a total of five Tamil Brahmi letters that seem to resemble Indus glyphs. Out of more than 40 Brahmi letters and more than 400 Indus glyphs. That’s far from sufficient to draw lasting conclusions, but even if that were admitted, we still have little basis to read Sanskrit into the renditions.

Now let’s look at some of Yajnadevam’s translations and examine their viability. Because if the reading checks out and enough number of Indus specimens are proven to express valid Sanskrit texts, the decipherment becomes not only tenable but also a frontrunner in the race to the final solution. But what does enough mean here? We’ll get to that question later, first let’s examine some translations.

## The Vedic Attestations

Among the longest Indus inscriptions discovered so far, according to Steve Farmer, is M-314.6 Yajnadevam gives us the following transcription, reading right to left:

रवामम्‌ मन सक्षनरं जठलधार रह  
 _rava-amam mana sakṣa-naraṃ jaṭhala-dhāra raha_

Which makes no sense in Sanskrit on face value but can be read as such with a little creativity. Before that, however, let’s see if his list (fig. 1) supports this reading. The first discrepancy that jumps out is the third glyph from the right. It’s a fish with a hat on top and two horizontal stripes across its body.

[![](https://substackcdn.com/image/fetch/$s_!h-e4!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F74288e68-d712-4887-95f5-f23631c23dea_447x241.png)](https://substackcdn.com/image/fetch/$s_!h-e4!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F74288e68-d712-4887-95f5-f23631c23dea_447x241.png)**Fig. 4** : The three fish symbols in M-314. [courtesy Yajnadevam in _A Cryptanalytic Decipherment of the Indus Script_ , Nov. 2024, p. 33. Preprint.]

The table of interpretations (fig. 1) does not list this variant as a separate glyph, although it does list two fish variants, one with two fins and the other with four, against म /m/. This would generally not be a problem but the fact that he reads two only slightly different variants of the jar symbol differently, assigning one with two tridents to र and one with horizontal strokes to an entirely unrelated /an/ or anusvāra, makes the decision a bit arbitrary. Also, stylistic variations are understandable when the text is written in multiple hands or when a glyph has evolved, simplified, or reduced over time. But here we have two different “variants” of the same glyph in the same inscription. We have no reason to believe it was not inscribed by a single person in a single sitting.

There is a similar discrepancy in his reading of क्ष as a ligature of क and ष. He reads as क a glyph that does not even appear on his list. The closest he has is a glyph for ग that lacks the horizontal line expressed in the M-314 variant. A variant does appear against क as well, but it features three horizontal lines on the outside, making it more distant than the ग variant. Again, the choice to read it as क rather than ग seems quite arbitrary.

Now let’s look at the transliteration itself. While it doesn’t on its own make any semantic sense, Yajnadevam reads it as a rendition of verse 5.45.10 from Rigveda:

“Honor the powerful Roarer. O Sustainer, O Ocean (Shiva) yield to the capable man.”

He offers a number of lexical derivations used for arriving at the conclusion, such as जठल meaning “ocean,” and so on. We won’t get into that here. But we will get into RV 5.45.10:7

Text within this block will maintain its original spacing when published
    
    
     _ā sūryo aruhac chukram arṇo yukta yad dharito vītapṛṣṭhāḥ,
    udnā na nāvam anayanta dhīrā āśṛṇvatīr āpo arvāg atiṣṭhan._
    “The Sun has mounted the gleaming flood, now that he has yoked his golden, straight-backed (horses).” (trans. Jamison)

As evident, the actual meaning of the verse is entirely divergent from what Yajnadevam posits. There’s no Shiva in the actual and no Sun or horse in Yajnadevam’s. But our “actual” is based on translation by Stephanie Jamison, an American. One might—and very wrongly so—dismiss her reading for its American gaze. So, what do Indian translators say? Here’s Dayananda Saraswati:8

Text within this block will maintain its original spacing when published
    
    
     _हे मनुष्यो! (यत्) जो (सूर्य्यः) सूर्य्य (शुक्रम्) वीर्य का (आ, अरुहत्) आरोहण करता और (अर्णः) उदक का (अयुक्त) योग करता है और (वीतपृष्ठाः) व्याप्त हैं लोकान्तरों के पृष्ठ जिनसे वे (हरितः) जल आदि को हरनेवाले (धीराः) ध्यानवान् बुद्धिमान् जन (उद्ना) जल से (नावम्) नौका को (न) जैसे वैसे (अनयन्त) प्राप्त होते अर्थात् व्यवहार को पहुँचते हैं (अर्वाक्) पीछे (आशृण्वतीः) जो चारों ओर से सुन पड़ते हैं वह (आपः) प्राण (अतिष्ठन्) स्थित होते हैं, उस सब को आप लोग जानें._
    “O mortals! That which the Sun ascends with its radiance, and which joins with the waters—those [realms] whose backs are traversed by the discerning, mindful men who, like navigating a boat through water, reach their course through practical action—those resound from all around. The waters, the life-breath, are established there. May you all come to know this.”

Again, no Shiva, not even a tangential reference. In Yajnadevam’s reading, the verse addresses the ocean (assumed to be Shiva with reference to the _Mahabharata_ for some reason). In the original, it addresses humans.

Next up is M-23 which comes from another Mohenjo-daro seal and is read by Yajnadevam as:

दाममन कंसं नः रन्धन  
 _dāma—mana kaṃsaṃ naḥ randhana_

Again, the Sanskrit equivalent is given as a composite of RV 2.37.2 and 10.112.6:

“Great Giver, this cup is for us, O Shiva.”

Here again, Yajnadevam interprets two completely dissimilar glyphs for the same phoneme, the anusvāra. The one with क features two strokes, one longer and curved and the other shorter and straight. His list assigns this one to म. Right after we have another anusvāra with स that features the expected jar symbol. Now, it’s still possible to express the anusvāra with a म phoneme as can be seen in words like _Saṃskṛta_. But the choice of expressing one anusvāra with the jar that’s closer to the /n/ sound and another with a full-fledged म sound is, once again, inexplicably arbitrary.

The next symbol is the standing hat which has been transliterated as न. Remember, the same symbol was interpreted as ण in M-734. Yajnadevam’s list assigns no fewer than a dozen different glyphs, including the standing hat, to the phoneme. But none to ण. He explains this with his caveat of interchangeability between dentals and retroflexes. One has, at this point, reasons to wonder why. If the speakers recognize the two sounds as different and they have a dozen symbols for it, why would they interchange? Why not assign an independent glyph to ण to avoid ambiguity? The interchangeability works if one of the phonemes came from a foreign register, or a symbol disappeared over centuries. But here we have, in the same specimen, two other instances of न represented not by the standing hat but by a broken vertical stroke. Now let’s examine the Rigvedic reference.

Yajnadevam attributes his derivation to two Rigvedic verses, 2.37.2 and 10.112.6. From the former, he derives _dāman_ or “the Great Giver.” Here’s the verse:9

Text within this block will maintain its original spacing when published
    
    
     _yam u pūrvam ahuve tam idaṃ huve sed u havyo dadir yo nāma patyateadhvaryubhiḥ prasthitaṃ somyam madhu potrāt somaṃ draviṇodaḥ piba ṛtubhiḥ_
    “The one I invoked previously, him I invoke right now. Just he is to be invoked, who owns the name ‘Giver.’ (trans. Jamison)

The word is _draviṇodaḥ_ , a compound of _dravina_ (wealth) and _dā_ (to give). This word has universally been translated as “The Giver.” But who _is_ this giver? A reading of the previous hymn tells us that it could be Indra, Mitra, or Varuna. Keep this in mind as we now take up 10.112.6, the other piece of the puzzle:10

Text within this block will maintain its original spacing when published
    
    
     _idaṃ te pātraṃ sanavittam indra pibā somam enā śatakrato,
    pūrṇa āhāvo madirasya madhvo yaṃ viśva id abhiharyanti devāḥ._
    “Here is your cup acquired of old, Indra: drink soma with it, you of a hundred resolves. The trough is full of exhilarating honey, which all the gods delight in.” (trans. Jamison)

This, again, is an invocation to Indra to accept the libation of soma which is described as a favorite of all gods. This time Indra is mentioned by name, not just an epithet like “The Giver.” Now, let’s revisit Yajnadevam’s rendition of M-23:

“Great Giver, this cup is for us, O Shiva.”

There is no Shiva in either of the verses he references. Where does he get the Shiva from? He arbitrarily interprets _mana_ in _dāmamana_ as _mahān_ (great), and just as arbitrarily decides that this Great Giver” must be Shiva and not Indra as indicated in the Rigveda itself. But this isn’t all. He further inverts the whole action by making humans or rather priests the intended recipient of the cup (“this cup is for us”) whereas the original is clear of the recipient being Indra.

Neither the inscription nor the verse gives even a semblance of a hint that it could be Shiva. Why would such an assumption be made then? Perhaps an attempt to lend legitimacy to the interpretation by connecting the inscriptions to the famous “​Pashupati” seal that has often been assumed to represent Shiva?

Let’s do one more before we move on to the next section. This time, we’ll pick a short one, M-1123. This one’s also from a Mohenjo-daro seal and is expressed with four trident glyphs and a final symbol that resembles a balance scale or a shoulder pole, the kind Shravana Kumara carried his parents in. This specimen stands out for its glyph quadrupling. Yajnadevam’s list assigns the trident to र and the scale to य, which gives us ररररय or _rarararaya_. If this does not make any sense, recall that ancient scripts did not have spaces between words. So this could be ररररय, रर ररय, रररर य, रर रर य, or any such permutation. Yajnadevam tries the second—रर ररय—but adds a terminal म् even though the inscription does not feature any m-related glyph, to make it रर ररयम्. In his defense, he does place this additional letter within brackets perhaps to indicate its status as a later addition—रर ररय[म्]. But why would he do that? Are रर and ररयम् valid words?

So, रा is a valid Sanskrit verb, it means “to bestow or grant.” And one of its conjugations in the perfect tense is रर (given). This is also how Yajnadevam interprets the first word. That leaves us with ररयम्, if we continue to ignore the arbitrariness of म् here). This, Yajnadevam splits between र and रयम्. Now what could र possibly mean? Monier-Williams gives it multiple meanings, among them “possessing” and “speed.” You can only take one. Yajnadevam goes with the former. For रयम्, he assumes speed, which Monier-Williams affirms. The terminal म् still seems unnecessary, though, because MW does list रय for speed. The final expression by Yajnadevam’s transliteration is now:

“Given possessing speed.”

Which he likens to RV 2.31.2:11

Text within this block will maintain its original spacing when published
    
    
     _adha smā na ud avatā sajoṣaso rathaṃ devāso abhi vikṣu vājayum,
    yad āśavaḥ padyābhis titrato rajaḥ pṛthivyāḥ sānau jaṅghananta pāṇibhiḥ._
    “Then help out our chariot, you gods of one accord, as it seeks prizes among the clans, when the swift ones, crossing through the airy realm with their strides, keep trampling on the back of the earth with their forefeet.” (trans. Jamison)

While the verse being about chariots and speed gives an impression of relevance, not without difficult questions. This verse is Vedic Sanskrit. According to Yajnadevam, the Indus tongue was post-Vedic dialect but pre-Classical. Also according to him, in 4.2, Indus seals use concise Vedic snippets as mottos or slogans, as we still do with expressions like _satyameva jayate_. M-1123, therefore, can be seen as a concise form of RV 2.31.2. But the RV verse does not use the root रा in any conjugation. Nor is it used as a noun to indicate speed. It instead uses _āśava_ (horse) as a metaphor for speed and does not even have the verbs “give” or “possess” in any form. Also, the sense of speed for रय comes not from the Vedas but the Puranas, as indicated in MW and also noted by Yajnadevam. Which makes it a word of Classical lexicon. The entire Puranic corpus has been confidently placed within the Common Era, coming thousands of years _after_ the Indus civilization.

## Other Problems with the Decipherment

Yajnadevam’s approach, as we have understood by now, is to assume that the Indus script represented a language and not, say volumetric figures or trade markings, and that language was Sanskrit. While this is already one too many assumptions, it does not invalidate the method itself because that’s how cryptography works. So far so good. But then we’ve also seen him make a number of arbitrary assumptions in glyph assignment. At times two completely dissimilar glyphs have been assigned to the same phoneme, at other times two almost identical glyphs have been given phonemes that sound nothing like each other. This is what we call curve-fitting.

Then there’s also a whole lot of anachronisms. Every living language undergoes change with time. The English spoken today is little like the English spoken 400 years ago. Chaucer’s English is not even intelligible to the average English speaker today. Even less so is the English of Beowulf. They might as well be two different tongues. Even in the case of Sanskrit the Classical dialect is already different enough from its Vedic predecessor to warrant a distinct nomenclature. And that’s with a gap of barely a thousand years. Sure, Classical Sanskrit has remained static to this day, but that’s only because the masses don’t speak it, haven’t in well over a thousand years. For a language to evolve, it ought to be alive, in currency—it ought to be the lingua franca.

The Indus civilization spanned well over 2,000 years. No living language can remain unchanged for that long. If the Indus people spoke Sanskrit, they could not have spoken the same Sanskrit throughout this period. And they could not have spoken the same Sanskrit in all cities. Dialect changes every few miles and almost becomes unintelligible after a certain distance. The Indus civilization spanned an area larger than Mesopotamia, the Golden Crescent, and Egypt combined. It’s absurd to think people in Harappa spoke the same tongue as those in Lothal. Yajnadevam uses Monier Williams as his key space. That is, he references words in MW to identify words Indus inscriptions as Sanskrit. But MW’s lexicon is good for Sanskrit as we know it. Do we have any reason to assume that people who lived 5,000 years ago used the same words that appear in a dictionary compiled in 1872? Sanskrit might be dormant today, but it wasn’t always.

Another problem is his dismissal of Dravidian as a possibility. While it isn’t necessarily (there’s a whole body of politics around curve-fitting Dravidian into the Indus language, but that’s for another day). But to dismiss it wholesale as even a possible candidate, one must offer some grounds. Yajnadevam does.

If the Dravidian lexicon lacks a word for something known to be ubiquitous in the Indus civilization, it’s a clear contraindication against a Dravidian reading of the script. If the same things do have names in Sanskrit, it further weakens the case for Dravidian and strengthens Sanskrit. Yajnadevam offers a couple of examples in this regard. One of them is _ūru_ , the word for city. He claims that the word entered Dravidian from Prakrit. In other words, the _-uru_ in names like Bengaluru and Mysuru, the _-oor_ in Kunoor, and the _-ur_ in Sriperumbudur are all borrowed from Prakrit. Isn’t it strange then that Sanskrit itself has no _ur_ in its lexicon? Yes, it has _pur_ , but that has nothing to do with ur. Even if one were to assume it did, what could possibly be the reason that the _p_ vanished in all Dravidian renditions? No reason. There is no evidence to support Yajnadevam’s claim that ur was a Prakrit or Sanskrit borrowing. In fact, pur did enter Dravidian with the later Aryans, with its _p_ intact, which is how we still have plenty placenames ending in _-pūram_.

He similarly posits that Dravidian lacks a native word for “brick,” an indispensable aspect of Indus architecture. Sanskrit, on the other hand, has _iṣṭikā_ from which we get Hindi _īṭ_. But this isn’t entirely true either. He perhaps bases his claim on Kannada ಇಟ್ಟಿಗೆ _iṭṭige_ , Telugu ఇటుక _iṭuka_ , and Malayalam ഇഷ്ടിക _ishtika_ , but there’s also Tamil செங்கல் _ceṅkal_. Since this is a compound of செம் (red) and கல் (stone), one might take it as a non-native construct, but that conclusion isn’t necessarily absolute. The Sanskrit word itself traces back to _iścem_ , the Tocharian word for not just brick but also clay.

A most glaring question this whole idea of Indus Sanskrit raises is that of continuity. Specimens like the Vaishali coin indicate some “continuity” between scripts (Indus and Brahmi), but it does not say anything about language.

* * *

* * *

The first verifiable attestation of written Sanskrit is in Naneghat where a text readable in Sanskrit has been inscribed in the Brahmi script. The earliest date we have for this specimen is someplace in the second century BC. Let’s assume 200 BC. The latest Indus seals date to roughly 1800 BC. That’s a gap of more than 1,500 years. Why did people stop writing for that long? What happened? And even if we consider Aśokan edicts, we only get as far back as 260 BC. Still the same gap. Yajnadevam’s hypothesis of Indus Sanskrit does not offer answers.

To sum it all up, meticulous though Yajnadevam’s process is, he proceeds with the following inexplicable caveats:

  1. That the Indus script was a full-blown language and not mere system of notation.

  2. That the language was Sanskrit and fell between Vedic and Classical in chronology.

  3. That Sanskrit remained in use over a million square miles and over millennia, and yet somehow remained static in both vocabulary and semantics.




That’s an unwieldy amount of very arbitrary and very subjective assumptions, some even downright incorrect, already. Add to it the arbitrary identification of similar glyphs as different phonemes and dissimilar glyphs as variants of the same phoneme, and we have a system that works on more assumptions than cryptography. Not to mention the forced congruence with Rigveda using interpretations that don’t exist in the original text. Also not to mention the reading of Puranic terms in inscriptions that predate the Puranas by more than 2,000 years.

Having said that, Yajnadevam’s work deserves all the applause coming its way for its sheer ingenuity and resourcefulness. A peer-review can’t come soon enough, because even if the assumptions and conclusions are incorrect, the method itself is sound and prime for expanded deployment using a number of candidates, including Proto-Dravidian, Elamite, and Mundari. With recent upshots in the area of generative AI, a solution might just be around the proverbial corner.

## References

1

goibhniu. “Perl Uses for Cryptograms—Part 1: One-Liners and Word Patterns.” _PerlMonks_ , 4 Sept. 2007, www.perlmonks.org/?node_id=636818. Accessed 8 Apr. 2025.

2

Rao, Rajesh P. N. “Probabilistic Analysis of an Ancient Undeciphered Script.” _Computer_ , vol. 43, no. 4, Apr. 2010, p. 77. _DOI.org (Crossref)_ , https://doi.org/10.1109/MC.2010.112.

3

 _Ibid_.

4

Sivanantham, R., and M. Seran, editors. _Keeladi: An Urban Settlement of Sangam Age on the Banks of River Vaigai_. Department of Archaeology, Government of Tamil Nadu, 2019, pp. 1–61.

5

Prinsep, James. “Résumé of Indian Pálí Alphabets.” _Essays on Indian Antiquities: Historic, Numismatic, and Palæographic_ , edited by Edward Thomas, vol. 2, John Murray, 1858, pp. 40, plates XXXVIII–XXXIX.

6

Farmer, Steve. “Claims Concerning the Longest Indus ‘Inscription.’” _Steve Farmer_ , February 2023, https://safarmer.com/indus-longestinscription. Accessed 10 Apr. 2025.

7

Jamison, Stephanie W., and Joel P. Brereton. “Maṇḍala 5.” _The Rigveda: The Earliest Religious Poetry of India_ , edited by Martha Shelby, vols. I–III, Oxford University Press, 2014, p. 720.

8

“Rigveda/5/45/10.” _Ved Portal_ , https://वेद.com/rigveda/5/45/10. Accessed 10 Apr. 2025.

9

Jamison and Brereton, _op. cit._ , “Maṇḍala 2,” p. 455.

10

Jamison and Brereton, _op. cit._ , “Maṇḍala 10,” p. 1579.

11

Jamison and Brereton, _op. cit._ , “Maṇḍala 2,” p. 446.
