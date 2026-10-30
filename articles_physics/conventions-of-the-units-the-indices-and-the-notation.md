# __Conventions of the Units, the Indices and the Notation__

## Introduction

These are the conventions of the units, of the two superscript tokens and of the subscripts. They are the last of the series because every earlier article depends on them, and they assume the base of *Conventions in the Biquaternion Universe* and the operators of *Conventions of the Operators and the Calculus*.

The order is from the physical to the typographical. The SI units come first, with the rule that the coefficients of one element share one unit and with the two writings of the temporal slot. Then the two superscript tokens, $\mathrm{fop}$ and $\mathrm{opp}$. Then the subscript, which counts or names and is never a derivative.

## Physical Units

**A unit element is not a physical unit.** The base $e_t,\vec e_x,\vec e_y,\vec e_z$ of *Conventions in the Biquaternion Universe*, §*The Base and Its Units* is algebraic: its structure constants are $0$ or $\pm1$, and the biquaternion norm is a sum of four squares of coefficients. No element of $\mathbb{B}$ carries a metre, a second or a kilogram. A physical unit enters only where an element is **identified** with a physical quantity, and that identification is a convention of the article that makes it, not a property of the algebra. The phrase *unit element* names a basis element and *physical unit* names a convention of measurement; the two are never exchanged.

**The series uses the SI.** Length is measured in metres, time in seconds, mass in kilograms, temperature in kelvin and charge in coulomb. The derived units follow from these, and the ones the articles use are collected here.

| Quantity | Symbol | Unit |
|---|---|---|
| Length | $x,y,z$; $ict'$ in the length coordinate | metre ($\mathrm{m}$) |
| Time | $t'$ in the time coordinate | second ($\mathrm{s}$) |
| Mass | $m$ | kilogram ($\mathrm{kg}$) |
| Temperature | $T$ | kelvin ($\mathrm{K}$) |
| Electric charge | $ϙ$ | coulomb ($\mathrm{C}$) |
| Speed | $c$, $c_0$ | $\mathrm{m\,s^{-1}}$ |
| Momentum | $\vec p$ | $\mathrm{kg\,m\,s^{-1}}$ |
| Energy | $E$ | joule ($\mathrm{J}$) |
| Action, angular momentum, spin | $S$, $S_0$, $I_\mu$, $\theta$, $\vec L$, $\tilde S_3$ | joule-second ($\mathrm{J\,s}$) |
| Metric coefficient, time writing | $g_{tt}=-c^2$ | $\mathrm{m^2\,s^{-2}}$ |
| Inverse length | $\mu=mc/\hbar$ | $\mathrm{m^{-1}}$ |
| Inverse temperature | $\beta=\hbar/(k_BT)$ | second ($\mathrm{s}$) |
| Planck constants | $h$, $\hbar$ | joule-second ($\mathrm{J\,s}$) |
| Boltzmann constant | $k_B$ | $\mathrm{J\,K^{-1}}$ |
| Gravitational constant | $G$ | $\mathrm{m^3\,kg^{-1}\,s^{-2}}$ |
| Permittivity and permeability | $\epsilon$, $\mu$ | $\mathrm{F\,m^{-1}}$, $\mathrm{H\,m^{-1}}$ |

**The coefficients of one element share one unit.** The biquaternion norm is a sum of four squares of the coefficients of a single element, so the four terms are commensurable only if the four coefficients carry the same unit. The requirement is per element and not across elements: the coefficients of a four-displacement are lengths and its norm a length squared, the coefficients of a four-velocity are speeds and its norm a speed squared, and the temporal slot of a four-potential carries $\phi/c$ rather than $\phi$ so that its four components share the unit of the vector potential. The unit is the unit of the quantity the element represents, and it is supplied by the identification.

**The two writings of the temporal slot.** In the length coordinate the material position is $\tilde R = ict'\,e_t+\vec q$, with time measured in metres; this is the corpus's default. In the time coordinate the temporal component is $it'$, time stays in seconds, and the conversion is carried by the metric coefficient $g_{tt}=-c^2$. The quadratic form is one and the same, $\langle\tilde R\rangle_{\natural}=-c^2{t'}^2+x^2+y^2+z^2$; the two differ only in where the factor $c$ is written, and an article that uses the second states it where the temporal slot is read.

**Dimensionless and dimensionful.** A pure number — the fine-structure constant $\alpha$, the ratio $g=2$, the phase $S/\hbar$, the trace normalisation $2$ — carries no unit and no conversion. A dimensionful constant is a unit conversion and is written with its unit. No dimensionful constant is derived by the algebra: $c$, $\hbar$, $k_B$, $G$, $m$ and $ϙ$ are inserted at the places where the structure requires a scale. The metrology says the same thing from the other side. Since the 2019 revision the SI fixes $c$, $h$, the elementary charge and $k_B$ by definition and realises the units from them, while a dimensionless constant such as $\alpha$ has to be measured. An article that sets a constant to one — $c=1$, $\hbar=1$ or $G=1$ — says so locally, and the constant returns wherever a dimensional statement is at issue.

