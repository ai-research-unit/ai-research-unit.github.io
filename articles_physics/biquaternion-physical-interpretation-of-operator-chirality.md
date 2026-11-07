# __Biquaternion Physical Interpretation of Operator Chirality__

## Introduction

**The question.** What does the operator chirality of the biquaternion algebra predict, and what does it leave to physics?

**The answer in one line.** Chirality is a side. A pure left multiplier carries the left slot, a pure right multiplier the right slot, a scalar both slots at once, and the remaining operators no single side. Physics uses one cell, $-iR_u$ for a traceless $u$ with $u^2=-e_t$, and that cell is a pure right multiplier: it is an example of the right slot, never the definition of it. The Dirac operator is the pure left multiplier $L(\tilde\nabla)$, the two sit on opposite sides and therefore commute, so the derivative carries the cell's value unchanged. What carries a field from one value to the other is not the mass of the pair but a right multiplication by an element that anticommutes with $u$.

**What this article does.** It restates the mathematics in the form a physicist reads, and it states what the algebra does not supply. The proofs are in *Operator Chirality on the Biquaternion Algebra*, one click away, and nothing here is proved twice.

**What it does not do.** It does not derive a gauge group, a matter content or a mass value. It does not claim that the two sides are two different kinds of field: they are not, and §*What the Algebra Does Not Supply* states that limit in full.

**The order of the article.** Section §*Operator Chirality in One Page* gives the definition and the dimensions. Section §*The Cell That Realises the Split* states the four properties of the cell and the two sides. Section §*The Dirac Equation Reads the Sides* shows what the sides do to the equation and where the mass sits. Section §*The Eight Objects the Physics Does Not Need* gives, for each object that usually carries the name, the physical reason it is not needed. Section §*What the Algebra Does Not Supply* records the one thing the cell does not buy.

**Conventions.** The algebra, the cells and the two slots are those of *Algebra and Element Conventions* and *Operator Family Conventions*, and none is redefined here. Nothing here is named after a direction of space, and no array is printed: the cell is named by the element it is built from, that element is a single letter, and every statement below is a statement about operators. The restriction is not a stylistic preference. A direction enters the choice of one cell and no part of the label, and an article that names a direction in its definitions teaches a reader that the label depends on it.

## The Results It Uses

| Mathematical Content | Source |
| --- | --- |
| The two slots, the two one-sided families and their dimensions | [Operator Chirality on the Biquaternion Algebra](../articles_maths/operator-chirality-on-the-biquaternion-algebra.html) |
| The label of an operator as a side, and one cell that realises the split, a pure right multiplier and hence an example of the right slot | same |
| The list of eleven objects the notion does not need, the cell among them | same |
| The swap $\sigma(L_aR_b)=L_bR_a$ and the conjugation $\mathsf C\,L(a^{\natural})\,\mathsf C=R(a)$ | same |
| The cells as a basis, the coefficient matrix and the length | [$M_4(\mathbb{C})$ Axis-Free Representation : Operators](../articles_maths/m4c-axis-free-representation-operators.html) |
| The chiral pair of the Dirac equation and its two-sided variant | [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html) |
| The mass as a breaking: a right multiplication by an element that anticommutes with $u$, not a left multiplication | [What the Biquaternion Algebra Cannot Do](what-the-biquaternion-algebra-cannot-do-a-catalogue-of-algebraic-obstructions.html) |
| The two statements kept apart: the mass shell belongs to the gradient equation, the chirality to the right multiplication | [The Roots of a General Element, Mass Frames and the Mass Shell](the-roots-of-a-general-element-mass-frames-and-the-mass-shell.html) |
| The two forms of the equation on the algebra, and the statement that the pair needs no carrier beyond the algebra | [The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism](the-minimal-coupling-of-the-biquaternion-dirac-field-to-electromagnetism.html) |

## Operator Chirality in One Page

**The definition.** An operator of $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ is a sum of cells, and a cell has two slots: the left one, where $a$ multiplies, and the right one, where $b$ multiplies. Operator chirality is the slot: the left slot for a pure left multiplier, the right slot for a pure right multiplier, both slots at once for the scalars, and no single side otherwise. The definition names the two regular maps and nothing else. No element of the algebra, no root, no idempotent, no projection, no module and no axis is needed to state it, and none is used to state it here.

**The dimensions.** The two families are four-dimensional each, they overlap in the scalars, and their sum is seven-dimensional inside the sixteen-dimensional endomorphism algebra:

