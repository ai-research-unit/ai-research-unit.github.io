# __Unit, Index and Notation Conventions__

## Introduction

These are the conventions of the units, of the labels and of the subscripts. They are the last of the series because every earlier article depends on them, and they assume the base of *Algebra and Element Conventions* and the operators of *Operator and Calculus Conventions*.

The order is from the physical to the typographical. The SI units come first, with the rule that the coefficients of one element share one unit and with the two writings of the temporal slot. Then the two labels, $\mathrm{fop}$ and $\mathrm{opp}$. Then the subscript, which counts or names and is never a derivative.

## Physical Units

**A unit element is not a physical unit.** The base $e_t,\vec e_x,\vec e_y,\vec e_z$ of *Algebra and Element Conventions*, §*The Base and Its Units* is algebraic: its structure constants are $0$ or $\pm1$, and the biquaternion norm is a sum of four squares of coefficients. No element of $\mathbb{B}$ carries a metre, a second or a kilogram. A physical unit enters only where an element is **identified** with a physical quantity, and that identification is a convention of the article that makes it, not a property of the algebra. The phrase *unit element* names a basis element and *physical unit* names a convention of measurement; the two are never exchanged.

**The series uses the SI.** Length is measured in metres, time in seconds, mass in kilograms, temperature in kelvin and charge in coulomb. The derived units follow from these, and the ones the articles use are collected here.

| Quantity | Symbol | Unit |
|---|---|---|
| Length | $x,y,z$; $i c r'_t$ in the length coordinate | metre ($\mathrm{m}$) |
| Time | $r'_t$ in the time coordinate | second ($\mathrm{s}$) |
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

**The coefficients of one element share one unit.** The biquaternion norm is a sum of four squares of the coefficients of a single element, so the four terms are commensurable only if the four coefficients carry the same unit. The requirement is per element and not across elements: the coefficients of a four-displacement are lengths and its norm a length squared, the coefficients of a four-velocity are speeds and its norm a speed squared, and the temporal slot of a four-potential carries the parameter $a'_t=\xi_{\mathrm{scp}}/c$ rather than $\xi_{\mathrm{scp}}$ so that its four components share the unit of the vector potential. The unit is the unit of the quantity the element represents, and it is supplied by the identification.

**The two writings of the temporal slot.** In the length coordinate the material position is $\tilde R_\varphi = i c r'_t\,e_t+\vec q$, with time measured in metres; this is the corpus's default. In the time coordinate the temporal component is $ir'_t$, time stays in seconds, and the conversion is carried by the square of the coordinate: $Q_t=i c r'_t$ has $Q_t^2=-c^2{r'_{t}}^2$, and the metric stays the unit metric, $\delta_{\mu\nu}=(1,1,1,1)$. The quadratic form is one and the same, $\langle\tilde R_\varphi\rangle_{\natural}=-c^2{r'_{t}}^2+r_x^2+r_y^2+r_z^2$; the two differ only in where the factor $c$ is written, and an article that uses the second states it where the temporal slot is read.

**Dimensionless and dimensionful.** A pure number — the fine-structure constant $\alpha$, the ratio $g=2$, the phase $S/\hbar$, the trace normalisation $2$ — carries no unit and no conversion. A dimensionful constant is a unit conversion and is written with its unit. No dimensionful constant is derived by the algebra: $c$, $\hbar$, $k_B$, $G$, $m$ and $ϙ$ are inserted at the places where the structure requires a scale. The metrology says the same thing from the other side. Since the 2019 revision the SI fixes $c$, $h$, the elementary charge and $k_B$ by definition and realises the units from them, while a dimensionless constant such as $\alpha$ has to be measured. An article that sets a constant to one — $c=1$, $\hbar=1$ or $G=1$ — says so locally, and the constant returns wherever a dimensional statement is at issue.

**A caution on $\mu$.** The letter $\mu$ names the permeability in $c=1/\sqrt{\epsilon\mu}$ and the inverse Compton length in $\mu=mc/\hbar$, and it is the direction label in $e_\mu$ and $Q_\mu$. The corpus distinguishes the uses by context; an article should not use two of them in one expression.

## The Upper and Low Marks

**These rules are real, and partial.** They fix the marks of the common uses and they bind wherever they apply. They do not cover every use: a mark that falls outside them is governed by the section that fixes it, and a stricter rule stated in the corpus overrides them — the derivation convention of *Operator and Calculus Conventions*, §*Conventions for Derivation*, the Fock and opposite tokens of §*The Labels*, and the forms of §*The Subscripts*.

