# __The Problematic Uses of $j$__

## Introduction

**The letter $j$ has carried four incompatible meanings in this corpus, and one of them contradicted the conventions.** It is the hyperbolic unit, $j^2=+1$; Hamilton's second vector unit, $j^2=-1$; a second central imaginary adjoined to the biquaternion algebra, again $j^2=-1$ but outside $\mathbb{B}$; and the spin label, a number, in $j(j+1)$ and $2j+1$. The second central imaginary is closed by the root convention and written $\tilde\Xi_{\mathrm{ad}}$ (§*Resolved*); the bound variable of the old gate criterion is closed the same way. One further use, the index of a sum, is harmless only because it is local.

This is a live audit. Each section states one use, says what is wrong with it, and closes with every file that carries it, or with the reason a list would be noise. A closed issue is removed from the body and recorded once in §*Resolved*, so the list of open defects stays exact. This is a reserve article: it documents a notation fault and a proposed correction, not a result of the algebra. No other file is changed by it.

## Status

| use | state | carriers |
|---|---|---|
| hyperbolic unit | sanctioned | the reduced biquaternion layer |
| bound variable of a general statement | resolved | the root convention |
| Hamilton's vector unit | **open** | 1 article |
| second central imaginary | resolved | the root convention |
| spin label | **open** | 22 physics articles, 7 maths articles, 19 drafts |
| index of a sum or a basis | confined | most of the corpus |
| second central imaginary named $\iota$ | resolved | none |

## The Four Meanings

| use | value | carrier | state |
|---|---|---|---|
| hyperbolic unit | $j^2=+1$ | $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$, basis $1,i,j,ij$ | the convention |
| vector unit | $j^2=-1$ | $\mathbb{H}=\mathbb{C}\oplus\mathbb{C}\vec e_y$ | local, contrary to the naming rule |
| spin label | $j\in\tfrac12\mathbb{Z}_{\geq0}$ | $j(j+1)$, $2j+1$, $\lvert j,m\rangle$ | **collision** |
| summation index | an integer | $e_j$, $\epsilon_{ijk}$, Clebsch–Gordan sums | harmless if local |

The vector-unit row is written in the corpus with the letter of the first row. The table is then the whole problem in one place: one glyph, three incompatible values, and three different types of object — an algebra element of the reduced layer, a vector unit of the quaternion layer, and a real number.

## The Hyperbolic Unit

**This is the only use the conventions sanction.** *Conventions in the Biquaternion Universe*, §*The Base and Its Units*, states that the letters $i$ and $j$ are already taken: $i$ is the central imaginary and $j$ is the hyperbolic unit. §*The Elements and their Coefficients* fixes the layer: the reduced biquaternion is written

$$
\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown},\qquad j^2=+1,\qquad ji=ij,
$$

on the basis $1,i,j,ij$, with $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\oplus\mathbb{C}$. The same section records that the split-complex numbers $\mathbb{D}$ use the same unit with the same sign, $j^2=+1$; what separates the two layers is the second, independent imaginary $i$, and the basis $1,i,j,ij$ rather than $1,j$.

Nothing in this article touches that use. The rule proposed at the end keeps it, and every other use yields to it. The reason is not aesthetic: the sign of $j^2$ is what separates the hyperbolic layers from the definite ones, and the dictionary of the twelve products, the four forms and the four norms is read off that sign.

**Carriers.** This use is not a defect, so it is not inventoried article by article. Its carriers are the reduced biquaternion and split-complex corpus, indexed in *The Mathematical Corpus*, together with §*The Base and Its Units* and §*The Elements and their Coefficients* of [Conventions in the Biquaternion Universe](../articles_physics/conventions-in-the-biquaternion-universe.html).

## Hamilton's Vector Unit

**A standard notation, local to one article, contrary to the corpus rule.** *Matrix Groups and Classical Groups*, §*The Representation of the Quaternion Algebra*, splits a quaternion over the second vector unit. Transcribed into the base, the object and its $2\times2$ image are

