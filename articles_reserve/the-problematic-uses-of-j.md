# __The Problematic Uses of $j$__

## Introduction

**The letter $j$ carries four incompatible meanings in this corpus, and one of them contradicts the conventions.** It is the hyperbolic unit, $j^2=+1$; Hamilton's second vector unit, $j^2=-1$; a second central imaginary adjoined to the biquaternion algebra, again $j^2=-1$ but outside $\mathbb{B}$; and the spin label, a number, in $j(j+1)$ and $2j+1$. Two further uses, the dummy variable of a general statement and the index of a sum, are harmless only because they are local.

A reader who meets $j$ in a display cannot tell which of the four is meant without reconstructing the context. That is the defect this article records. The article inventories each use, states what is wrong with it, lists the articles that carry it, and proposes the rule that removes it. It is a reserve article: it documents a notation fault and a proposed correction, not a result of the algebra. No other file is changed by it.

The order of the sections follows the severity. The sanctioned use comes first, so that the rule has a fixed point. The dummy variable comes next, because it is the point at which a placeholder becomes an element. Then the two uses that damage the biquaternion corpus: the second central imaginary, which contradicts the conventions, and the spin label, which collides with all of the above. The index uses and the inventory close the article.

## The Four Meanings

| use | value | carrier | status |
|---|---|---|---|
| hyperbolic unit | $j^2=+1$ | $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$, basis $1,i,j,ij$ | the convention |
| vector unit | $j^2=-1$ | $\mathbb{H}=\mathbb{C}\oplus\mathbb{C}j$ | local, contrary to the naming rule |
| dummy central element | $j^2=-1$ | a general statement about a real algebra | bound variable, harmless alone |
| new central element | $j^2=-1$, $j\notin\mathbb{B}$ | $\mathbb{B}[j]=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{B}_{\mathbb{R}}$ | **defect** |
| spin label | $j\in\tfrac12\mathbb{Z}_{\geq0}$ | $j(j+1)$, $2j+1$, $|j,m\rangle$ | **collision** |
| summation index | an integer | $e_j$, $\epsilon_{ijk}$, Clebsch–Gordan sums | harmless if local |

The table is the whole problem in one place: one glyph, four incompatible values, and three different types of object — an algebra element of the reduced layer, an element of the quaternion layer, an element outside the biquaternion algebra, and a real number.

## The Hyperbolic Unit

**This is the only use the conventions sanction.** *Conventions in the Biquaternion Universe*, §*The Base and Its Units*, states that the letters $i$ and $j$ are already taken: $i$ is the central imaginary and $j$ is the hyperbolic unit. §*The Elements and their Coefficients* fixes the layer: the reduced biquaternion is written

$$
\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown},\qquad j^2=+1,\qquad ji=ij,
$$

on the basis $1,i,j,ij$, with $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\oplus\mathbb{C}$. The same section records that the split-complex numbers $\mathbb{D}$ use the same unit with the same sign, $j^2=+1$; what separates the two layers is the second, independent imaginary $i$, and the basis $1,i,j,ij$ rather than $1,j$. The sign $+1$ is what the two share, and it is what separates both from every use of $j$ with $j^2=-1$.

Nothing in this article touches that use. The rule proposed at the end keeps it, and every other use yields to it. The reason is not aesthetic: the sign of $j^2$ is what separates the hyperbolic layers from the definite ones, and the dictionary of the twelve products, the four forms and the four norms is read off that sign.

## The Dummy Variable

**A bound variable is not an element, and the corpus does not always mark the difference.** *The Biquaternion Algebra*, §*The Gate: a Central Element of Square $-1$*, states the general criterion: a $\mathbb{C}$-algebra structure on a real algebra, with the structure map landing in the centre, is the same thing as a central element $j$ with $j^2=-1$. The same paragraph then evaluates the criterion for $\mathbb{B}$: the element is the central imaginary $i$ itself, $j=i$.

In that paragraph $j$ is a dummy. It names no element of $\mathbb{B}$; it is the slot that the central imaginary fills. Read alone, the paragraph is correct. Read beside *Chirality: The Conjugate Pair*, where $j$ is introduced as a **new** central imaginary with $j^2=-1$ commuting with $i$, the two statements are indistinguishable in symbols and opposite in content: in the first, $j$ is $i$; in the second, $j$ is not $i$ and not in $\mathbb{B}$ at all.

