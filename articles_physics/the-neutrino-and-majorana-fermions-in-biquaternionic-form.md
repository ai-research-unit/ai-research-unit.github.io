# __The Neutrino and Majorana Fermions in Biquaternionic Form__

## Introduction

**The question.** Three words name three fermions, and the difference between them is a difference between three conditions on one field. A **Dirac** fermion has two independent chiral parts and a mass that pairs one part with the other. A **Weyl** fermion keeps one part and carries no mass while its chirality is protected. A **Majorana** fermion is its own antiparticle: one field instead of two, half the components, and a mass that pairs the field with its own conjugate. The neutrino is the particle on which the three meet, because it is the only fermion whose mass the gauge quantum numbers do not settle.

**The answer in one line.** In the biquaternion framework the three conditions are conditions on one element $\tilde{Ξ}_{\mathrm{sp}}$ of $\mathbb{B}$, and no second carrier is needed. An arbitrary element is Dirac. An element of one chirality value is Weyl. An element fixed by one antilinear involution is Majorana. The involution is the coefficient conjugation multiplied by the central $i$; its fixed space is four-real-dimensional, it exchanges the two values, and it commutes with the kinetic operator of the frame. The mass of the self-conjugate field is permitted, and its vector current vanishes.

**What the article uses, and what it does not.** The field is an element. The article uses the product, four multipliers of one declared frame, the chirality operator, and three conjugations. It uses no array, no ideal, no idempotent, no projector, no Peirce basis, no transpose and no Kronecker product. The gammas appear once, in the closing block, as a display of the same objects in the older notation.

**The ledger.** Four kinds of statement are in play, and the article keeps them apart.

- **Established, and recomputed below.** A Dirac field is an element with independent values and eight real components. A Weyl field is an element of one value, with four. A Majorana field is the fixed space of an antilinear involution of square one, also with four. The Majorana condition is consistent with a mass: the mass shell stays $p^{2}=m^{2}c^{2}$, and half the degrees of freedom are removed, not the mass. The vector current of the self-conjugate field vanishes, so the field carries no fermion number.
- **Established elsewhere in the corpus, and sharpened here.** The three notions are read directly on the element, because the field *is* an element and the two values are the two eigenspaces of one operator of the frame. Nothing in the construction is a column, a block or an ideal, and none of the older objects enters.
- **Arithmetical, and recorded because it looks paradoxical.** A commuting c-number element that satisfies the same algebraic condition gives the *opposite* bilinear pattern: its scalar pairing vanishes and its vector current does not. The pattern is a property of the anticommuting field, and the sign by which the two cases differ is the anticommutativity alone.
- **Not established, and left visible.** The left-handedness of the neutrino is empirical. The framework transcribes the chiral gauge structure, it does not derive the assignment. The value of the mass and the size of the mixing are outside the algebra.

**The programme's own limit.** The framework supplies the arena and imports the dynamics: the field, the values, the conjugations and the pairings are the algebra's, and the Dirac operator of the frame is written here because the algebra can write it, not because the algebra forces it. The neutrino's masses are measured, and the algebra supplies the structure in which they are expressed.

The article is organized as follows. The next section fixes the field, the two values and the three conditions. A section constructs the charge conjugation as an antilinear involution on the element and checks that it commutes with the kinetic operator. A section writes the Majorana condition, computes what it does to the mass and to the bilinears, and compares it with the Weyl case. Which of the algebra's conjugations is the charge conjugation is the subject of the following section, and the sector split comes after it. The neutrino section states what the framework transcribes and what it does not. A section then separates what the algebra supplies from what it merely displays, and a short section records an external geometric use of the pair. Open questions close the argument, and a last block records the older display of the frame once, for comparison with the literature.

## The Field, Its Two Values, and Three Conditions

**The field is an element.** In this framework the state of a fermion is an element of $\mathbb{B}$, written $\tilde{Ξ}_{\mathrm{sp}}$, and a general element is written $Q$. An element has four complex coefficients and eight real components. Every statement below is a statement about elements, their products, and the multipliers of one declared frame.

**The chirality is a value of one operator.** Chirality is the side on which an operator multiplies; the basis operator that supplies a sign is

$$
\xi=-iR_{\mathrm{axf},\vec e_z},\qquad \xi Q=-i\,Q\,\vec e_z ,\qquad \xi^{2}=1 ,
$$

a pure right multiplier, so it is an example of the right slot and never its definition. It carries part of the coefficient space to minus itself and part to plus itself, and the basis operator returns $-1$ on one and $+1$ on the other: $\xi\tilde{Ξ}_{\mathrm{sp},L}=-\tilde{Ξ}_{\mathrm{sp},L}$ and $\xi\tilde{Ξ}_{\mathrm{sp},R}=+\tilde{Ξ}_{\mathrm{sp},R}$. Every element is one part of each value, $\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp},L}+\tilde{Ξ}_{\mathrm{sp},R}$, each part is of two complex dimensions, and only the zero element is both. The letters are the Dirac ones, $L$ for the minus value and $R$ for the plus one (*Matrix Representations Conventions*, §*The Subscript on an Element*).

**The rule for products.** A product takes the value of its right factor, $(QR)\vec e_z=Q(R\vec e_z)$, and a left multiplication keeps the value. Both follow at once from the definition, and they are the rule the section on the mass runs on.

**An element is not a column, and a value is not an ideal.** The two values are two eigenspaces of one operator, and the operator is defined without a basis, a root, an idempotent or a Peirce decomposition. A reader who writes the element as a column of four numbers is displaying it in the Peirce basis, which is a choice of frame that the algebra does not make; the display is legitimate, and the article does not use it. The same caution applies to the word *spinor*: the field here is the element, and the columns of the older literature are displays of its carrier in a basis chosen from a root. Nothing below depends on such a choice.

**Three conditions, one carrier.** The three notions are now three conditions on $\tilde{Ξ}_{\mathrm{sp}}$, and the table states them before anything is computed.

| Notion | Condition on the element | Real components | Chiral parts |
|---|---|---|---|
| Dirac | none: an arbitrary element | $8$ | two, independent |
| Weyl | one value absent, $\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp},L}$ or $\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp},R}$ | $4$ | one |
| Majorana | fixed by a conjugate-linear involution, $\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp}}^c$ | $4$ | two, mutually conjugate |

