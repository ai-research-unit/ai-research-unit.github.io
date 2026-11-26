# __The Lagrangian and the Scalar Matrix: One Field, One Commutator, Four Quartics__

## Introduction

**The question.** What is the scalar piece of the $\mathrm{SU}(4)$ action, written once, and what does it imply?

**The answer.**

$$
\boxed{\;\mathcal{L}_{\Phi}=\operatorname{tr}\bigl(D_{\imath}Ξ\bigr)^{\dagger}\bigl(D_{\imath}Ξ\bigr)-V(Ξ),
\qquad
D_{\imath}Ξ=\partial_{\imath}Ξ-ig_4\sum_{a=1}^{15}A_{a,\imath}\bigl[t_{a},Ξ\bigr].\;}
$$

**One field, one commutator, four quartics.** The commutator is what a matrix index forces; two of the quartics are what a matrix admits in its traceless part, and a vector admits only one; the trace adds two more quartics and a second quadratic; and the one coupling is the same $g_4$ that multiplies the curvature. **The title counts the quartic coefficients the display carries**, and the trace channel is the part of the potential that never rotates the field in colour space: its terms enter the field equation only through multiples of $\mathbb 1$ and of $Ξ$ itself.

**What this article does.** It writes the piece, expands it, derives the field equation and the constraint, counts the equations against the components, and computes the four numbers the piece implies: fifteen trilinear vertices, one hundred and twenty quadrilinear ones, a rank-six vector mass matrix, and a kinetic normalisation of one.

**What it does not do.** It does not discuss the potential's minima — [The Primordial Potential](the-primordial-potential-one-symmetric-minimum-above-m-c.html) does — and it does not derive the Yukawa piece, which is [The Lagrangian and the Sixteen](the-lagrangian-and-the-sixteen-kinetic-term-and-yukawa-coupling.html)'s. **The full display, with all four pieces at once, is [The Lagrangian and the Primordial Force](the-lagrangian-and-the-primordial-force.html)'s**, and this article is the scalar piece of it at working size.

## The Piece, and Why Each Symbol Is There

**The covariant derivative acts by commutation because $Ξ$ carries one colour index of each kind.**

$$
Ξ\mapsto UΞ U^{\dagger}
\qquad\Longrightarrow\qquad
D_{\imath}Ξ=\partial_{\imath}Ξ-ig_4A_{a,\imath}\bigl(t_{a}Ξ-Ξ t_{a}\bigr).
$$

**The $t_{a}$ are the normalised Hermitian generators of [The Lagrangian and the Primordial Force](the-lagrangian-and-the-primordial-force.html)'s §*The Normalisation*, $t_{a}=iG_{a}/2$ for the thirteen arrays of trace norm $2$, $t_{c_{3}}=i(d_{2}-d_{3})/\sqrt{12}$ and $t_{15}=iG_{15}/\sqrt{24}$, with $\operatorname{tr}(t_{a}t_{b})=\tfrac12\delta_{ab}$.** The printed arrays $G_{a}$ are anti-Hermitian, and the pair (Hermitian $t_{a}$, coupling $-ig_4$) is the one that keeps the three-point vertex nonzero: **with an anti-Hermitian generator and the same $i$, the two orderings of the cross term have equal trace and cancel, and the cubic term vanishes identically.** That is the one place where a change of basis silently deletes an interaction, and it is why this article and the parent article use the same pair.

**A field in the fundamental would have $t_{a}Ξ$ and no second term.** The second term is the price of the matrix index, and the matrix index is what the mass operator needs: $\bar\xiΞ\xi$ is a singlet only for $Ξ\in\bar{\mathbf4}\otimes\mathbf4=\mathbf{15}\oplus\mathbf1$, while $\mathbf4\otimes\mathbf4=\mathbf6\oplus\mathbf{10}$ has no $\bar{\mathbf4}$.

