# __The Four Forms and Their Algebraic Norms at $n=4$__

## Introduction

**An element of $M_4(\mathbb{C})$ carries four quadratic invariants, each the quarter-trace of a word in the matrix: the plain $P=Q_t^{2}-B^{2}=\tfrac14\operatorname{tr}(A^{2})$, the quaternionic $N=Q_t^{2}+B^{2}=\tfrac14\operatorname{tr}(A^{\mathsf T}A)$, the Hermitian $H=\sum_\mu|Q_\mu|^{2}=\tfrac14\operatorname{tr}(A^{\ast}A)$ and the Krein $K=|Q_t|^{2}-\sum_k|Q_k|^{2}=\tfrac14\operatorname{tr}(A^{\mathsf T}A^{\ast})$; the determinant is the square of $N$, and the trace is $4Q_t$.**

The article writes the four forms, explains the factor of four, determines which are multiplicative, which are positive and which are invariant under which group, sets the matrix formulas against their biquaternion counterparts row by row, and states the two warnings that go with them: the transpose is the quaternion conjugation only in the axis-free frame, and the determinant is not a norm on the full algebra.

It assumes *The Trace Form and Its Inertia on the Two Halves of $M_4(\mathbb{C})$* and *The Hilbert–Schmidt Form at $n=4$*. The biquaternion original is *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*; the axis-free computation is §*The Four Norms* of *The Axis-Free Representation of $M_4(\mathbb{C})$*.

## The Four Quarter-Traces

**Definition.** For $A$ the matrix of $\tilde Q$ in the axis-free frame, with $Q_t$ the scalar part and $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}$,

$$
P=\tfrac14\operatorname{tr}(A^{2}),\qquad N=\tfrac14\operatorname{tr}(A^{\mathsf T}A),\qquad H=\tfrac14\operatorname{tr}(A^{\ast}A),
$$

and the **Krein form** $K$ as the coordinate-weighted quadratic form $\sum_\mu\sigma_\mu|c_\mu|^{2}$ with $\sigma=(1,-1,-1,-1)$ and $c_\mu=\tfrac14\operatorname{tr}(T_{\mu t}^{\dagger}A)$ the four coefficients of $A$.

**Theorem.** $P=Q_t^{2}-B^{2}$, $N=Q_t^{2}+B^{2}$, $H=\sum_\mu|Q_\mu|^{2}$ and $K=|Q_t|^{2}-\sum_k|Q_k|^{2}$, together with $\operatorname{tr}A=4Q_t$ and $\det A=N^{2}$.

**Proof.** The four identities are verified on the sixteen basis matrices and extended by the multiplicativity of the representation; in the axis-free frame $A^{\mathsf T}=A^{\natural}$, so $A^{\mathsf T}A=A^{\natural}A$ is the matrix of $\tilde Q^{\natural}\tilde Q=\langle\tilde Q\rangle_{\natural}e_t$, a scalar, and its quarter-trace is $\langle\tilde Q\rangle_{\natural}=Q_t^{2}+B^{2}=N$. The plain form is the quarter-trace of $A^{2}=A(\tilde Q^{2})$, whose scalar part is $Q_t^{2}-B^{2}$.

**Corollary.** $K=H-2\sum_k|Q_k|^{2}$ and $P=N-2B^{2}$, so over the reals the two pairs differ by twice the modulus of the vector part.

**Proof.** Compute from the coordinate lists.

**The word that collapses.** The naive mixed word $\tfrac14\operatorname{tr}(A^{\mathsf T}A^{\ast})$ is **not** the Krein form: since $\operatorname{tr}(M^{\mathsf T}N^{\mathsf T})=\operatorname{tr}(NM)$, it equals $\tfrac14\operatorname{tr}(\bar AA)=\tfrac14\lVert A\rVert_F^{2}=H$. The Krein form needs the coordinate weights of the frame and cannot be written as a single quarter-trace of a word in $A$ alone.

**Proof.** $\operatorname{tr}(A^{\mathsf T}A^{\ast})=\operatorname{tr}((\bar AA)^{\mathsf T})=\operatorname{tr}(\bar AA)=\sum_{ij}|a_{ij}|^{2}$.

**The trace and the determinant.** $\operatorname{tr}A=4Q_t$ and $\det A=(Q_t^{2}+B^{2})^{2}=N^{2}$.

**Proof.** The eigenvalues are $Q_t\pm iB$, each twice, so the trace is their sum and the determinant their product.

## The Factor Four

**Proposition.** The quarter is the price of the block: $\operatorname{tr}A=2\operatorname{tr}\mathsf M_2(\tilde Q)$ and $A$ is a repetition of the $2\times2$ image, so a quadratic word in $A$ has four times the $2\times2$ value.

**Proof.** $A$ is the Kronecker product of the identity with the $2\times2$ image, so its trace is twice, and a quadratic word twice again, giving four.

**Corollary.** In the biquaternion article the same numbers are the values of the four forms, and the matrix formulas here reproduce them with the factor four, which is $2\times2$.

