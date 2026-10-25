# __The Generalized Polar Decomposition of a Biquaternion: Partial Isometries and the Null Cone__

## Introduction

Every biquaternion of non-vanishing norm has the Cartan pairing

$$
\tilde Q=\tilde H\tilde U,\qquad \tilde H=\sqrt{\tilde Q\tilde Q^{*}}\ \text{Hermitian positive},\qquad \tilde U=\tilde H^{-1}\tilde Q\ \text{unitary},
$$

the two-factor form of the polar word. The pairing stops at the zero-divisor cone: on the cone the norm vanishes, the modulus is zero, and no four-factor word exists. The two-factor form itself need not stop. The unitary factor can be replaced by a **partial isometry** and the positive definite factor by a **positive semidefinite** one, and the equation $\tilde Q=\tilde H\tilde U$ then has a solution for every element, including the zero divisors and the origin.

**The thesis.** Every biquaternion has exactly one generalized Cartan pairing once the two projections of the partial isometry and the range of the positive factor are fixed: the positive factor is the Hermitian square root $\tilde H=\sqrt{\tilde Q\tilde Q^{*}}$, the second factor is $\tilde U=\tilde H^{+}\tilde Q$, and the initial and final projections of $\tilde U$ are those of $\tilde Q$. On the complement of the cone the pair is the Cartan pairing. On the cone it degenerates in a precise way: a nonzero null element is a positive scalar times a partial isometry, $\tilde Q=\sigma\tilde U$, the positive factor is the scaled final projection $\tilde H=\sigma\tilde U\tilde U^{*}$, and both projections are rank-one Hermitian idempotents, the pure states of the algebra.

**What the extension buys.** The cone is the singular locus of the algebra, the $N$-degenerate set: an element is $N$-degenerate exactly when its norm vanishes, and then it is non-invertible, so every nonzero singular element is a zero divisor. The generalized pairing is therefore not a remedy for a rare accident; it is the polar decomposition of the whole algebra, and the classical pairing is its restriction to the $N$-regular set. The price is a loss of continuity: the positive factor extends continuously to the cone, the partial isometry does not, and the rank drop is exactly the discontinuity.

**What this article is not.** It is not the four-factor word. The scale, the phase, the boost and the rotor are not defined on the cone, and the generalized factors are not a regrouping of factors that do not exist. It is not a new decomposition off the cone: there it coincides with the Cartan pairing. It is not the operator polar decomposition of [The Polar Decomposition of an Operator of the Form](the-polar-decomposition-of-an-operator-of-the-form.html), which is a statement about a Tomita operator on a completion. It is the matrix polar decomposition read in the algebra, with the two projection conditions that make the singular case canonical.

## The Results Used

| result | established in | used here for |
|---|---|---|
| the matrix model and the transport of ${}^{*}$ to ${}^{\dagger}$ | *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*, §*The Representation* | the reduction of the theorem to matrices |
| the Cartan pairing on $\langle\tilde Q\rangle_{\natural}\neq0$ | *The Cartan Hermitian Pairing of the Polar Decomposition of Biquaternions*, §*The Statement* | the restriction that the generalized pair extends |
| the Hermitian positive cone and the positive square root | *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*, §*The Polar Decomposition* | $\tilde H=\sqrt{\tilde Q\tilde Q^{*}}$ and its positivity |
| the zero-divisor cone | *Quaternionic Norm Regularity and Degeneracy in the Biquaternion Algebra*, §*The Zero Divisors* | the identification of the singular locus with the cone |
| the rank-one elements and the matrix rank | *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*, §*The Rank-One Elements and the Outer Product* | rank one on the cone |
| the rank-one Hermitian idempotents | *Square Roots of One and the Idempotents of the Biquaternion Algebra*, §*The Classification of the Idempotents* | the Bloch form $\tfrac12(e_t+i\vec u)$ of the two projections |
| the unitary group | *The Unitary Group of the Biquaternion Algebra*, §*The Structure of the Unitary Group* | the unitary factor off the cone |

The article proves no new matrix theorem. It states the left form of the matrix polar decomposition, reduces the biquaternion statement to it, and computes the consequences of the rank drop. The only algebraic inputs are the isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$, the positivity of $\tilde Q\tilde Q^{*}$, and the classification of the rank-one idempotents.

## The Matrix Theorem

### The Right Form and the Left Form