**The trace is the canonical invariant of degree two, and it is not the only one.** $\operatorname{tr}Ξ^{\dagger}Ξ$ is invariant under $Ξ\to UΞ U^{\dagger}$ by cyclicity, and it is the sum of the absolute squares of the sixteen entries; for a Hermitian $Ξ$ it equals the real $\operatorname{tr}Ξ^{2}$. **$(\operatorname{tr}Ξ)^{2}$ is a second and independent invariant**, and it is why the potential needs two quadratics. **In the kinetic term the second one is removable**: writing $Ξ=h+\tfrac{t}{4}\mathbb 1$ with $h$ traceless gives $\operatorname{tr}(\partial Ξ)^{2}=\operatorname{tr}(\partial h)^{2}+\tfrac14(\partial t)^{2}$, so a term $b\,(\partial\operatorname{tr}Ξ)^{2}$ is absorbed by rescaling the singlet, and only the singlet is rescaled. **That is why one kinetic coefficient suffices and two quadratic coefficients do not**, with the qualification that this is a field redefinition and not an absence: **the same rescaling moves the potential's trace coefficients**, $\mu_{2}^{2}\to\mu_{2}^{2}/(1+4b)$, $\lambda_{3}\to\lambda_{3}/(1+4b)$ and $\lambda_{4}\to\lambda_{4}/(1+4b)^{2}$, so the six coefficients counted below are quoted in the basis where the kinetic term is canonical.

**No factor of $\tfrac12$ appears, unlike the curvature's $\tfrac14$.** The reason is the normalisation $\operatorname{tr}(t_{a}t_{b})=\tfrac12\delta_{ab}$: the curvature is an algebra element squared and its trace supplies a $\tfrac12$, and the scalar bilinear is a trace of two fields and supplies none. **The two normalisations are checked in [The Lagrangian and the Primordial Force](the-lagrangian-and-the-primordial-force.html) against the printed arrays**, where the corner direction carries trace norm $12$ and sets the coefficient.

**Nothing is summed but the colour indices.** $Ξ$ carries one lower and one upper colour index and no other label, so the trace over colour is the whole of the contraction, and the sixteen real components are the algebra's $15+1$.

**The potential, with all four quartic coefficients written.**

$$
V(Ξ)=\mu_{\Phi}^{2}\operatorname{tr}Ξ^{2}+\mu_{2}^{2}(\operatorname{tr}Ξ)^{2}
+\underbrace{\lambda_{1}\operatorname{tr}Ξ^{4}+\lambda_{2}(\operatorname{tr}Ξ^{2})^{2}}_{\text{traceless channel}}
+\underbrace{\lambda_{3}(\operatorname{tr}Ξ)^{2}\operatorname{tr}Ξ^{2}+\lambda_{4}(\operatorname{tr}Ξ)^{4}}_{\text{trace channel}} .
$$

**Two quadratics and four quartics, six coefficients in all, which is the scalar sector's count in [The Lagrangian and the Primordial Force](the-lagrangian-and-the-primordial-force.html).** The traceless pair is the one the commutator and the field equation can tell apart, since $\lambda_{1}$ multiplies a matrix product and $\lambda_{2}$ a number times the field; the trace pair multiplies only scalars, so it shifts the equation without rotating the field in colour space.

**The fifth quartic and the three cubics are absent and not forbidden.** $\operatorname{tr}Ξ^{3}\operatorname{tr}Ξ$ is invariant and of degree four, and $\operatorname{tr}Ξ^{3}$, $\operatorname{tr}Ξ^{2}\operatorname{tr}Ξ$ and $(\operatorname{tr}Ξ)^{3}$ are invariant and of degree three; the model drops them all, and dropping them is a choice of coefficients — zero — rather than a property of the group. **The cubics are odd under $Ξ\to-Ξ$, so a potential even in the field removes those three and does not touch the quartic.** **The count of what the group allows is five quartics and three cubics**, and the article writes four quartics and no cubic. **The four are exactly those built from $Ξ^{2}$ and $\operatorname{tr}Ξ$**: $\operatorname{tr}Ξ^{4}=\operatorname{tr}(Ξ^{2}Ξ^{2})$, $(\operatorname{tr}Ξ^{2})^{2}$, $(\operatorname{tr}Ξ)^{2}\operatorname{tr}Ξ^{2}$ and $(\operatorname{tr}Ξ)^{4}$, while the dropped one needs $Ξ^{3}$. **That is the rule the corpus follows and it is a declaration of zero coefficients**, not a symmetry: the group allows all five. **The boundedness cone in [The Primordial Potential](the-primordial-potential-one-symmetric-minimum-above-m-c.html) is the cone for this potential with $\lambda_{5}=0$**, which is the potential written here; a nonzero $\lambda_{5}$ would need a row of its own there.