**A caret is the exclusive carrier of those things:**

- a power, $2^k$, $e^\lambda$, $(-1)^j$, $\alpha^k$, $2^{k/2-1}$;
- a conjugation, $a^{*}$, $a^{\dagger}$, $a^{\natural}$;
- a transposition, $L^T$, $\tilde{Ξ}_{\mathrm{sp}}^T$;
- a construction, $\mathbb{B}^\times$, $S^{\otimes n}$, $\mathrm{sym}^l$, $\Lambda^kTM$ (degree).

**A low mark is the exclusive carrier of two things: an index and a label.**

- an index — a numeric count, $Q_1$, $M_2$; the slot of a coordinate, $q_i$, $x_i$, $p_i$, $Q_i$, $\theta_i$, $\zeta_k$, $v_i$; the slot of a basis vector or a gamma, $\vec e_i$, $\gamma_i$; the slots of an invariant symbol, $\delta_{ij}$, $\varepsilon_{ijk}$, $\eta_{ij}$; the generator of a gauge, colour, isospin or spin family, $T_a$, $G_a$, $\sigma_z$; the slot of a connection or curvature component, $\Gamma_k$, $\mathrm{Ric}_{ij}$, $\omega_i$, $g_{ij}$; the slot of a differential, $dx_i$.
- a label naming the object, a part of it or a role of it, $E_{\mathrm{wkb}}$, $s_{\mathrm{tot}}$, $S_{\mathrm{int}}$, with every label of §*The Three-Letter Labels*; the label comes first in the subscript and an index already there follows it after a comma, $T_{\mathrm{em},\mu\nu}$; the family letters of a regular matrix are of this kind, $L$ and $R$ naming the left and the right part, $\mathsf M_{4L}$ and $\mathsf M_{4R}$.

**The word *metric* has one meaning in the series. There is one metric, the unit metric $\delta_{\mu\nu}=(1,1,1,1)$: diagonal, all four coefficients $+1$, the matrix of the interval $\sum_\mu Q_\mu^2$. A frame carries a coordinate, not a metric. The minus of the material sector is not a metric: it is $i^2=-1$ in $Q_t=i c r'_t$, made once on the time.**

**No index is raised, because the one metric is the identity.** The series has one metric, the unit metric $\delta_{\mu\nu}=(1,1,1,1)$, and raising with it changes nothing: a raised index would be the same index. A gamma is written low, $\gamma_\mu$, and the weight does the only work a raising could do, $\gamma^\mu=-\varepsilon_\mu\gamma_\mu$. A text that needs a raised index on a coefficient is writing a metric the series does not have.

**The object is not the role.** A coordinate, a basis vector, a gamma, an invariant symbol, a gauge generator, a component of a connection and a differential are seven kinds of object, and the low mark does one thing on all seven: it gives the index that names the slot of the family the glyph belongs to. The index says **which** member, never **what kind**, and the kind is carried by the glyph itself, $x_i$ against $\gamma_i$ against $\delta_{ij}$. A differential carries the same mark as the coordinate it differentiates, $x_i$ and $dx_i$, because the slot is the same in both. Nor does the alphabet divide the work: a letter is an index in $q_i$ and a number is an index in $Q_1$, and the two are of different kinds only where a coefficient and an element meet (§*The Subscripts*).

**The lists rule on these uses, not on the names.** A raised grade, parameter, sector or order is a name, not a power, a conjugation, a transposition or a construction, and the article that uses it says which name it is.

## The Labels

Two labels run beside the marks of the elements and the marks of the conjugations, and neither is to be read for the other:

| Label | Written on | Meaning |
|---|---|---|
| $\mathrm{fop}$ | a Fock-operator glyph | an operator on the Fock space, the Fock-operator mark |
| $\mathrm{opp}$ | an algebra name, or an element naming a tensor factor | the opposite algebra, the algebra with the reversed product |
| $\mathrm{spl}$ | an algebra name | the split variant, $\mathbb{C}_{\mathrm{spl}}$, $\mathbb{H}_{\mathrm{spl}}$, $\mathbb{B}_{\mathrm{spl}}$ |
| $\mathrm{red}$ | an algebra name | the reduced variant, $\mathbb{B}_{\mathrm{red}}=\mathbb{C}\oplus\mathbb{C}$ |
| $\mathrm{dln}$ | an algebra name | the dual numbers, $\mathbb{C}_{\mathrm{dln}}=\mathbb{R}[\varepsilon]/(\varepsilon^{2})$ |