| Space | Dimension | Physical reading |
| --- | --- | --- |
| $L(\mathbb{B})$ | $4$ | the operators that multiply on the left |
| $R(\mathbb{B})$ | $4$ | the operators that multiply on the right |
| $L\cap R$ | $1$ | the scalars, which multiply on both sides and carry the label both slots |
| $L+R$ | $7$ | the one-sided operators |
| $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ | $16$ | all operators; the other nine directions have no single side |

**What this buys physically.** The object that the older routes obtained after adjoining a root and complexifying the algebra is here one operator, reached without adjoining anything. Any traceless $u$ with $u^2=-e_t$ produces it: the cell $-iR_u$ squares to the identity, has trace zero, and has spectrum $\pm1$ with two eigenvalues of each sign. Its side is not chosen but read, because the cell is a right multiplier by construction. Nothing is adjoined, no root is chosen, no module is declared, and no direction of space is named.

**What it costs.** Nothing is said about states. The slot is a property of an operator, and §*The Dirac Equation Reads the Sides* shows how that property reaches the equation.

## The Cell That Realises the Split

**The object.** Take a single element $u$ of the algebra, traceless and with $u^2=-e_t$. The cell is
$$
-iR_u:\quad \tilde X\mapsto-i\tilde Xu .
$$
That is the whole definition: one element, one multiplication on the right, one phase. It is the operator that the Dirac literature names after the product of its four generators; here it needs no generator, no product and no array, and it is written with the element it is built from.

**Its properties.** Four, each verified by multiplying cells:

| Property | Value | Physical reading |
| --- | --- | --- |
| square | $(-iR_u)^2=\mathrm I$ | an involution, so a sign |
| trace | $\operatorname{tr}(-iR_u)=0$ | the two halves are of equal size |
| spectrum | $+1$ and $-1$, two dimensions each | two chiral components, two states each |
| with a left multiplier | $[\,L(a),-iR_u\,]=0$ for every $a$ | it sits on the opposite side to the gradient, so the gradient keeps the value |

The square follows from $R_u^2=R_{u^2}=-\mathrm I$, so that $(-iR_u)^2=\mathrm I$. The trace vanishes because $u$ is traceless: the trace of $R_u$ is four times the scalar part of $u$, and the hypothesis is exactly that this part is zero. The spectrum is the spectrum of $u$ read four times, and $u^2=-e_t$ with $\operatorname{Sc}u=0$ gives $\pm i$ twice each.

**The cell has a side of its own.** $-iR_u$ is a pure right multiplier, so under the label of the previous section it carries the right slot. That is not a circularity. The label is a membership in one of the two images, it is fixed with no element chosen, and the cell is one operator that happens to lie in the right image. The cell realises the split of the algebra, and it also has a side; the two statements are different, and only the first is what the physics uses it for (*Operator Chirality on the Biquaternion Algebra*, §*What Operator Chirality Is Not*).

The twin on the other side shows that the slot, and not the element, is what tells the two apart. For the same $u$ the left multiplier $iL_u$ also squares to the identity, also has trace zero, and has the same spectrum, and it also splits the algebra in two. It differs from $-iR_u$ in one respect only, and that respect is the slot. So the physics does not single out an element; it singles out a side, and $u$ merely picks which member of that side is used.

**The side, which is the point of the article.** $-iR_u$ multiplies on the **right**. The gradient multiplies on the **left**. This is not a detail of notation: it is the reason the two operators commute,
$$
L(a)\,R(b)=R(b)\,L(a)\quad\text{for all }a,b,
$$
so that
$$
[\,L(\tilde\nabla),-iR_u\,]=0 .
$$
A left multiplier and a right multiplier never fail to commute. The cell and the Dirac operator are the two sides of the same algebra, and their commutation is a consequence of the sides, not a computation about arrays.

**What the cell does.** It has two eigenvalues, and a field carries one of the two values. The value belongs to the field and the side belongs to the operator; nothing else is in play.

## The Dirac Equation Reads the Sides

**The equation.** The biquaternion Dirac equation is the chiral pair
$$
\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=k_m\tilde{Ξ}_{\mathrm{sp},L},\qquad \tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=k_m\tilde{Ξ}_{\mathrm{sp},R},
$$
in which both operators act by left multiplication: the first by $\tilde\nabla$, the second by its natural conjugate $\tilde\nabla^{\natural}$. The conjugation is what relates the two, and its identity is the one of the mathematics article,
$$
\mathsf C\,L(a^{\natural})\,\mathsf C=R(a),
$$
so the conjugate member of the pair is the same operator read on the other side. Nothing else is used: no carrier, no splitting of a carrier, no projector, no idempotent, no ideal. Here $k_m=mc/\hbar$ is the mass wave number, the inverse of the mass length.

