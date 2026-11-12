# __The Majorana Equation in Biquaternionic Form__

## Introduction

A **Majorana fermion** is a fermion that equals its own antiparticle. Two consequences follow at once: the field carries no conserved charge, and it carries half the coefficients of a Dirac field, because equality with its own conjugate is a condition and not a second field. The equation of such a field is the Dirac equation with the mass term pairing the field with its conjugate instead of with the other chiral half.

This article asks what the biquaternion framework supplies for that equation, in the notation of the companion articles. The carrier is the algebra $\mathbb{B}$. The field is an **element** $\tilde{Ξ}$, a general element is written $\tilde Q$, and every statement below is a statement about elements, their products, the gradient and two conjugations. Nothing below is written as a component list, and no product of such a list enters the body.

The presentation is organized around one question — *where can the mass term sit?* — and the answer is split, at the outset, into the three categories the corpus uses.

- **Established, and recomputed below.** The equation is one element equation, with the derivative from the left and the mass from the right, through $\vec e_z$ and the coefficient conjugation,
$$i\frac{\partial\tilde{Ξ}}{\partial r'_t}+\sum_\eta\vec e_\eta\frac{\partial\tilde{Ξ}}{\partial R_\eta}-k_mi\,\bar{\tilde{Ξ}}\,\vec e_z=0 .$$
This is the corpus's two-sided form, the dictionary of Kravchenko used throughout the series (*The Dirac Equation in Biquaternionic Form*). Its plane waves sit on the ordinary shell, $k_{t}^{\prime\,2}-\lvert\vec k_\Phi\rvert^{2}=k_m^{2}$; the warrant is the nullity table of §*Why the Mass Sits on the Right*, which also shows that the two obvious alternatives — the mass as a bare conjugation, and the mass through the star — put their solutions on the spacelike locus instead.
- **Sharpened here.** The mass is on the right because a letter cannot be moved from the left: left multiplication keeps the letter of its operand, so a mass inside the left slot applies one factor to both letters and couples nothing. The mass term of an $L$ part is an $R$ element, and the same display read on its two letters is a pair of equations, each carrying the conjugate of the other letter. That is the biquaternionic form of the chiral pair, with one field and no second one.
- **Gap, left visible.** Equality with the conjugate is a reality condition, and the algebra's conjugations are classified here: the coefficient conjugation and the star are involutions with four-real-dimensional fixed spaces, and the unit-conjugated conjugations that exchange the two letters are involutions of the same size. None of them commutes with the equation — the sixteen bar-two-sided-operatored forms were tested — so the condition is not propagated at the level of the algebra, and the physical Majorana field is defined by the construction of *The Neutrino and Majorana Fermions in Biquaternionic Form*. The companion *Antilinear Structure and the Two Kinds of Mass* owns the diagnosis, and the present article states only its algebraic content.

The article is organized as follows. The next section fixes the frame, the two operators and the two conjugations, and states the one letter rule the argument runs on. The section after that writes the equation and its three forms. A section then shows why the mass sits in the right slot and gives the nullity table that decides among the three readings. A section classifies the conjugations and counts the coefficients. A section treats the fixed space and the neutrality; a section the plane waves and the counting of states; and a section separates what the algebra supplies, what it transcribes and what it does not. Open questions close the argument, and a last section writes out the legacy display once, for comparison with the literature.

Every display below is an element, a product of elements, or a conjugation of one; the argument never leaves them.

## Frame and Notation

**The coordinates.** An element is written $\tilde Q=Q_te_t+\vec Q$, with $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ and complex coefficients $Q_\mu$; the scalar part is $\mathrm{Sc}(\tilde Q)=Q_t$ (*Algebra and Element Conventions*). The units satisfy $\vec e_x^{2}=\vec e_y^{2}=\vec e_z^{2}=-e_t$ and $\vec e_x\vec e_y=\vec e_z$, and $e_t$ is the unit of the algebra.

**The frame.** Every display is written in the $\mathbb{B}_{\Phi}$ frame, where $Q_t=i q'_t$ and $r'_t$ is a length, the time carried with the constant kept, $r'_t=c\,t'$; the metric coefficient of the seconds $t'$ is $g_{tt}=-c^{2}$ and the quadratic form in $r'_t$ is $\langle\tilde Q\rangle_{\natural}=-{r'_{t}}^{2}+r_x^{2}+r_y^{2}+r_z^{2}$ (*Frame and Metric Conventions*). The constant $c$ is carried in every display below, and none of them sets it to one.

**The two operators.** The gradient $\tilde\nabla_\Phi$ and the d'Alembertian $\Box_\Phi$ are the series operators (*Operator and Calculus Conventions*); the article names them and does not restate them. It uses one property, which the same article fixes: the product of the gradient with its quaternion conjugate is the d'Alembertian. That product is the sense in which the two first-order operators of the pair below are square roots of $\Box$, and it is a convention of the series, not a result of this article.

**The letters.** The basis operator of a frame is the right multiplication by the third unit with the phase $-i$, a pure right multiplier whose side is the right slot,
$$
\tilde{Ξ}\longmapsto-i\,\tilde{Ξ}\,\vec e_z ,
$$
a pure right multiplier that squares to the identity and splits the coefficient space two and two (*Special Element Conventions*, §*The Chirality Convention*). The part of value $-1$ is written $\tilde{Ξ}_{L}$ and the part of value $+1$ is written $\tilde{Ξ}_{R}$; the letters are the Dirac ones, and they are a subscript on an element and not a property of a display. Two rules come with the letters, and the article uses both:

- a product takes the letter of its right factor;
- **left multiplication keeps the letter**, because $(a\tilde{Ξ})\vec e_z=a(\tilde{Ξ}\vec e_z)$ for every element $a$.

The second is the identity the whole of §*Why the Mass Sits on the Right* rests on, and it is one line of associativity. It was checked on elements of each letter against a hundred random multipliers, with residual $0$.

**The two conjugations.** The coefficient bar $\bar\cdot$ conjugates the four coefficients and fixes the units; it is an automorphism of the algebra and antilinear over $\mathbb{C}$. The star is the Hermitian conjugation, the anti-automorphism that conjugates the coefficients and reverses the vector part (*Product and Form Conventions*). Both are involutions of the underlying real vector space, and both are antilinear; the bar is the one that touches no unit, and it is the one the mass term uses.

**What the letters are not.** The letter is a name and not a quantity. It is read from one action on the element, not from a sign carried by the algebra; a grading would need a multiplicative functional, and the two families of multipliers overlap in the scalars, which have no side. No root, no projection and no nilpotent enters it, and none of them enters this article.

## The Equation and Its Three Forms

The equation is one equation, and the three forms of the literature are three readings of it, distinguished by what they display. The table is the map.

| the form | what acts | what it displays |
|---|---|---|
| the element form | the gradient from the left, the mass from the right through $\vec e_z$ with the coefficient conjugation | the equation as one product, and the slot of the mass |
| the letter form | the same equation read on its two letters | the pair, and the coupling of the two letters by the mass |
| the real form | the same equation on the fixed space of the coefficient bar | the count: four real coefficients, and no phase |

**The element form.** The equation is

$$
i\frac{\partial\tilde{Ξ}}{\partial r'_t}+\sum_\eta\vec e_\eta\frac{\partial\tilde{Ξ}}{\partial R_\eta}-k_mi\,\bar{\tilde{Ξ}}\,\vec e_z=0 ,
$$

which is the corpus's two-sided form on the algebra: the derivative from the left, and the mass from the right through the spatial unit. Three actions sit in it, and none is decoration.

- The **derivative** acts from the left, on the element.
- The **coefficient conjugation** $\bar\cdot$ acts on the field and has **no side**.
- The **right multiplication** by $\vec e_z$ ends the mass term and carries it to the other letter.

The conjugation is what makes the mass antilinear; the right multiplication is what makes it a coupling. §*Why the Mass Sits on the Right* shows that the third cannot be dropped: without it the equation has no timelike solution.

**The letter form.** Read on the two letters, the equation is a pair. The mass of an $L$ part is an $R$ element, and the mass of an $R$ part is an $L$ element, so each member of the pair acts on one letter and carries the conjugate of the other:

$$
(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{L}=-k_mi\,\overline{\tilde{Ξ}_{R}}\,\vec e_z ,
\qquad
(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{R}=-k_mi\,\overline{\tilde{Ξ}_{L}}\,\vec e_z .
$$

The two lines are the equation of the display above, split; nothing is added. Each is an equation for one letter, and each carries the conjugate of the other, which is the precise sense in which the mass couples the letters and not a side of one of them. The mass terms are elements of the opposite letter, and that was checked on elements of each letter: the mass of an $L$ part is an $R$ element and the mass of an $R$ part is an $L$ element, exactly.

**The real form.** On the fixed space of the coefficient bar the field is coefficient-real, the conjugation does nothing, and the equation is real. The fixed space has four real coefficients against the eight of the algebra, and it carries no phase; that is the count of §*The Conjugation and the Count*, and the neutrality of §*The Fixed Space and the Neutrality*.

**One operator, three carriers.** The three readings are one equation and not three laws. The element form is the equation as written; the letter form is its split, and it is the form in which the chiral pair appears; the real form is its restriction to a real subspace. A reader who compares them compares one equation at three carriers, and the nullity table of the next section is what tells the three readings apart.

## Why the Mass Sits on the Right

**The letter cannot be moved from the left.** Left multiplication keeps the letter, by the one line of associativity above. So a mass term written inside the left action — a scalar multiple $k_m\tilde{Ξ}$, or a conjugation $k_mJ(\tilde{Ξ})$ — applies the same factor to the two letters and can couple nothing. It is diagonal on the letters whatever the scalar or the conjugation is, and a mass that is diagonal on the letters pairs no letter with another.

**The right slot can move it.** A right multiplication by an element takes the letter of its right factor, so a mass term that ends in a right multiplication acts on the two letters with two different factors. The mass term of the display above ends in $\vec e_z$, and the split of §*The Equation and Its Three Forms* is the result: the mass of an $L$ part is an $R$ element.

**The three candidate mass terms, and the nullity table.** The question is not one of taste. For each of three mass terms the equation was written on the plane-wave pair of §*Solutions and the Counting of States*, and the nullity of the real linear system was computed on the eight-real-dimensional coefficient space. The nullity is the number of real parameters of the solution at a fixed momentum, and it is constant across twelve momenta on each locus and at two masses:

| mass term | timelike, $k_{t}^{\prime\,2}-\lvert\vec k_\Phi\rvert^{2}=k_m^{2}$ | spacelike, $\lvert\vec k_\Phi\rvert^{2}-k_{t}^{\prime\,2}=k_m^{2}$ |
|---|---|---|
| $k_mi\,\bar{\tilde{Ξ}}\,\vec e_z$, the mass from the right | $8$ | $0$ |
| $k_m\,\bar{\tilde{Ξ}}$, a bare coefficient conjugation | $0$ | $8$ |
| $k_m\,\tilde{Ξ}^*$, the star | $0$ | $4$ |

Only the first row has its solutions on the ordinary shell. The second is the equation the series retired, and its spacelike family is the signature of a pairing built on the algebra's own conjugation rather than on a coupling of the two letters (*Antilinear Structure and the Two Kinds of Mass*, §*The Retired Equation: The Diagnosis Is the Dispersion*). The third row is no better on the timelike shell and has half the spacelike family.

**What the table says and does not say.** It does not say that an antilinear term is unphysical: the mass term of the first row is antilinear and its solutions are timelike. It says that the antilinearity must come with the right multiplication, because the right multiplication is what makes the term a coupling between the two letters; a conjugation alone pairs the field with a field of the same letter, and that pairing has no timelike solution. The discriminator is the slot, and the table is the measurement of the slot.

## The Conjugation and the Count

**The conjugation of the mass is not a reality condition.** The mass term of the display pairs $\tilde{Ξ}$ with $\bar{\tilde{Ξ}}\vec e_z$, so the conjugation it carries is the map
$$
\mathcal{C}(\tilde{Ξ})=\bar{\tilde{Ξ}}\,\vec e_z .
$$
Applied twice it returns minus the field, $\mathcal{C}(\mathcal{C}(\tilde{Ξ}))=-\tilde{Ξ}$: the bar is an involution and the two right multiplications by $\vec e_z$ multiply to $-1$. It is therefore a **square root of minus one** and not an involution. No non-zero element equals its own conjugate under it, and what it produces is a second field of the same size. That is the exact reason the two-sided form is the Dirac equation: its mass pairs the field with a second field, and the phase acts on the two linearly.

**The involutions the algebra does supply.** The bar and the star are involutions, each with a fixed space of four real dimensions: the coefficient-real elements for the bar, the Hermitian elements for the star. The unit-conjugated conjugations
$$
\tilde{Ξ}\longmapsto a\,\bar{\tilde{Ξ}}\,b ,
\qquad a,b\in\{e_t,\vec e_x,\vec e_y,\vec e_z\} ,
$$
are the conjugations that exchange the two letters, because the bar exchanges them and the two multipliers are units. Of the sixteen such forms, ten are involutions, and each of the ten has a fixed space of four real dimensions. The map $\tilde{Ξ}\mapsto\bar{\tilde{Ξ}}\vec e_z$ of the mass term is one of the six that are not.

**The count.** An antilinear involution on an eight-real-dimensional algebra has eigenspaces of four real dimensions each, and this is structural rather than a coincidence of a basis: the map is antilinear, so $\mathcal{C}(i\tilde{Ξ})=-i\,\mathcal{C}(\tilde{Ξ})$, and multiplication by the central $i$ carries the $+1$ eigenspace onto the $-1$ eigenspace; the two therefore have equal dimension, and their sum is the whole space. The count is

$$
\boxed{\;\text{Dirac field}: 8 \text{ real coefficients}, \qquad
\text{Majorana field}: 4 \text{ real coefficients}\;},
$$

and the Majorana field is the fixed space of such a conjugation: a carrier of half the size, singled out by an antilinear structure, and not a linear constraint bolted onto a Dirac field.

**Why the condition is not propagated here.** A reality condition is usable only if the equation carries the fixed space into itself, and that needs a conjugation commuting with the equation. None of the sixteen unit-conjugated forms commutes with it: the commutator was computed for each at a representative momentum and none vanishes. The fixed space is therefore not preserved by the flow, and a field that equals its conjugate at one time does not stay equal to it. The condition that is propagated is built in the companion articles, where the conjugation carries an operator of its own (*The Neutrino and Majorana Fermions in Biquaternionic Form*; *Antilinear Structure and the Two Kinds of Mass*, §*What the Failure Does and Does Not Show*). The algebra supplies the count of the box and the form of the equation; the propagation of the condition belongs to the companion articles.

## The Fixed Space and the Neutrality

**The real form.** The fixed space of the coefficient bar is the set of coefficient-real elements, of four real coefficients. On it the conjugation is the identity and the equation of §*The Equation and Its Three Forms* is a real equation: real coefficients, real derivatives, and a real mass. This is the form the literature calls the real form of the equation, and in this notation it needs no new operator and no second conjugation: it is the same equation, read on a subspace.

**The phase is not available.** The fixed space of an antilinear conjugation is not closed under multiplication by a phase. For a real $\alpha$ one has
$$
\mathcal{C}\bigl(e^{i\alpha}\tilde{Ξ}\bigr)=e^{-i\alpha}\,\mathcal{C}(\tilde{Ξ}) ,
$$
so $e^{i\alpha}\tilde{Ξ}$ lies in the fixed space only when $\alpha$ is a multiple of $\pi$; at $\alpha=\pi$ it lies in it, with the opposite sign. A field that equals its conjugate therefore carries no continuous phase, and a continuous phase is what a conserved charge is. The neutrality of the Majorana field is a property of the conjugation, and the algebra is not made smaller to obtain it.

**One field and not two.** The two eigenspaces of a conjugation are of the same size and are exchanged by $i$; the fixed space is not one member of a pair of fields. The reading of the two eigenspaces as the two signs of a charge-conjugation eigenvalue belongs to the companion articles, where that operator is constructed; on the algebra the two eigenspaces are one space and its rotation by $i$, and the equation of the display above does not distinguish them.

**No vector current.** A Dirac field carries the current of the two-sided form, $i[\tilde{Ξ}^*(\tilde\nabla_\Phi\tilde{Ξ})-(\tilde\nabla_\Phi\tilde{Ξ}^*)\tilde{Ξ}]$ in the products of *Product and Form Conventions*; a field equal to its conjugate has no independent second factor to put there, and the bilinear collapses. The statement is qualitative here and computed in the companion articles; what the algebra supplies is the reason, which is that the fixed space is real and the current needs a phase.

## Solutions and the Counting of States

**A single plane wave is never a solution.** The corpus's ansatz is $\tilde{Ξ}=\tilde{Ξ}_{0}\exp(i\theta_{\mathrm{cen}})$ with $\theta_{\mathrm{cen}}=\mathrm{Sc}(\tilde P_{\Phi}\tilde Q^{\natural})$ and $\tilde P_{\Phi}=ik_{t}^{\prime}e_t+\vec k_\Phi$ (*The Dirac Equation in Biquaternionic Form*). On it the derivative of the display is the left multiplication by the element $k_{t}^{\prime}e_t+i\vec k_\Phi$, and the coefficient conjugation conjugates the phase, so the two sides of an antilinear equation carry $\exp(+i\theta_{\mathrm{cen}})$ and $\exp(-i\theta_{\mathrm{cen}})$ and cannot match. The solutions are therefore two-frequency superpositions,

Here $\theta_{\mathrm{cen}}$ is the central phase: it is the argument of a unit complex number, so it is real.

$$
\tilde{Ξ}=\tilde{Ξ}_{0}\exp(i\theta_{\mathrm{cen}})+\tilde{Ξ}_{1}\exp(-i\theta_{\mathrm{cen}}) ,
$$

and the equation becomes a real linear system for the pair $(\tilde{Ξ}_{0},\tilde{Ξ}_{1})$ of amplitudes.

**The system.** Matching the two exponentials gives

$$
\bigl(k_{t}^{\prime}e_t+i\vec k_\Phi\bigr)\tilde{Ξ}_{0}=k_mi\,\overline{\tilde{Ξ}_{1}}\,\vec e_z ,
\qquad
-\bigl(k_{t}^{\prime}e_t+i\vec k_\Phi\bigr)\tilde{Ξ}_{1}=k_mi\,\overline{\tilde{Ξ}_{0}}\,\vec e_z ,
$$

sixteen real equations in the sixteen real parameters of the two amplitudes. The second line is the first with the sign of the amplitude reversed, which is what the two exponentials do to a derivative that is first order; the two lines are one equation and not two. Its nullity is the one tabulated in §*Why the Mass Sits on the Right*.

**The solution at fixed momentum.** On the shell the nullity is eight, and the projection onto the first amplitude is of rank eight: the amplitude $\tilde{Ξ}_{0}$ is free and the conjugate amplitude $\tilde{Ξ}_{1}$ is determined by it. The amplitude carries four real coefficients and the conjugate amplitude four more, which is the eight of the Dirac field; the counting of the previous section is the counting of one of the two.

**The shell.** Squaring the equation, and using that the product of the gradient with its quaternion conjugate is the d'Alembertian, gives $\Box_\Phi\tilde{Ξ}=k_m^{2}\tilde{Ξ}$ for each amplitude, so the solutions sit on the ordinary mass shell and the mass enters as the parameter of the dispersion and not as a normalisation. The computation is elementary and exact; its result is the first row of the nullity table. Here $k_m=mc/\hbar$ is the mass wave number, the inverse of the mass length.

**What the pair is not.** The pair is not a second equation. The two lines are the two exponentials of one equation, and a reader who counts them as two fields counts the field and its conjugate twice.

## What the Algebra Supplies, Transcribes, and Does Not Supply

The article's ledger, in the corpus's three categories.

| the item | status | where it stands |
|---|---|---|
| the equation as one element equation, derivative left and mass right through $\vec e_z$ | **supplied** | the display of §*The Equation and Its Three Forms*, and the nullity table |
| the coupling of the two letters by the mass, with one field | **supplied** | the pair of §*The Equation and Its Three Forms* |
| the count, four real coefficients against eight | **supplied** | the box of §*The Conjugation and the Count* |
| the neutrality, and the absence of a vector current | **supplied** | §*The Fixed Space and the Neutrality* |
| the two-frequency structure of the solutions, and the mass shell | **supplied** | §*Solutions and the Counting of States* |
| the propagation of the reality condition | **transcribed from the companions** | §*The Conjugation and the Count*, and the companions |
| the two-component form with the symplectic coefficient | **not supplied** | it needs the operator of the companion articles, and it is not restated here |
| the neutrino mass, the phases and the question whether a given fermion is Majorana | **outside the algebra** | the algebra cannot decide it |

The last two rows are the gaps the article leaves visible, and they are of different kinds. The two-component form is a transcription the companion articles perform and the algebra does not; the neutrino questions are not questions of the algebra at all, and no reading of the displays above answers them.

## Open Questions

- **A conjugation outside the sixteen.** The commutator was computed for the unit-conjugated forms and for the bar and the star. Whether a conjugation built from a general element, rather than from a unit, commutes with the equation and preserves a four-real fixed space is not settled here.
- **The descent of that condition.** The conjugation of the companion articles carries an operator of its own, and whether that operator has an element-level expression in the frame of this article is the natural question the count leaves open.
- **The sign of the mass on the two eigenspaces.** On the algebra the two eigenspaces of a conjugation are exchanged by $i$ and the equation does not distinguish them; the companions' reading gives them the two signs of the mass, and the translation between the two readings is not made here.
- **The ELKO reading.** The literature's class of self-conjugate fields with the opposite eigenvalue is a statement about the operator of the companion articles, and the algebra's count of four real coefficients is compatible with it without selecting it.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The generators carry no frame label: $\gamma_\mu$ is one set of matrices, and the frame is named on the coordinate.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\tilde{Ξ}=a\tilde{Ξ}$ and $R_b\tilde{Ξ}=\tilde{Ξ} b$, and $c(M)$ is the coefficient matrix of $M$ in the basis of the sixteen products.

$$
\gamma_0=iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_x},\quad \gamma_1=iL_{\mathrm{pau},\vec e_x}R_{\mathrm{pau},\vec e_y},\quad \gamma_2=iL_{\mathrm{pau},\vec e_y}R_{\mathrm{pau},\vec e_y},\quad \gamma_3=iL_{\mathrm{pau},\vec e_z}R_{\mathrm{pau},\vec e_y},\quad \gamma_5=-iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_z} .
$$

The same in the axis-free display:

$$
\gamma_0=iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_x},\quad \gamma_1=iL_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_y},\quad \gamma_2=iL_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y},\quad \gamma_3=iL_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y},\quad \gamma_5=-iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_z} .
$$