**Four qualifiers name a variant of an algebra.** They stand low, three lowercase letters each, the label first and any index after it:  $\mathrm{spl}$ on a split variant, $\mathbb{C}_{\mathrm{spl}}$ the split-complex numbers, $\mathbb{H}_{\mathrm{spl}}$ the split-quaternions and $\mathbb{B}_{\mathrm{spl}}$ the split-biquaternions; $\mathrm{red}$ on the reduced biquaternions, $\mathbb{B}_{\mathrm{red}}$; and $\mathrm{dln}$ on the dual numbers, $\mathbb{C}_{\mathrm{dln}}$. Italic is a power and upright is a name, and the label is low, so $\mathbb{C}_{\mathrm{spl}}$ is never a power of $\mathbb{C}$. **$\mathrm{dln}$ is not $\mathrm{dual}$**: $\mathrm{dual}$ marks the Hodge dual of a field, $F_{\mathrm{dual}}$, and the two tokens are never exchanged. **$\mathbb{B}_{\mathrm{red}}$ is not a part of $\mathbb{B}$.** The reduced biquaternions are $\mathbb{C}\oplus\mathbb{C}$, of real dimension four, and the biquaternions are of real dimension eight; the qualifier names a different algebra and not a subalgebra of $\mathbb{B}$.

**The mark, and its one use.** The marks of the elements say what a glyph **is**, not that it is an **operator** (*Operator and Calculus Conventions*, §*The Operators*). The single exception is the **Fock layer**, whose operators act on a Fock space and are **not** elements of the algebra. Only these carry the Fock label $\mathrm{fop}$, set low on the glyph and read as part of it:

$$
a_{\mathrm{fop}},\quad b_{\mathrm{fop}},\quad a_{\mathrm{fop}}^{\dagger},\quad b_{\mathrm{fop}}^{\dagger},\quad \tilde{Ξ}_{\mathrm{fop}},\quad N_{\mathrm{fop}},\quad H_{\mathrm{fop}},\quad F_{\mathrm{fop}},\quad Ϙ_{\mathrm{fop}},\quad U_{\mathrm{fop}} .
$$

The mark says exactly one thing — the glyph is not an element, it is an operator on the Fock space — and it is written on nothing else. It is not a general mark of operators: the momentum $\vec p=-i\hbar\nabla$ keeps its element glyph and never takes the Fock mark, the quadratures $x$ and $p$ of the oscillator are written $x$ and $p$, the spin $S_k=\tfrac{\hbar}{2}\sigma_k$ is written $S_k$, and the parity, charge-conjugation and time-reversal maps $P$, $C$ and $T$ carry no mark. Where a ladder is meant as an element of the algebra it is written with the element's glyph, the truncated pair $\vec\Upsilon_1,\vec\Upsilon_2$, and the abstract ladder operator keeps the mark, $a_{\mathrm{fop}}$.

**It stands low, and the dagger stands in the caret.** The dagger is the general adjoint (*Operator and Calculus Conventions*, §*The Operators*); the label marks the Fock operator. Where both are written on the same glyph the two occupy two slots, the Fock label low and the adjoint raised, $(a_{\mathrm{fop}})^{\dagger}$, contracted to $a_{\mathrm{fop}}^{\dagger}$. The dagger alone never says that its glyph is an operator, and the label alone never says that the Fock operator is self-adjoint; the two are read together, so that $a_{\mathrm{fop}}^{\dagger}$ is the adjoint of the ladder and $N_{\mathrm{fop}}$ is written without an adjoint because it is self-adjoint.