**The two letters of the pair are not the two values of the cell.** They are written alike, and they are different objects, so the difference comes before anything about the mass. The pair is two equations for two elements, and the mass is the number that relates them: each element is the gradient of the other divided by $k_m$, which at $k_m\neq0$ is a change of variable. The two values of the cell are a second partition of the same algebra, cut by an operator the pair never uses. A reader who takes the letters of the pair for the values of the cell finds that the pair has only the zero solution, and the reason is one line: both members of every line are left multiplications, a left multiplication keeps the value, so each line would equate a field of one value with a field of the other.

**What the derivative does to the value.** A left multiplier and a right multiplier never fail to commute,
$$
L(a)\,R(b)=R(b)\,L(a)\quad\text{for all }a,b,
$$
so
$$
[\,L(\tilde\nabla),-iR_u\,]=0 .
$$
The derivative therefore carries each value into itself: if $\tilde\Xi$ has a value then so does $\tilde\nabla\tilde\Xi$, and a field of definite value stays of definite value under differentiation. The cell and the Dirac operator are the two sides of the same algebra, and their commutation is a consequence of the sides and not a computation about arrays.

**The massless case, and the split.** At $m=0$ the pair decouples into $\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=0$ and $\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=0$. For a null gradient the solution space of either member is two-dimensional over $\mathbb{C}$, and $-iR_u$ acts on it with the two eigenvalues $+1$ and $-1$, one state each. So a massless biquaternion Dirac field carries **one state of each value**, which is the standard statement that a massless Dirac fermion has both helicities. The mechanism is the commutation above: the solution space is stable under the cell, so a solution of definite value may be chosen.

**The mass of the pair is a number, and a number has both slots.** In the pair the mass enters as $k_m$, and $k_m$ is central: it is a left multiplier and a right multiplier at once, so it holds both slots and has no single side. That is where its physical reading comes from, and it is also where the reading stops. Being in both slots, it acts on the two values alike, and a term that acts on them alike does not move a field from one to the other. In the projectors of the cell the statement is one equation, with $P_\pm=\tfrac12(\mathrm I\mp iR_u)$,
$$
P_+\,(k_m\mathrm I)\,P_-=0 ,
$$
which holds for every $k_m$: a central scalar is diagonal in the cell's own decomposition. The mass is the constant of proportionality that lets the pair say that each component is the derivative of the other, and a constant of proportionality is not a carrier.

| Term | Multiplier | Slot | What it does to the value |
| --- | --- | --- | --- |
| $\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}$ | left by $\tilde\nabla$ | left | keeps it |
| $\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L}$ | left by the conjugate | left | keeps it |
| $k_m\tilde{Ξ}_{\mathrm{sp}}$ | central scalar | both slots, hence no single side | keeps it |
| $\tilde{Ξ}_{\mathrm{sp}}v$, $uv+vu=0$ | right by $v$ | right | exchanges it |

**What carries a field from one value to the other.** The exchange is a right-slot operation, and its condition is anticommutation with $u$:
$$
u v+v u=0\quad\Longrightarrow\quad R_v\,(-iR_u)=-(-iR_u)\,R_v ,
$$
since $R_vR_u=R_{uv}$ and $R_uR_v=R_{vu}$. Then $R_v$ carries one half into the other, and when $v$ is a unit perpendicular to $u$ it does so isometrically: $\lVert R_vP_+\rVert_{\mathrm F}=\lVert P_+\rVert_{\mathrm F}=\sqrt2$. For the cell $-iR_{\vec e_z}$ the elements that work are the complex combinations $a\vec e_x+b\vec e_y$, and not the two units alone.

**How the corpus writes the mass as an operator.** A term that does the carrying exists in the corpus, and it is not the $k_m$ of the pair. The catalogue of what the algebra cannot host states it as the reading of an obstruction: *since a left multiplication acts by the same element on the two parts and cannot couple them, a mass term is not a left multiplication but a breaking, which the conventions realise as the right multiplication by $\tfrac12(i\vec e_x-\vec e_y)$* (*What the Biquaternion Algebra Cannot Do*, §*Physical Readings*). The element $\tfrac12(i\vec e_x-\vec e_y)$ anticommutes with $\vec e_z$ and is nilpotent, $\bigl(\tfrac12(i\vec e_x-\vec e_y)\bigr)^2=0$, so the map it gives is one-way: it carries the $-1$ part onto the $+1$ part, and applying it a second time gives zero. The word *breaking* is therefore a computation: the carrier is nilpotent, so the term is one-way, and it sits in the right slot.