The same dummy appears in *Introduction to the General Quaternionic Sesqualgebra*, §*The Gate: a Central Element of Square $-1$*, where the gate is empty because the centre is trivial. There the letter is harmless because no element follows it. The lesson is not that the dummy is wrong. The lesson is that a dummy and an element must not share a glyph, and that the passage from one to the other must be written as a construction, not as a rename.

## Hamilton's Vector Unit

**A standard notation, local to one article, contrary to the corpus rule.** *Matrix Groups and Classical Groups*, §*The Representation of the Quaternion Algebra*, writes a quaternion as

$$
q=z+wj,\qquad z=a+bi,\qquad w=c+di,\qquad i=\vec e_x,\quad j=\vec e_y,\quad ij=\vec e_z,
$$

with $j^2=-1$ and $jz=\bar z j$, and uses the splitting $\mathbb{H}=\mathbb{C}\oplus\mathbb{C}j$ to build the $2\times2$ representation. The notation is the textbook one and the computation is correct.

It is nevertheless the second sign on the same glyph. In this article $j^2=-1$; in the reduced biquaternion layer $j^2=+1$. A reader who carries the first into the second, or the second into the first, gets a wrong algebra with no visible error. The article is also the exact case that *Conventions in the Biquaternion Universe*, §*The Base and Its Units*, forbids: a vector unit written as $i$ or $j$ rather than as $\vec e_x$ or $\vec e_y$.

The repair is local and does not change a single product. Write $z=a+b\vec e_x$, $w=c+d\vec e_x$, and replace $j$ by $\vec e_y$ throughout; the relation $\vec e_y z=\bar z\,\vec e_y$ and the matrix $\rho(z+w\vec e_y)$ are unchanged. The article then uses one convention and no exception.

## The Second Central Imaginary

**This is the defect.** *Chirality: The Conjugate Pair*, §*The Complexification*, defines the object in one sentence: let $j$ be a new central imaginary unit, $j^2=-1$, commuting with $i$. It then writes

$$
\mathbb{B}[j]=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{B}_{\mathbb{R}}\cong\mathbb{B}\oplus\mathbb{B},\qquad
\chi=ij,\qquad
e_\pm=\tfrac12(e_t\pm\chi),\qquad
\chi^2=e_t .
$$

The construction is correct and the article needs it: the central idempotents do not exist in $\mathbb{B}_{\mathbb{R}}$, whose centre is $\mathbb{C}e_t$ with no nontrivial idempotent, and they exist in the double. What is wrong is the notation, in four ways.

**The sign.** The same letter that the conventions fix at $j^2=+1$ is given $j^2=-1$. This is not a local slip: the two signs define different algebras, and the reduced biquaternion layer is the corpus's standard example of the positive sign.

**The type.** The element $j$ is not in $\mathbb{B}$. The notation $\mathbb{B}[j]$ is the notation of a polynomial ring, and a polynomial ring would be $\mathbb{B}[j]/(j^2+e_t)$; the object actually meant is the tensor product with a new copy of $\mathbb{C}$, whose generator is $1\otimes i$. The bracket hides both the tensor product and the quotient. Worse, it suggests that a central imaginary is being adjoined to $\mathbb{B}$ as one adjoins a scalar, when the centre of $\mathbb{B}$ already is $\mathbb{C}$ with unit $i$; a second central imaginary cannot be an element of $\mathbb{B}$.

**The identity of the element.** Under the isomorphism $\mathbb{B}[j]\cong\mathbb{B}\oplus\mathbb{B}$, the adjoined generator is the pair $(i,-i)$: one imaginary unit in each summand, with opposite signs. It is a central element of the double, not a complex number of either summand and not an element of $\mathbb{B}$. A notation that writes it as a single letter conceals the pair, and with it the reason the two chiral halves are conjugate.

**The dictionary.** *The Dirac Algebra and Biquaternions — A Dictionary* records that $\iota_{\mathrm{Cl}}$, being $\mathbb{R}$-linear, does not determine the image of an element outside $\mathbb{B}$; the image of $j$ must be chosen, and the choice $\iota_{\mathrm{Cl}}(j)=-i_{\mathrm{Cl}}$ is what gives $\iota_{\mathrm{Cl}}(\chi)=+\gamma_5$. The letter $j$ hides a binary choice that the article has to state in full.