**The bar is the coefficient conjugation, and it is never the Dirac adjoint.** It is the involution of *Algebra and Element Conventions*, $\bar{\tilde Q}=\bar Q_te_t+\bar Q_x\vec e_x+\bar Q_y\vec e_y+\bar Q_z\vec e_z$, and it conjugates the coefficients of an element. The Dirac adjoint is not an involution of the algebra and takes no mark of its own: it is the adjoint of the column followed by the timelike frame cell, written as the two multipliers of that cell,
$$
\tilde{Ξ}_{\mathrm{sp}}^{\dagger}\,iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_x} \;=\; \tilde{Ξ}_{\mathrm{sp}}^{\dagger}\,iR_{\mathrm{axf},\vec e_x} .
$$
In a bilinear the cell multiplies the one that follows, $\tilde{Ξ}_{\mathrm{sp}}^{\dagger}\bigl(iR_{\mathrm{axf},\vec e_x}\Gamma\bigr)\tilde{Ξ}_{\mathrm{sp}}$. No letter stands for the cell (*Matrix Representations Conventions*, §*The Clifford Structure*), and the bar is not reused for the composite: a display that writes $\tilde{Ξ}_{\mathrm{sp}}^{\dagger}iR_{\mathrm{axf},\vec e_x}$ and reads it as the adjoint puts a conjugation and a frame cell under one mark. A display already written that way is read as the expression above, and the bar itself stays the conjugation, as in $\bar{\tilde Q}$.

**The opposite algebra carries a different token.** The reversed-product algebra is written with the label $\mathrm{opp}$, low, $\mathbb{B}_{\mathrm{opp}}$, $A_{\mathrm{opp}}$, $M_n(D)_{\mathrm{opp}}$, on an **algebra name**, where the Fock mark is written on a **Fock-operator glyph**. The two tokens are distinct and neither is read for the other: $a_{\mathrm{fop}}$ is never an opposite algebra, and $\mathbb{B}_{\mathrm{opp}}$ is never an operator.

**On an element the mark names a tensor factor.** Written on an element it means the same element read in the opposite algebra, $e_{\mathrm{opp},\nu}$, and it is written there for that one purpose: to name the second factor of the tensor product $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}_{\mathrm{opp}}$, whose elementary tensors $e_\mu\otimes e_{\mathrm{opp},\nu}$ are the cells $L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu}$ of the two-sided operators. The element is not thereby an operator, the mark says nothing about a side, and on an operator glyph it is a defect. It marks an algebra, a module of one, and an element read in that algebra; it never marks a set or a bare vector space.

**Every label stands in the subscript.** The upright roman name of a construction, a frame or a variant of an object is written low, and the physical corpus writes its own beside the two of the algebra: $\mathrm{orb}$ on the orbital part, $\mathrm{inc}$ on the incident field, $\mathrm{out}$ on the outgoing solution, $\mathrm{ret}$ on the retarded field, $\mathrm{rgs}$ on the regularised kernel, $\mathrm{reg}$ on the regular representation, $\mathrm{can}$ on the canonical tensor, $\mathrm{pol}$ on the polarisation vector, $\mathrm{lor}$ on the Lorentz object, $\mathrm{wkb}$ on the approximation, $\mathrm{mhv}$ on the amplitude, $\mathrm{epr}$ on the steering value, $\mathrm{axf}$ on the axis-free display of the regular matrices, the display of the corpus, and $\mathrm{pau}$ on the Pauli display of the same matrices, which the gamma sections keep. Italic is a power and upright is a name, so $E_{\mathrm{wkb},0}$ is a labelled energy and never a power of $E_0$. The label is three lowercase letters by default, and the index of the three-letter labels, mathematical and physical together, is *Index, Notation and Corpus Conventions*, §*The Three-Letter Labels*; a label names the object the glyph denotes, a part of it or a role of it, $E_{\mathrm{wkb}}$, $s_{\mathrm{tot}}$, $S_{\mathrm{int}}$, and it stands first in the subscript, an index already there following it after a comma, $T_{\mathrm{em},\mu\nu}$. **No label carries a capital.** The operator name is written lowercase with its argument, $\operatorname{sym}(V)$ and $\operatorname{sym}^2(E)$. The twelve algebraic structures carry no code at all: a product is written by its two slots and the conjugation each one carries, $\tilde Q_1\tilde Q_2$, $\tilde Q_1\tilde Q_2^{*}$, $\tilde Q_1^{\natural}\tilde Q_2$, $\tilde Q_1^{\natural}\tilde Q_2^{*}$, $\tilde Q_1\bullet\tilde Q_2$, $\tilde Q_1\bullet_{*}\tilde Q_2$, $\tilde Q_1\bullet_{\natural}\tilde Q_2$, $\tilde Q_1\bullet_{\natural*}\tilde Q_2$, $\tilde Q_1\wedge\tilde Q_2$, $\tilde Q_1\wedge_{*}\tilde Q_2$, $\tilde Q_1\wedge_{\natural}\tilde Q_2$, $\tilde Q_1\wedge_{\natural*}\tilde Q_2$, and the operator names the structure on its own. Six spelling codes run beside the labels, $\mathrm{rgs}$, $\mathrm{tpl}$, $\mathrm{prm}$, $\mathrm{dfc}$, $\mathrm{obf}$, $\mathrm{adg}$, each separating the rarer of two words that share three letters — regularised from regular, topological from top, perimeter from periodic, defective from defining, orbifold from orbital, adjugate from adjoint — so that the corpus carries six codes in all. A code stands low like every other label, on the object it qualifies. A code is a label like the rest and stands low with them. The families the rule reaches — the labels, the operator names and the codes — are stated once in *Index, Notation and Corpus Conventions*, §*The Three-Letter Labels*. A label names the object, a part of it or a role of it, and every one of them stands low; the fifteen labels that name the object — $\mathrm{aff}$, $\mathrm{amp}$, $\mathrm{app}$, $\mathrm{est}$, $\mathrm{geo}$, $\mathrm{hom}$, $\mathrm{hyp}$, $\mathrm{iso}$, $\mathrm{lab}$, $\mathrm{mat}$, $\mathrm{mix}$, $\mathrm{mot}$, $\mathrm{obs}$, $\mathrm{pot}$, $\mathrm{src}$ — are low with the rest. Thirteen qualifiers that named the same object followed the same road, low, then on the caret, and now low again: $\mathrm{ret}$, $\mathrm{odd}$, $\mathrm{sgn}$, $\mathrm{opp}$, $\mathrm{fix}$, $\mathrm{lin}$, $\mathrm{nil}$, $\mathrm{wkb}$, $\mathrm{rep}$, $\mathrm{exp}$, $\mathrm{pol}$, $\mathrm{new}$, $\mathrm{imp}$. Six more carried two English words on one spelling; each took a code of its own, and the six pairs are in §*The Three-Letter Labels*.