**The counts are read off the algebra.** An element is four complex coefficients, hence eight real ones. A single value is two complex coefficients, hence four. An antilinear involution of the eight-dimensional real space has a fixed space of dimension four, because the multiplication by $i$ exchanges its $+1$ and $-1$ eigenspaces and the two have equal dimension. So the Majorana condition halves the field, and it does so by an antilinear structure and not by a linear constraint bolted onto a Dirac field. That is the content of the boxed count of the companion *Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form*, restated on the element.

**The mass is what remains to be decided.** A condition on values is a linear condition and a condition of self-conjugacy is an antilinear one, and the two are independent. What decides whether a mass is possible is not the count but the equation: a mass term is the non-derivative part of the equation, and whether it survives the condition is a computation. The next two sections perform it.

## Charge Conjugation: the Conjugation and Its Frame

**What a charge conjugation has to be.** Three requirements fix it, and each is a requirement on the equation rather than on the name.

- It is **conjugate-linear and involutive**, $\mathcal{C}(\alpha\tilde{Ξ}_{\mathrm{sp}})=\bar\alpha\,\mathcal{C}\tilde{Ξ}_{\mathrm{sp}}$ and $\mathcal{C}^{2}=1$. A linear map would be a symmetry of the field and not a map to the conjugate field, and a map of square $-1$ has no real fixed points at all.
- It **exchanges the two values**. The conjugate of a left-handed field is a right-handed field; that is what makes the antiparticle of a chiral fermion carry the opposite chirality.
- It **commutes with the kinetic operator**. If it did not, the condition $\tilde{Ξ}_{\mathrm{sp}}^c=\tilde{Ξ}_{\mathrm{sp}}$ would not be preserved by the evolution, and a field self-conjugate at one time would not stay self-conjugate.

**The frame, declared once.** The kinetic operator of this article is built from four multipliers of the axis-free frame: the right multiplication by $\vec e_x$, and, for each spatial direction, the left multiplication by the unit of that direction followed by the right multiplication by $\vec e_y$. Written as actions on an element,

$$
c_0:\tilde{Ξ}_{\mathrm{sp}}\longmapsto\tilde{Ξ}_{\mathrm{sp}}\,\vec e_x,\qquad
c_k:\tilde{Ξ}_{\mathrm{sp}}\longmapsto\vec e_\eta\,\tilde{Ξ}_{\mathrm{sp}}\,\vec e_y,\quad k=x,y,z .
$$

The four are real: the coefficient conjugation fixes each of them, because it fixes the units and negates only $i$, and none of the four carries an $i$. Two squares and six anticommutators are all that is used below,

$$
c_0^{2}=-1,\qquad c_k^{2}=+1,\qquad \{c_\mu,c_\nu\}=0\quad(\mu\neq\nu),
$$

and they are read at once: $c_0^{2}$ is $\vec e_x^{2}=-1$, $c_k^{2}$ is $\vec e_\eta^{2}\vec e_y^{2}=(-1)(-1)=+1$, and a pair anticommutes because one quaternion unit passes the other and $\vec e_y$ passes $\vec e_y$.

**The operator.** With $x_0=r'_t$ and $x_k$ the three spatial coordinates, and with $Q_t=ix_0$, $Q_\eta=x_k$ the material reading of the four coordinates,

$$
D=\sum_\mu \varepsilon_\mu\, c_\mu\,\frac{\partial}{\partial x_\mu},\qquad
\varepsilon=(1,-1,-1,-1),\qquad
D^{2}=\Box=\sum_\mu\frac{\partial^{2}}{\partial R_\mu^{2}}=-\frac{\partial^{2}}{\partial {r'_{t}}^{2}}+\Delta .
$$

The sign vector is the one that makes the square the d'Alembertian: the time direction enters with $c_0^{2}=-1$ and the three space directions with $c_k^{2}=+1$. The minus on the time term of $\Box$ is the square of the $i$ in $Q_t=ix_0$: the derivative is taken with respect to a coefficient that is imaginary, and $i^{2}=-1$ is the whole of the sign. The operator carries no $i$; the $i$ of a plane wave comes from the wave and not from the frame.

**The conjugation.** The charge conjugation of this article is

$$
\boxed{\;\tilde{Ξ}_{\mathrm{sp}}^c=\mathcal{C}\tilde{Ξ}_{\mathrm{sp}}=i\,\bar{\tilde{Ξ}}_{\mathrm{sp}}\;},
$$

the coefficient conjugate of the element, multiplied by the central imaginary. Four checks fix it, and each is one line.

$$
\mathcal{C}^{2}\tilde{Ξ}_{\mathrm{sp}}=i\,\overline{i\bar{\tilde{Ξ}}_{\mathrm{sp}}}=i\,(-i)\,\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp}} ,
$$

so it is an involution. It exchanges the two values, because

$$
\xi(\mathcal{C}\tilde{Ξ}_{\mathrm{sp}})=-i\,(i\bar{\tilde{Ξ}}_{\mathrm{sp}})\vec e_z=\bar{\tilde{Ξ}}_{\mathrm{sp}}\vec e_z,
\qquad
\mathcal{C}(\xi\tilde{Ξ}_{\mathrm{sp}})=i\,\overline{(-i\tilde{Ξ}_{\mathrm{sp}}\vec e_z)}=i\,(i)\,\bar{\tilde{Ξ}}_{\mathrm{sp}}\vec e_z=-\bar{\tilde{Ξ}}_{\mathrm{sp}}\vec e_z ,
$$

and the two differ by the sign that exchanges the values. It fixes $i\bar{\tilde{Ξ}}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp}}$, that is $\tilde{Ξ}_{\mathrm{sp}}=(1+i)A$ with $A$ fixed by the bar, a real four-dimensional space. And it commutes with $D$:

$$
\mathcal{C}(D\tilde{Ξ}_{\mathrm{sp}})=i\,\overline{D\tilde{Ξ}_{\mathrm{sp}}}=i\,D\bar{\tilde{Ξ}}_{\mathrm{sp}}=D\,(i\bar{\tilde{Ξ}}_{\mathrm{sp}})=D\,\mathcal{C}\tilde{Ξ}_{\mathrm{sp}} ,
$$

