# __$M_4(\mathbb{C})$ Representation : The Conjugations and the Adjoints__

## Introduction

The four involutions of the biquaternion algebra become four matrix operations in the regular model: the transpose, the entrywise conjugation, the conjugate transpose and its negative. The dictionary is simpler than in the $2\times2$ model, because complex conjugation is now entrywise and the antisymmetric dressing disappears; the price is that the adjugate of the $4\times4$ matrix is no longer a linear involution.

This article proves the four formulas, identifies the fixed spaces and relates the operations to the right regular matrix. It is the $4\times4$ counterpart of *$M_2(\mathbb{C})$ Representation : The Conjugations and the Adjoints*.

**Conventions.** The algebra and the model are those of *$M_4(\mathbb{C})$ Model : The Product, the Trace and the Determinant*. The four involutions are
$$
\tilde Q^{\natural}=Q_t-\vec Q,\qquad
\overline{\tilde Q}=\overline{Q_t}+\overline{\vec Q},\qquad
\tilde Q^{*}=\overline{\tilde Q^{\natural}},\qquad
\tilde Q^{\flat}=-\tilde Q^{*}.
$$
The matrix is $M=\mathsf{M}_4^{L}(\tilde Q)$.

**Boundaries.** The fixed spaces are *$M_4(\mathbb{C})$ Model : The Six Subspaces as Matrix Conditions*; the four forms are *$M_4(\mathbb{C})$ Representation : The Four Words and the Four Traces*; the right regular matrix is *$M_4(\mathbb{C})$ Model : The Centraliser and the Double Centraliser*, §*The Right Regular Image*; the $2\times2$ version is *$M_2(\mathbb{C})$ Representation : The Conjugations and the Adjoints*.

**Frame.** This article uses the coefficient basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$, because that is the basis in which quaternion conjugation is transposition: $\mathsf M_4^{L}(\tilde Q^{\natural})=M^{\mathsf T}$. The canonical frame of *Conventions in Mathematics*, §*The Matrix Models*, is the Peirce frame, where $\mathsf M_4^{L}(\tilde Q)=I_2\otimes\mathsf M_2(\tilde Q)$; the two displays differ by the change $S$ of *The Product, the Trace and the Determinant*. In the canonical frame the same involution is $M\mapsto C\,M^{\mathsf T}\,C^{-1}$ with $C=R_y=-i\sigma_2\otimes\mathrm I_2$.

## The Four Involutions

**Theorem.** For every $\tilde Q$,

$$
\mathsf{M}_4^{L}(\tilde Q^{\natural})=M^{\mathsf T},\qquad
\mathsf{M}_4^{L}(\overline{\tilde Q})=\overline M,\qquad
\mathsf{M}_4^{L}(\tilde Q^{*})=M^{\dagger},\qquad
\mathsf{M}_4^{L}(\tilde Q^{\flat})=-M^{\dagger}.
$$

*Proof.* The first is checked entrywise: transposing the displayed matrix changes the signs of the three vector coefficients, which is quaternion conjugation. The second is immediate because every entry of $M$ is a coefficient of $\tilde Q$ with a sign, so conjugating the entries conjugates the coefficients. The third follows from the first two: $M^{\dagger}=\overline{M^{\mathsf T}}=\mathsf{M}_4^{L}(\overline{\tilde Q^{\natural}})=\mathsf{M}_4^{L}(\tilde Q^{*})$. The fourth is the definition of $\flat$.

**The table.**

| Involution | Algebra definition | Matrix operation | Fixed space | Anti-fixed space |
|---|---|---|---|---|
| ${}^{\natural}$ | $Q_t-\vec Q$ | $M^{\mathsf T}$ | centre | vector subspace |
| $\bar{\cdot}$ | $\overline{Q_\mu}$ | $\overline M$ | quaternion subspace | anti-quaternion subspace |
| ${}^{*}$ | $\overline{Q_t}-\overline{\vec Q}$ | $M^{\dagger}$ | $\mathbb{M}_+$ | $\mathbb{M}_-$ |
| ${}^{\flat}$ | $-\tilde Q^{*}$ | $-M^{\dagger}$ | $\mathbb{M}_-$ | $\mathbb{M}_+$ |

The table is the complete dictionary. Each row is proved by applying the formula and reading the coefficient condition; the details are in the six-subspaces article.

**The relations.** The first three generate a Klein four-group,
$$
{}^{*}=\bar{\cdot}\circ{}^{\natural}={}^{\natural}\circ\bar{\cdot},
\qquad
\bar{\cdot}={}^{*}\circ{}^{\natural}={}^{\natural}\circ{}^{*},
\qquad
{}^{\natural}={}^{*}\circ\bar{\cdot}=\bar{\cdot}\circ{}^{*}.
$$
The fourth is the negative of the third, $\flat=-{}^{*}$; it is an involution, but it is not an anti-automorphism: the minus sign gives $\flat(PQ)=-\flat(Q)\flat(P)$, so it is not in the Klein group.

