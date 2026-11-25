# __The Lagrangian and the Scalar Matrix: One Field, One Commutator, Two Quartics__

## Introduction

**The question.** What is the scalar piece of the $\mathrm{SU}(4)$ action, written once, and what does it imply?

**The answer.**

$$
\boxed{\;\mathcal{L}_{\Phi}=\operatorname{tr}\bigl(D_{\imath}\Phi\bigr)^{\dagger}\bigl(D_{\imath}\Phi\bigr)-V(\Phi),
\qquad
D_{\imath}\Phi=\partial_{\imath}\Phi-ig_4\sum_{a=1}^{15}A_{a,\imath}\bigl[T_{a},\Phi\bigr].\;}
$$

**One field, one commutator, two quartics.** The commutator is what a matrix index forces; the two quartics are what a matrix admits; and the one coupling is the same $g_4$ that multiplies the curvature.

**What this article does.** It writes the piece, expands it, derives the field equation and the constraint, counts the equations against the components, and computes the four numbers the piece implies: fifteen trilinear vertices, one hundred and twenty quadrilinear ones, a rank-six vector mass matrix, and a kinetic normalisation of one.

**What it does not do.** It does not discuss the potential's minima — [The Primordial Potential](the-primordial-potential-one-symmetric-minimum-above-m-c.html) does — and it does not derive the Yukawa piece, which is [The Lagrangian and the Sixteen](the-lagrangian-and-the-sixteen-kinetic-term-and-yukawa-coupling.html)'s. **The full display, with all four pieces at once, is [The Lagrangian and the Primordial Force](the-lagrangian-and-the-primordial-force.html)'s**, and this article is the scalar piece of it at working size.

## The Piece, and Why Each Symbol Is There

**The covariant derivative acts by commutation because $\Phi$ carries one colour index of each kind.**

$$
\Phi\mapsto U\Phi U^{\dagger}
\qquad\Longrightarrow\qquad
D_{\imath}\Phi=\partial_{\imath}\Phi-ig_4A_{a,\imath}\bigl(T_{a}\Phi-\Phi T_{a}\bigr).
$$

**A field in the fundamental would have $T_{a}\Phi$ and no second term.** The second term is the price of the matrix index, and the matrix index is what the mass operator needs: $\bar\xi\Phi\xi$ is a singlet only for $\Phi\in\bar{\mathbf4}\otimes\mathbf4=\mathbf{15}\oplus\mathbf1$, while $\mathbf4\otimes\mathbf4=\mathbf6\oplus\mathbf{10}$ has no $\bar{\mathbf4}$.

**The trace is the only invariant of degree two.** $\operatorname{tr}\Phi^{\dagger}\Phi$ is invariant under $\Phi\to U\Phi U^{\dagger}$ by cyclicity, and it is the sum of the absolute squares of the sixteen entries. **There is no second one**: $\operatorname{tr}\Phi^{2}$ vanishes for the traceless part only in special bases and is not real in general, and $\operatorname{tr}\Phi^{\dagger}\Phi^{\dagger}$ is not invariant.

**No factor of $\tfrac12$ appears, unlike the curvature's $\tfrac14$.** The reason is the normalisation $\operatorname{tr}(t_{a}t_{b})=\tfrac12\delta_{ab}$: the curvature is built from an anti-Hermitian object whose square has a factor $2$ to absorb, and the scalar bilinear has none. **The two normalisations are checked in [The Lagrangian and the Primordial Force](the-lagrangian-and-the-primordial-force.html) against the printed arrays**, where the corner direction carries trace norm $12$ and sets the coefficient.

**Nothing is summed but the colour indices.** $\Phi$ carries one lower and one upper colour index and no other label, so the trace over colour is the whole of the contraction, and the sixteen real components are the algebra's $15+1$.

## The Expansion

**Four kinds of term, counted.**

$$
\operatorname{tr}\bigl(D_{\imath}\Phi\bigr)^{\dagger}\bigl(D_{\imath}\Phi\bigr)
=
\underbrace{\operatorname{tr}\partial_{\imath}\Phi^{\dagger}\partial_{\imath}\Phi}_{\text{kinetic}}
\underbrace{-ig_4A_{a,\imath}\operatorname{tr}\bigl(\partial_{\imath}\Phi^{\dagger}[T_{a},\Phi]-[T_{a},\Phi]^{\dagger}\partial_{\imath}\Phi\bigr)}_{\text{one gauge field}}
\underbrace{+g_4^{2}A_{a,\imath}A_{b,\imath}\operatorname{tr}\bigl([T_{a},\Phi]^{\dagger}[T_{b},\Phi]\bigr)}_{\text{two gauge fields}} .
$$

**The counts follow from the indices and not from a diagram.**

| term | what it is | how many distinct vertices |
| --- | --- | --- |
| $\Phi^{\dagger}\Phi\,\partial\partial$ | the propagator | $1$ |
| $A\,\Phi^{\dagger}\partial\Phi$ | one generator per vertex | $15$ |
| $A A\,\Phi^{\dagger}\Phi$ | a symmetric pair $(a,b)$ per vertex | $\tfrac{15\cdot16}{2}=120$ |
| $V(\Phi)$ | three coefficients | $3$ |