because every coefficient of $D$ is real and the central $i$ passes through the operator. The fourth line is the whole reason the construction works, and it is a statement about where the $i$ sits: the operator is built from multipliers the conjugation fixes, so the conjugation passes through it, and the phase $i$ is carried by the field and not by the frame.

**What the conjugation reverses.** The operator is real, and its symbol at fixed momentum is not. On a plane wave $e^{-i(p\cdot x)/\hbar}$ the operator acts as the multiplier

$$
D_p=-i\sum_\mu\varepsilon_\mu\,p_\mu\,c_\mu ,
$$

whose coefficients are purely imaginary, so $\overline{D_p}=-D_p$. The conjugation therefore **anticommutes with the symbol** while it commutes with the operator, and the two statements are one: the conjugate of a wave of momentum $p$ is a wave of momentum $-p$, and the symbol changes sign with the momentum. That is why the conjugate of a positive-frequency amplitude is a negative-frequency one, and it is why the space of solutions is closed under conjugation without any single mode being its own conjugate.

**The four, with two consequences, in one table.** Every entry was checked on random elements to machine precision, and the fourth and sixth decide the construction.

| Check | Statement | Result |
|---|---|---|
| involution | $\mathcal{C}^{2}=1$ | holds |
| antilinear | $\mathcal{C}(\alpha\tilde{Ξ}_{\mathrm{sp}})=\bar\alpha\,\mathcal{C}\tilde{Ξ}_{\mathrm{sp}}$ | holds by construction |
| value exchange | $\xi\mathcal{C}=-\mathcal{C}\xi$ | holds |
| fixed space | $\dim_{\mathbb{R}}\{\tilde{Ξ}_{\mathrm{sp}}:\tilde{Ξ}_{\mathrm{sp}}^c=\tilde{Ξ}_{\mathrm{sp}}\}=4$ | holds |
| kinetic operator | $\mathcal{C}D=D\mathcal{C}$ | holds, coefficients real |
| symbol | $\mathcal{C}D_p=-D_p\mathcal{C}$ | holds, symbol imaginary |

**Why the conjugation is the bar, and not another.** The algebra has three antilinear involutions and one linear one, and the choice among them is not free. The coefficient bar is the only conjugate-linear **automorphism** of $\mathbb{B}$: it is the only one that respects the order of a product, and therefore the only one that commutes with the action of the algebra on itself by left multiplication. A real structure on a field that carries that action must commute with it. This is the criterion, and the section *Which Conjugation of the Algebra Is the Charge Conjugation?* below applies it in full.

**The phase in front of the bar is free, and the article says so.** Every $\lambda\bar{\cdot}$ of unit modulus is antilinear, involutive and value-exchanging, and every one of them commutes with $D$. The checks are statements about multipliers, and a scalar multiplies none of them. What the phase moves is the fixed space, and nothing else: the phase of a real form is not an invariant, and the pattern of vanishing bilinears is decided by two parities that a scalar does not touch. So $\tilde{Ξ}_{\mathrm{sp}}^c=i\bar{\tilde{Ξ}}_{\mathrm{sp}}$ and $\tilde{Ξ}_{\mathrm{sp}}^c=\bar{\tilde{Ξ}}_{\mathrm{sp}}$ describe one structure, with one four-dimensional real form up to a phase. The value $i$ is a convention, chosen to agree with the conjugation of a column in the coefficient basis, where the conjugate of $\tilde{Ξ}_{\mathrm{sp}}$ is $i\bar{\tilde{Ξ}}_{\mathrm{sp}}$. What is not a convention is the bar: the antiautomorphisms reverse the order, and no phase rescues a reversed order.

## The Majorana Condition and the Mass

**The condition.** A Majorana field is an element equal to its own charge conjugate,

$$
\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp}}^c=i\bar{\tilde{Ξ}}_{\mathrm{sp}} .
$$

The condition is one antilinear equation on eight real parameters, and its solutions are four-real-dimensional. It ties the two values to each other: taking the $L$ part and the $R$ part of the equation gives

$$
\tilde{Ξ}_{\mathrm{sp},L}=i\,\overline{\tilde{Ξ}_{\mathrm{sp},R}},\qquad \tilde{Ξ}_{\mathrm{sp},R}=i\,\overline{\tilde{Ξ}_{\mathrm{sp},L}},
$$

so each value is determined by the conjugate of the other. This is the precise sense in which a Majorana field has two chiral parts and only half the freedom of a Dirac field: the two parts are present, and they are not independent.

**The equation.** The equation of the field is

$$
D\,\tilde{Ξ}_{\mathrm{sp}}=k_m\,\tilde{Ξ}_{\mathrm{sp}}^c,
$$

with $D$ the operator of the previous section and $m$ real. Written on the two values it is a pair, one first-order equation for each value, and the mass couples the equation of one value to the other. The companion *The Dirac Equation in Biquaternionic Form* writes the same two values in the frame of the gradient. The two frames differ by where the central $i$ sits, and only the present frame is used below: it is the one in which the conjugation is transparent.

**The constraint is propagated.** Apply $\mathcal{C}$ to the equation and use the two properties already checked:

$$
D\,\mathcal{C}\tilde{Ξ}_{\mathrm{sp}}=\mathcal{C}(D\tilde{Ξ}_{\mathrm{sp}})=k_m\,\mathcal{C}^{2}\tilde{Ξ}_{\mathrm{sp}}=k_m\,\tilde{Ξ}_{\mathrm{sp}} .
$$

So the conjugate field solves the same equation with the two sides exchanged, and the deviation $\delta=\tilde{Ξ}_{\mathrm{sp}}-\mathcal{C}\tilde{Ξ}_{\mathrm{sp}}$ solves

$$
D\,\delta=m\,(\mathcal{C}\tilde{Ξ}_{\mathrm{sp}}-\tilde{Ξ}_{\mathrm{sp}})=-m\,\delta .
$$

The equation is first order in the time derivative, so the deviation is fixed by its value at one time: a field self-conjugate at one time stays self-conjugate at every time. The sign in front of $m$ is not a change of mass. It is the reversal of the frequency that the conjugation performs on the symbol, and the squared operator sees neither sign.