**Two readings of one word, kept apart.** The pair and the operator statement are both in the corpus, and they are not the same statement: the first uses the mass as a number and leaves the value alone, the second uses it as a right multiplier and moves the value. Which one a computation needs depends on the question. A mass shell, a dispersion relation, a plane wave: the pair, because the value plays no part in them. A chiral current, an axial rotation, a condensate, an anomaly coefficient: the right multiplier, because there the value is the whole subject. The corpus keeps the two apart in the same words in *The Roots of a General Element, Mass Frames and the Mass Shell*: the mass shell is a statement of the gradient equation, and the chirality, the axial current and the condensate are statements of the field's right multiplication.

**Commutation, and the anticommutation a reader will expect.** On $\mathbb{B}$ the cell multiplies on the right and the derivative on the left, so the two commute, and the commutation says that the cell preserves each of its own eigenspaces. In a matrix display the cell is diagonal and the derivative is off-diagonal, and the anticommutation of the two is that display's way of saying the derivative carries one eigenspace into the other. The anticommutation is therefore a statement about the derivative, and it is true of the display's derivative and not of the algebra's left multiplier. The display's four frame cells are $iL_{e_a}R_{e_{\nu(a)}}$, and each of the four anticommutes with the cell: that is the standard chiral structure, and it is a property of those four operators rather than of the cell. The conclusion for a solution is the same in either account and needs no display: if $\tilde{Ξ}_{\mathrm{sp}}$ is massless then $-iR_u\tilde{Ξ}_{\mathrm{sp}}$ is massless too.

## The Eleven Objects the Physics Does Not Need

**The list.** The mathematics article separates operator chirality from eleven objects. The table repeats the separation and states, for each object, what a physicist would otherwise think it is doing.

| Object | What a physicist might expect it to do | Why the physics does not need it |
| --- | --- | --- |
| a root | supply the element from which the cell is built | the cell needs one element, not a root with an idempotent beside it |
| an idempotent | supply a state or a superselection sector | the cell is an involution, $(-iR_u)^2=\mathrm I$, not a projector |
| a Peirce decomposition | supply the two chiral halves | the halves are the eigenspaces of one operator, not four corners of two idempotents |
| a Peirce basis | supply the working basis | a basis is a display; the side is read without one |
| a spectrum | supply the sign, as the pair $+1,-1$ | a list of numbers belonging to one chosen operator |
| a spinor | supply the object that carries chirality | a spinor is an element of $\mathbb{B}$; the label is a property of an operator |
| the module $S$ | supply the space the states live in | $S$ is one minimal left ideal, and it needs a point of a projective line |
| an ideal | supply the state space | a subspace of $\mathbb{B}$, and no ideal is mentioned in the definition |
| a Clifford algebra | supply the sign as a product of generators | the sign is the side of a right multiplier, and a product of generators is one operator among many |
| a matrix unit of $M_4(\mathbb{C})$ | supply the cell, since the cell is a basis element of the display | the cell is a sum of four matrix units, and $4$ is the display's number and not the algebra's |
| the cell itself | be what chirality means | it is an example of the right slot, and an example cannot be the definition |

**No root.** A root $\tilde{Ζ}$ with $\tilde{Ζ}^2=e_t$ is an element chosen in the algebra, and it is needed when a Peirce decomposition is wanted. The cell needs one element with a stated square and a stated trace, so the choice stops where $u$ is named. A change of root changes the Peirce data and leaves the label of every operator untouched.

**No idempotent.** An idempotent satisfies $\tilde\Pi^2=\tilde\Pi$, and it is the algebraic form of a projection, hence of a state preparation. The cell satisfies $(-iR_u)^2=\mathrm I$ and is not a projection: it is a sign, and a sign is not a state. The projectors $\tfrac12(\mathrm I\pm iR_u)$ are built from it when a projection is wanted, and they are derived objects.

**No spectrum, and no pair of eigenvalues.** The sentence a physicist is likeliest to write is that chirality is the two eigenvalues $+1$ and $-1$. It is true of one chosen cell and false of the notion, and the difference is visible in counting: the label has four cases, a spectrum is a list of numbers, and two of the four cases have no spectrum at all. The eigenvalues follow from the cell the moment the cell is fixed, and they do not tell a reader which slot it sits in. What they do supply is the balance, two of each sign, and that balance is what lets the cell be used as a projector once it has been chosen.