## The Adjugate

**Quaternion conjugation is transposition.** The identity
$$
\mathsf{M}_4^{L}(\tilde Q^{\natural})=M^{\mathsf T}
$$
is the cleanest statement of the regular model. The fixed matrices are the symmetric ones; the condition $M^{\mathsf T}=M$ is $Q^{\natural}=Q$, hence $\vec Q=0$. The fixed space is the centre and the anti-fixed space is the vector subspace.

**The adjugate is the transpose scaled by the norm.**
$$
\operatorname{adj}M=\langle\tilde Q\rangle_{\natural}\,M^{\mathsf T}
=\langle\tilde Q\rangle_{\natural}\,\mathsf{M}_4^{L}(\tilde Q^{\natural}).
$$
*Proof.* For invertible $M$, the adjugate is $\det(M)M^{-1}=N^2M^{-1}$, and $M^{-1}=M^{\mathsf T}/N$, so the formula holds. Both sides are polynomial in the coefficients and the invertible elements are dense, so the identity extends to all $\tilde Q$.

For singular $\tilde Q$ the norm vanishes, and the adjugate of a rank-two $4\times4$ matrix is zero; the formula gives zero on both sides.

**The properties.** The adjugate is an anti-automorphism,
$$
\operatorname{adj}(MX)=\operatorname{adj}(X)\operatorname{adj}(M),
\qquad
M\operatorname{adj}M=(\det M)\mathrm I_4,
$$
but it is not an involution: $\operatorname{adj}(\operatorname{adj}M)=N^4M$. It is homogeneous of degree three, while the quaternion conjugation is linear; the two differ by the quadratic norm. The fixed space of the adjugate is the centre, as in the $2\times2$ model, and the anti-fixed space is the vector subspace.

**The right regular matrix.** The transpose also determines the right regular matrix:
$$
\mathsf{M}_4^{R}(\tilde Q)=D\,M^{\mathsf T}D=D\,\mathsf{M}_4^{L}(\tilde Q^{\natural})D,
\qquad
D=\operatorname{diag}(1,-1,-1,-1).
$$
The sign matrix $D$ is the price of using the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ instead of a basis adapted to the right action. In the Peirce basis the right matrix is $\mathsf{M}_2(\tilde Q)^{\mathsf T}\otimes\mathrm I_2$.

## Complex Conjugation

**Complex conjugation is entrywise.** In the regular model,
$$
\mathsf{M}_4^{L}(\overline{\tilde Q})=\overline M,
$$
with no dressing. This is the main simplification with respect to the $2\times2$ model, where the entrywise conjugate is the image of a fifth involution, $\sigma(\tilde Q)=\overline{Q_t}-\overline{Q_x}\vec e_x+\overline{Q_y}\vec e_y-\overline{Q_z}\vec e_z$, and complex conjugation must be dressed by $\epsilon$.

**Why the dressing disappears.** The regular basis $e_t,\vec e_x,\vec e_y,\vec e_z$ is stable under coefficient conjugation, and the entries of the regular matrix are single coefficients. In the $2\times2$ model the entries are combinations such as $-iQ_x-Q_y$, and conjugating them conjugates both the coefficient and the central $i$, which is not the same as conjugating the coefficient alone. The dressing by $\epsilon$ corrects the combination. In the regular model there is no combination to correct.

**The fixed space.** The condition $\overline M=M$ is the reality of all four coefficients, so the fixed space is the quaternion subspace and the anti-fixed space is the anti-quaternion subspace. The matrices are the real and the purely imaginary matrices of the regular form.

## Hermitian and Anti-Hermitian Conjugation

**The dagger is the conjugate transpose.**
$$
\mathsf{M}_4^{L}(\tilde Q^{*})=M^{\dagger}=\overline{M}^{\mathsf T}.
$$
The fixed matrices are the Hermitian ones, the image of $\mathbb{M}_+$, and the anti-fixed ones are the anti-Hermitian matrices, the image of $\mathbb{M}_-$. The trace is real on the Hermitian subspace and purely imaginary on the anti-Hermitian one.

**The anti-Hermitian conjugation.**
$$
\mathsf{M}_4^{L}(\tilde Q^{\flat})=-M^{\dagger}.
$$
Its fixed space is the anti-Hermitian image and its anti-fixed space is the Hermitian one. The two rows of the table for ${}^{*}$ and ${}^{\flat}$ are exchanged, as they must be, because $\flat=-{}^{*}$.

**The positive structure.** The dagger is the only one of the four operations that is positive: $M^{\dagger}M$ is Hermitian and positive semidefinite for every $M$, and its trace is four times the Hermitian norm. The other three operations do not define a positive form.

## The Four Adjoints