The defect has already propagated into the conventions themselves. *Conventions in the Biquaternion Universe*, §*The Special Elements: Root, Idempotent and Nilpotent*, writes the chirality as $\chi=ij$, with the same $j$, later in the same article that fixed $j$ as the hyperbolic unit in §*The Base and Its Units*. The two statements cannot both be read with one meaning of the letter. That contradiction is the clearest evidence that the notation is untenable, and it is internal to the article that is supposed to settle notation.

**The repair.** Write the double as $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{B}_{\mathbb{R}}$ and the adjoined generator as $1\otimes i$; both are already used in the chirality article, in the same section, and are unambiguous. Introduce no letter. If the repetition becomes unmanageable, a short name may be adopted, but only after it is registered in *Conventions in the Biquaternion Universe*; a name chosen inside one article is how the present defect began.

## The Spin Label

**The conventions fix the spin as $s$, and the physics articles write it as $j$.** *Conventions in the Biquaternion Universe*, §*The Special Elements: Root, Idempotent and Nilpotent*, defines the spin by $S^2=\hbar^2s(s+1)$ and $S_z=\hbar m_s$, with $s$ an integer or half-integer and $m_s=-s,\dots,s$, and states that the algebra supplies the rotation action and the weights of its generator but not the one-particle space. The physics articles instead write

$$
\tilde{J}^2|j,m\rangle=j(j+1)\hbar^2|j,m\rangle,\qquad
\dim V_j=2j+1,\qquad
j=\tfrac12,\tfrac32,\dots
$$

This is the standard physics notation, and that is the difficulty: it is not an error of physics, it is a collision of alphabets. In a display that also contains the quaternion unit $j$, as several of these articles do, the same glyph is a number in one term and an element in the next. The reader has no rule for telling them apart, and neither does a search.

The collision is also redundant. The corpus already has $s$ and $m_s$, fixed in the conventions article, and the two edited spin articles of the mathematical corpus already use $s$. The repair is a replacement of labels, not of mathematics: $j\to s$, $m\to m_s$, $V_j\to V_s$, $j_1,j_2\to s_1,s_2$, $m_j\to m_s$. The replacement is not textual: in the Clebsch–Gordan series $j$ is also a summation index, and in $\epsilon_{ijk}$ it is a spatial index, so the two must be left alone.

## The Index Uses

**Two uses are harmless, and only because they are local.** The first is the summation index of a Clebsch–Gordan sum or of $\epsilon_{ijk}$; it is bound, it never denotes an element, and it disappears from the result. The second is the basis label $e_j$ of a Clifford algebra, which is a subscript on a fixed symbol and cannot be read as a scalar.

Both become harmful the moment they share an expression with an element or a spin. The rule below therefore does not ban them; it confines them. An index may be $j$ when the expression contains no algebra element and no spin labelled $j$; otherwise it is renamed. The confined uses are not counted in the inventory, because they are not defects and a count of them would obscure the count of the defects.

## The Inventory

**The articles that carry the defective notation.** The count is the number of occurrences of $\mathbb{B}[j]$ or $\chi=ij$ in the file. The role is what the file does with the notation.