**No Peirce decomposition and no Peirce basis.** A Peirce decomposition needs two idempotents and returns four lines. The chiral splitting is one operator and returns two halves. Four lines and two halves are not the same partition, and the difference is measurable: the Peirce lines are one-dimensional corners of $\mathbb{B}$, and the chiral halves are two-dimensional left modules.

**No spinor, and no module $S$.** A spinor is an element of a minimal left ideal, and the corpus writes one such ideal $S$ and its conjugate $S^{\mathrm{c}}$. Both are subspaces of $\mathbb{B}$: $S$ is four real dimensions of the algebra, and a state is a vector in it. The label is not in that space at all. A spinor is an object the algebra multiplies; the label is a property of the thing that multiplies. That is why an article can define chirality and never mention a spinor, and why a sentence of the form *this spinor is left-handed* is a statement about the value of one cell on one vector and not about the notion.

**No ideal.** An ideal is a subspace $I$ of $\mathbb{B}$ closed under multiplication, and none is needed, because the two spaces are different: the label is a membership in the sixteen-dimensional space of operators, and an ideal is a subspace of the four-dimensional algebra those operators act on. The objection is not that ideals are hard to compute with; it is that no ideal can appear in the definition, and no statement about the label is proved by exhibiting one. The temptation is real, because a minimal left ideal is the natural home of a spinor and a spinor is where a physicist expects the handedness to live. The expectation is met by a different object: the value of the cell on the spinor.

**No ideal.** The minimal left ideals of $\mathbb{B}$ are indexed by the points of a projective line, and no point is distinguished. An operator that multiplied on one side and selected a point would be an ideal in disguise. The cell selects nothing: it multiplies, and the two eigenspaces follow from its square and its trace alone.

**No Clifford algebra.** This deserves a paragraph, because the Clifford reading is the one a physicist is most likely to reach for. A Clifford algebra is generated by vectors with $\{e_i,e_j\}=2g_{ij}$, and in it the sign is the product of the generators by construction. In the biquaternion algebra the corresponding identity holds as a fact about five cells, and it is a fact, not an axiom. The relation fixes squares and anticommutators; what operator chirality uses is the side, and the relation says nothing about sides. A Clifford algebra also fixes a dimension and a signature, while the two images exist for every algebra in every dimension. The Clifford reading is a display of the algebra, and a correct display; it is not a foundation, and nothing in the physics is derived from it that the cells do not already give.

**No matrix unit, and no basis element of the display.** In a display the cell is a diagonal of signs, and the smallest thing a display has is a matrix unit $E_{ij}$; so the cell is often described as a basis element of $M_4(\mathbb{C})$, or as the unit of a basis in which it is diagonal. It is not one. Written in any display the cell is a sum of four matrix units, and it is a single operator rather than a combination of four. The number $4$ is the size of one display of an algebra of complex dimension four; the two images are defined by the multiplication of any algebra, in any dimension, with no display at all. A definition that names a matrix unit names one display, and it fails the moment the display changes, while the label of every operator stays where it was.

**Why no anticommutation can give the sign.** It is worth stating the reason, because it explains why the side is the right notion and not merely an available one. If the sign were characterised by anticommuting with the generators, it would have to anticommute with $L(e_t)$, which is the identity, and an operator anticommuting with the identity is zero. There is no such operator. The sign is not produced by an anticommutator; it is produced by the side.

## What the Algebra Does Not Supply

**The values coincide in kind.** The cell has two eigenspaces, and the algebra gives them the same size and the same action: every left multiplier commutes with the cell, so it acts on both, and it acts on them alike. A label that one operator assigns by sign therefore separates two things of one kind. That is a limit of the algebra and not of the bookkeeping.

**What the physics needs instead.** The Standard Model separates two things of different kinds: the left-handed Weyl field and its conjugate. The biquaternion algebra contains one such field, applied twice, so it cannot supply the second. The pair is the subject of *The Unpolarized Module of the Biquaternion Algebra*.

**So what has been gained.** The cell supplies, without adjoining anything, the sign a Lagrangian needs in order to write a chiral current or an axial coefficient: an involution of the algebra, of trace zero, with two equal eigenspaces, commuting with the Dirac operator and available in every display. What it does not supply is a second, different kind of field, and no operator of $\mathbb{B}$ can supply one.

## Limits

