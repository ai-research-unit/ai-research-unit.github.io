# __Unit, Index and Notation Conventions__

## Introduction

These are the conventions of the units, of the two superscript tokens and of the subscripts. They are the last of the series because every earlier article depends on them, and they assume the base of *Algebra and Element Conventions* and the operators of *Operator and Calculus Conventions*.

The order is from the physical to the typographical. The SI units come first, with the rule that the coefficients of one element share one unit and with the two writings of the temporal slot. Then the two superscript tokens, $\mathrm{fop}$ and $\mathrm{opp}$. Then the subscript, which counts or names and is never a derivative.

## Physical Units

**A unit element is not a physical unit.** The base $e_t,\vec e_x,\vec e_y,\vec e_z$ of *Algebra and Element Conventions*, §*The Base and Its Units* is algebraic: its structure constants are $0$ or $\pm1$, and the biquaternion norm is a sum of four squares of coefficients. No element of $\mathbb{B}$ carries a metre, a second or a kilogram. A physical unit enters only where an element is **identified** with a physical quantity, and that identification is a convention of the article that makes it, not a property of the algebra. The phrase *unit element* names a basis element and *physical unit* names a convention of measurement; the two are never exchanged.

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

## The Upper and Low Marks

**These rules are real, and partial.** They fix the marks of the common uses and they bind wherever they apply. They do not cover every use: a mark that falls outside them is governed by the section that fixes it, and a stricter rule stated in the corpus overrides them — the derivation convention of *Operator and Calculus Conventions*, §*Conventions for Derivation*, the Fock and opposite tokens of §*The Superscripts*, and the forms of §*The Subscripts*.

**A caret is the exclusive carrier of those things:**

- a power, $2^k$, $e^\lambda$, $(-1)^j$, $\alpha^k$, $2^{k/2-1}$;
- a conjugation, $a^{*}$, $a^{\dagger}$, $a^{\natural}$;
- a transposition, $L^T$, $\psi^T$;
- a construction, $\mathbb{B}^\times$, $S^{\otimes n}$, $\mathrm{sym}^l$, $\Lambda^kTM$ (degree).

**A low mark is the exclusive carrier of those things:**

- a numeric count, $Q_1$, $M_2$;
- a coordinate or a component, $q_i$, $dq_i$, $x_i$, $p_i$, $Q_i$, $\theta_i$, $\xi_k$, $v_i$;
- a frame or basis vector, a gamma, $\vec e_i$, $\gamma_i$;
- a sign symbol, $\delta_{ij}$, $\varepsilon_{ijk}$, $\eta_{ij}$;
- a gauge, colour, isospin or spin index, $T_a$, $G_a$, $\sigma_z$;
- a connection or curvature component, $\Gamma_k$, $\mathrm{Ric}_{ij}$, $\omega_i$, $g_{ij}$;
- a differential, $dx_i$.

**The lists rule on these uses, not on the names.** A raised grade, parameter, sector or order is a name, not a power, a conjugation, a transposition or a construction, and the article that uses it says which name it is.

## The Superscripts

Two superscript tokens run beside the marks of the elements and the marks of the conjugations, and neither is to be read for the other:

| Token | Written on | Meaning |
|---|---|---|
| $^{\mathrm{fop}}$ | a Fock-operator glyph | an operator on the Fock space, the Fock-operator mark |
| $^{\mathrm{opp}}$ | an algebra name, or an element naming a tensor factor | the opposite algebra, the algebra with the reversed product |

**The mark, and its one use.** The marks of the elements say what a glyph **is**, not that it is an **operator** (*Operator and Calculus Conventions*, §*The Operators*). The single exception is the **Fock layer**, whose operators act on a Fock space and are **not** elements of the algebra. Only these carry the upright superscript $\mathrm{fop}$, set on the glyph and read as part of it:

$$
a^{\mathrm{fop}},\quad b^{\mathrm{fop}},\quad a^{\mathrm{fop}\dagger},\quad b^{\mathrm{fop}\dagger},\quad \psi^{\mathrm{fop}},\quad N^{\mathrm{fop}},\quad H^{\mathrm{fop}},\quad F^{\mathrm{fop}},\quad Ϙ^{\mathrm{fop}},\quad U^{\mathrm{fop}} .
$$