## The Subscripts

A subscript is written with the underscore, `_`, inside the math delimiters, and the underscore takes a single token: one character is written bare, $Q_t$ and $Q_k$, and two characters or more are wrapped in braces, $Q_{n+1}$ and $\tilde Q_{\mathrm{f}t}$, because a bare underscore would take the first character alone.

**The label is written first in the field, and an index already there follows it after a comma.** $L_{\mathrm{axf},e_\mu}$ is the matrix of $\vec e_\mu$ in the axis-free frame, $s_{\mathrm{tot},z}$ the projection of the total, $\tilde S_{\mathrm{tot},k}$ the generator; the rule, its reasons and its four contrasts are stated in *Index, Notation and Corpus Conventions*, §*The Labels*.

**A subscript is never a partial derivative.** The subscript is an index or a label, a partial derivative is written with $\partial$, and the rule is fixed in *Operator and Calculus Conventions*, §*Conventions for Derivation*.

**A coefficient carries a letter index and an element a number.** In the quaternionic layers a coefficient is indexed by the direction it multiplies, $Q_x$ and $q_x$, and an element that is counted carries a number on its tilde, $\tilde Q_1, \tilde Q_2$. In the commutative layers, which have no direction, both the element and its coefficients carry the number of the element, $Q_1 = q_1 + iq'_1$. The two indices are of different kinds, a letter against a number, so a coefficient index is never read as the number of an element, nor the reverse.

**It is allowed to add subscripts when several elements of the same kind are used.** The permission covers the general elements, the units, the roots, the idempotents and the nilpotents alike: wherever a statement carries more than one element of one kind, the occurrences are told apart by a subscript.

**A subscript counts, or it names.** A subscript that only tells one occurrence from another is numeric, so that a family is $\tilde Q_1, \tilde Q_2, \dots$ and a second numbered family of the same statement takes the next numbers. A subscript that names the object or the role it qualifies is a **role label**, and a role label is written in upright roman, as in $\tilde Q_{\mathrm{f}t}$ and $\tilde U_{\mathrm r}$.

**A role-labelled element carries its label in its coefficients.** The generic element-valued field is $\tilde Q_{\mathrm f}=Q_{\mathrm{f}r_t}e_t+\vec Q_{\mathrm f}$, and its components are $Q_{\mathrm{f}t}$ and $Q_{\mathrm{f}\mu}$: the label $\mathrm f$ belongs to the element and is carried once into the component subscript, beside the direction, so that the components are $Q_{\mathrm{f}t}$ and $Q_{\mathrm{f}\mu}$; it does not count a family. A numbered family is unaffected, $\tilde Q_1=Q_{1t}e_t+\vec Q_1$.