| article | count | role |
|---|---|---|
| [Chirality: The Conjugate Pair](../articles_maths/chirality-the-conjugate-pair.html) | 12 | the definition and its consequences |
| [The Dirac Equation in Biquaternionic Form](../articles_physics/the-dirac-equation-in-biquaternionic-form.html) | 11 | chirality projectors, mass pairing, $\gamma_5$ |
| [Biquaternion Physical Interpretation of Chirality](../articles_physics/biquaternion-physical-interpretation-of-chirality.html) | 8 | the physical reading of the central sign |
| [The Four Uses of Spin in the Biquaternion Algebra](../articles_maths/the-four-uses-of-spin-in-the-biquaternion-algebra.html) | 7 | the chirality as one of the four uses |
| [Angular Momentum and Spin in the Biquaternion Algebra](../articles_maths/angular-momentum-and-spin-in-the-biquaternion-algebra.html) | 4 | the doubled algebra in the spin article |
| [The Dirac Algebra and Biquaternions — A Dictionary](../articles_physics/the-dirac-algebra-and-biquaternions-a-dictionary.html) | 4 | the choice of $\iota_{\mathrm{Cl}}(j)$ |
| [The Spectral Triple of the Biquaternion Algebra](../articles_physics/the-spectral-triple-of-the-biquaternion-algebra.html) | 3 | the chirality operator of the triple |
| [The Clifford Layer of the Physics Corpus](../articles_reserve/the-clifford-layer-of-the-physics-corpus-inventory-and-the-odd-sector.html) | 3 | inventory of the complexified layer |
| [The Mathematical Corpus, menu](../maths.html) | 3 | menu comments |
| [The Two Chiralities of $M_4(\mathbb{C})$](../articles_maths/the-two-chiralities-of-m4c.html) | 2 | cross-reference |
| [The Two Chiralities of $M_6(\mathbb{C})$](../articles_maths/the-two-chiralities-of-m6c.html) | 2 | cross-reference |
| [$M_2(\mathbb{C})$ Model: The Peirce Coordinates](../articles_maths/m2c-model-the-peirce-coordinates-matrix-units-and-the-spinor-planes.html) | 1 | cross-reference |
| [$M_4(\mathbb{C})$ Representation: The Two-Sided Operators](../articles_maths/m4c-representation-the-two-sided-operators-on-the-biquaternion-algebra.html) | 1 | cross-reference |
| [The Schwinger–Dyson Equations](../articles_physics/the-schwinger-dyson-equations-and-the-ward-takahashi-identities-in-biquaternionic-form.html) | 1 | the axial current |
| [Conventions in the Biquaternion Universe](../articles_physics/conventions-in-the-biquaternion-universe.html) | 1 | the internal contradiction |
| [Spin and the Three Elementary Carriers](../articles_physics/spin-and-the-three-elementary-carriers.html) | 1 | the chiral mass pairing |

The file `_reserve/BRAINSTORMING.md` carries three further occurrences and is outside the built corpus.

**The physics articles that use $j$ as the spin label.** The count is the number of occurrences of $2j+1$, $j(j+1)$, $|j,m\rangle$ or spin-$j$ in the file.

| article | count |
|---|---|
| [Addition of Angular Momenta and Clebsch–Gordan Coefficients](../articles_physics/addition-of-angular-momenta-and-clebsch-gordan-coefficients-in-biquaternionic-form.html) | 26 |
| [Angular Momentum and Spin in Biquaternionic Form](../articles_physics/angular-momentum-and-spin-in-biquaternionic-form.html) | 18 |
| [Higher Spin from Tensor Products](../articles_physics/higher-spin-from-tensor-products-why-the-biquaternion-algebra-admits-only-spin-0-and-one-half.html) | 13 |
| [The Hydrogen Atom, the Relativistic Case](../articles_physics/the-hydrogen-atom-in-biquaternionic-form-the-relativistic-case.html) | 11 |
| [The Classical Coulomb Problem and Its Hidden $SO(4)$ Symmetry](../articles_physics/the-classical-coulomb-problem-and-its-hidden-so4-symmetry-in-biquaternionic-form.html) | 8 |
| [Spin Squeezing and the Tavis–Cummings Model](../articles_physics/spin-squeezing-and-the-tavis-cummings-model-in-biquaternionic-form.html) | 7 |
| [The Spinor Representation of the Lorentz Group](../articles_physics/the-spinor-representation-of-the-lorentz-group-in-biquaternionic-form.html) | 6 |
| [The Majorana Representation](../articles_physics/the-majorana-representation-in-biquaternionic-form.html) | 5 |
| [Two Spin-Half Particles](../articles_physics/two-spin-half-particles-in-biquaternionic-form.html) | 3 |
| [The Self-Dual and Anti-Self-Dual Split Spin 1](../articles_physics/the-self-dual-and-anti-self-dual-split-spin-1-from-the-biquaternion-material-sector.html) | 2 |
| [The Classical Origin of $g-2$](../articles_physics/the-classical-origin-of-g-2-in-biquaternionic-form.html) | 2 |
| [The Spin-Half Path Integral](../articles_physics/the-spin-half-path-integral-in-biquaternionic-form.html) | 2 |
| [The Lorentz Group in Biquaternionic Form](../articles_physics/the-lorentz-group-in-biquaternionic-form-structure-and-representations.html) | 2 |
| [The Spin–Statistics Theorem](../articles_physics/the-spin-statistics-theorem-in-biquaternionic-form.html) | 2 |
| [Spin and the Three Elementary Carriers](../articles_physics/spin-and-the-three-elementary-carriers.html) | 2 |
| [The Fermionic Fock Space](../articles_physics/the-fermionic-fock-space-in-biquaternionic-form.html) | 2 |
| [Exercise: The Non-Relativistic Limit and the Pauli Equation](../articles_physics/exercise-the-non-relativistic-limit-and-the-pauli-equation.html) | 1 |
| [The Dirac Oscillator](../articles_physics/the-dirac-oscillator-in-biquaternionic-form.html) | 1 |
| [AI Physics Review](../articles_physics/ai-physics-review.html) | 1 |
| [Frames, Rotations and the Lorentz Group](../articles_physics/frames-rotations-and-the-lorentz-group.html) | 1 |
| [The Scalar Field in the Centre](../articles_physics/the-scalar-field-in-the-centre-why-spin-0-escapes-the-biquaternion-state-module.html) | 1 |
| [The Qutrit Problem](../articles_physics/the-qutrit-problem-three-level-systems-outside-the-biquaternion-algebra.html) | 1 |