For a matrix $A\in M_2(\mathbb{C})$, write $A^{\dagger}$ for the conjugate transpose. The **right polar decomposition** is $A=V\lvert A\rvert$ with $\lvert A\rvert=\sqrt{A^{\dagger}A}$ positive semidefinite and $V$ a partial isometry whose kernel is $\ker A$. It is unique. The **left form**, which is the order of the corpus, is the adjoint statement:

$$
\boxed{\; A=\lvert A^{\dagger}\rvert\,U,\qquad \lvert A^{\dagger}\rvert=\sqrt{AA^{\dagger}},\qquad U=\lvert A^{\dagger}\rvert^{+}A \;},
$$

with ${}^{+}$ the Moore–Penrose inverse. The matrix $U$ is the adjoint of the right factor of $A^{\dagger}$, hence a partial isometry, and its projections are the two projections of $A$:

$$
\boxed{\; U^{\dagger}U=P_{\operatorname{ran}A^{\dagger}},\qquad UU^{\dagger}=P_{\operatorname{ran}A} \;}.
$$

The condition is stated on the two projections, not on the kernel alone. The kernel condition $\ker U=\ker A$ fixes the initial projection; the range condition $\operatorname{ran}U=\operatorname{ran}A$ fixes the final one. Both are needed for uniqueness, as the examples at the end of this section show.

### The Singular Value Form

Let $A=\sum_{i=1}^{r}\sigma_i u_i v_i^{\dagger}$ be a singular value decomposition, with $\sigma_i>0$, $r=\operatorname{rank}A$, and orthonormal families $(u_i)$ and $(v_i)$. Then

$$
H=\sqrt{AA^{\dagger}}=\sum_{i=1}^{r}\sigma_i\,u_i u_i^{\dagger},\qquad
U=H^{+}A=\sum_{i=1}^{r}u_i v_i^{\dagger},\qquad
H^{+}=\sum_{i=1}^{r}\sigma_i^{-1}u_i u_i^{\dagger}.
$$

| object | formula | property |
|---|---|---|
| $H$ | $\sqrt{AA^{\dagger}}=\sum_i\sigma_i u_i u_i^{\dagger}$ | Hermitian, positive semidefinite, $\operatorname{ran}H=\operatorname{ran}A$ |
| $U$ | $H^{+}A=\sum_i u_i v_i^{\dagger}$ | partial isometry, $U^{\dagger}U=P_{\operatorname{ran}A^{\dagger}}$, $UU^{\dagger}=P_{\operatorname{ran}A}$ |
| $H^{+}$ | $\sum_i\sigma_i^{-1}u_i u_i^{\dagger}$ | Moore–Penrose inverse, the inverse of $H$ on its range |

The formulas are the whole theorem. The positive factor is the square root on the range of $A$; the partial isometry is the isometry that carries the singular directions $v_i$ to $u_i$; the pseudoinverse is the inverse of $H$ where $H$ is invertible and zero where it is not.

### Uniqueness

**Theorem (matrix, left form).** Let $A\in M_2(\mathbb{C})$. There is exactly one pair $(H,U)$ such that $H$ is Hermitian positive semidefinite, $U$ is a partial isometry, $A=HU$, $U^{\dagger}U=P_{\operatorname{ran}A^{\dagger}}$, $UU^{\dagger}=P_{\operatorname{ran}A}$ and $\operatorname{ran}H=\operatorname{ran}A$. It is $H=\sqrt{AA^{\dagger}}$ and $U=H^{+}A$.

**Proof.** The pair displayed above has the properties. For uniqueness, $A=HU$ gives $AA^{\dagger}=HUU^{\dagger}H=HP_{\operatorname{ran}A}H$. Since $\operatorname{ran}H=\operatorname{ran}A$ and $H$ is Hermitian, $P_{\operatorname{ran}A}H=H$, so $AA^{\dagger}=H^{2}$ and $H$ is the positive square root. Then $H^{+}H=P_{\operatorname{ran}H}=P_{\operatorname{ran}A}=UU^{\dagger}$, so $H^{+}A=H^{+}HU=UU^{\dagger}U=U$; the pair is fixed.