**The two parts are named by their star.** The Hermitian part is $\tilde R_\psi$, the fixed element of the star, and the anti-Hermitian part is $\tilde R_\varphi$, its anti-fixed element: $\tilde Q=\tilde R_\psi+\tilde R_\varphi$ is the split read on the coefficients, defined in *Algebra and Element Conventions*, §*The Hermitian and Anti-Hermitian Subspaces*. The words **informational** and **material** name $\tilde R_\psi$ and $\tilde R_\varphi$ in the physical articles. The two letters label the parts of one element and not two fields, so no label passes into the coefficients: $\tilde R_\psi$ and $\tilde R_\varphi$ keep the names $Q_t,Q_x,Q_y,Q_z$ and select the slots.

**An angular-momentum total takes the role subscript, and its projection the axis.** A spin label is $s$ with projection $s_z$; the total of an orbital and a spin part, or of several spins, is $s_{\mathrm{tot}}$ with projection $s_{\mathrm{tot},z}$, and the operator is $\tilde S_{\mathrm{tot},k}=\tilde L_k+\tilde S_k$. The subscript $k$ is the vector index of the operator, and the three components close on $[\tilde S_{\mathrm{tot},i},\tilde S_{\mathrm{tot},j}]=i\hbar\epsilon_{ijk}\tilde S_{\mathrm{tot},k}$. The projection is not a component of the operator: it is the scalar weight, the eigenvalue of $\tilde S_{\mathrm{tot},3}$ on $|s_{\mathrm{tot}},s_{\mathrm{tot},z}\rangle$, and it names the axis $z$ on which the measurement is made. The role is repeated in the projection so that $s_{1z}$, $s_{2z}$ and $s_{\mathrm{tot},z}$ are told apart without the context; the operator keeps the vector index $k$, and the weight never takes it. The role and the axis share one pair of braces, $s_{\mathrm{tot},z}$, with a comma between them.

**A sign is a subscript where the statement needs one**, the member attached to $+1$ taking the subscript $+$ and the member attached to $-1$ the subscript $-$, as in $\tilde\Pi_+$ and $\tilde\Pi_-$. In the reduced biquaternion layer the sign belongs to the idempotent pair and to its coordinates, $\Pi_\pm$, $Q_{+}$ and $Q_{-}$, the two basis coordinates carrying the triangles, $Q_{\blacktriangle}$ and $Q_{\blacktriangledown}$, and a numbered element putting its number first in either case, $Q_{1+}$ and $Q_{1\blacktriangle}$; the element they build is $\breve Q$. The sign is read with the glyph: $\tilde Q_\pm$ names an element of the sector $\mathbb{B}_{\Psi}$ or $\mathbb{B}_{\Phi}$, while $Q_\pm$ names the idempotent coordinates of $\breve Q$.

The forms a subscript takes are these.

| The subscript is | Example |
|---|---|
| a digit | $\tilde Q_1$, $\tilde Q_2$ |
| a letter | $Q_k$, $Q_\mu$ |
| two indices | $Q_{ab}$ |
| a sign | $\tilde\Pi_\pm$ |
| an upright word | $\tilde Q_{\mathrm{f}t}$, $\tilde U_{\mathrm r}$ |
| a grouped expression | $Q_{n+1}$ |

**The letter $\iota$ is not used.** No physics article uses $\iota$, in any spelling. The comparison of the biquaternion algebra with the even Clifford algebra is written by its values, $e_t\mapsto I_4$ and $\vec e_x\mapsto\gamma_2\gamma_3$, or by the words "the Clifford image", and never by a symbol. An interior product is written as the pairing it is, $\omega(X_f,\,\cdot\,)=df$, and an inner automorphism in words. The letter is not reserved for a third object: it carries no meaning in the series, and a display that introduces it is a defect.

## Summary

A unit element is not a physical unit. The series uses the SI, the coefficients of one element share one unit, and the default temporal slot is $i c r'_t$ in metres, with $ir'_t$ and $g_{tt}=-c^2$ stated where an article uses it. A dimensionless number carries no unit and no conversion, and $\mu$ is read by context among the permeability, the inverse Compton length and the direction label.