The mark says exactly one thing — the glyph is not an element, it is an operator on the Fock space — and it is written on nothing else. It is not a general mark of operators: the momentum $\vec p=-i\hbar\nabla$ keeps its element glyph and never takes the Fock mark, the quadratures $x$ and $p$ of the oscillator are written $x$ and $p$, the spin $S_k=\tfrac{\hbar}{2}\sigma_k$ is written $S_k$, and the parity, charge-conjugation and time-reversal maps $P$, $C$ and $T$ carry no mark. Where a ladder is meant as an element of the algebra it is written with the element's glyph, the truncated pair $\vec\Upsilon_1,\vec\Upsilon_2$, and the abstract ladder operator keeps the mark, $a^{\mathrm{fop}}$.

**It combines with the dagger, the mark first.** The dagger is the general adjoint (*Operator and Calculus Conventions*, §*The Operators*); the superscript marks the Fock operator. Where both are written on the same glyph, the Fock mark comes first and the adjoint follows, $(a^{\mathrm{fop}})^{\dagger}$, contracted to $a^{\mathrm{fop}\dagger}$. The dagger alone never says that its glyph is an operator, and the superscript alone never says that the Fock operator is self-adjoint; the two are read together, so that $a^{\mathrm{fop}\dagger}$ is the adjoint of the ladder and $N^{\mathrm{fop}}$ is written without an adjoint because it is self-adjoint.

**The opposite algebra carries a different token.** The reversed-product algebra is written with the superscript $\mathrm{opp}$, $\mathbb{B}^{\mathrm{opp}}$, $A^{\mathrm{opp}}$, $M_n(D)^{\mathrm{opp}}$, on an **algebra name**, where the Fock mark is written on a **Fock-operator glyph**. The two tokens are distinct and neither is read for the other: $a^{\mathrm{fop}}$ is never an opposite algebra, and $\mathbb{B}^{\mathrm{opp}}$ is never an operator.

**On an element the mark names a tensor factor.** Written on an element it means the same element read in the opposite algebra, $e_\nu^{\mathrm{opp}}$, and it is written there for that one purpose: to name the second factor of the tensor product $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}$, whose elementary tensors $e_\mu\otimes e_\nu^{\mathrm{opp}}$ are the cells $L_{e_\mu}R_{e_\nu}$ of the two-sided operators. The element is not thereby an operator, the mark says nothing about a side, and on an operator glyph it is a defect. It marks an algebra, a module of one, and an element read in that algebra; it never marks a set or a bare vector space.

**A caret carries a label as it carries a power.** The upright roman name of a construction, a frame or a variant of an object is written in the caret, and the physical corpus writes its own beside the two tokens: $\mathrm{orb}$ on the orbital part, $\mathrm{inc}$ on the incident field, $\mathrm{out}$ on the outgoing solution, $\mathrm{ret}$ on the retarded field, $\mathrm{reg}$ on the regularised Green function, $\mathrm{can}$ on the canonical tensor, $\mathrm{pol}$ on the polarisation vector, $\mathrm{lor}$ on the Lorentz object, $\mathrm{wkb}$ on the approximation, $\mathrm{mhv}$ on the amplitude, $\mathrm{epr}$ on the steering value. Italic is a power and upright is a name, so $E_0^{\mathrm{wkb}}$ is a labelled energy and never a power of $E_0$. The label is three lowercase letters by default, and the index of the three-letter labels, mathematical and physical together, is *Index, Notation and Corpus Conventions*, §*The Three-Letter Labels*; a label names the object the glyph denotes on the caret and a part or a role of it in the low slot, $s_{\mathrm{tot}}$, $U_{\mathrm{lor}}$. **No three-letter token in the caret carries a capital.** The operator name is written lowercase with its argument, $\operatorname{sym}(V)$ and $\operatorname{sym}^2(E)$, and so are the twelve codes of the algebraic structures, $\mathrm{gpa}$, $\mathrm{gps}$, $\mathrm{gqa}$, $\mathrm{gqs}$, $\mathrm{spa}$, $\mathrm{sps}$, $\mathrm{sqa}$, $\mathrm{sqs}$, $\mathrm{apa}$, $\mathrm{aps}$, $\mathrm{aqa}$, $\mathrm{aqs}$, whose letters are the initials of general, symmetric, antisymmetric, plain, quaternionic, algebra and sesqualgebra. A code sits in the caret, on the object and on its multiplication: $V^{\mathrm{gpa}}=V^{\mathrm{spa}}+V^{\mathrm{apa}}$, $\tilde Q_1\diamond^{\mathrm{aqs}}\tilde Q_2$. The three families the rule reaches — the labels, the operator names and the codes — are stated once in *Index, Notation and Corpus Conventions*, §*The Three-Letter Labels*. A label that names the object goes on the caret and a label that names a part stays low, and the fifteen labels that name the object — $\mathrm{aff}$, $\mathrm{amp}$, $\mathrm{app}$, $\mathrm{est}$, $\mathrm{geo}$, $\mathrm{hom}$, $\mathrm{hyp}$, $\mathrm{iso}$, $\mathrm{lab}$, $\mathrm{mat}$, $\mathrm{mix}$, $\mathrm{mot}$, $\mathrm{obs}$, $\mathrm{pot}$, $\mathrm{src}$ — are on the caret.