$$
q=z+w\vec e_y,\qquad z=a+b\vec e_x,\qquad w=c+d\vec e_x,\qquad \vec e_y^2=-e_t,\qquad \vec e_y z=\bar z\,\vec e_y,
$$

$$
\rho(q)=\rho(z+w\vec e_y)=\begin{pmatrix} z & w \\ -\bar w & \bar z \end{pmatrix},
$$

and the splitting $\mathbb{H}=\mathbb{C}\oplus\mathbb{C}\vec e_y$ is what the matrix block represents. The source prints the two vector units with the letters that the conventions reserve for the central imaginary and for the hyperbolic unit; the notation is the textbook one and the computation is correct.

It is nevertheless the second sign on a reserved letter. In the source the second vector unit squares to $-1$; the hyperbolic unit of the conventions squares to $+1$. A reader who carries one sign into the other gets a wrong algebra with no visible error. The article is also the exact case that *Conventions in the Biquaternion Universe*, §*The Base and Its Units*, forbids: a vector unit written with a reserved letter rather than with $\vec e_x$ or $\vec e_y$.

The repair is local and changes no product: it is the transcription above. The relation $\vec e_y z=\bar z\,\vec e_y$ and the matrix $\rho(z+w\vec e_y)$ are unchanged, and only the glyph moves. The article then uses one convention and no exception.

**Articles using this sense.**

- [Matrix Groups and Classical Groups](../articles_maths/matrix-groups-and-classical-groups.html) — nine occurrences, the splitting $\mathbb{H}=\mathbb{C}\oplus\mathbb{C}\vec e_y$ and the map $\rho(z+w\vec e_y)$.

## The Spin Label

**The conventions fix the spin as $s$, and the physics articles write it as $j$.** *Conventions in the Biquaternion Universe*, §*The Special Elements: Root, Idempotent and Nilpotent*, defines the spin by $S^2=\hbar^2s(s+1)$ and $S_z=\hbar m_s$, with $s$ an integer or half-integer and $m_s=-s,\dots,s$, and states that the algebra supplies the rotation action and the weights of its generator but not the one-particle space. The physics articles instead write

$$
\tilde{J}^2|j,m\rangle=j(j+1)\hbar^2|j,m\rangle,\qquad
\dim V_j=2j+1,\qquad
j=\tfrac12,\tfrac32,\dots
$$

This is the standard physics notation, and that is the difficulty: it is not an error of physics, it is a collision of alphabets. In a display that also contains the quaternion unit $j$, as several of these articles do, the same glyph is a number in one term and an element in the next. The reader has no rule for telling them apart, and neither does a search.

The collision is also redundant. The corpus already has $s$ and $m_s$, fixed in the conventions article, and the two edited spin articles of the mathematical corpus already use $s$. The repair is a replacement of labels, not of mathematics: $j\to s$, $m\to m_s$, $V_j\to V_s$, $j_1,j_2\to s_1,s_2$, $m_j\to m_s$. The replacement is not textual: in the Clebsch–Gordan series $j$ is also a summation index, and in $\epsilon_{ijk}$ it is a spatial index, so the two must be left alone.

**Physics corpus.** The count is the number of occurrences of $2j+1$, $j(j+1)$, $\lvert j,m\rangle$ or spin-$j$ in the file.