**The mass shell is unchanged.** Squaring the equation and using $\mathcal{C}^{2}=1$ and $D^{2}=\Box$,

$$
\Box\,\tilde{Ξ}_{\mathrm{sp}}=D^{2}\tilde{Ξ}_{\mathrm{sp}}=k_mD\,\tilde{Ξ}_{\mathrm{sp}}^c=k_m^{2}\,\tilde{Ξ}_{\mathrm{sp}} ,
$$

so a plane wave of the field sits on $p^{2}=m^{2}c^{2}$, exactly as in the Dirac case. The mass shell is the one of a massive fermion, and the Majorana restriction has removed half the degrees of freedom and nothing else. The bilinear that normalises the field is the one of the companion quantisation article, and it is nonzero for $m>0$. Here $k_m=mc/\hbar$ is the mass wave number, the inverse of the mass length.

**No single mode is self-conjugate.** At fixed momentum the equation reads $D_p u=m\,\mathcal{C}u$, and $\mathcal{C}$ anticommutes with $D_p$, so it carries the kernel of $D_p-m$ to the kernel of $D_p+m$. A solution of definite frequency therefore has a conjugate of the opposite frequency, and no one mode is its own conjugate. The self-conjugate field is a pair of opposite frequencies, one amplitude at $p$ and its conjugate at $-p$, and each amplitude solves its own equation. That is the standard statement that the charge conjugate of a positive-frequency amplitude is a negative-frequency one, and it is why the condition does not quantise the theory into nothing.

**Which bilinears survive.** The physical statements are about the field, whose components anticommute. Two things decide the fate of a bilinear, and neither is a computation of a value.

- **The parity of the bilinear under the conjugation.** The field is fixed by $\mathcal{C}$, so the image of the bilinear under $\mathcal{C}$ must be the bilinear itself. A bilinear whose image carries a minus sign is therefore its own negative, and it vanishes.
- **The sign of the exchange.** The image under $\mathcal{C}$ is the bilinear with the two fields interchanged. For anticommuting components the interchange carries a minus sign; for commuting ones it carries none.

The two combine, and the second is what makes the commuting case the mirror of the physical one.

| Bilinear | Parity under the conjugation | Anticommuting self-conjugate field | Commuting element of the same fixed space |
|---|---|---|---|
| scalar pairing, built from $c_0$ | even | nonzero: the mass term is permitted | zero |
| vector current, built from $c_\mu$ | odd | zero for every $\mu$ | nonzero |
| axial current, built from $c_\mu$ and $\xi$ | even | nonzero | zero |

The vanishing of the vector current is the statement that a self-conjugate field carries no fermion number. The two surviving bilinears are what such a field can couple to: the scalar, which is the mass, and the axial current, which is the spin density. The mass of a Majorana field is exactly the pairing of the field with its own conjugate, and the barrier that forbids it for a Weyl field does not exist here.

**A caution that must be recorded.** The two right-hand columns are not the same computation, and the difference between them is the whole of the anticommutativity. Read with ordinary complex coefficients, the exchange carries no sign, so every bilinear is even and nothing is forced to vanish; the antisymmetric contractions that produced the scalar pairing then cancel instead, and the pattern inverts. The construction of the condition above is classical, and a reader may attempt the bilinears at that level; he will find the vanished scalar and conclude that a Majorana mass is impossible. The sign by which the two columns differ is the interchange of two components, and nothing else. Every bilinear statement for a Majorana field is therefore a statement about an anticommuting field, and the anticommutation is supplied by the mode operators of the companion quantisation article and not by $\mathbb{B}$ itself.

**Contrast with the Weyl field.** A Weyl field is an element of one value, and the mass term of the equation pairs the two values, so the term vanishes on it: a single-valued element has no Dirac mass. The only mass such a field can carry is the one of the previous paragraphs, a pairing with its own conjugate, and that pairing is available only when the field is not protected by a conserved charge. Where the chirality is protected by a complex gauge representation, as for the Standard-Model neutrino, the term is forbidden and the field is exactly massless; where the field is a gauge singlet, the same term is allowed and the field, once massive, is Majorana and no longer Weyl. A Dirac fermion is the remaining case: independent values, a mass that pairs them, and neither the Weyl protection nor the Majorana self-conjugacy.

## Which Conjugation of the Algebra Is the Charge Conjugation?

**The question.** The conjugation of the previous sections was written $\tilde{Ξ}_{\mathrm{sp}}^c=i\bar{\tilde{Ξ}}_{\mathrm{sp}}$ and used. The algebra supplies four conjugations, and the question is which of them can play that role and which cannot. The answer is one criterion, and the criterion is order.

**The four conjugations.** They divide into two kinds, and the division is the whole of the answer.

| Conjugation | Action on the units and on $i$ | Type |
|---|---|---|
| ${}^{\natural}$ quaternion | $\vec e_\eta\mapsto-\vec e_\eta$, $i\mapsto i$, $e_t\mapsto e_t$ | $\mathbb{C}$-linear antiautomorphism |
| $\bar{\cdot}$ complex | units fixed, $i\mapsto-i$ | conjugate-linear **automorphism** |
| ${}^{*}={}^{\natural}\circ\bar{\cdot}$ Hermitian | $\vec e_\eta\mapsto-\vec e_\eta$, $i\mapsto-i$ | conjugate-linear antiautomorphism |
| $\flat=-{}^{*}$ | $\vec e_\eta\mapsto\vec e_\eta$, $i\mapsto i$, $e_t\mapsto-e_t$ | conjugate-linear, order-reversing with a sign |

**The criterion is automorphism against antiautomorphism.** A conjugation that is to be a real structure on the field must commute with the algebra's action on it, and on the regular element the action is left multiplication. Commuting with the order of a product is what an automorphism does and what an antiautomorphism reverses:

$$
\overline{QR}=\bar Q\,\bar R,\qquad
(QR)^{*}=R^{*}Q^{*},\qquad
(QR)^{\flat}=-R^{\flat}Q^{\flat}.
$$

Only the bar is an automorphism. The other two reverse the order, and the third carries a sign as well, so neither can serve as the real structure of a field that carries the left action. That is the whole criterion, and it is a statement about the order of a product and not about the fixed spaces.