## The Subscripts

A subscript is written with the underscore, `_`, inside the math delimiters, and the underscore takes a single token: one character is written bare, $Q_t$ and $Q_k$, and two characters or more are wrapped in braces, $Q_{n+1}$ and $\mathbb{B}_{\mathrm{r}}$, because a bare underscore would take the first character alone.

**A subscript is never a partial derivative.** The subscript marks a component or a label, a partial derivative is written with $\partial$, and the rule is fixed in *Operator and Calculus Conventions*, §*Conventions for Derivation*.

**A coefficient carries a letter index and an element a number.** In the quaternionic layers a coefficient is indexed by the direction it multiplies, $Q_x$ and $q_x$, and an element that is counted carries a number on its tilde, $\tilde Q_1, \tilde Q_2$. In the commutative layers, which have no direction, both the element and its coefficients carry the number of the element, $Q_1 = q_1 + iq'_1$. The two indices are of different kinds, a letter against a number, so a coefficient index is never read as the number of an element, nor the reverse.

**It is allowed to add subscripts when several elements of the same kind are used.** The permission covers the general elements, the units, the roots, the idempotents and the nilpotents alike: wherever a statement carries more than one element of one kind, the occurrences are told apart by a subscript.

**A subscript counts, or it names.** A subscript that only tells one occurrence from another is numeric, so that a family is $\tilde Q_1, \tilde Q_2, \dots$ and a second numbered family of the same statement takes the next numbers. A subscript that names the object or the role it qualifies is a **role label**, and a role label is written in upright roman, as in $\mathbb{B}_{\mathrm{r}}$ and $\tilde U_{\mathrm r}$.

**A role-labelled element carries its label in its coefficients.** The generic element-valued field is $\tilde Q_{\mathrm f}=Q_{\mathrm{f}t}e_t+\vec Q_{\mathrm f}$, and its components are $Q_{\mathrm{f}t}$ and $Q_{\mathrm{f}\mu}$: the label $\mathrm f$ belongs to the element and is carried once into the component subscript, beside the direction, so that the components are $Q_{\mathrm{f}t}$ and $Q_{\mathrm{f}\mu}$; it does not count a family. A numbered family is unaffected, $\tilde Q_1=Q_{1t}e_t+\vec Q_1$.

**The two parts are named by their star.** The Hermitian part is $\tilde Q_{\mathrm H}$, the fixed element of the star, and the anti-Hermitian part is $\tilde Q_{\mathrm A}$, its anti-fixed element: $\tilde Q=\tilde Q_{\mathrm H}+\tilde Q_{\mathrm A}$ is the split read on the coefficients, defined in *Algebra and Element Conventions*, §*The Hermitian and Anti-Hermitian Subspaces*. The words **informational** and **material** name $\tilde Q_{\mathrm H}$ and $\tilde Q_{\mathrm A}$ in the physical articles. The two letters label the parts of one element and not two fields, so no label passes into the coefficients: $\tilde Q_{\mathrm H}$ and $\tilde Q_{\mathrm A}$ keep the names $Q_t,Q_x,Q_y,Q_z$ and select the slots.

**An angular-momentum total takes the role subscript, and its projection the axis.** A spin label is $s$ with projection $s_z$; the total of an orbital and a spin part, or of several spins, is $s_{\mathrm{tot}}$ with projection $s_{\mathrm{tot},z}$, and the operator is $\tilde S_{\mathrm{tot},k}=\tilde L_k+\tilde S_k$. The subscript $k$ is the vector index of the operator, and the three components close on $[\tilde S_{\mathrm{tot},i},\tilde S_{\mathrm{tot},j}]=i\hbar\epsilon_{ijk}\tilde S_{\mathrm{tot},k}$. The projection is not a component of the operator: it is the scalar weight, the eigenvalue of $\tilde S_{\mathrm{tot},3}$ on $|s_{\mathrm{tot}},s_{\mathrm{tot},z}\rangle$, and it names the axis $z$ on which the measurement is made. The role is repeated in the projection so that $s_{1z}$, $s_{2z}$ and $s_{\mathrm{tot},z}$ are told apart without the context; the operator keeps the vector index $k$, and the weight never takes it. The role and the axis share one pair of braces, $s_{\mathrm{tot},z}$, with a comma between them.

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