In the notation of the body the dictionary is one line: $\gamma_\mu=i c_\mu$ and $\gamma_5=\Gamma$. A single product is a pure tensor; the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$.

$\gamma_5$ is the reference-frame basis operator of the chirality $\Gamma$; the central grading $\chi=i\tilde{Ζ}_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module.

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

The Majorana equation is the relativistic equation of a field equal to its own conjugate, and its biquaternionic form is one element equation: the derivative acts from the left, and the mass from the right, through the spatial unit $\vec e_z$ and the coefficient conjugation,
$$i\frac{\partial\tilde{Ξ}}{\partial r'_t}+\sum_\eta\vec e_\eta\frac{\partial\tilde{Ξ}}{\partial R_\eta}-k_mi\,\bar{\tilde{Ξ}}\,\vec e_z=0 .$$
The three forms of the literature are three readings of it and not three laws. Read on the two letters it is a pair, each member acting on one letter and carrying the conjugate of the other, which is the chiral pair with one field and no second one. Read on the fixed space of the coefficient bar it is a real equation on four real coefficients.

The mass sits in the right slot and not in the left, and that is a statement about letters: left multiplication keeps the letter of its operand, so a mass written as a left action is diagonal on the letters and couples nothing; a right multiplication takes the letter of its factor and couples them. The nullity table is the measurement: the mass from the right has eight real solutions on the timelike shell and none on the spacelike one, a bare conjugation has none on the timelike shell and eight on the spacelike one, and the star has none and four.

The conjugation carried by the mass term is $\tilde{Ξ}\mapsto\bar{\tilde{Ξ}}\vec e_z$, and it is a square root of minus one, not an involution: no field equals its own conjugate under it, and the two-sided form pairs the field with a second field of the same size. The involutions the algebra supplies are the coefficient bar, the star, and the unit-conjugated conjugations that exchange the two letters; each has a fixed space of four real dimensions, and the count is four against eight, with the two eigenspaces exchanged by the central $i$. None of them commutes with the equation, so the fixed space is not preserved by the flow and the reality condition is not propagated at the level of the algebra; the condition that is propagated is built on the state space, where the conjugation carries an operator of its own.

A field equal to its conjugate carries no continuous phase, and a continuous phase is what a conserved charge is; the neutrality is a property of the conjugation and not a truncation of the algebra. A single plane wave is never a solution, because the conjugation conjugates the phase; the solutions are two-frequency superpositions whose amplitude and conjugate amplitude carry four real coefficients each, and the shell is the ordinary one. Whether a given fermion is a Majorana fermion, and the neutrino mass and phases, are outside the algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde{Ξ}$, $\tilde Q$ | The field, and a general element of $\mathbb{B}$ |
| $\tilde{Ξ}_{L}$, $\tilde{Ξ}_{R}$ | The two letters; the $-1$ and $+1$ parts under $\tilde{Ξ}\mapsto-i\tilde{Ξ}\vec e_z$ |
| $e_t$, $\vec e_x$, $\vec e_y$, $\vec e_z$ | The units of the algebra; $\vec e_z$ is the unit whose right multiplication reads the letter |
| $\bar\cdot$ | The coefficient conjugation: an automorphism, antilinear over $\mathbb{C}$, an involution |
| ${}^{*}$ | The Hermitian conjugation: an anti-automorphism, antilinear, an involution |
| $\tilde\nabla_\Phi$, $\Box_\Phi$ | The gradient and the d'Alembertian in the material reading, as the series fixes them |
| $\mathbb{B}_{\Phi}$ | The frame with $Q_t=i q'_t$ and $g_{tt}=-c^{2}$ |
| $\theta_{\mathrm{cen}}$, $\tilde P_{\Phi}$ | The phase $\mathrm{Sc}(\tilde P_{\Phi}\tilde Q^{\natural})$ and the momentum element $ik_{t}^{\prime}e_t+\vec k_\Phi$ |
| $k_{t}^{\prime}e_t+i\vec k_\Phi$ | The derivative of the display on $\exp(i\theta_{\mathrm{cen}})$, as a left multiplication |
| $\tilde{Ξ}_{0}$, $\tilde{Ξ}_{1}$ | The amplitudes of $\exp(i\theta_{\mathrm{cen}})$ and $\exp(-i\theta_{\mathrm{cen}})$ |
| $\mathcal{C}(\tilde{Ξ})=\bar{\tilde{Ξ}}\vec e_z$ | The conjugation of the mass term; $\mathcal{C}^{2}=-1$ |
| $a\,\bar{\tilde{Ξ}}\,b$ | The unit-conjugated conjugations; ten of the sixteen are involutions |
| four real dimensions | The fixed space of every antilinear involution on $\mathbb{B}$ |
| $8$ against $4$ | The real coefficients of a Dirac field and of a Majorana field |
| the nullity table | $8$ and $0$ for the mass from the right; $0$ and $8$ for the bare conjugation; $0$ and $4$ for the star |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html), for the two-sided form, the plane-wave ansatz and the mass shell used here.
- [The Neutrino and Majorana Fermions in Biquaternionic Form](the-neutrino-and-majorana-fermions-in-biquaternionic-form.html), for the charge conjugation on the state space and the condition that is propagated there.
- [Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form](antilinear-structure-and-the-two-kinds-of-mass-in-biquaternionic-form.html), for the diagnosis of the retired equation and the dispersion table that separates the two pairings.
- E. Majorana, "Teoria simmetrica dell'elettrone e del positrone," *Nuovo Cimento* **14** (1937) 171–184, for the original equation and the real form of the Dirac theory.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), Chapter 2 and Appendix A, for the charge-conjugation matrix, the Majorana condition and the conventions used here.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), Chapter 5, for the charge-conjugation operator and its two eigenstates.
- P. B. Pal, "Dirac, Majorana, and Weyl fermions," *American Journal of Physics* **79** (2011) 485–498, for the counting of components and the neutrality of the Majorana field.
- A. Aste, "A direct road to Majorana fields," *Symmetry* **2** (2010) 1776–1809, for the two-component construction and the symplectic group $\mathrm{Sp}(2,\mathbb{C})$ as the double cover of the Lorentz group.
- E. Marsch, "On the Majorana equation: relations between its complex two-component and real four-component eigenfunctions," *ISRN Mathematical Physics* **2012** (2012) 760239, for the two-component and four-component eigenfunctions and their relation.
- P. Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the Lounesto classification and the class-5 (ELKO-type) field with the charge-conjugation eigenvalue $-1$.
- D. V. Ahluwalia and D. Grumiller, "Spin-half fermions with mass dimension one: theory, phenomenology, and dark matter," *Journal of Cosmology and Astroparticle Physics* **0507** (2005) 012, for the ELKO field and its properties.
- H. B. Lawson and M.-L. Michelsohn, *Spin Geometry* (Princeton, 1989), and P. Budinich and A. Trautman, *The Spinorial Chessboard* (Springer, 1988), for the real, complex and quaternionic types of Clifford modules and the reality of the generators by signature.