## The Expansion

**Four kinds of term, counted.**

$$
\operatorname{tr}\bigl(D_{\imath}Ξ\bigr)^{\dagger}\bigl(D_{\imath}Ξ\bigr)
=
\underbrace{\operatorname{tr}\partial_{\imath}Ξ^{\dagger}\partial_{\imath}Ξ}_{\text{kinetic}}
\underbrace{-2ig_4A_{a,\imath}\operatorname{tr}\bigl(\partial_{\imath}Ξ\,[t_{a},Ξ]\bigr)}_{\text{one connection}}
\underbrace{+g_4^{2}A_{a,\imath}A_{b,\imath}\operatorname{tr}\bigl([t_{a},Ξ]^{\dagger}[t_{b},Ξ]\bigr)}_{\text{two connections}} .
$$

**The counts follow from the indices and not from a diagram.**

| term | what it is | how many distinct vertices |
| --- | --- | --- |
| $Ξ^{\dagger}Ξ\,\sum_{\imath}\varepsilon_{\imath}\partial_{\imath}\partial_{\imath}$ | the propagator | $1$ |
| $A\,Ξ^{\dagger}\partialΞ$ | one generator per vertex | $15$ |
| $A A\,Ξ^{\dagger}Ξ$ | a symmetric pair $(a,b)$ per vertex | $\tfrac{15\cdot16}{2}=120$ |
| $V(Ξ)$ | two quadratics, four quartics | $6$ |

**One hundred and twenty is the number a quartet reading gives differently, and the difference is an index count and not a structure constant.** A quartet couples to all fifteen generators, so its trilinear count is also fifteen; its quadrilinear term is $g_4^{2}A_{a}A_{b}\,\phi^{\dagger}t_{a}t_{b}\phi=g_4^{2}A_{a}A_{b}\tfrac12\delta_{ab}\lvert\phi\rvert^{2}$, **diagonal in $(a,b)$ and therefore fifteen vertices and not one hundred and twenty.** The matrix's term is $g_4^{2}A_{a}A_{b}\operatorname{tr}([t_{a},Ξ]^{\dagger}[t_{b},Ξ])$, **which is not diagonal, because $[t_{a},Ξ]$ and $[t_{b},Ξ]$ are independent anti-Hermitian matrices for $a\ne b$.** The structure constants enter the value of a matrix vertex once $Ξ$ is expanded in generators; **they do not enter the count, which is the count of symmetric $15\times15$ pairs, $15\cdot16/2=120$, and is fixed by the group alone.**

## The Field Equation

**Vary $Ξ^{\dagger}$ and the commutator appears twice.**

$$
\sum_{\imath}\varepsilon_{\imath}D_{\imath}D_{\imath}Ξ+\frac{\partial V}{\partialΞ^{\dagger}}=0,
\qquad
\frac{\partial V}{\partialΞ^{\dagger}}=\Bigl(\mu_{\Phi}^{2}+2\lambda_{2}\operatorname{tr}Ξ^{2}+\lambda_{3}(\operatorname{tr}Ξ)^{2}\Bigr)Ξ+2\lambda_{1}ΞΞ^{\dagger}Ξ+\Bigl(\mu_{2}^{2}\operatorname{tr}Ξ+\lambda_{3}\operatorname{tr}Ξ\operatorname{tr}Ξ^{2}+2\lambda_{4}(\operatorname{tr}Ξ)^{3}\Bigr)\mathbb 1 .
$$