**A caution on $\mu$.** The letter $\mu$ names the permeability in $c=1/\sqrt{\epsilon\mu}$ and the inverse Compton length in $\mu=mc/\hbar$, and it is the direction label in $e_\mu$ and $Q_\mu$. The corpus distinguishes the uses by context; an article should not use two of them in one expression.

## The Superscripts

Two superscript tokens run beside the marks of the elements and the marks of the conjugations, and neither is to be read for the other:

| Token | Written on | Meaning |
|---|---|---|
| $^{\mathrm{fop}}$ | a Fock-operator glyph | an operator on the Fock space, the Fock-operator mark |
| $^{\mathrm{opp}}$ | an algebra name | the opposite algebra, the algebra with the reversed product |

**The mark, and its one use.** The marks of the elements say what a glyph **is**, not that it is an **operator** (*Conventions of the Operators and the Calculus*, §*The Operators*). The single exception is the **Fock layer**, whose operators act on a Fock space and are **not** elements of the algebra. Only these carry the upright superscript $\mathrm{fop}$, set on the glyph and read as part of it:

$$
a^{\mathrm{fop}},\quad b^{\mathrm{fop}},\quad a^{\mathrm{fop}\dagger},\quad b^{\mathrm{fop}\dagger},\quad \psi^{\mathrm{fop}},\quad N^{\mathrm{fop}},\quad H^{\mathrm{fop}},\quad F^{\mathrm{fop}},\quad Ϙ^{\mathrm{fop}},\quad U^{\mathrm{fop}} .
$$

The mark says exactly one thing — the glyph is not an element, it is an operator on the Fock space — and it is written on nothing else. It is not a general mark of operators: the momentum $\vec p=-i\hbar\nabla$ keeps its element glyph and never takes the Fock mark, the quadratures $x$ and $p$ of the oscillator are written $x$ and $p$, the spin $S_k=\tfrac{\hbar}{2}\sigma_k$ is written $S_k$, and the parity, charge-conjugation and time-reversal maps $P$, $C$ and $T$ carry no mark. Where a ladder is meant as an element of the algebra it is written with the element's glyph, the truncated pair $\vec\Upsilon_1,\vec\Upsilon_2$, and the abstract ladder operator keeps the mark, $a^{\mathrm{fop}}$.

**It combines with the dagger, the mark first.** The dagger is the general adjoint (*Conventions of the Operators and the Calculus*, §*The Operators*); the superscript marks the Fock operator. Where both are written on the same glyph, the Fock mark comes first and the adjoint follows, $(a^{\mathrm{fop}})^{\dagger}$, contracted to $a^{\mathrm{fop}\dagger}$. The dagger alone never says that its glyph is an operator, and the superscript alone never says that the Fock operator is self-adjoint; the two are read together, so that $a^{\mathrm{fop}\dagger}$ is the adjoint of the ladder and $N^{\mathrm{fop}}$ is written without an adjoint because it is self-adjoint.

**The opposite algebra carries a different token.** The reversed-product algebra is written with the superscript $\mathrm{opp}$, $\mathbb{B}^{\mathrm{opp}}$, $A^{\mathrm{opp}}$, $M_n(D)^{\mathrm{opp}}$, on an **algebra name**, where the Fock mark is written on a **Fock-operator glyph**. The two tokens are distinct and neither is read for the other: $a^{\mathrm{fop}}$ is never an opposite algebra, and $\mathbb{B}^{\mathrm{opp}}$ is never an operator.

## The Subscripts

A subscript is written with the underscore, `_`, inside the math delimiters, and the underscore takes a single token: one character is written bare, $Q_t$ and $Q_k$, and two characters or more are wrapped in braces, $Q_{n+1}$ and $\mathbb{B}_{\mathrm{r}}$, because a bare underscore would take the first character alone.

**A subscript is never a partial derivative.** The subscript marks a component or a label, a partial derivative is written with $\partial$, and the rule is fixed in *Conventions of the Operators and the Calculus*, §*Conventions for Derivation*.

**A coefficient carries a letter index and an element a number.** In the quaternionic layers a coefficient is indexed by the direction it multiplies, $Q_x$ and $q_x$, and an element that is counted carries a number on its tilde, $\tilde Q_1, \tilde Q_2$. In the commutative layers, which have no direction, both the element and its coefficients carry the number of the element, $Q_1 = q_1 + iq'_1$. The two indices are of different kinds, a letter against a number, so a coefficient index is never read as the number of an element, nor the reverse.

**It is allowed to add subscripts when several elements of the same kind are used.** The permission covers the general elements, the units, the roots, the idempotents and the nilpotents alike: wherever a statement carries more than one element of one kind, the occurrences are told apart by a subscript.

**A subscript counts, or it names.** A subscript that only tells one occurrence from another is numeric, so that a family is $\tilde Q_1, \tilde Q_2, \dots$ and a second numbered family of the same statement takes the next numbers. A subscript that names the object or the role it qualifies is a **role label**, and a role label is written in upright roman, as in $\mathbb{B}_{\mathrm{r}}$ and $\tilde U_{\mathrm r}$.