**What each one fixes.** The fixed spaces separate the three antilinear ones, and they are why the count alone decides nothing.

$$
\{\tilde{Ξ}_{\mathrm{sp}}:\bar{\tilde{Ξ}}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp}}\}=\mathbb{B}_{H},\qquad
\{\tilde{Ξ}_{\mathrm{sp}}:\tilde{Ξ}_{\mathrm{sp}}^*=\tilde{Ξ}_{\mathrm{sp}}\}=\mathbb{B}_{\Psi},\qquad
\{\tilde{Ξ}_{\mathrm{sp}}:\tilde{Ξ}_{\mathrm{sp}}^{\flat}=\tilde{Ξ}_{\mathrm{sp}}\}=\mathbb{B}_{\Phi},
$$

each of real dimension four. So all three antilinear involutions fix a four-dimensional space, and the count that a Majorana field needs is met by all three. What distinguishes them is what the fixed space is and whether the conjugation respects the order. The bar fixes the real quaternions, and the fixed space of the charge conjugation is that space multiplied by the central phase $(1+i)/\sqrt2$, because $\tilde{Ξ}_{\mathrm{sp}}^c=\tilde{Ξ}_{\mathrm{sp}}$ reads $\tilde{Ξ}_{\mathrm{sp}}=i\bar{\tilde{Ξ}}_{\mathrm{sp}}$ and not $\tilde{Ξ}_{\mathrm{sp}}=\bar{\tilde{Ξ}}_{\mathrm{sp}}$. The phase is a relabelling of the same four-dimensional real form.

**The conjugate field and its action.** Under a Lorentz rotor $U$ the field goes to $U\tilde{Ξ}_{\mathrm{sp}}$, and the conjugation carries that into $\bar U\,\bar{\tilde{Ξ}}_{\mathrm{sp}}$: the conjugate field carries the conjugate rotor and not the same one. For a rotor of unit norm $(\bar U)^{\natural}=U^{-1}$, so the conjugate action is the inverse one read through the quaternion conjugation. The two roles are different and neither replaces the other: the coefficient conjugation is the real structure, and the conjugate rotor is what the conjugate field transforms by.

**$\flat$ is a different conjugation, and the difference is the order.** The parent articles retain $\flat=-{}^{*}$ as the algebra's real structure. It is antilinear and involutive, so it is a real structure on the algebra read as a real vector space, and its fixed space is the material sector $\mathbb{B}_{\Phi}$. But it is order-reversing, and its fixed space is a sector of the algebra and not a real form of the field. It is the map that pairs a field with its conjugate in a Majorana-type coupling; it is not the map that identifies a field with its own antiparticle, and it is not the parent's mass term, which is the linear chiral pair. Mixing the two is the natural error, and it is the error the next section tests. The four levels at which the corpus uses the name charge conjugation — the algebra's real structure $\flat$, the Clifford pseudoautomorphism, the operation on the carrier, and the real structure $\mathcal{C}$ — are tabulated in *Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form*.

## Does the Material/Informational Split Help or Obstruct?

**The split.** The algebra carries a second decomposition, by the Hermitian conjugation, and it must not be conflated with the one used above. It is real,

$$
\mathbb{B}_{\Phi}=\{Q:Q^{*}=-Q\},\qquad
\mathbb{B}_{\Psi}=\{Q:Q^{*}=Q\},\qquad
\dim_{\mathbb{R}}\mathbb{B}_{\Phi}=\dim_{\mathbb{R}}\mathbb{B}_{\Psi}=4,
$$

and it is the algebra's own, the anti-Hermitian part carrying the four-vectors and the interval and the Hermitian part carrying the observables and the states. The question is whether the Majorana real form can be located there.

**The tempting interpretation, and why it is wrong.** $\mathbb{B}_{\Phi}$ is the fixed space of the real structure $\flat$, it is four-real-dimensional, and the dimension matches the Majorana count exactly. The temptation is to say that a Majorana field is a field with values in $\mathbb{B}_{\Phi}$. The framework's own structure refuses it, and the reason is one line: **the operator does not preserve the sector.** The unit $\vec e_x$ is anti-Hermitian, $(\vec e_x)^{*}=-\vec e_x$, so it lies in $\mathbb{B}_{\Phi}$; its square is $\vec e_x^{2}=-e_t$, which is Hermitian and lies in $\mathbb{B}_{\Psi}$. A derivative along $x$ therefore carries a field of the material sector into the informational one, and no first-order equation with the algebra's units can be written inside either sector alone.

**The fixed space of the conjugation is not a sector.** The fixed space of $\tilde{Ξ}_{\mathrm{sp}}^c=\tilde{Ξ}_{\mathrm{sp}}$ is four-real-dimensional and it is not $\mathbb{B}_{\Phi}$: it is the real-quaternion form multiplied by the central phase, and both the multiplication by $i$ and the conjugation are needed to state it. The two four-dimensional spaces are different objects, and the coincidence of their dimensions is the coincidence that makes the sector split look like a candidate. The distinction is one of kind: a sector is a fixed space of an antilinear map read on the algebra, and the Majorana real form is the fixed space of an antilinear map read on the field.

**The physical test, and the answer.** The test is the one a physicist would apply: impose the condition, evolve, and see whether the condition survives. The previous section performed it, and the answer is that the condition survives because $\mathcal{C}$ commutes with the operator. A sector, by contrast, is not preserved by the operator at all, so a constraint of the form "the field lies in $\mathbb{B}_{\Phi}$" cannot be propagated. It would be violated by the first time step. The sector split therefore **obstructs** the reality condition rather than supplying it, and it cannot be used as it stands.

**What survives of the split.** The split is not idle: it is the decomposition that separates the two kinds of physical quantity, and the material sector is where the four-vectors live. What it does not do is supply the charge conjugation. The two decompositions, by $\xi$ and by ${}^{*}$, are different decompositions of one algebra, and an argument that needs one of them cannot borrow the other's dimension.

## The Neutrino: What the Framework Does and Does Not Derive

**The empirical constraints.** The neutrino is electrically neutral, it comes in three species, and it is left-handed in the charged-current interaction. Two consequences follow from the Standard Model alone, and neither depends on a mass mechanism.