**Proof.** The two computations agree term by term.

**The trace as a quarter.** $\operatorname{tr}A=4Q_t$ is the linear member of the family, and $Q_t=\tfrac14\operatorname{tr}A$ is the scalar part of the element.

**Proof.** The trace of the scalar part is four times it, and the traceless part contributes nothing.

## What Is Multiplicative

**Theorem.** $N(AB)=N(A)N(B)$ and $\det(AB)=\det A\det B$; $P$, $H$ and $K$ are not multiplicative.

**Proof.** $N=\langle\tilde Q\rangle_{\natural}$ and the quaternionic norm is multiplicative because it is central: $\langle\tilde Q_1\tilde Q_2\rangle_{\natural}=\tilde Q_1\tilde Q_2\tilde Q_2^{\natural}\tilde Q_1^{\natural}=\tilde Q_1\langle\tilde Q_2\rangle_{\natural}\tilde Q_1^{\natural}=\langle\tilde Q_1\rangle_\natural\langle\tilde Q_2\rangle_\natural$. The determinant is the square of $N$, hence multiplicative. For the failure of $P$, take $A=E_{12}+E_{21}$: then $A^{2}=E_{11}+E_{22}$, so $P(A)=\tfrac12$ and $P(A^{2})=\tfrac12$, while $P(A)^{2}=\tfrac14$.

**Corollary.** The determinant is the multiplicative invariant of degree four and $N$ the multiplicative invariant of degree two; the pair $(N,\det)$ is one invariant counted twice.

**Proof.** $\det=N^{2}$, and $N$ is multiplicative.

**The failure of $H$.** $H(AB)=\tfrac14\lVert AB\rVert_F^{2}\le\lVert A\rVert_2^{2}H(B)$, with equality for an isometry in the first slot, so $H$ is submultiplicative and not multiplicative.

**Proof.** $\lVert AB\rVert_F\le\lVert A\rVert_2\lVert B\rVert_F$.

**The failure of $K$.** For $A$ the matrix of $e_t+e_x$ one has $K(A)=|1|^{2}-|1|^{2}=0$ while $K(A^{2})=K(2e_x)=-4$.

**Proof.** $(e_t+e_x)^{2}=e_t^{2}+2e_x+e_x^{2}=2e_x$ because $e_x^{2}=-e_t$, so the coefficients of $A^{2}$ are $Q_t=0$, $Q_x=2$.

## What Is Positive and What Is Not

**Theorem.** $H$ is positive definite on the complex algebra; $N$ and $P$ are indefinite over $\mathbb{C}$ and definite of opposite signs over $\mathbb{R}$ on the real and imaginary parts; $K$ has inertia $(2,6)$ on the real algebra.

**Proof.** $H=\sum_\mu|Q_\mu|^{2}$ vanishes only at zero. $N=Q_t^{2}+B^{2}$ vanishes at $Q_t=i$, $Q_x=1$, all other coordinates zero, so it is indefinite over $\mathbb{C}$; over $\mathbb{R}$ it is positive definite. $P=Q_t^{2}-B^{2}$ is positive on the scalar line and negative on the vector space. $K$ is $+1$ on the two real directions of the scalar part and $-1$ on the six real directions of the vector part, so its inertia is $(2,6)$.

**Corollary.** Exactly one of the four is an inner product on the complex algebra, and it is the Hilbert–Schmidt form divided by four.

**Proof.** Only $H$ is positive definite, and $H=\tfrac14\langle A,A\rangle$.

**The null cones.** $P$ vanishes on the cone $Q_t^{2}=B^{2}$, $N$ on the cone $Q_t^{2}=-B^{2}$, and those two complex cones are the zero sets of the plain and quaternionic norms; $H$ has no nonzero zero.

**Proof.** Solve each equation for $Q_t$.

**Corollary.** The determinant vanishes exactly where $N$ does, so the singular set is the zero set of the quaternionic norm and has complex codimension one.

**Proof.** $\det=N^{2}$.

## The Invariance Groups

**Proposition.** $P$ is invariant under conjugation by $\mathrm{GL}_4$; $N$ is invariant under conjugation by $O(4,\mathbb{C})$; $H$ is invariant under conjugation by $U(4)$; $K$ is invariant under conjugation by the real orthogonal group $O(4)$ and under the signed permutations of the frame.

**Proof.** $P$ is a quarter-trace of $A^{2}$, and the trace of a square is conjugation invariant. For $N$, if $Q^{\mathsf T}Q=\mathrm I$ then $(QAQ^{-1})^{\mathsf T}(QAQ^{-1})=Q^{-\mathsf T}A^{\mathsf T}AQ^{-1}$, whose trace is that of $A^{\mathsf T}A$. For $H$ the invariance is the unitary invariance of the Hilbert–Schmidt form. $K$ is a weighted sum of the squared moduli of the four coordinates, and a conjugation that preserves the coordinate weights preserves it.

**Corollary.** The four forms are ordered by the size of their invariance group, with $P$ invariant under the largest and $K$ under the smallest.