Three conditions do the work. The range condition on $H$ fixes the positive factor: for $A=\operatorname{diag}(1,0)$, the pair $(I_2,\operatorname{diag}(1,0))$ satisfies $A=HU$ with $H$ positive definite, $U$ a partial isometry and both projections of $U$ equal to $P_{\operatorname{ran}A}$, but $H\neq\sqrt{AA^{\dagger}}$. The range projection of $U$ fixes the second factor: for $A=\Pi=\operatorname{diag}(1,0)$, the pair $(\Pi,I_2)$ satisfies $A=HU$ with $H$ positive semidefinite and $U$ unitary, but $UU^{\dagger}=I_2\neq P_{\operatorname{ran}A}$, and the canonical pair is $(\Pi,\Pi)$. The kernel condition alone also excludes the second pair, since $\ker I_2\neq\ker\Pi$; both projections are stated because they are the initial and final spaces of $U$. Fixing only the two kernels is weaker still: for $A=\operatorname{diag}(1,0)$, the pairs $(\operatorname{diag}(1,0),\operatorname{diag}(1,0))$ and $(\operatorname{diag}(\sqrt2,0),U)$, with $Ue_1=(e_1+e_2)/\sqrt2$ and $Ue_2=0$, both have $H$ positive semidefinite, $\operatorname{ran}H=\operatorname{ran}A$, $A=HU$, $U$ a partial isometry and $\ker U=\ker H=\ker A$; only the first has $UU^{\dagger}=P_{\operatorname{ran}A}$.

### The Zero Matrix

For $A=0$ the sums are empty, $H=0$, $U=0$, and the two projections are $0$. The pair is unique under the theorem. The zero element is therefore included, and it is the only element whose two projections have rank zero.

## The Biquaternion Reading

### The Two Factors

Transport the matrix theorem through $\mathsf M_2$. The Hermitian conjugation ${}^{*}$ becomes ${}^{\dagger}$, the positive square root becomes the Hermitian positive square root in the algebra, and the Moore–Penrose inverse is computed in the matrix model and transported back.

**Theorem (generalized Cartan pairing).** Every $\tilde Q\in\mathbb{B}$ has exactly one pair $(\tilde H,\tilde U)$ with

1. $\tilde H$ Hermitian positive semidefinite, $\tilde H=\tilde H^{*}$ and $\operatorname{ran}\tilde H=\operatorname{ran}\tilde Q$;
2. $\tilde U$ a partial isometry, $\tilde U\tilde U^{*}\tilde U=\tilde U$, with $\tilde U^{*}\tilde U$ the projection onto $\operatorname{ran}\tilde Q^{*}$ and $\tilde U\tilde U^{*}$ the projection onto $\operatorname{ran}\tilde Q$;
3. $\tilde Q=\tilde H\tilde U$.

It is

$$
\tilde H=\sqrt{\tilde Q\tilde Q^{*}},\qquad \tilde U=\tilde H^{+}\tilde Q .
$$

On $\langle\tilde Q\rangle_{\natural}\neq0$, $\tilde H$ is positive definite, $\tilde U$ is unitary, and the pair is the Cartan pairing.

The theorem is the matrix theorem with the two projections written in the algebra. The positive factor is the unique Hermitian positive semidefinite square root of $\tilde Q\tilde Q^{*}$; the second factor is the pseudoinverse applied to the element. The equation $\tilde Q\tilde Q^{*}=\tilde H^{2}$ still holds, now with a semidefinite $\tilde H$, and it is the defining equation of the positive factor.

### The Invariants

The rank and the two norms are read on the positive factor. Let $\sigma_1\ge\sigma_2$ be the singular values of $\mathsf M_2(\tilde Q)$.

| invariant | on $\tilde Q$ | on $\tilde H$ | why |
|---|---|---|---|
| rank | $r$ | $r$ | $\operatorname{ran}\tilde H=\operatorname{ran}\tilde Q$ |
| Hermitian norm | $\langle\tilde Q\rangle_{*}=\tfrac12\sum_i\sigma_i^{2}$ | $\langle\tilde H\rangle_{*}=\tfrac12\sum_i\sigma_i^{2}$ | $\tilde H$ and $\tilde Q$ have the same singular values |
| quaternionic norm | $\langle\tilde Q\rangle_{\natural}$ | $\langle\tilde H\rangle_{\natural}=\lvert\langle\tilde Q\rangle_{\natural}\rvert$ | $\det\tilde H=\lvert\det\tilde Q\rvert$ |

The Hermitian norm is the squared Frobenius norm, halved: $\langle\tilde Q\rangle_{*}=\tfrac12\operatorname{tr}(\mathsf M_2(\tilde Q)^{\dagger}\mathsf M_2(\tilde Q))=\tfrac12\sum_i\sigma_i^{2}$. The quaternionic norm of $\tilde H$ is real and non-negative because $\tilde H$ is Hermitian positive semidefinite, and its modulus is the modulus of the norm of $\tilde Q$. The two statements are different: the Hermitian norm is the half-sum of the squared singular values, the modulus of the quaternionic norm is their product. The generalized $\tilde H$ carries the first in full and the modulus of the second.