First, the light neutrino cannot carry an ordinary Dirac mass with a Standard-Model Higgs doublet: a right-handed partner is absent, and a bare mass term would break the gauge symmetry.

Second, the electromagnetic moments are unobservably small. The moment is proportional to the mass in the minimal extension, and it vanishes identically for a strictly self-conjugate field, because the only multiplier that can carry it is odd under the conjugation.

The framework transcribes both facts, and neither is a derivation.

**What the framework supplies.** The arena supplies the field, the two values, the chiral gauge action and the two kinds of mass. The chiral gauge structure is the algebra's, and the companion *Chiral Fermions in the Biquaternion Framework* computes it: a chiral abelian symmetry needs an element off the centre, the mass bilinear is invariant exactly when the two charges are equal, and the abelian sector the algebra supplies canonically is vector-like. The two kinds of mass are the linear chiral pair and the antilinear self-pairing, and the section above fixed which conjugation carries the second.

**What the framework does not supply.** It does not fix the mass matrix, the mixing angles or the phase, and it does not choose between the Dirac and the Majorana mechanisms for a given species. Those are measured. What the algebra does is narrower, and it is not small: it makes the choice a choice between two structures it carries. The Dirac mass is the linear pairing of the two values. The Majorana mass is the antilinear pairing of the field with its conjugate. The two are different objects, and they conserve different charges.

**The consequence for the mass term.** A Majorana mass for the neutrino conserves no fermion number and permits neutrinoless double beta decay; a Dirac mass conserves it and forbids the process. The framework states the difference as the difference between the linear chiral pair and the antilinear self-pairing. The linear pair is built from the two values of one element, and it passes a continuous central phase. The antilinear pairing is built from the element and its conjugate, and it does not. The difference of the two terms is therefore not a numerical one, and no adjustment of parameters turns one into the other.

**The see-saw, in one line.** The see-saw mechanism combines both: a heavy self-conjugate state and a light one mixed by a Dirac pairing, and the light mass is suppressed by the heavy scale. The framework carries the three objects the mechanism needs, because it carries the three terms, and it derives none of the scales. The companion *The See-Saw Mechanism and Majorana Mass in Biquaternionic Form* writes the mechanism in this notation.

## What the Framework Supplies, Transcribes, and Does Not Supply

**The ledger of the section, in one table.** The three columns are the three kinds of claim, and the table is the whole of the section.

| Statement | Status | Warrant |
|---|---|---|
| Three notions are three conditions on one element | supplied | the conditions are the two values and one antilinear involution |
| Weyl: four real components; Majorana: four; Dirac: eight | supplied | the dimensions of a value and of a fixed space of an involution |
| The charge conjugation is the coefficient bar | supplied | the bar is the only conjugate-linear automorphism; the phase in front of it is convention |
| The conjugation commutes with the kinetic operator | supplied | the four coefficients of the operator are real |
| The mass shell stays $p^{2}=m^{2}c^{2}$ | supplied | $D^{2}=\Box$ and $\mathcal{C}^{2}=1$ |
| The vector current of the self-conjugate field vanishes | supplied | the anticommutation of the components |
| A commuting element gives the opposite pattern | recorded | the same computation without anticommutation |
| The sector split is not the Majorana real form | supplied | the operator does not preserve $\mathbb{B}_{\Phi}$ |
| The chiral gauge group is vector-like | supplied | the centre multiplies the two values alike |
| The left-handedness of the neutrino | transcribed | experiment |
| The mass values, mixings and phases | not supplied | measurement |
| Whether a given species is Dirac or Majorana | not supplied | measurement |

**The shape of the answer.** The framework supplies the structure and not the numbers, and the structure is not a formalism laid over the algebra: it is the algebra's own two values, its own conjugations, and its own product. Every supplied row of the table is a statement about an element, and every not-supplied row is a number.

**The strongest objection.** The objection is that the construction is a transcription: the Dirac operator of the frame is written here rather than derived, and the mass is inserted as a parameter. The answer is the one the programme gives everywhere: the arena is derived and the dynamics is imported, and the ledger classifies claims rather than concepts. What the algebra adds is that the four objects the subject needs — the field, the two values, the conjugation and the pairing — are one object each and not four formalisms that must be proved consistent with one another. That consistency is not a small thing: the standard treatment needs a charge-conjugation matrix in a chosen basis, and the basis-independence of the physics is a theorem to be proved. Here the charge conjugation is a conjugation of the algebra, and the basis never enters.

## Majorana Fermions in a Geometric Setting Outside the Framework

**The external use.** Separately from the particle interpretation, the Majorana pair has a use in three-dimensional quantum gravity: a pair of self-conjugate fields with a real structure commuting with $SU(1,1)$ models a time-like surface, and the sign of the area spectrum is what forces the pair rather than a single chiral field. The object of that literature is a spinor in the older sense: a column of the defining module of the group. The word is used here because that object is the subject of the citation, and it names nothing in the construction above.

**What the framework does and does not say about it.** The framework carries the structures the construction uses — a conjugation, a real form, an invariant pairing — and it derives none of the geometry. Whether a pair of self-conjugate fields with an $SU(1,1)$-invariant pairing models a time-like surface is a question about that model and not about the algebra. The citation changes nothing in the sections above, and the sections above change nothing in it.

**Why it is recorded.** It is recorded because it is a place where the Majorana condition is used for something other than a mass, and because a reader who meets the condition here will meet it there. The condition is the same antilinear involution, and the use is different.

## Open Questions

**Three questions are left open by the construction, and each is a question about the algebra rather than about the physics.**