- [Addition of Angular Momenta and Clebsch–Gordan Coefficients](../articles_physics/addition-of-angular-momenta-and-clebsch-gordan-coefficients-in-biquaternionic-form.html) — 26.
- [Angular Momentum and Spin in Biquaternionic Form](../articles_physics/angular-momentum-and-spin-in-biquaternionic-form.html) — 18.
- [Higher Spin from Tensor Products](../articles_physics/higher-spin-from-tensor-products-why-the-biquaternion-algebra-admits-only-spin-0-and-one-half.html) — 13.
- [Spin Squeezing and the Tavis–Cummings Model](../articles_physics/spin-squeezing-and-the-tavis-cummings-model-in-biquaternionic-form.html) — 12.
- [The Hydrogen Atom, the Relativistic Case](../articles_physics/the-hydrogen-atom-in-biquaternionic-form-the-relativistic-case.html) — 11.
- [The Classical Coulomb Problem and Its Hidden $SO(4)$ Symmetry](../articles_physics/the-classical-coulomb-problem-and-its-hidden-so4-symmetry-in-biquaternionic-form.html) — 8.
- [The Majorana Representation](../articles_physics/the-majorana-representation-in-biquaternionic-form.html) — 6.
- [The Spinor Representation of the Lorentz Group](../articles_physics/the-spinor-representation-of-the-lorentz-group-in-biquaternionic-form.html) — 6.
- [Two Spin-Half Particles](../articles_physics/two-spin-half-particles-in-biquaternionic-form.html) — 3.
- [Spin and the Three Elementary Carriers](../articles_physics/spin-and-the-three-elementary-carriers.html) — 2.
- [The Classical Origin of $g=2$](../articles_physics/the-classical-origin-of-g-2-in-biquaternionic-form.html) — 2.
- [The Fermionic Fock Space](../articles_physics/the-fermionic-fock-space-in-biquaternionic-form.html) — 2.
- [The Lorentz Group in Biquaternionic Form](../articles_physics/the-lorentz-group-in-biquaternionic-form-structure-and-representations.html) — 2.
- [The Self-Dual and Anti-Self-Dual Split: Spin 1](../articles_physics/the-self-dual-and-anti-self-dual-split-spin-1-from-the-biquaternion-material-sector.html) — 2.
- [The Spin-Half Path Integral](../articles_physics/the-spin-half-path-integral-in-biquaternionic-form.html) — 2.
- [The Spin–Statistics Theorem](../articles_physics/the-spin-statistics-theorem-in-biquaternionic-form.html) — 2.
- [AI Physics Review](../articles_physics/ai-physics-review.html) — 1.
- [Exercise: The Non-Relativistic Limit and the Pauli Equation](../articles_physics/exercise-the-non-relativistic-limit-and-the-pauli-equation.html) — 1.
- [Frames, Rotations and the Lorentz Group](../articles_physics/frames-rotations-and-the-lorentz-group.html) — 1.
- [The Dirac Oscillator](../articles_physics/the-dirac-oscillator-in-biquaternionic-form.html) — 1.
- [The Qutrit Problem](../articles_physics/the-qutrit-problem-three-level-systems-outside-the-biquaternion-algebra.html) — 1.
- [The Scalar Field in the Centre](../articles_physics/the-scalar-field-in-the-centre-why-spin-0-escapes-the-biquaternion-state-module.html) — 1.

**Mathematical corpus.** The label is the standard $\mathrm{SU}(2)$ label there and is not a defect, because the biquaternion convention $s$ is not in force; the files are listed because a reader acquires the habit there and because a cross-reference can carry the label into a physics display. Incidental matches elsewhere — an exponent, a summation index — are excluded.

- [Analysis on Compact Groups](../articles_maths/analysis-on-compact-groups.html) — 8.
- [The Peter–Weyl Theorem](../articles_maths/the-peter-weyl-theorem.html) — 7.
- [Spinors as Peirce Coordinates in $M_6(\mathbb{C})$](../articles_maths/spinors-as-peirce-coordinates-in-m6c.html) — 4.
- [Representation Theory of Locally Compact Groups](../articles_maths/representation-theory-of-locally-compact-groups.html) — 3.
- [Spinors as Peirce Coordinates in $M_3(\mathbb{C})$](../articles_maths/spinors-as-peirce-coordinates-in-m3c.html) — 3.
- [Spinors as Peirce Coordinates in $M_4(\mathbb{C})$](../articles_maths/spinors-as-peirce-coordinates-in-m4c.html) — 3.
- [Spinors as Peirce Coordinates in $M_5(\mathbb{C})$](../articles_maths/spinors-as-peirce-coordinates-in-m5c.html) — 3.