**The positive factor is not the quaternionic modulus.** The quaternionic modulus $\Rho=\sqrt{\langle\tilde Q\rangle_{\natural}}$ is a central complex scalar; $\tilde H$ is a non-central Hermitian element. For a nonzero null element the modulus is zero and $\tilde H$ is a scaled idempotent, neither zero nor central. The notation $\tilde H$ is reserved for the factor, and $\Rho$ for the modulus.

### The Three Strata

Write $\tilde\Pi_{\mathrm i}=\tilde U^{*}\tilde U$ and $\tilde\Pi_{\mathrm f}=\tilde U\tilde U^{*}$ for the initial and final projections. They are $e_t$ when $\tilde U$ is unitary, rank-one idempotents when $\tilde U$ has rank one, and $0$ when $\tilde U=0$.

| stratum | quaternionic norm | rank | $\tilde H$ | $\tilde U$ | $\tilde U^{*}\tilde U$ | $\tilde U\tilde U^{*}$ |
|---|---|---|---|---|---|---|
| invertible | $\neq0$ | $2$ | positive definite | unitary | $e_t$ | $e_t$ |
| nonzero null | $0$ | $1$ | $\sigma\tilde\Pi_{\mathrm f}$ | $\tilde Q/\sigma$ | $\tilde\Pi_{\mathrm i}$ | $\tilde\Pi_{\mathrm f}$ |
| zero | $0$ | $0$ | $0$ | $0$ | $0$ | $0$ |

The table is the whole content of the next two sections. The first row is the Cartan pairing. The second is the cone, where the positive factor becomes a scaled projection and the partial isometry becomes the normalized element. The third is the origin.

## The Null Cone

### The Rank-One Case

An element is $N$-degenerate exactly when $\langle\tilde Q\rangle_{\natural}=0$, because the quaternionic norm is the determinant of the $2\times2$ image; the $N$-degenerate element is then non-invertible, and a nonzero one is a zero divisor. A nonzero element of the cone therefore has rank one: its matrix has one non-zero singular value and one zero singular value. Write $\sigma=\sigma_1>0$. The singular value form gives

$$
\boxed{\; \tilde Q=\sigma\,\tilde U,\qquad \tilde H=\sigma\,\tilde U\tilde U^{*},\qquad \tilde U=\frac{\tilde Q}{\sigma} \;},
$$

with $\sigma^{2}=2\langle\tilde Q\rangle_{*}=\lVert\tilde Q\rVert_{\mathrm F}^{2}$. The element is a positive scalar times a partial isometry, and the positive factor is the scalar times the final projection of that partial isometry. The two equations are the rank-one reading of $\tilde H=\sqrt{\tilde Q\tilde Q^{*}}$ and $\tilde U=\tilde H^{+}\tilde Q$.

**The projections.** For a rank-one partial isometry, the two projections $\tilde\Pi_{\mathrm i}$ and $\tilde\Pi_{\mathrm f}$ are rank-one Hermitian idempotents, and

$$
\tilde U=\tilde\Pi_{\mathrm f}\,\tilde U\,\tilde\Pi_{\mathrm i}.
$$

Every non-trivial Hermitian idempotent of the algebra is of the Bloch form

$$
\tilde\Pi_{\vec u}=\tfrac12\left(e_t+i\vec u\right),\qquad \vec u\ \text{a real unit vector},
$$

and $\tilde\Pi_{\vec u}^{2}=\tilde\Pi_{\vec u}$, $\tilde\Pi_{\vec u}^{*}=\tilde\Pi_{\vec u}$, $\langle\tilde\Pi_{\vec u}\rangle_{\natural}=0$, $\langle\tilde\Pi_{\vec u}\rangle_{*}=\tfrac12$. The two projections of $\tilde U$ are therefore two points of the Bloch sphere, and the partial isometry is the isometry that carries the initial line to the final one.

**The positive factor on the cone.** Since $\tilde H=\sigma\tilde\Pi_{\mathrm f}$, the positive factor is a scaled pure state. It is itself on the cone, $\langle\tilde H\rangle_{\natural}=\sigma^{2}\langle\tilde\Pi_{\mathrm f}\rangle_{\natural}=0$, and it is not invertible. Its Hermitian norm is $\langle\tilde H\rangle_{*}=\sigma^{2}/2=\langle\tilde Q\rangle_{*}$, as the invariant table requires.