**The derivative of the potential is a matrix and not a number**, and that is the difference between this field and a quartet: $\partial V/\partialΞ^{\dagger}$ carries the same two indices as $Ξ$, so the equation is an equation between matrices and holds entry by entry.

**The trace terms shift the equation and never rotate it.** The pieces carrying an unpaired $\operatorname{tr}Ξ$ give multiples of $\mathbb 1$; the pieces carrying $(\operatorname{tr}Ξ)^{2}\Xi$ or $\operatorname{tr}Ξ^{2}\,\Xi$ rescale the matrix part without rotating it in colour space. **That is why the trace channel changes masses and never the breaking pattern**: a shift of $Ξ$ by $c\,\mathbb 1$ commutes with all fifteen generators, so the sector never sees it.

**The two quartics of the traceless part produce two different cubic terms in the equation of motion.** $ΞΞ^{\dagger}Ξ$ is a matrix product of three factors; $(\operatorname{tr}Ξ^{\dagger}Ξ)Ξ$ is a number times the field. **A potential with one quartic would have only the second kind**, and the difference is what makes the model's vacuum shape a dynamical question. **The two trace quartics add no third kind**: they produce $(\operatorname{tr}Ξ)^{2}Ξ$ and $(\operatorname{tr}Ξ)^{2}\operatorname{tr}Ξ^{2}\,\mathbb 1$, a rescaling and a shift, and neither is a matrix product.

**The covariant derivative is the commutator, so the equation is a matrix equation with a connection.** Its flat-space limit is not a wave equation with a potential but a wave equation with a connection, and the difference is the whole of the gauge–scalar coupling.

## The Constraint

**The temporal component of the gauge equation is a Gauss law, and the scalar contributes to its charge.**

$$
\sum_{\imath}\varepsilon_{\imath}D_{\imath}F_{a,t\imath}=j^{Ξ}_{a,t},
\qquad
j^{Ξ}_{a,t}=-2ig_4\operatorname{tr}\Bigl(\bigl(D_{t}Ξ\bigr)\bigl[t_{a},Ξ\bigr]\Bigr).
$$

**The current here carries its own power of $g_4$, so the equation has none on the left**; [The Lagrangian and the Primordial Force](the-lagrangian-and-the-primordial-force.html) factors the same $g_4$ out and writes $\sum_{\imath}\varepsilon_{\imath}D_{\imath}F_{a,t\imath}=-g_4j^{Ξ}_{a,t}$ with the $g_4$ removed from $j$. **One convention or the other, and never both.**

**The factor $2$ is the commutator's two orderings and the $i$ is the one in the covariant derivative.** The derivative of the kinetic term with respect to $A_{a,t}$ is $-2ig_4\operatorname{tr}((D_{t}Ξ)[t_{a},Ξ])$: the two cross terms are equal and add rather than cancel, **because $(D_{t}Ξ)^{\dagger}=D_{t}Ξ$: the dagger flips the sign of the anti-Hermitian factor $[t_{a},Ξ]$ and leaves the Hermitian one alone, so both terms read $-ig_4\operatorname{tr}((D_{t}Ξ)[t_{a},Ξ])$.** **The product is purely imaginary, since $(D_{t}Ξ)$ is Hermitian and $[t_{a},Ξ]$ is anti-Hermitian, so the current is real and the $i$ is not a sign error.** A current written with one $i$, one power of $g_4$ and no $2$ is off by a factor two on every emission.

**The scalar current is quadratic in $Ξ$ above $M_C$ and linear below it**, because only below the transition is there a $\langleΞ\rangle$ to split off. **That shift is the whole mechanism of the vector masses**: with $Ξ=Ξ_{0}+\delta Ξ$ the quadratic term produces a piece linear in $\delta Ξ$, and a piece linear in the fluctuation is what a mass term is.

**The current is conserved covariantly and not ordinarily.** $D_{\imath}j_{\imath}=0$ follows from the invariance of the action; $\partial_{\imath}j_{\imath}=0$ does not, because of the $[A_{\imath},j_{\imath}]$ term. **So no gauge charge exists above $M_C$**, exactly as in the strong sector, and the corpus's charge theorem below $M_C$ is a statement about the residual group and not about this one.