**One hundred and twenty is the number that a quartet reading would have got wrong in the other direction**: a quartet couples to all fifteen generators too, so the trilinear count is the same, but the quadrilinear count differs because the commutator's structure constants enter. **The count of pairs, $15\cdot16/2=120$, is the count of symmetric $15\times15$ matrices and is fixed by the group alone.**

## The Field Equation

**Vary $\Phi^{\dagger}$ and the commutator appears twice.**

$$
D_{\imath}D_{\imath}\Phi+\frac{\partial V}{\partial\Phi^{\dagger}}=0,
\qquad
\frac{\partial V}{\partial\Phi^{\dagger}}=\mu_{\Phi}^{2}\Phi+2\lambda_{1}\Phi\Phi^{\dagger}\Phi+2\lambda_{2}\bigl(\operatorname{tr}\Phi^{\dagger}\Phi\bigr)\Phi .
$$

**The derivative of the potential is a matrix and not a number**, and that is the difference between this field and a quartet: $\partial V/\partial\Phi^{\dagger}$ carries the same two indices as $\Phi$, so the equation is an equation between matrices and holds entry by entry.

**The two quartics produce two different cubic terms in the equation of motion.** $\Phi\Phi^{\dagger}\Phi$ is a matrix product of three factors; $(\operatorname{tr}\Phi^{\dagger}\Phi)\Phi$ is a number times the field. **A potential with one quartic would have only the second kind**, and the difference is what makes the model's vacuum shape a dynamical question.

**The covariant derivative is the commutator, so the equation is a matrix equation with a connection.** Its flat-space limit is not a wave equation with a potential but a wave equation with a connection, and the difference is the whole of the gauge–scalar coupling.

## The Constraint

**The temporal component of the gauge equation is a Gauss law, and the scalar contributes to its charge.**

$$
D_{\imath}F_{a,0\imath}=j_{a,0},
\qquad
j^{\Phi}_{a,0}=ig_4\sum_{\alpha=1}^{2}\operatorname{tr}\Bigl(\bigl(D_{0}\Phi\bigr)^{\dagger}\bigl[T_{a},\Phi\bigr]\Bigr).
$$

**The scalar current is quadratic in $\Phi$ above $M_C$ and linear below it**, because only below the transition is there a $\langle\Phi\rangle$ to split off. **That shift is the whole mechanism of the vector masses**: with $\Phi=\Phi_{0}+\varphi$ the quadratic term produces a piece linear in $\varphi$, and a piece linear in the fluctuation is what a mass term is.

**The current is conserved covariantly and not ordinarily.** $D_{\imath}j_{\imath}=0$ follows from the invariance of the action; $\partial_{\imath}j_{\imath}=0$ does not, because of the $[A_{\imath},j_{\imath}]$ term. **So no gauge charge exists above $M_C$**, exactly as in the strong sector, and the corpus's charge theorem below $M_C$ is a statement about the residual group and not about this one.

## The Count of Components Against the Count of Equations

**Sixteen real components and sixteen real equations, and the counting is one to one.**

| statement | count |
| --- | --- |
| real components of $\Phi$ | $16$ |
| independent real equations | $16$ |
| on-shell real degrees of freedom | $16$ before any eating |

**The reason there is nothing to halve is Hermiticity.** The field is Hermitian, so varying with respect to $\Phi$ and varying with respect to $\Phi^{\dagger}$ give the *same* equation and not a conjugate pair; the sixteen equations are sixteen and not half of thirty-two. **A complex matrix would have needed the dagger to be tracked separately**, and that is one more reason the physical field is the Hermitian one.

**Below $M_C$ the count changes and the arithmetic is the census's.** Six components become the longitudinal modes of six vectors, and the count of physical scalars falls to ten. **The two numbers, sixteen and ten, are the same field counted in two phases**, and [The Scalar Content](the-scalar-content-one-matrix-and-ten-survivors.html) does the second count.

## The Vector Mass Matrix, Read as a Gram Matrix

**At a vacuum $\Phi_{0}=v_C D$ the quadrilinear term is the only one that survives, and it is a Gram matrix.**

$$
M^{2}_{ab}=g_4^{2}\operatorname{tr}\Bigl(\bigl[T_{a},v_CD\bigr]^{\dagger}\bigl[T_{b},v_CD\bigr]\Bigr)
=g_4^{2}v_C^{2}\,\bigl\langle[T_{a},D],[T_{b},D]\bigr\rangle .
$$

**The matrix is the Gram matrix of fifteen vectors in a fifteen-dimensional space**, so its rank is the dimension of the span of $\{[T_{a},D]\}$ — which is the number of generators that do not commute with $D$.