### The Cone as the Singular Locus

| object | rank | singular? | on the cone? |
|---|---|---|---|
| invertible element | $2$ | no | no |
| nonzero null element | $1$ | yes | yes |
| zero element | $0$ | yes | yes |

There is no singular element off the cone. This is the structural reason the generalized pairing is a cone extension and not a separate theory: the matrix polar decomposition degenerates only at rank one or rank zero, and in this algebra those are exactly the singular elements, the nonzero ones being the zero divisors. The cone has real codimension two, and the generalized pair is defined on all of it, including the origin.

### The Element as a Normalized Partial Isometry

The rank-one formulas say that the punctured cone is the set of positive multiples of rank-one partial isometries. Two elements on the same ray have the same $\tilde U$ and rescaled $\tilde H$; the ray is the orbit of the partial isometry under the positive scalars. The normalized element $\tilde Q/\lVert\tilde Q\rVert_{\mathrm F}$ is a partial isometry for every nonzero null element, and the normalization is the generalized polar factor.

This is the sharpest difference from the invertible case. Off the cone the polar factor is unitary and carries the whole phase; on the cone it has rank one, and the phase has collapsed to an isometry between two lines.

## Relation to the Cartan Pairing

### The Restriction

On the complement of the cone the generalized pair is the Cartan pair. The positive factor is positive definite, the partial isometry is unitary, and the two projections are both $e_t$. The generalized theorem therefore contains the classical one, and the classical one is the restriction to the group of units.

| property | Cartan pairing | generalized pairing |
|---|---|---|
| domain | $\langle\tilde Q\rangle_{\natural}\neq0$ | all $\mathbb{B}$ |
| first factor | $\tilde H$ positive definite | $\tilde H$ positive semidefinite |
| second factor | $\tilde U$ unitary | $\tilde U$ partial isometry |
| equation | $\tilde Q=\tilde H\tilde U$ | $\tilde Q=\tilde H\tilde U$ |
| projections | $\tilde U^{*}\tilde U=\tilde U\tilde U^{*}=e_t$ | the projections of $\tilde Q$ |
| uniqueness | unique on the domain | unique with the projections and the range of $\tilde H$ |
| continuity | continuous on the domain | $\tilde H$ continuous, $\tilde U$ not |

The first factor is continuous across the cone; the second is not. The product $\tilde H\tilde U$ is continuous because it is $\tilde Q$. The discontinuity is a rank drop of $\tilde U$, not a failure of the product.

### The Discontinuity at the Cone

Take the family

$$
\tilde Q_{\epsilon}=\frac{1+\epsilon}{2}\,e_t+i\,\frac{1-\epsilon}{2}\,\vec e_z,\qquad \epsilon>0 .
$$

Its matrix is $\operatorname{diag}(1,\epsilon)$, positive definite, so $\tilde H_{\epsilon}=\tilde Q_{\epsilon}$ and $\tilde U_{\epsilon}=e_t$. At $\epsilon=0$ the element is

$$
\tilde\Pi_{\vec e_z}=\tfrac12\left(e_t+i\vec e_z\right),
$$

a Hermitian idempotent on the cone, and the generalized pair is $\tilde H=\tilde U=\tilde\Pi_{\vec e_z}$. The positive factor has the continuous limit $\tilde\Pi_{\vec e_z}$, while the partial isometry has the limit $e_t$ from the family and the value $\tilde\Pi_{\vec e_z}$ at the cone. The factor jumps.

The pair $(\tilde\Pi_{\vec e_z},e_t)$ still multiplies to the element: $\tilde\Pi_{\vec e_z}e_t=\tilde\Pi_{\vec e_z}$. It is excluded by the two projection conditions, since $e_t e_t^{*}=e_t$ is the projection onto the whole space and not onto the line of $\tilde\Pi_{\vec e_z}$, and $\ker e_t$ is not $\ker\tilde\Pi_{\vec e_z}$. The example shows why the theorem fixes the two projections: the pair fails both, and the canonical pair is the one whose final projection is the line of the element.

**The reading.** The positive factor is the part of the polar data that survives the cone; the partial isometry is the part that records the collapse of the rank. A continuous unitary factor cannot reach a rank-one element and remain unitary; the canonical partial isometry is the unique algebraic limit that keeps the two lines.