**Unbuilt drafts.** The files in `articles_reserve/spin/` carry the same label and are outside the build.

- `spin/the-spin-chain-and-the-adjoint-decomposition-of-m6c.md` — 19; `spin/the-approaches-to-spin-weight-half-angle-ladder-and-adjoint.md` — 17; `spin/the-general-definition-of-spin.md` — 17; `spin/the-dubious-definitions-of-the-spin-of-an-algebra.md` — 15; `spin/the-spin-chain-and-the-adjoint-decomposition-of-m5c.md` — 11; `spin/the-spin-of-the-quaternion-algebra-a-worked-computation.md` — 8; `spin/the-spin-of-a-biquaternion.md` — 7; `spin/the-principal-pair-of-m2c-a-worked-computation.md` — 6; `spin/the-principal-pair-of-m3c-a-worked-computation.md` — 6; `spin/the-general-definitions-of-the-spin-of-an-algebra.md` — 5; `spin/the-principal-pair-of-m4c-a-worked-computation.md` — 5; `spin/the-principal-pair-of-m5c-a-worked-computation.md` — 5; `spin/the-spin-chain-and-the-adjoint-decomposition-of-m3c.md` — 3; `spin/the-spin-two-chain-and-the-adjoint-of-m5c.md` — 3; `spin/the-triple-and-the-highest-weight-list-a-summary.md` — 2; `spin/the-incomplete-definitions-of-the-spin-of-an-algebra.md` — 1; `spin/the-spin-of-the-complex-numbers-the-absence-of-a-pair.md` — 1; `spin/the-spin-of-the-split-complex-numbers-a-root-without-a-ladder.md` — 1; `spin/the-weight-of-a-frame-root-and-the-spin-quantum-number.md` — 1.

## The Index Uses

**Two uses are harmless, and only because they are local.** The first is the summation index of a Clebsch–Gordan sum or of $\epsilon_{ijk}$; it is bound, it never denotes an element, and it disappears from the result. The second is the basis label $e_j$ of a Clifford algebra, which is a subscript on a fixed symbol and cannot be read as a scalar.

Both become harmful the moment they share an expression with an element or a spin. The rule below therefore does not ban them; it confines them. An index may be $j$ when the expression contains no algebra element and no spin labelled $j$; otherwise it is renamed.

**Carriers.** This use is not a defect and is not inventoried. The bound index occurs in most of the corpus — the Clebsch–Gordan sums, the $\epsilon_{ijk}$ of the rotation algebra, the $e_j$ of the Clifford basis — so a list would name several hundred files and would not distinguish a defect from a formula. The rule is what matters here, not a count.

## Why a Single Replacement Is Unsafe

**The same glyph means three things, so a blind substitution corrupts at least two of them.** The traps are concrete. A replacement of every $j$ by $s$ would rewrite $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ as a split-complex element with the wrong unit, would rewrite $e_j$ of a Clifford basis as $e_s$, would rewrite $\epsilon_{ijk}$ as $\epsilon_{isk}$, and would rewrite the Clebsch–Gordan summation index, which is bound and must stay. A replacement of every $j$ by $i$ would collapse the hyperbolic unit into the central imaginary.

The replacement therefore had to be semantic, and it followed the order of dependence: first the definition in *Chirality: The Conjugate Pair*, then the articles that copy its notation, then the cross-references, then the menus. The definition is the only place where the object is introduced; every other occurrence is either a copy or a citation of it.

## The Rule