Two labels run beside the element marks. $\mathrm{fop}$ marks the Fock operator, the one glyph that is not an element; $\mathrm{opp}$ marks the opposite algebra, and it is written on an algebra name or on an element that names a tensor factor. The Fock label is low and the dagger raised, $a_{\mathrm{fop}}^{\dagger}$. An upright label of a construction or a variant stands in the subscript as well, three lowercase letters by default — $\mathrm{orb}$, $\mathrm{inc}$, $\mathrm{out}$, $\mathrm{ret}$, $\mathrm{reg}$, $\mathrm{lor}$, $\mathrm{wkb}$, $\mathrm{epr}$ in this corpus — and the index of the labels is *Index, Notation and Corpus Conventions*, §*The Three-Letter Labels*. Every label is lowercase, and the caret carries nothing else here: $\operatorname{sym}(V)$ the symmetric algebra and $\tilde Q_1\tilde Q_2$ the general plain algebra are written as $\mathrm{opp}$ is.

A subscript is written with the underscore and one token. It is a component or a label, never a derivative. A coefficient carries a letter index and a counted element a number; a subscript either counts or names, and a role label is carried once into the coefficients. A sign is a subscript where the statement needs one. The allowed forms are the digit, the letter, two indices, a sign, an upright word and a grouped expression. The family letters $L$ and $R$ of a regular matrix are labels of that kind, and they are written italic as the letters of the operators rather than upright as a word; they follow the size in the same subscript, $\mathsf M_{4L}$ and $\mathsf M_{4R}$. A label is written first in the subscript and an index already there follows it after a comma, $L_{\mathrm{axf},e_\mu}$ and $T_{\mathrm{em},\mu\nu}$; the frame closes the same field, $\mathsf M_{4L,\mathrm{pau}}$. The letter $\iota$ is not used at all. An **angular-momentum total** takes the role subscript, $s_{\mathrm{tot}}$, and its projection the axis, $s_{\mathrm{tot},z}$; the operator carries the vector index, $\tilde S_{\mathrm{tot},k}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| SI | Metre, second, kilogram, kelvin, coulomb, with the derived units built on them |
| $i c r'_t$, $\vec q$ | The default material coordinate, time measured in metres |
| $ir'_t$, $g_{tt}=-c^2$ | The second writing of the temporal slot, time in seconds; stated where used |
| $\mu$ | Permeability, inverse Compton length $\mu=mc/\hbar$, or direction label; read by context |
| $\mathrm{fop}$ | The Fock-operator mark, the one glyph that is not an element |
| $\mathrm{opp}$ | The opposite algebra, written on an algebra name or on an element that names a tensor factor |
| $\mathrm{orb}$, $\mathrm{inc}$, $\mathrm{out}$, $\mathrm{lor}$, $\mathrm{rgs}$, $\mathrm{tpl}$, $\mathrm{prm}$, $\mathrm{dfc}$, $\mathrm{obf}$, $\mathrm{adg}$ | The three-letter labels of a construction or a variant, the last six separating two spellings; the index is *Index, Notation and Corpus Conventions*, §*The Three-Letter Labels* |
| $\tilde Q_1\tilde Q_2$, $\tilde Q_1^{\natural}\tilde Q_2$, $\tilde Q_1\tilde Q_2^{*}$, $\tilde Q_1^{\natural}\tilde Q_2^{*}$ | The four general products, written by their two slots and their conjugations, never by a code; with $\bullet$ their symmetric parts and with $\wedge$ their antisymmetric parts, the class carried by the subscript |
| $Q_{\mathrm{f}t}$, $Q_{n+1}$, $\tilde\Pi_\pm$, $L_{\mathrm{axf},e_\mu}$ | The subscript forms: a label carried with its direction in one field, a grouped expression, a sign, a label first and an index after a comma |
| $s_{\mathrm{tot}}$, $s_{\mathrm{tot},z}$, $\tilde S_{\mathrm{tot},k}$ | Total angular-momentum label, its projection, and the operator, which carries the vector index $k$ |

## Further Reading

- [Conventions in the Biquaternion Universe](algebra-and-element-conventions.html), for the base these conventions qualify.
- [Operator and Calculus Conventions](operator-and-calculus-conventions.html), for the operators that take the Fock mark and the derivative that is never a subscript.
- [Conventions in Mathematics](../articles_maths/algebra-and-element-conventions.html), for the same subscript rules on the mathematical corpus.