### What the Extension Adds

The generalized pairing gives the cone what the four-factor word cannot: a two-factor decomposition. The first factor is a scaled pure state, the second an isometry between two pure states. The four factors of the word are gone; the remaining scalar is the Frobenius length, and the phase is the partial isometry. The extension is therefore a degeneration of the word, not a regrouping of it.

## Physical Interpretation

Off the cone the Cartan pairing is read as a positive scale and a unitary phase. On the cone the same two slots carry a state and a transition between states. The reading is not an extra postulate; it is the algebraic content of the two factors, and the physics articles own the identifications.

- $\tilde H=\sigma\tilde\Pi_{\mathrm f}$: the positive factor is a pure state of weight $\sigma$, not a scalar. The cone is the massless boundary, and the positive factor has become the state on it.
- $\tilde U=\tilde Q/\sigma$: the second factor is the isometry from the initial pure state $\tilde\Pi_{\mathrm i}$ to the final pure state $\tilde\Pi_{\mathrm f}$. The unitary phase of the invertible case has collapsed to a transition.
- The discontinuity: a sequence of unitary phases has no unitary limit at the cone. The canonical limit keeps the two lines, not the whole space. The reversible factor loses rank at the boundary, and the lost rank is the lost reversible part.

*The Zero-Divisor Cone and the Massless Spectrum* and *Roots, Idempotents and Observables* develop the physical identifications; this article supplies the factorisation and makes no further claim. The one structural statement that is physics-facing is the rank drop.

## Worked Examples

### The Hermitian Idempotent

Take $\tilde\Pi_{\vec e_z}=\tfrac12(e_t+i\vec e_z)$. Its matrix is $\operatorname{diag}(1,0)$, so it is Hermitian, idempotent and rank one. Then

$$
\langle\tilde\Pi_{\vec e_z}\rangle_{\natural}=0,\qquad \langle\tilde\Pi_{\vec e_z}\rangle_{*}=\tfrac12,\qquad \tilde H=\tilde U=\tilde\Pi_{\vec e_z}.
$$

The equation $\tilde H=\sqrt{\tilde\Pi\tilde\Pi^{*}}$ reads $\tilde\Pi=\sqrt{\tilde\Pi^{2}}=\tilde\Pi$, and $\tilde U=\tilde H^{+}\tilde\Pi=\tilde\Pi^{+}\tilde\Pi=\tilde\Pi$. The element is its own generalized polar factor.

### The Scaled Idempotent

Take $\tilde Q=e_t+i\vec e_x=2\tilde\Pi_{\vec e_x}$ with $\tilde\Pi_{\vec e_x}=\tfrac12(e_t+i\vec e_x)$. Then

$$
\langle\tilde Q\rangle_{\natural}=0,\qquad \langle\tilde Q\rangle_{*}=2,\qquad \sigma=2,\qquad \tilde H=\tilde Q=2\tilde\Pi_{\vec e_x},\qquad \tilde U=\tilde\Pi_{\vec e_x}.
$$

The positive factor is the scaled idempotent and the partial isometry is the idempotent itself. The two projections are both $\tilde\Pi_{\vec e_x}$. The element is $2\tilde U$, in agreement with $\tilde Q=\sigma\tilde U$.

### A Non-Hermitian Null Element

Take $\tilde Q=i\vec e_x-\vec e_y$. It has $\langle\tilde Q\rangle_{\natural}=i^{2}+(-1)^{2}=0$ and $\langle\tilde Q\rangle_{*}=2$, so $\sigma=2$. The matrix is

$$
\mathsf M_2(\tilde Q)=\begin{pmatrix}0&2\\0&0\end{pmatrix},
$$

of rank one. Then

$$
\tilde H=e_t+i\vec e_z=2\tilde\Pi_{\vec e_z},\qquad
\tilde U=\tfrac{i}{2}\vec e_x-\tfrac12\vec e_y=\tfrac12\tilde Q,
$$

and the two projections are

$$
\tilde U^{*}\tilde U=\tfrac12\left(e_t-i\vec e_z\right)=\tilde\Pi_{-\vec e_z},\qquad
\tilde U\tilde U^{*}=\tfrac12\left(e_t+i\vec e_z\right)=\tilde\Pi_{\vec e_z}.
$$

The partial isometry carries the initial pure state $\tilde\Pi_{-\vec e_z}$ to the final pure state $\tilde\Pi_{\vec e_z}$, and $\tilde Q=2\tilde U$. The example is non-Hermitian: $\tilde U$ is not a projection, only its two projections are. It shows that the rank-one case is not the idempotent case, and that the two Bloch points need not coincide.