- **No derivation of the gauge group.** The algebra supplies the sign; it does not supply the Standard Model gauge group, its representations or its breaking pattern.
- **No second kind of field.** The two values of the cell belong to fields of one kind; distinguishing the left-handed field from its conjugate is not something an operator of $\mathbb{B}$ does.
- **No matter content and no generations.** The number of copies is an input.
- **No mass value and no spectrum.** The algebra fixes the slot of the mass term, which is the right slot, and the element that can carry it, which is any $v$ with $uv+vu=0$; the number $m$ is dynamical, and the pair says nothing about it beyond its appearance as $k_m$.
- **No dynamics.** The algebra names the term that carries a field from one value to the other; it does not say when the term acts, nor with what coefficient beyond the $k_m$ of the pair.
- **The element is a choice.** The cell is built from one element. Another traceless $u$ with $u^2=-e_t$ gives another cell, with the same four properties and the same slot, while every label of every operator stays where it was. The choice is invisible to the physics, which uses the side.

## Summary

Operator chirality is the side on which an operator multiplies: the left slot, the right slot, both slots at once for the scalars, and no single side otherwise. One cell realises the split, $-iR_u$ for a traceless $u$ with $u^2=-e_t$. It is a pure right multiplier, so it is an example of the right slot and not the definition of chirality. The Dirac operator is the pure left multiplier $L(\tilde\nabla)$, and the two commute because a left multiplier never fails to commute with a right one. That commutation is why a massless field carries states of both chiralities. The mass appears twice and the two appearances are not one statement. As $k_m$ in the pair it is central, it holds both slots, and it keeps the value. As a right multiplication by an element that anticommutes with $u$ it is a one-sided term that carries the field from one value to the other. Only the second of these is a coupling of the two values, and only the second is in the right slot.

The construction needs none of the eleven objects that usually carry the name: no root, no idempotent, no Peirce decomposition, no Peirce basis, no spectrum, no spinor, no module $S$, no ideal, no Clifford algebra, no matrix unit of a display, and no separate chirality element standing in for the definition. Each of them is a choice, and each of them is invisible in the numbers a display prints, which is why the numbers were mistaken for the notion. The cell prints the same in every reading, and none of those structures is needed to reach it.

The limit is stated once and it is not small: the two values of the cell separate fields of one kind, so the algebra is vector-like, and the distinction the Standard Model draws between the left-handed field and its conjugate is not an operator distinction of $\mathbb{B}$.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra |
| $L_aR_b$ | the cell, $L_aR_b\tilde X=a\tilde Xb$, with a left and a right slot |
| left slot, right slot, both slots, no single side | operator chirality, the membership in one of the two images |
| $\tilde\nabla$ | the biquaternion gradient, acting by left multiplication |
| $\tilde\nabla^{\natural}$ | its natural conjugate, related to the other side by $\mathsf C L(a^{\natural})\mathsf C=R(a)$ |
| $u$ | a traceless element with $u^2=-e_t$ |
| $-iR_u$ | the cell that realises the split, a pure right multiplier: an example of the right slot and not the definition |
| $\tfrac12(\mathrm I\pm iR_u)$ | the two chiral projectors, derived from the sign |
| $P_\pm=\tfrac12(\mathrm I\mp iR_u)$ | the projectors onto the two values |
| $m$, $k_m=mc/\hbar$ | the mass and its wave number; in the pair the coefficient is central and keeps the value |
| $v$, $uv+vu=0$ | the carrier of the mass as an operator: a right multiplier that exchanges the two values |

## Further Reading

- [Operator Chirality on the Biquaternion Algebra](../articles_maths/operator-chirality-on-the-biquaternion-algebra.html), for the definition, the dimensions, the swap, the conjugation and the list of unrelated objects.
- [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html), for the chiral pair, the one-sided and the two-sided equation, and the plane-wave solutions.
- [The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism](the-minimal-coupling-of-the-biquaternion-dirac-field-to-electromagnetism.html), for the two forms of the equation and the gauge covariance of the pair on the algebra.
- [The Unpolarized Module of the Biquaternion Algebra](../articles_maths/the-unpolarized-module-of-the-biquaternion-algebra.html), for the distinction the limit of this article points to: the left-handed field and its conjugate are not two copies of one thing.
- [Chiral Fermions in the Biquaternion Framework](chiral-fermions-in-the-biquaternion-framework.html), for the chiral projectors and the mass selection rule in the physics corpus.
- [The Two Chiralities of $M_4(\mathbb{C})$](../articles_maths/the-two-chiralities-of-m4c.html), for the comparison with the matrix case.