**The letter $\iota$ is not used.** No physics article uses $\iota$, in any spelling. The comparison of the biquaternion algebra with the even Clifford algebra is written by its values, $e_t\mapsto I_4$ and $\vec e_x\mapsto\gamma_2\gamma_3$, or by the words "the Clifford image", and never by a symbol. An interior product is written as the pairing it is, $\omega(X_f,\,\cdot\,)=df$, and an inner automorphism in words. The letter is not reserved for a third object: it carries no meaning in the series, and a display that introduces it is a defect.

## Summary

A unit element is not a physical unit. The series uses the SI, the coefficients of one element share one unit, and the default temporal slot is $ict'$ in metres, with $it'$ and $g_{tt}=-c^2$ stated where an article uses it. A dimensionless number carries no unit and no conversion, and $\mu$ is read by context among the permeability, the inverse Compton length and the direction label.

Two superscript tokens run beside the element marks. $\mathrm{fop}$ marks the Fock operator, the one glyph that is not an element; $\mathrm{opp}$ marks the opposite algebra, and it is written on an algebra name or on an element that names a tensor factor. The Fock mark comes first and the dagger follows it, $a^{\mathrm{fop}\dagger}$. An upright label of a construction or a variant is written in the caret as well, three lowercase letters by default — $\mathrm{orb}$, $\mathrm{inc}$, $\mathrm{out}$, $\mathrm{ret}$, $\mathrm{reg}$, $\mathrm{lor}$, $\mathrm{wkb}$, $\mathrm{epr}$ in this corpus — and the index of the labels is *Index, Notation and Corpus Conventions*, §*The Three-Letter Labels*. Every token the caret carries is lowercase: $\operatorname{sym}(V)$ the symmetric algebra and $\mathrm{gpa}$ the general plain algebra are written as $\mathrm{opp}$ is.

A subscript is written with the underscore and one token. It is a component or a label, never a derivative. A coefficient carries a letter index and a counted element a number; a subscript either counts or names, and a role label is carried once into the coefficients. A sign is a subscript where the statement needs one. The allowed forms are the digit, the letter, two indices, a sign, an upright word and a grouped expression. The letter $\iota$ is not used at all. An **angular-momentum total** takes the role subscript, $s_{\mathrm{tot}}$, and its projection the axis, $s_{\mathrm{tot},z}$; the operator carries the vector index, $\tilde S_{\mathrm{tot},k}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| SI | Metre, second, kilogram, kelvin, coulomb, with the derived units built on them |
| $ict'$, $\vec q$ | The default material coordinate, time measured in metres |
| $it'$, $g_{tt}=-c^2$ | The second writing of the temporal slot, time in seconds; stated where used |
| $\mu$ | Permeability, inverse Compton length $\mu=mc/\hbar$, or direction label; read by context |
| $^{\mathrm{fop}}$ | The Fock-operator mark, the one glyph that is not an element |
| $^{\mathrm{opp}}$ | The opposite algebra, written on an algebra name or on an element that names a tensor factor |
| $\mathrm{orb}$, $\mathrm{inc}$, $\mathrm{out}$, $\mathrm{lor}$ | The three-letter labels of a construction or a variant; the index is *Index, Notation and Corpus Conventions*, §*The Three-Letter Labels* |
| $\operatorname{sym}$, $^{\mathrm{gpa}}$ … $^{\mathrm{aqs}}$ | An operator name in the caret, $\operatorname{sym}(V)$, $\operatorname{sym}^2(E)$, and a code of the twelve structures, written in the caret beside it, $V^{\mathrm{gqa}}=V^{\mathrm{sqa}}$; both lowercase |
| $Q_{\mathrm{f}t}$, $Q_{n+1}$, $\tilde\Pi_\pm$, $\mathbb{B}_{\mathrm{r}}$ | The subscript forms: letter index, grouped expression, sign, upright word |
| $s_{\mathrm{tot}}$, $s_{\mathrm{tot},z}$, $\tilde S_{\mathrm{tot},k}$ | Total angular-momentum label, its projection, and the operator, which carries the vector index $k$ |

## Further Reading

- [Conventions in the Biquaternion Universe](conventions-in-the-biquaternion-universe.html), for the base these conventions qualify.
- [Conventions of the Operators and the Calculus](conventions-of-the-operators-and-the-calculus.html), for the operators that take the Fock mark and the derivative that is never a subscript.
- [Conventions in Mathematics](../articles_maths/conventions-in-mathematics.html), for the same subscript rules on the mathematical corpus.