**The four words.** The four involutions are the switches of the four forms. With $X=\mathsf{M}_4^{L}(\tilde P)$ and $Y=\mathsf{M}_4^{L}(\tilde Q)$,
$$
\tfrac14\operatorname{Tr}(XY)=\langle\tilde P,\tilde Q\rangle,\qquad
\tfrac14\operatorname{Tr}(X^{\mathsf T}Y)=\langle\tilde P,\tilde Q\rangle_{\natural},
$$
$$
\tfrac14\operatorname{Tr}(XY^{\dagger})=\langle\tilde P,\tilde Q\rangle_{*},\qquad
\tfrac14\operatorname{Tr}(X^{\mathsf T}Y^{\dagger})=\langle\tilde P,\tilde Q\rangle_{\natural*}.
$$
The first form uses no involution, the second uses the transpose in the first slot, the third the dagger in the second slot, and the fourth both.

**The element-level and operator-level adjoints.** The transpose and the dagger are element-level operations on matrices; the adjoint of a linear map is a different object, defined by $\varphi(Tx,y)=\varphi(x,T^{\varphi}y)$. The two are related by the Gram matrix of the form, and the relation is the four-adjoint theory of *The Four Adjoints of the Biquaternion Algebra in Examples*. In the regular model the Gram matrices are the identity or $\operatorname{diag}(1,-1,-1,-1)$, so the operator adjoints are the transposes and daggers composed with the sign matrix.

## The Adjugate of the Dagger

**The identity.**
$$
\operatorname{adj}(M^{\dagger})=(\operatorname{adj}M)^{\dagger}
=\langle\tilde Q\rangle_{\natural}\,\bar M,
$$
because the adjugate is a polynomial in $M$ with real coefficients, so it commutes with the dagger, and $M^{\dagger\mathsf T}=\bar M$.

**The Klein group fails by one.** The three operations $\operatorname{adj}$, ${}^{\dagger}$ and $\operatorname{adj}\circ{}^{\dagger}$ do not form a Klein four-group in the regular model, because $\operatorname{adj}$ is not an involution: $\operatorname{adj}^2(M)=N^4M$. The involutions are the transpose $M^{\mathsf T}$, the entrywise conjugation $\bar M$, the dagger $M^{\dagger}$ and its negative $-M^{\dagger}$. They satisfy
$$
{}^{\dagger}=\bar{\cdot}\circ{}^{\mathsf T}={}^{\mathsf T}\circ\bar{\cdot},
\qquad
\bar{\cdot}={}^{\dagger}\circ{}^{\mathsf T}={}^{\mathsf T}\circ{}^{\dagger},
$$
and the fourth is $-{}^{\dagger}$. The adjugate is outside this group by the scalar factor $N$, and that factor is the whole difference from the $2\times2$ model.

**The algebra reading.** The identity is the matrix form of $\bar{\cdot}={}^{\natural}\circ{}^{*}={}^{*}\circ{}^{\natural}$ composed with the norm: the algebra conjugation is the adjugate of the Hermitian conjugate up to the norm, and the two operations commute because one acts on the order of the factors and the other on their values. The scalar $N$ is invisible in the algebra, where the conjugation is linear, and visible in the matrix, where the adjugate is cubic.

## Summary

The four involutions become the transpose, the entrywise conjugation, the conjugate transpose and its negative. The transpose is quaternion conjugation, the entrywise conjugation is complex conjugation with no dressing, and the dagger is Hermitian conjugation. Their fixed spaces are the centre, the quaternion subspace, the two sectors, and the anti-fixed spaces are the complementary three. The adjugate of the regular matrix is the norm times the transpose, a cubic operation, not the linear adjugate of the $2\times2$ model.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M^{\mathsf T}$ | the image of ${}^{\natural}$ |
| $\overline M$ | the image of $\bar{\cdot}$ |
| $M^{\dagger}$ | the image of ${}^{*}$ |
| $-M^{\dagger}$ | the image of ${}^{\flat}$ |
| $\operatorname{adj}M=N M^{\mathsf T}$ | the adjugate of the regular matrix |
| $D=\operatorname{diag}(1,-1,-1,-1)$ | the sign matrix of the right regular matrix |

## Further Reading

- [$M_4(\mathbb{C})$ Model : The Six Subspaces as Matrix Conditions](m4c-model-the-six-subspaces-as-matrix-conditions.html), for the fixed spaces
- [$M_4(\mathbb{C})$ Model : The Centraliser and the Double Centraliser](m4c-model-the-centraliser-and-the-double-centraliser.html), §*The Right Regular Image*, for the relation with the right matrix
- [$M_2(\mathbb{C})$ Representation : The Conjugations and the Adjoints](m2c-representation-the-conjugations-and-the-adjoints.html), for the $2\times2$ dictionary
- [The Group of Involutions](the-group-of-involutions.html), for the abstract involutions
- [The Four Adjoints of the Biquaternion Algebra in Examples](the-four-adjoints-of-the-biquaternion-algebra-in-examples.html), for the operator-level adjoints