- **The operator of the frame.** The article writes the kinetic operator in the frame in which the conjugation is transparent. The companion *The Dirac Equation in Biquaternionic Form* writes it in the frame of the gradient. The two are related by the placement of the central $i$, and the relation has not been written as an identity of operators. A proof that the two frames give the same solution space, in the sense of an invertible multiplier, would close the question.
- **The Grassmann structure.** The bilinear statements hold for anticommuting components, and the algebra of an element does not carry the anticommutation: it is supplied by the mode operators of the companion quantisation article. Whether a single algebraic structure carries both the coefficient algebra and the anticommutation, or whether the two are necessarily separate, is open.
- **The count of the real forms.** The three antilinear involutions all fix four real dimensions, and the criterion of order selects the bar. Whether the other two have a physical use — $\flat$ for a coupling, ${}^{*}$ for a sector — or whether the selection is the whole of their content, is not settled here.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The generators carry no frame label: $\gamma_\mu$ is one set of matrices, $\gamma_0^2=I_4$ and $\gamma_\eta^2=-I_4$. The frame belongs to the coordinate, not to the array.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra. In basis operators they are

$$
\gamma_0=iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_x},\quad \gamma_1=iL_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_y},\quad \gamma_2=iL_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y},\quad \gamma_3=iL_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y},\quad \gamma_5=-iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_z} .
$$

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\tilde{Ξ}_{\mathrm{sp}}=a\tilde{Ξ}_{\mathrm{sp}}$ and $R_b\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp}} b$. Each of these is one product of a left and a right multiplication, so its coefficient matrix $c(\gamma_\mu)$ is a pure tensor: the single products fill the seven-dimensional cone $\operatorname{rank}c(M)\le1$ inside the sixteen-dimensional basis operator algebra, a general element is a sum of at most four of them, and the least number of products needed is $\ell(M)=\operatorname{rank}c(M)$.

The four multipliers of the body are the real parts of these basis operators: $c_\mu=-i\gamma_\mu$, and the operator $D=\sum_\mu\varepsilon_\mu c_\mu\partial/\partial x_\mu$ is the one the conjugation commutes with. That is the whole content of the statement that the $i$ belongs to the generator and not to the operator, and the two displays are two readings of one frame.

$\gamma_5$ is the reference-frame basis operator of the chirality; the chirality operator of the body is its axis-free form, $\xi=-iR_{\mathrm{axf},\vec e_z}$.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the basis operators span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The identities the bodies cite.** In the $\gamma$ reading, with $\varepsilon=(1,-1,-1,-1)$ the sign vector of the basis operators,
$$
\{\gamma_\mu,\gamma_\nu\}=2\varepsilon_\mu\delta_{\mu\nu}I_4,\qquad
(\gamma_\eta)^2=-I_4,\qquad
\gamma_5^2=I_4,\qquad
\{\gamma_\mu,\gamma_5\}=0,
$$
$$
[\gamma_\mu,\gamma_\nu]=2\gamma_\mu\gamma_\nu\quad(\mu\ne\nu),\qquad
[\gamma_a,S_{cd}]=\varepsilon_a\delta_{ac}\gamma_d-\varepsilon_a\delta_{ad}\gamma_c,\qquad
S_{cd}=\tfrac14[\gamma_c,\gamma_d],
$$
$$
\mathrm{tr}(\gamma_\mu\gamma_\nu)=4\varepsilon_\mu\delta_{\mu\nu},\qquad
\mathrm{tr}(\gamma_5\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)=-4i\,\epsilon_{\mu\nu\rho\sigma},
$$
$$
\mathrm{tr}(\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)
=4\bigl(\varepsilon_\mu\delta_{\mu\nu}\varepsilon_\rho\delta_{\rho\sigma}
-\varepsilon_\mu\delta_{\mu\rho}\varepsilon_\nu\delta_{\nu\sigma}
+\varepsilon_\mu\delta_{\mu\sigma}\varepsilon_\nu\delta_{\nu\rho}\bigr).
$$
The contraction sums follow from the squares. With one index raised, $\gamma^\mu=-\varepsilon_\mu\gamma_\mu$, so that $\sum_\mu\gamma^\mu\gamma_\mu=-4I_4$, $\sum_\mu\gamma^\mu\gamma_\alpha\gamma_\mu=2\gamma_\alpha$, $\sum_\mu\gamma^\mu\gamma_\alpha\gamma_\beta\gamma_\mu=-4\varepsilon_\alpha\delta_{\alpha\beta}I_4$ and $\sum_\mu\gamma^\mu\gamma_\gamma\gamma_\beta\gamma_\alpha\gamma_\mu=-2\gamma_\gamma\gamma_\beta\gamma_\alpha$.

## Summary

The field is an element of $\mathbb{B}$. Its chirality is a value of one operator, $\xi=-iR_{\mathrm{axf},\vec e_z}$, and the three notions are three conditions on that element: an arbitrary element is Dirac, an element of one value is Weyl, and an element fixed by the charge conjugation is Majorana.

The charge conjugation is the coefficient conjugate, $\tilde{Ξ}_{\mathrm{sp}}^c=i\bar{\tilde{Ξ}}_{\mathrm{sp}}$ up to the phase discussed above. It is conjugate-linear, it squares to one, it exchanges the two values, it fixes a real four-dimensional space, and it commutes with the kinetic operator of the frame. The last property holds because every coefficient of the operator is real: the operator is built from multipliers the conjugation fixes, so the conjugation passes through it. On the symbol the same fact reads as anticommutation, and it is the reversal of the frequency that the conjugation performs on a plane wave.

The Majorana condition $\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp}}^c$ is therefore consistent with a mass. The constraint is propagated, the deviation from self-conjugacy solves the equation with the reversed sign of the mass, the mass shell stays $p^{2}=m^{2}c^{2}$, and the restriction removes half the degrees of freedom and not the mass. No single mode is self-conjugate: the condition pairs an amplitude at $p$ with its conjugate at $-p$. The vector current of the self-conjugate field vanishes, so the field carries no fermion number; the scalar pairing survives, and it is the mass term. Both statements are statements about an anticommuting field, and a commuting element gives the opposite pattern.

Which conjugation of the algebra plays the role is decided by one criterion: a real structure on a field that carries the algebra's left action must be an automorphism, and the coefficient bar is the only conjugate-linear automorphism. The Hermitian conjugation and $\flat$ reverse the order and cannot serve. The fixed space of the charge conjugation is the real-quaternion form multiplied by the central phase, and it is not the material sector: the sector split is a different decomposition of the same algebra, and the operator does not preserve it, because $\vec e_x$ is anti-Hermitian and $\vec e_x^{2}=-e_t$ is not. The split therefore obstructs the reality condition rather than supplying it.