## The Count of Components Against the Count of Equations

**Sixteen real components and sixteen real equations, and the counting is one to one.**

| statement | count |
| --- | --- |
| real components of $Ξ$ | $16$ |
| independent real equations | $16$ |
| on-shell real degrees of freedom | $16$ before any eating |

**The reason there is nothing to halve is Hermiticity.** The field is Hermitian, so varying with respect to $Ξ$ and varying with respect to $Ξ^{\dagger}$ give the *same* equation and not a conjugate pair; the sixteen equations are sixteen and not half of thirty-two. **A complex matrix would have needed the dagger to be tracked separately**, and that is one more reason the physical field is the Hermitian one.

**Below $M_C$ the count changes and the arithmetic is the census's.** Six components become the longitudinal modes of six vectors, and the count of physical scalars falls to ten. **The two numbers, sixteen and ten, are the same field counted in two phases**, and [The Scalar Content](the-scalar-content-one-matrix-and-ten-survivors.html) does the second count.

## The Vector Mass Matrix, Read as a Gram Matrix

**At a vacuum $Ξ_{0}=v_C D$ the quadrilinear term is the only one that survives, and it is a Gram matrix.**

$$
M^{2}_{ab}=g_4^{2}\operatorname{tr}\Bigl(\bigl[t_{a},v_CD\bigr]^{\dagger}\bigl[t_{b},v_CD\bigr]\Bigr)
=g_4^{2}v_C^{2}\,\bigl\langle[t_{a},D],[t_{b},D]\bigr\rangle .
$$

**The bracket is the pairing $\langle X,Y\rangle=\operatorname{tr}(X^{\dagger}Y)=-\operatorname{tr}(XY)$ on anti-Hermitian matrices**, which is what the display's $[t_{a},D]^{\dagger}[t_{b},D]$ already writes. **It is positive definite on that space**, since $\operatorname{tr}(X^{\dagger}X)=\lVert X\rVert^{2}$ is a sum of absolute squares; and positivity is what the rank statement below needs, because a Gram matrix is positive semi-definite only under such a pairing.

**The matrix is the Gram matrix of fifteen vectors in a fifteen-dimensional space**, so its rank is the dimension of the span of $\{[t_{a},D]\}$ — which is the number of generators that do not commute with $D$.

**Fifteen generators, nine commuting with $D$, so six vectors span.** Therefore $\operatorname{rank}M^{2}=6$ and $\ker M^{2}$ has dimension $15-6=9$. **The nine zero eigenvalues are the nine massless vectors**, and the six nonzero ones are the leptoquarks. **This is the vector mass spectrum derived from the scalar kinetic term and from nothing else**, and it agrees with the breaking article's generator-by-generator computation.

**The kernel is a subalgebra.** If $[D,X]=[D,Y]=0$ then $[D,[X,Y]]=0$ by Jacobi, so $\ker\operatorname{ad}(D)$ is closed under commutation. **That is why the nine massless vectors form the group they do**, and it is the reason the residual group is $\mathrm{U}(3)$ rather than an arbitrary nine-dimensional subspace.

**One number the Gram matrix fixes.** The nonzero eigenvalues are equal, $M_X^{2}=16g_4^{2}v_C^{2}$ with $Ξ_0=v_CD$ and $\operatorname{tr}(t_at_b)=\tfrac12\delta_{ab}$, and the ratio to the right-handed vector's mass is $\sqrt2$ times a coupling ratio. **The Gram matrix gives equality; the $\sqrt2$ is the group's**, and [The Six Leptoquarks](six-leptoquarks-above-m-c-quantum-numbers-mass-and-the-bound.html) carries it.

## What the Piece Does Not Contain

**Five absences, each with the article where it is supplied.**