**A role-labelled element carries its label in its coefficients.** The generic element-valued field is $\tilde Q_{\mathrm f}=Q_{\mathrm{f}t}e_t+\vec Q_{\mathrm f}$, and its components are $Q_{\mathrm{f}t}$ and $Q_{\mathrm{f}\mu}$: the label $\mathrm f$ belongs to the element and is carried once into the component subscript, beside the direction, so that the components are $Q_{\mathrm{f}t}$ and $Q_{\mathrm{f}\mu}$; it does not count a family. A numbered family is unaffected, $\tilde Q_1=Q_{1t}e_t+\vec Q_1$.

**The two parts are named by their star.** The Hermitian part is $\tilde Q_{\mathrm H}$, the fixed element of the star, and the anti-Hermitian part is $\tilde Q_{\mathrm A}$, its anti-fixed element: $\tilde Q=\tilde Q_{\mathrm H}+\tilde Q_{\mathrm A}$ is the split read on the coefficients, defined in *Conventions in the Biquaternion Universe*, §*The Hermitian and Anti-Hermitian Subspaces*. The words **informational** and **material** name $\tilde Q_{\mathrm H}$ and $\tilde Q_{\mathrm A}$ in the physical articles. The two letters label the parts of one element and not two fields, so no label passes into the coefficients: $\tilde Q_{\mathrm H}$ and $\tilde Q_{\mathrm A}$ keep the names $Q_t,Q_x,Q_y,Q_z$ and select the slots.

**A sign is a subscript where the statement needs one**, the member attached to $+1$ taking the subscript $+$ and the member attached to $-1$ the subscript $-$, as in $\tilde\Pi_+$ and $\tilde\Pi_-$. In the reduced biquaternion layer the sign belongs to the idempotent pair and to its coordinates, $\Pi_\pm$, $Q_{+}$ and $Q_{-}$, the two basis coordinates carrying the triangles, $Q_{\blacktriangle}$ and $Q_{\blacktriangledown}$, and a numbered element putting its number first in either case, $Q_{1+}$ and $Q_{1\blacktriangle}$; the element they build is $\breve Q$. The sign is read with the glyph: $\tilde Q_\pm$ names an element of the sector $\mathbb{M}_\pm$, while $Q_\pm$ names the idempotent coordinates of $\breve Q$.

The forms a subscript takes are these.

| The subscript is | Example |
|---|---|
| a digit | $\tilde Q_1$, $\tilde Q_2$ |
| a letter | $Q_k$, $Q_\mu$ |
| two indices | $Q_{ab}$ |
| a sign | $\tilde\Pi_\pm$ |
| an upright word | $\mathbb{B}_{\mathrm{r}}$, $\tilde U_{\mathrm r}$ |
| a grouped expression | $Q_{n+1}$ |

## Summary

A unit element is not a physical unit. The series uses the SI, the coefficients of one element share one unit, and the default temporal slot is $ict'$ in metres, with $it'$ and $g_{tt}=-c^2$ stated where an article uses it. A dimensionless number carries no unit and no conversion, and $\mu$ is read by context among the permeability, the inverse Compton length and the direction label.

Two superscript tokens run beside the element marks. $\mathrm{fop}$ marks the Fock operator, the one glyph that is not an element; $\mathrm{opp}$ marks the opposite algebra, and it is written on an algebra name. The Fock mark comes first and the dagger follows it, $a^{\mathrm{fop}\dagger}$.

A subscript is written with the underscore and one token. It is a component or a label, never a derivative. A coefficient carries a letter index and a counted element a number; a subscript either counts or names, and a role label is carried once into the coefficients. A sign is a subscript where the statement needs one. The allowed forms are the digit, the letter, two indices, a sign, an upright word and a grouped expression.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| SI | Metre, second, kilogram, kelvin, coulomb, with the derived units built on them |
| $ict'$, $\vec q$ | The default material coordinate, time measured in metres |
| $it'$, $g_{tt}=-c^2$ | The second writing of the temporal slot, time in seconds; stated where used |
| $\mu$ | Permeability, inverse Compton length $\mu=mc/\hbar$, or direction label; read by context |
| $^{\mathrm{fop}}$ | The Fock-operator mark, the one glyph that is not an element |
| $^{\mathrm{opp}}$ | The opposite algebra, written on an algebra name |
| $Q_{\mathrm{f}t}$, $Q_{n+1}$, $\tilde\Pi_\pm$, $\mathbb{B}_{\mathrm{r}}$ | The subscript forms: letter index, grouped expression, sign, upright word |

## Further Reading

- [Conventions in the Biquaternion Universe](conventions-in-the-biquaternion-universe.html), for the base these conventions qualify.
- [Conventions of the Operators and the Calculus](conventions-of-the-operators-and-the-calculus.html), for the operators that take the Fock mark and the derivative that is never a subscript.
- [Conventions in Mathematics](../articles_maths/conventions-in-mathematics.html), for the same subscript rules on the mathematical corpus.