The left-handedness of the neutrino is empirical, and the mass values and mixings are measured. The framework supplies the two kinds of mass — the linear pairing of the two values and the antilinear pairing with the conjugate — and it does not choose between them for a given species. That choice is a measurement, and the algebra's service is to make it a choice between two structures it carries and not between two formalisms imported from outside.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_\mu^2=-e_t$, $\vec e_x \vec e_y=\vec e_z$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp},L}+\tilde{Ξ}_{\mathrm{sp},R}$ | The field, an element, and its two values |
| $\xi=-iR_{\mathrm{axf},\vec e_z}$ | One basis operator that carries the split, a pure right multiplier; $\xi\tilde{Ξ}_{\mathrm{sp},L}=-\tilde{Ξ}_{\mathrm{sp},L}$, $\xi\tilde{Ξ}_{\mathrm{sp},R}=+\tilde{Ξ}_{\mathrm{sp},R}$ |
| $\mathbb{B}_{\Phi}, \mathbb{B}_{\Psi}$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{B}_{H} = \{Q:\bar{Q}=Q\}$ | Real-quaternion subspace, fixed space of $\bar{\cdot}$ |
| $\mathbb{B}_{C} = \mathrm{span}_{\mathbb{R}}\{e_t, ie_t\}$ | Complex scalar subspace; the centre |
| ${}^{\natural},\ \bar{\cdot},\ {}^{*}=({}^{\natural})^{\,*}$ | Quaternion, complex and Hermitian conjugations |
| $Q^{\flat}=-Q^{*}$ | Algebra's real structure; fixed space $\mathbb{B}_{\Phi}$ |
| $c_0:\tilde{Ξ}_{\mathrm{sp}}\mapsto\tilde{Ξ}_{\mathrm{sp}}\vec e_x$; $c_k:\tilde{Ξ}_{\mathrm{sp}}\mapsto\vec e_\eta\tilde{Ξ}_{\mathrm{sp}}\vec e_y$ | The four real multipliers of the frame; $c_0^2=-1$, $c_k^2=+1$, pairwise anticommuting |
| $D=\sum_\mu\varepsilon_\mu c_\mu\partial/\partial x_\mu$ | Kinetic operator; $D^2=\Box$; $D_p=-i\sum_\mu\varepsilon_\mu p_\mu c_\mu$ |
| $\Box=\sum_\mu\partial^2/\partial R_\mu^2=-\partial^2/\partial {r'_{t}}^2+\Delta$ | d'Alembertian; $\Delta$ is the spatial Laplacian |
| $\varepsilon=(1,-1,-1,-1)$ | Sign vector of the frame |
| $\mathcal{C}:\tilde{Ξ}_{\mathrm{sp}}\mapsto i\bar{\tilde{Ξ}}_{\mathrm{sp}}$ | Charge conjugation; $\mathcal{C}^2=1$, $\xi\mathcal{C}=-\mathcal{C}\xi$, $\mathcal{C}D=D\mathcal{C}$ |
| $\tilde{Ξ}_{\mathrm{sp}}^c=\mathcal{C}\tilde{Ξ}_{\mathrm{sp}}$ | Charge conjugate; $\tilde{Ξ}_{\mathrm{sp}}^c=\tilde{Ξ}_{\mathrm{sp}}$ defines Majorana |
| $\tilde{Ξ}_{\mathrm{sp}}=i\bar{\tilde{Ξ}}_{\mathrm{sp}}$ | Majorana condition; equivalent to $\tilde{Ξ}_{\mathrm{sp},L}=i\overline{\tilde{Ξ}_{\mathrm{sp},R}}$ |
| $D\tilde{Ξ}_{\mathrm{sp}}=k_m\tilde{Ξ}_{\mathrm{sp}}^c$ | Majorana equation |
| $\dim_{\mathbb{R}}\{\tilde{Ξ}_{\mathrm{sp}}:\tilde{Ξ}_{\mathrm{sp}}^c=\tilde{Ξ}_{\mathrm{sp}}\}=4$ | Majorana component count |
| $\delta=\tilde{Ξ}_{\mathrm{sp}}-\mathcal{C}\tilde{Ξ}_{\mathrm{sp}}$ | Deviation from self-conjugacy; $D\delta=-m\delta$ |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices, and for the intrinsic form of an operator.
- Ettore Majorana, "Teoria simmetrica dell'elettrone e del positrone", *Nuovo Cimento* **14** (1937) 171–184, the original symmetric theory of the electron and positron, where the self-conjugate spinor is introduced.
- Steven Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the construction of Dirac, Weyl and Majorana fields, the charge-conjugation matrix, and the relation between the reality of the mass term and fermion-number conservation.
- Michael E. Peskin and Daniel V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the Dirac bilinears, charge conjugation in the chiral basis, and the Majorana mass term.
- Rabindra N. Mohapatra and Palash B. Pal, *Massive Neutrinos in Physics and Astrophysics* (World Scientific, 2004), for the Dirac/Majorana distinction, the see-saw mechanism, and neutrinoless double beta decay.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the classification of real structures on the carrier by signature.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the relation between spinors, the charge-conjugation operation, and the Lorentz group in a real Clifford algebra.
- J. D. Simão, "Biquaternions, Majorana spinors and time-like spin-foams," arXiv:2401.10324 [gr-qc] (2024), for the geometric use of a *pair* of Majorana spinors modelling a time-like surface in three-dimensional quantum gravity, with a real structure commuting with $SU(1,1)$ and the area-spectrum sign argument that distinguishes the pair from a single Weyl field. External; cited for the geometric use only.
- Companion articles: [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html); [Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form](antilinear-structure-and-the-two-kinds-of-mass-in-biquaternionic-form.html); [Chiral Fermions in the Biquaternion Framework](chiral-fermions-in-the-biquaternion-framework.html); [The See-Saw Mechanism and Majorana Mass in Biquaternionic Form](the-seesaw-mechanism-and-majorana-mass-in-biquaternionic-form.html); [Canonical Quantization of the Biquaternion Dirac Field](canonical-quantization-of-the-biquaternion-dirac-field.html); [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html); [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html); [Introduction to the Biquaternion Universe](introduction-to-the-biquaternion-universe.html).