- *No mass term.* $\mu_{\Phi}^{2}$ is a coefficient of the potential, and a mass for the fifteen is forbidden by local invariance.
- *No second scale.* The piece has $g_4$ and no other coupling; $v_C$ is the potential's.
- *No Yukawa.* The fermion–scalar vertex $y\bar\xiΞ\xi$ is a separate piece and a separate matrix.
- *No second kinetic structure.* $(\partial_{\imath}\operatorname{tr}Ξ)^{2}$ is a second invariant of degree two and one rescaling of the singlet absorbs it (§*The Piece*); the kinetic term therefore has one coefficient, while the potential's two quadratics are independent.
- *No loop.* The piece is classical, and the one-loop correction is [The One-Loop Effective Potential](the-one-loop-effective-potential-of-the-scalar-matrix-at-sixteen-real-components.html)'s.

## The Checks

| claim | check | result |
| --- | --- | --- |
| trilinear vertices | one per generator | $15$ |
| quadrilinear vertices | symmetric pairs $(a,b)$ | $120$ |
| the derivative of the potential | a matrix with $Ξ$'s indices | entry by entry |
| real equations | one per real component | $16$ |
| on-shell real scalars above $M_C$ | $16-0$ | $16$ |
| the vector mass matrix | a Gram matrix of $[t_{a},D]$ | rank $6$ |
| massless vectors at $M_C$ | $15-\operatorname{rank}$ | $9$ |
| the kernel | $\ker\operatorname{ad}(D)$, closed by Jacobi | a subalgebra |
| the trace normalisation | corner direction, trace norm $12$ | coefficient fixed, no parameter |

## Summary

**One field of sixteen real components, one commutator, four quartics, one coupling.** The commutator is forced by the matrix index, two of the quartics by the matrix's two contractions in the traceless part, the other two and a second quadratic by the singlet that no condition removes, and the coupling is the same $g_4$ as everywhere else in the display. **The trace terms are the ones a reader is most likely to miss**, and they change only the scalar's mass matrix, never the vector's.

**Four numbers come out of the piece and not out of a diagram**: fifteen trilinear vertices, one hundred and twenty quadrilinear ones, sixteen independent real equations, and a vector mass matrix of rank six whose kernel is nine-dimensional and closed.

**The scalar current is quadratic above $M_C$ and linear below it**, and that change of degree is the mechanism of the vector masses: a term linear in the fluctuation of the vacuum is what a mass term is, and above the transition there is no fluctuation to be linear in.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $Ξ$ | the Hermitian scalar matrix, $16$ real components |
| $D_{\imath}Ξ$ | $\partial_{\imath}Ξ-ig_4\sum_{a}A_{a,\imath}[t_{a},Ξ]$, the commutator form |
| $V(Ξ)$ | $\mu_{\Phi}^{2}\operatorname{tr}Ξ^{2}+\mu_{2}^{2}(\operatorname{tr}Ξ)^{2}+\lambda_{1}\operatorname{tr}Ξ^{4}+\lambda_{2}(\operatorname{tr}Ξ^{2})^{2}+\lambda_{3}(\operatorname{tr}Ξ)^{2}\operatorname{tr}Ξ^{2}+\lambda_{4}(\operatorname{tr}Ξ)^{4}$ |
| $j^{Ξ}_{a,\imath}$ | the scalar current, $-2ig_4\operatorname{tr}((D_{\imath}Ξ)[t_{a},Ξ])$ |
| $M^{2}_{ab}$ | the vector mass matrix, a Gram matrix of $[t_{a},D]$ |
| $D$ | $\operatorname{diag}(-3,1,1,1)$, the declared vacuum's shape |

## Further Reading

- [The Lagrangian and the Primordial Force](the-lagrangian-and-the-primordial-force.html). The same piece inside the full display, with the four pieces and the ceiling.
- [The Primordial Potential](the-primordial-potential-one-symmetric-minimum-above-m-c.html). $V(Ξ)$'s minima, its boundedness cone and the declared vacuum's status.
- [The Breaking of the Primordial Force](the-breaking-of-the-primordial-force-and-the-mass-of-the-six-leptoquarks.html). The Gram matrix computed generator by generator.
- [The One-Loop Effective Potential](the-one-loop-effective-potential-of-the-scalar-matrix-at-sixteen-real-components.html). The correction to this classical piece.