### The Generic Element

Take $\tilde Q=(1+i)e_t+\vec e_x+2\vec e_y$, the worked example of *The Cartan Hermitian Pairing of the Polar Decomposition of Biquaternions*. Then $\langle\tilde Q\rangle_{\natural}=5+2i$, $\langle\tilde Q\rangle_{*}=7$, and the generalized pair is the Cartan pair,

$$
\tilde H=2.488489985\,e_t-0.401850120\,i\,\vec e_x-0.803700241\,i\,\vec e_y,
$$

positive definite with $\langle\tilde H\rangle_{\natural}=5.385164807=\lvert5+2i\rvert$, and

$$
\tilde U=(0.462100989+0.088992519i)e_t+(0.387479295+0.074621694i)\vec e_x+(0.774958590+0.149243388i)\vec e_y,
$$

unitary. The example is the control: off the cone the generalized pair is the Cartan pair, and the invariants of the table hold with $\sigma_1\sigma_2=5.385164807$ and $\sigma_1^{2}+\sigma_2^{2}=14$.

## What This Does Not Claim

- It does not extend the four-factor word. There is no scale, phase, boost or rotor on the cone, and the generalized factors are not a regrouping of them.
- It does not make the partial isometry continuous. The positive factor is continuous; the partial isometry jumps at the rank drop, and no unitary factor can reach a rank-one element.
- It does not replace the Cartan pairing off the cone. There the generalized pair is the Cartan pair.
- It does not identify $\tilde H$ with the quaternionic modulus. $\tilde H$ carries the Hermitian norm and the modulus of the quaternionic norm; the modulus itself is the central $\Rho$.
- It does not prove the matrix polar decomposition. It reads the left form of the matrix theorem in the algebra and computes the cone.

## Summary

### Main Results

| item | result |
|---|---|
| domain | every $\tilde Q\in\mathbb{B}$, including $0$ |
| first factor | $\tilde H=\sqrt{\tilde Q\tilde Q^{*}}$, Hermitian positive semidefinite, $\operatorname{ran}\tilde H=\operatorname{ran}\tilde Q$ |
| second factor | $\tilde U=\tilde H^{+}\tilde Q$, partial isometry, $\tilde U^{*}\tilde U=P_{\operatorname{ran}\tilde Q^{*}}$, $\tilde U\tilde U^{*}=P_{\operatorname{ran}\tilde Q}$ |
| equation | $\tilde Q=\tilde H\tilde U$, with $\tilde Q\tilde Q^{*}=\tilde H^{2}$ |
| off the cone | $\tilde H$ positive definite, $\tilde U$ unitary, the Cartan pairing |
| on the punctured cone | $\tilde Q=\sigma\tilde U$, $\tilde H=\sigma\tilde U\tilde U^{*}$, $\sigma=\lVert\tilde Q\rVert_{\mathrm F}$ |
| projections on the cone | two Hermitian idempotents $\tfrac12(e_t+i\vec u)$ on the Bloch sphere |
| zero element | $\tilde H=\tilde U=0$ |
| invariants | $\langle\tilde H\rangle_{*}=\langle\tilde Q\rangle_{*}$, $\langle\tilde H\rangle_{\natural}=\lvert\langle\tilde Q\rangle_{\natural}\rvert$ |
| uniqueness | unique with the initial and final projections and the range of $\tilde H$ |
| continuity | $\tilde H$ continuous, $\tilde U$ discontinuous at the cone |

The generalized Cartan pairing is the polar decomposition of the whole biquaternion algebra. It is the Cartan pairing off the null cone and a rank-one degeneration on it: the positive factor becomes a scaled pure state, the unitary factor becomes a partial isometry between two pure states, and the element becomes a positive scalar times that partial isometry. The two projections and the range of $\tilde H$ are the data that make the singular case unique, and the projections are exactly the data that jump at the cone.

### What the Reader Should Retain