1. **$j$ is the hyperbolic unit.** It is written only in the reduced biquaternion layer, with $j^2=+1$, $ji=ij$, and the basis $1,i,j,ij$. No other use of the letter is sanctioned.
2. **No $i,j,k$ for quaternion vector units.** The vector units are $\vec e_x,\vec e_y,\vec e_z$. A source that writes them as $i,j,k$ is translated, not copied.
3. **The second central imaginary is a root, and it carries the root glyph.** The double is written $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{B}_{\mathbb{R}}$, and its adjoined generator $\tilde\Xi_{\mathrm{ad}}$, a central root of $-1$ with the role subscript; the chirality is $\chi=i\tilde\Xi_{\mathrm{ad}}$. The glyph is registered in *Conventions in the Biquaternion Universe*, §*The Root Convention*. A name is not chosen inside an article.
4. **The spin is $s$.** In the biquaternion corpus the labels are $s$ and $m_s$; $j$ is not a spin label. A cited source that writes $j$ is quoted with its own letter and translated in the surrounding text.
5. **An index may be $j$ only where it cannot be read as an element or a label.** In the presence of an algebra element or a spin, the index is renamed.

## Resolved

**Closed items are removed from the body and recorded here once.**

- **The adjoined generator named $\iota$.** The notation was replaced in *Eigenvalue Decomposition and Eigenbasis of a Complex Number* by $i_1=i\otimes1$ and $i_2=1\otimes i$, with $e_\pm=\tfrac12(1\mp i_1i_2)$; the file now has zero occurrences of $\iota$. It remains only in its established senses — the Clifford map, the involution, the inner automorphism $\iota_u$, the canonical embedding, the Newman–Penrose dyad element — never as a central imaginary.
- **The dummy of the gate criterion.** The criterion is now stated as a central root of $-1$, with the root glyph $\tilde\Xi$ of §*The Root Convention*, and its instantiation reads $\tilde\Xi=i$. Applied in *The Biquaternion Algebra*, §*The Gate*, in *Introduction to the General Quaternionic Sesqualgebra*, §*The Gate*, and in *Roots, Idempotents and Observables*. The reserved letter is no longer a bound variable anywhere in the corpus.
- **The second central imaginary.** The adjoined generator is a root like any other: $\tilde\Xi_{\mathrm{ad}}$, central, with $\tilde\Xi_{\mathrm{ad}}^2=-e_t$ and outside $\mathbb{B}_{\mathbb{R}}$, and the chirality is $\chi=i\tilde\Xi_{\mathrm{ad}}=e_+-e_-$. The double is written $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{B}_{\mathbb{R}}$ where it is defined, and *the double* after that. The glyph is registered in *Conventions in the Biquaternion Universe*, §*The Root Convention*. Applied in the sixteen built entries, the seven unbuilt drafts, the menu comments and `_reserve/BRAINSTORMING.md`; no occurrence of $\mathbb{B}[j]$, $\chi=ij$, $\rho(j)$ or $\iota_{\mathrm{Cl}}(j)$ remains.
- **False positive struck from the secondary-imaginary inventory.** *Split-Complex Element Representations* writes $\rho(j)=\pm1$: there $j$ is the hyperbolic unit and $\rho$ is a character, not the adjoined generator. It is not a carrier and is no longer listed.

## Summary

The letter $j$ is the hyperbolic unit of the reduced biquaternion layer, and that is the only meaning the conventions give it. Two other meanings are in circulation: Hamilton's vector unit and the spin label. The second central imaginary, formerly the worst of the three, is closed: it is the root $\tilde\Xi_{\mathrm{ad}}$, and the chirality is $\chi=i\tilde\Xi_{\mathrm{ad}}$ (§*Resolved*). The spin label still collides with both reserved letters and duplicates a label the corpus has already fixed as $s$.

The second central imaginary no longer appears in the built corpus, in the menu or in the drafts. One article still carries Hamilton's vector unit; twenty-nine built articles carry the spin label, twenty-two in the physics corpus and seven in the mathematical one, plus nineteen unbuilt drafts. The remaining repair is the translation of Hamilton's vector unit into $\vec e_y$ and the renaming of the spin label to $s$, with the summation and basis indices left alone. The definition in *Chirality: The Conjugate Pair* was the place to start for the generator, because every other occurrence was a copy of it.