**Proof.** $\mathrm{GL}_4\supset O(4,\mathbb{C})\supset U(4)$ and $O(4)\subset U(4)$.

**The reading.** Each form is the invariant of the structure used to write it: the product for $P$, the product and the transpose for $N$, the product and the dagger for $H$, and the coordinate weights for $K$.

## The Correspondence with the Biquaternion Article

**The table.**

| Form | Biquaternion value | Matrix formula | Definite over $\mathbb{C}$ | Multiplicative | Invariance group |
|---|---|---|---|---|---|
| plain $P$ | $Q_t^{2}-B^{2}$ | $\tfrac14\operatorname{tr}(A^{2})$ | no | no | $\mathrm{GL}_4$ |
| quaternionic $N$ | $Q_t^{2}+B^{2}$ | $\tfrac14\operatorname{tr}(A^{\mathsf T}A)$ | no | yes | $O(4,\mathbb{C})$ |
| Hermitian $H$ | $\sum_\mu|Q_\mu|^{2}$ | $\tfrac14\operatorname{tr}(A^{\ast}A)$ | yes | no | $U(4)$ |
| Krein $K$ | $|Q_t|^{2}-\sum_k|Q_k|^{2}$ | weighted coordinates, no single word | no | no | $O(4)$ |
| the determinant of the image | $N^{2}$ | $\det A$ | not a form | yes | all |

**Proposition.** The correspondence is entry by entry: each row of the biquaternion table becomes a row here with the same value, read on the matrix.

**The two rows that need the frame.** The second row uses $A^{\mathsf T}=A^{\natural}$ and the fourth the weights $\sigma_\mu$; both are properties of the axis-free frame, since the stitch $R=D(L)^{\mathsf T}D$ holds only there.

## The Two Warnings

**The first warning.** $\tfrac14\operatorname{tr}(A^{\mathsf T}A)$ is the quaternionic norm only in a frame where the transpose is the quaternion conjugation. In another frame the quarter-trace is a different quadratic form, with the same eigenvalues only if the frame is orthogonal for the pairing.

**Proof.** The identity $A^{\mathsf T}=A^{\natural}$ is a property of the entries in the axis-free frame, and a general change of frame makes $A^{\mathsf T}$ the transpose in the new coordinates, which is not the matrix of $\tilde Q^{\natural}$.

**The second warning.** The determinant is not a norm on the full algebra: it is quartic, it takes the value zero on a cone, and it is not positive. It is the square of the quaternionic norm, and the quaternionic norm is the honest multiplicative invariant of degree two.

**Proof.** $\det=N^{2}$ and $N$ vanishes on the cone $Q_t^{2}+B^{2}=0$.

**Corollary.** A statement of the form "the norm of a product is the product of the norms" is a statement about $N$ or $\det$ only.

## Summary

The element carries four quadratic invariants, each a quarter-trace: the plain $Q_t^{2}-B^{2}$, the quaternionic $Q_t^{2}+B^{2}$, the Hermitian $\sum|Q_\mu|^{2}$ and the Krein $|Q_t|^{2}-\sum_k|Q_k|^{2}$, with the trace $4Q_t$ linear and the determinant $N^{2}$ quartic. The quarter is the block factor, four being twice the repetition and twice the quadratic word.

The quaternionic norm and the determinant are multiplicative; the plain, Hermitian and Krein forms are not. Only the Hermitian form is positive definite on the complex algebra; over the reals the plain form is positive on the scalar line and negative on the vector space, the quaternionic one is positive definite, and the Krein one has inertia $(2,6)$.

The invariance groups are $\mathrm{GL}_4$ for the plain form, $O(4,\mathbb{C})$ for the quaternionic and Krein forms, and $U(4)$ for the Hermitian one. The transpose equals the quaternion conjugation only in the axis-free frame, and the determinant is the square of a norm and not a norm itself.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P=\tfrac14\operatorname{tr}(A^{2})$ | the plain form, $Q_t^{2}-B^{2}$ |
| $N=\tfrac14\operatorname{tr}(A^{\mathsf T}A)$ | the quaternionic norm, $Q_t^{2}+B^{2}$ |
| $H=\tfrac14\operatorname{tr}(A^{\ast}A)$ | the Hermitian form, positive definite |
| $K=|c_t|^{2}-\sum_k|c_k|^{2}$ | the Krein form, inertia $(2,6)$ |
| $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}$ | the squared vector length |
| $\det A=N^{2}$ | the determinant as the square of a norm |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for norms on algebras, multiplicative forms and composition.
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the biquaternion original of the table.
- [The Axis-Free Representation of $M_4(\mathbb{C})$](m4c-axis-free-representation.html), for §*The Four Norms* and the transpose.
- [The Hilbert–Schmidt Form at $n=4$](the-hilbert-schmidt-form-at-n-4.html), for the form that supplies $H$.
- [The Four Forms and Their Algebraic Norms at $n=2$](the-four-forms-and-their-algebraic-norms-at-n-2.html), for the same four forms at order two.