**The mathematical corpus.** Seven articles use $j$ as the standard $\mathrm{SU}(2)$ label rather than as an element: *Analysis on Compact Groups*, *The Peter–Weyl Theorem*, *Representation Theory of Locally Compact Groups*, and the four *Spinors as Peirce Coordinates* articles. In those articles the label is the standard one and is not a defect, because the biquaternion convention $s$ is not in force there. They are listed because they are where a reader of the mathematical corpus acquires the habit, and because a cross-reference from a physics article can carry the label into a display that also contains a quaternion unit.

## Why a Single Replacement Is Unsafe

**The same glyph means four things, so a blind substitution corrupts at least three of them.** The traps are concrete. A replacement of every $j$ by $s$ would rewrite $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ as a split-complex element with the wrong unit, would rewrite $e_j$ of a Clifford basis as $e_s$, would rewrite $\epsilon_{ijk}$ as $\epsilon_{isk}$, and would rewrite the Clebsch–Gordan summation index, which is bound and must stay. A replacement of every $j$ by $i$ would collapse the second central imaginary into the first and destroy the distinction between the two chiral halves. A deletion of every $\mathbb{B}[j]$ would leave the sentences that depend on the double without an object.

The replacement must therefore be semantic, and it must follow the order of dependence: first the definition in *Chirality: The Conjugate Pair*, then the articles that copy its notation, then the cross-references, then the menus. The definition is the only place where the object is introduced; every other occurrence is either a copy or a citation of it.

## The Rule

1. **$j$ is the hyperbolic unit.** It is written only in the reduced biquaternion layer, with $j^2=+1$, $ji=ij$, and the basis $1,i,j,ij$. No other use of the letter is sanctioned.
2. **No $i,j,k$ for quaternion vector units.** The vector units are $\vec e_x,\vec e_y,\vec e_z$. A source that writes them as $i,j,k$ is translated, not copied.
3. **No letter for the second central imaginary.** The double is written $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{B}_{\mathbb{R}}$, and its generator $1\otimes i$. A short name requires a prior entry in *Conventions in the Biquaternion Universe*; it is not chosen inside an article.
4. **The spin is $s$.** In the biquaternion corpus the labels are $s$ and $m_s$; $j$ is not a spin label. A cited source that writes $j$ is quoted with its own letter and translated in the surrounding text.
5. **An index may be $j$ only where it cannot be read as an element or a label.** In the presence of an algebra element or a spin, the index is renamed.

## Summary

The letter $j$ is the hyperbolic unit of the reduced biquaternion layer, and that is the only meaning the conventions give it. Three other meanings are in circulation: Hamilton's vector unit, a second central imaginary adjoined to the biquaternion algebra, and the spin label. The second contradicts the conventions outright — the same letter cannot have both signs, and the conventions article itself now uses both — and it hides a tensor product, a pair of conjugate summands and a binary choice in the Clifford dictionary. The third collides with the first two and duplicates a label the corpus has already fixed as $s$. Sixteen files carry the defective notation, twenty-two physics articles carry the spin label, and the defect reaches the conventions article and the menu.

The repair is not a substitution. It is the removal of one object — the second central imaginary — from the letter $j$, the confinement of $j$ to the hyperbolic layer, the translation of Hamilton's vector unit into $\vec e_y$, and the renaming of the spin label to $s$. The definition in *Chirality: The Conjugate Pair* is the place to start, because every other occurrence is a copy of it.