The three statements to carry away are: the formulas $\tilde H=\sqrt{\tilde Q\tilde Q^{*}}$ and $\tilde U=\tilde H^{+}\tilde Q$ hold for every element; on the cone they read $\tilde H=\sigma\tilde\Pi_{\mathrm f}$ and $\tilde U=\tilde Q/\sigma$; and the pair is unique only when the initial and final projections and the range of $\tilde H$ are fixed. The first is the extension, the second is the degeneration, and the third is the price.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde Q=\tilde H\tilde U$ | the generalized Cartan pairing |
| $\tilde H=\sqrt{\tilde Q\tilde Q^{*}}$ | Hermitian positive semidefinite factor |
| $\tilde U=\tilde H^{+}\tilde Q$ | partial isometry factor |
| $\tilde H^{+}$ | Moore–Penrose inverse of $\tilde H$ |
| $P_L$ | orthogonal projection onto the subspace $L$ |
| $\tilde\Pi_{\vec u}=\tfrac12(e_t+i\vec u)$ | rank-one Hermitian idempotent, $\vec u$ a real unit vector |
| $\tilde\Pi_{\mathrm i}=\tilde U^{*}\tilde U$, $\tilde\Pi_{\mathrm f}=\tilde U\tilde U^{*}$ | initial and final projections of $\tilde U$ |
| $\sigma=\lVert\tilde Q\rVert_{\mathrm F}$ | Frobenius length, the non-zero singular value on the cone |
| $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2}$ | quaternionic norm, the determinant |
| $\langle\tilde Q\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2}$ | Hermitian norm, half the squared Frobenius norm |
| $\sigma_i,u_i,v_i$ | singular values and singular vectors of $\mathsf M_2(\tilde Q)$ |
| $\mathsf M_2$ | the matrix model $\mathbb{B}\cong M_2(\mathbb{C})$ |
| ${}^{*}$, ${}^{\dagger}$ | Hermitian conjugation in $\mathbb{B}$, conjugate transpose in $M_2(\mathbb{C})$ |
| $\mathcal N=\{\langle\tilde Q\rangle_{\natural}=0\}$ | the zero-divisor cone, the singular locus |

## Further Reading

- [The Cartan Hermitian Pairing of the Polar Decomposition of Biquaternions](the-cartan-hermitian-pairing-of-the-polar-decomposition-of-biquaternions.html), for the pairing that this article extends and for the domain $\langle\tilde Q\rangle_{\natural}\neq0$.
- [Modulus–Unit Polar Decomposition of Biquaternions](modulus-unit-polar-decomposition-of-biquaternions.html), for the four factors, the modulus $\Rho=\sqrt{\langle\tilde Q\rangle_{\natural}}$ and the boundary of the word.
- [Exponential Polar Decomposition of Biquaternions](exponential-polar-decomposition-of-biquaternions.html), for the boundary limits of the word and the idempotents at infinite rapidity.
- [The Quaternion Pairing of the Polar Decomposition of Biquaternions](the-quaternion-pairing-of-the-polar-decomposition-of-biquaternions.html) and [The Hamilton Root Pairing of the Polar Decomposition of Biquaternions](the-hamilton-root-pairing-of-the-polar-decomposition-of-biquaternions.html), for the two partial pairings whose domains are cut by the cone and the quadric cone.
- [Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions](introduction-to-the-2x2-matrix-element-representation-of-biquaternions.html), for the isomorphism, the transport of ${}^{*}$ to the matrix adjoint and the rank-one elements.
- [Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint](positivity-and-the-hermitian-cone-of-the-biquaternion-algebra-with-hermitian-adjoint.html), for the positive cone and the Hermitian square root.
- [Quaternionic Norm Regularity and Degeneracy in the Biquaternion Algebra](quaternionic-norm-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the cone and its real dimension.
- [Square Roots of One and the Idempotents of the Biquaternion Algebra](square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.html), for the Hermitian idempotents $\tfrac12(e_t+i\vec u)$ and the Bloch sphere.
- [The Unitary Group of the Biquaternion Algebra](the-unitary-group-of-the-biquaternion-algebra.html), for the unitary factor off the cone.\n- [The Polar Decomposition of an Operator of the Form](the-polar-decomposition-of-an-operator-of-the-form.html), for the operator polar decomposition that this article is not.
- [The Zero-Divisor Cone and the Massless Spectrum](../articles_physics/the-zero-divisor-cone-and-the-massless-spectrum.html) and [Roots, Idempotents and Observables](../articles_physics/roots-idempotents-and-observables.html), for the physical interpretation of the cone and the idempotents, which this article does not develop.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 1985), for the polar decomposition and the singular value decomposition; Adi Ben-Israel and Thomas N. E. Greville, *Generalized Inverses: Theory and Applications* (Springer, 2003), for the Moore–Penrose inverse and the projection conditions.