**Fifteen generators, nine commuting with $D$, so six vectors span.** Therefore $\operatorname{rank}M^{2}=6$ and $\ker M^{2}$ has dimension $15-6=9$. **The nine zero eigenvalues are the nine massless vectors**, and the six nonzero ones are the leptoquarks. **This is the vector mass spectrum derived from the scalar kinetic term and from nothing else**, and it agrees with the breaking article's generator-by-generator computation.

**The kernel is a subalgebra.** If $[D,X]=[D,Y]=0$ then $[D,[X,Y]]=0$ by Jacobi, so $\ker\operatorname{ad}(D)$ is closed under commutation. **That is why the nine massless vectors form the group they do**, and it is the reason the residual group is $\mathrm{U}(3)$ rather than an arbitrary nine-dimensional subspace.

**One number the Gram matrix fixes.** With the corpus's normalisation the nonzero eigenvalues are equal, $M_X^{2}=\tfrac12g_4^{2}v_C^{2}$, and the ratio to the right-handed vector's mass is $\sqrt2$ times a coupling ratio. **The Gram matrix gives equality; the $\sqrt2$ is the group's**, and [The Six Leptoquarks](six-leptoquarks-above-m-c-quantum-numbers-mass-and-the-bound.html) carries it.

## What the Piece Does Not Contain

**Five absences, each with the article where it is supplied.**

- *No mass term.* $\mu_{\Phi}^{2}$ is a coefficient of the potential, and a mass for the fifteen is forbidden by gauge invariance.
- *No second scale.* The piece has $g_4$ and no other coupling; $v_C$ is the potential's.
- *No Yukawa.* The fermion–scalar vertex $y\bar\xi\Phi\xi$ is a separate piece and a separate matrix.
- *No second colour contraction.* The trace is the only invariant of degree two, so no second kinetic structure is available.
- *No loop.* The piece is classical, and the one-loop correction is [The One-Loop Effective Potential](the-one-loop-effective-potential-of-the-scalar-matrix-at-sixteen-real-components.html)'s.

## The Checks

| claim | check | result |
| --- | --- | --- |
| trilinear vertices | one per generator | $15$ |
| quadrilinear vertices | symmetric pairs $(a,b)$ | $120$ |
| the derivative of the potential | a matrix with $\Phi$'s indices | entry by entry |
| real equations | one per real component | $16$ |
| on-shell real scalars above $M_C$ | $16-0$ | $16$ |
| the vector mass matrix | a Gram matrix of $[T_{a},D]$ | rank $6$ |
| massless vectors at $M_C$ | $15-\operatorname{rank}$ | $9$ |
| the kernel | $\ker\operatorname{ad}(D)$, closed by Jacobi | a subalgebra |
| the trace normalisation | corner direction, trace norm $12$ | coefficient fixed, no parameter |

## Summary

**One field of sixteen real components, one commutator, two quartics, one coupling.** The commutator is forced by the matrix index, the two quartics by the matrix's contractions, and the coupling is the same $g_4$ as everywhere else in the display.

**Four numbers come out of the piece and not out of a diagram**: fifteen trilinear vertices, one hundred and twenty quadrilinear ones, sixteen independent real equations, and a vector mass matrix of rank six whose kernel is nine-dimensional and closed.

**The scalar current is quadratic above $M_C$ and linear below it**, and that change of degree is the mechanism of the vector masses: a term linear in the fluctuation of the vacuum is what a mass term is, and above the transition there is no fluctuation to be linear in.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\Phi$ | the Hermitian scalar matrix, $16$ real components |
| $D_{\imath}\Phi$ | $\partial_{\imath}\Phi-ig_4[A_{a,\imath}T_{a},\Phi]$, the commutator form |
| $V(\Phi)$ | $\mu_{\Phi}^{2}\operatorname{tr}\Phi^{2}+\lambda_{1}\operatorname{tr}\Phi^{4}+\lambda_{2}(\operatorname{tr}\Phi^{2})^{2}$ |
| $j^{\Phi}_{a,\imath}$ | the scalar current, $ig_4\operatorname{tr}((D_{\imath}\Phi)^{\dagger}[T_{a},\Phi])$ |
| $M^{2}_{ab}$ | the vector mass matrix, a Gram matrix of $[T_{a},D]$ |
| $D$ | $\operatorname{diag}(-3,1,1,1)$, the declared vacuum's shape |

## Further Reading

- [The Lagrangian and the Primordial Force](the-lagrangian-and-the-primordial-force.html). The same piece inside the full display, with the four pieces and the ceiling.
- [The Primordial Potential](the-primordial-potential-one-symmetric-minimum-above-m-c.html). $V(\Phi)$'s minima, its boundedness cone and the declared vacuum's status.
- [The Breaking of the Primordial Force](the-breaking-of-the-primordial-force-and-the-mass-of-the-six-leptoquarks.html). The Gram matrix computed generator by generator.
- [The One-Loop Effective Potential](the-one-loop-effective-potential-of-the-scalar-matrix-at-sixteen-real-components.html). The correction to this classical piece.
