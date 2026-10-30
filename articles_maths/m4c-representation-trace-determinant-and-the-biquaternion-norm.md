# __$M_4(\mathbb{C})_{\mathbb{B}}$ Representation : Trace, Determinant and the Biquaternion Norm__

## Introduction

The trace of the regular matrix is four times the scalar part and the determinant is the square of the quaternionic norm. The doubling of the spectrum squares the determinant and doubles the trace; the norm itself survives as a quarter-trace of a word, not as the determinant.

This article develops the two invariants, the four algebraic norms as matrix invariants, the characteristic and minimal polynomials, and the singular locus. It is the $4\times4$ counterpart of *$M_2(\mathbb{C})$ Representation : Trace, Determinant and the Biquaternion Norm*.

**Conventions.** The algebra and the model are those of *$M_4(\mathbb{C})_{\mathbb{B}}$ Model : The Product, the Trace and the Determinant*. Write $\mathsf{M}_4^{L}(\tilde Q)=M$, $\langle\tilde Q\rangle_{\natural}=Q_t^2+Q_x^2+Q_y^2+Q_z^2$, $B^2=Q_x^2+Q_y^2+Q_z^2$ and $\lambda_\pm=Q_t\pm iB$.

**Boundaries.** The determinant as a group homomorphism is *$M_4(\mathbb{C})_{\mathbb{B}}$ Representation : $GL_2(\mathbb{C})$, $SL_2(\mathbb{C})$ and the Determinant*; the rank stratification is *$M_4(\mathbb{C})_{\mathbb{B}}$ Representation : Rank-One Matrices and the Determinantal Variety*; the four forms are *$M_4(\mathbb{C})_{\mathbb{B}}$ Representation : The Four Words and the Four Traces*. The $2\times2$ version is *$M_2(\mathbb{C})$ Representation : Trace, Determinant and the Biquaternion Norm*.

**Frame.** This article uses the coefficient basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$, because that is the basis in which quaternion conjugation is transposition: $\mathsf M_4^{L}(\tilde Q^{\natural})=M^{\mathsf T}$. The canonical frame of *Conventions of the Representations*, §*The Matrix Models*, is the Peirce frame, where $\mathsf M_4^{L}(\tilde Q)=I_2\otimes\mathsf M_2(\tilde Q)$; the two displays differ by the change $S$ of *The Product, the Trace and the Determinant*. In the canonical frame the same involution is $M\mapsto C\,M^{\mathsf T}\,C^{-1}$ with $C=-\sigma_2\otimes\sigma_2$, the signed reversal of the four Peirce coordinates.

## The Trace

**The trace is four times the scalar part.**

$$
\operatorname{Tr}M=4Q_t,\qquad Q_t=\tfrac14\operatorname{Tr}M.
$$

The trace kills the vector part and is blind to the two copies: each block contributes $2Q_t$, and the two blocks together contribute $4Q_t$. It is $\mathbb{C}$-linear and invariant under conjugation by units.

**The trace of a power.** Since $M=\mathrm I_2\otimes\mathsf{M}_2(\tilde Q)$,

$$
\operatorname{Tr}(M^k)=2\operatorname{Tr}\bigl(\mathsf{M}_2(\tilde Q)^k\bigr)
$$

for every $k\ge1$. The trace of the square is $4(Q_t^2-B^2)=4P$, where $P$ is the plain norm. The trace of the cube is $2(2Q_t^3-6Q_tB^2)=4Q_t(Q_t^2-3B^2)$.

**The trace is not the norm.** It is additive and complex-valued; it does not detect the vector part, and it does not see the doubling except through the factor four. An element with $Q_t=0$ is traceless whatever its vector part.

## The Determinant

**The determinant is the squared norm.**

$$
\det M=\langle\tilde Q\rangle_{\natural}^2
=(Q_t^2+B^2)^2.
$$

*Proof.* The block form gives $\det M=\det\mathsf{M}_2(\tilde Q)^2$ and $\det\mathsf{M}_2(\tilde Q)=\langle\tilde Q\rangle_{\natural}$.

The determinant is multiplicative, $\det(M_PM_Q)=\det M_P\det M_Q$, and invariant under conjugation, $\det(PMP^{-1})=\det M$. Its modulus is the squared modulus of the norm, and its argument is twice the argument of the norm:
$$
\lvert\det M\rvert=\lvert\langle\tilde Q\rangle_{\natural}\rvert^2,
\qquad
\arg\det M=2\arg\langle\tilde Q\rangle_{\natural}.
$$

**Invertibility.** The matrix is invertible exactly when the norm is nonzero:
$$
M\text{ invertible}\iff\tilde Q\text{ is a unit}\iff\langle\tilde Q\rangle_{\natural}\neq0.
$$
The inverse is
$$
M^{-1}=\mathsf{M}_4^{L}(\tilde Q^{-1})=\frac{\mathsf{M}_4^{L}(\tilde Q^{\natural})}{\langle\tilde Q\rangle_{\natural}}
=\frac{M^{\mathsf T}}{\langle\tilde Q\rangle_{\natural}},
$$
because the transpose is quaternion conjugation in the regular model. Compare the $2\times2$ formula, where the numerator is the adjugate; in the $4\times4$ model the adjugate is degree three and the transpose is the linear object.

**The zero divisors.** A nonzero singular regular matrix has rank two, not rank one. The singular nonzero elements form the null cone $\{\langle\tilde Q\rangle_{\natural}=0\}$, and the zero matrix is its apex. The cone is the determinantal variety of the regular model.

## The Four Norms as Matrix Invariants

The four algebraic norms are four quarter-traces of words in $M$ and its transpose and dagger.

| Norm | Algebra value | Matrix formula | Value ring | Definite |
|---|---|---|---|---|
| Plain $P$ | $Q_t^2-Q_x^2-Q_y^2-Q_z^2$ | $\tfrac14\operatorname{Tr}(M^2)$ | $\mathbb{C}$ | no |
| Quaternionic $N$ | $Q_t^2+Q_x^2+Q_y^2+Q_z^2$ | $\tfrac14\operatorname{Tr}(M^{\mathsf T}M)$ | $\mathbb{C}$ | no |
| Hermitian $H$ | $\sum_\mu\lvert Q_\mu\rvert^2$ | $\tfrac14\operatorname{Tr}(M^{\dagger}M)$ | $\mathbb{R}$ | yes |
| Krein $K$ | $\lvert Q_t\rvert^2-\sum_k\lvert Q_k\rvert^2$ | $\tfrac14\operatorname{Tr}(M^{\mathsf T}M^{\dagger})$ | $\mathbb{R}$ | no |

*Proof.* The block form and the identities $M^{\mathsf T}=\mathsf{M}_4^{L}(\tilde Q^{\natural})$, $M^{\dagger}=\mathsf{M}_4^{L}(\tilde Q^{*})$ reduce each quarter-trace to the scalar part of the corresponding product. For the quaternionic norm, $\tilde Q^{\natural}\tilde Q=\langle\tilde Q\rangle_{\natural}e_t$; for the Hermitian norm, $\tilde Q^{*}\tilde Q=He_t$; for the Krein norm, $\tilde Q^{\natural}\tilde Q^{*}=Ke_t$. The plain norm is $\tilde Q^2$ read in the scalar part.

**The quaternionic norm is not the determinant.** In the $2\times2$ model $\det\mathsf{M}_2(\tilde Q)=N$. In the $4\times4$ model $\det M=N^2$, and $N$ itself is the quarter-trace of $M^{\mathsf T}M$. The determinant is the square of the norm because the regular representation contains two copies of the defining module; the norm is recovered from the matrix by a word, not by the determinant.

**The signatures.** The Hermitian norm is positive definite; the Krein norm has signature $(2,6)$ on the real algebra; the plain and quaternionic norms are complex-valued and have no sign. The table is the regular-model form of the four-norm table of *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*.

## The Characteristic Polynomial

**The characteristic polynomial is the square of the biquadratic.**

$$
\chi_M(t)=\bigl(t^2-2Q_tt+\langle\tilde Q\rangle_{\natural}\bigr)^2
=t^4-4Q_tt^3+(4Q_t^2+2\langle\tilde Q\rangle_{\natural})t^2-4Q_t\langle\tilde Q\rangle_{\natural}t+\langle\tilde Q\rangle_{\natural}^2.
$$

*Proof.* The block form gives $\chi_M(t)=\chi_{\mathsf{M}_2(\tilde Q)}(t)^2$.

The roots are $\lambda_+=Q_t+iB$ and $\lambda_-=Q_t-iB$, each of algebraic multiplicity two. The discriminant of the quadratic factor is $-4B^2$, so the eigenvalues are distinct exactly when $B^2\neq0$. When $B^2=0$, the four eigenvalues coincide at $Q_t$.

**The minimal polynomial does not square.** If $\tilde Q$ is scalar, the minimal polynomial is $t-Q_t$. If $\tilde Q$ is not scalar, the minimal polynomial is
$$
t^2-2Q_tt+\langle\tilde Q\rangle_{\natural},
$$
of degree two, even when the eigenvalues coincide. The regular matrix is never nonderogatory: its minimal polynomial has degree at most two, while its characteristic polynomial has degree four.

**Cayley–Hamilton.** The matrix satisfies
$$
M^2-2Q_tM+\langle\tilde Q\rangle_{\natural}\mathrm I_4=0,
$$
and therefore also $\chi_M(M)=0$. The degree-two identity is the block form of the $2\times2$ Cayley–Hamilton identity; the degree-four identity is its square and carries no additional information.

## The Determinant and the Euclidean Norm

Over $\mathbb{C}$ the determinant is a complex volume. Its modulus is the real volume of the image of the unit cube, and its argument is twice the phase of the linear map. On the Hermitian and anti-Hermitian subspaces the norm is real, so the determinant is real and non-negative. On the null cone the volume vanishes.

The Euclidean norm of the element is
$$
\lVert\tilde Q\rVert_E=\sqrt{H}=\sqrt{\sum_\mu\lvert Q_\mu\rvert^2},
$$
and the modulus of the determinant is $\lvert\det M\rvert=\lvert N\rvert^2$, not $\lvert\tilde Q\rvert^4$. The inequality
$$
\lvert N\rvert\le H
$$
is the triangle inequality for the four squares $Q_\mu^2$, with equality exactly when the four squares are non-negative real multiples of one another, that is, when all four coefficients lie on one real line through the origin. Normality does not force equality: $\tilde Q=e_t+i\vec e_x$ is normal, with $N=0$ and $H=2$.

## Summary

The trace is $4Q_t$ and the determinant is the squared norm $\langle\tilde Q\rangle_{\natural}^2$. The four algebraic norms are quarter-traces of the words $M^2$, $M^{\mathsf T}M$, $M^{\dagger}M$ and $M^{\mathsf T}M^{\dagger}$. The characteristic polynomial is the square of the $2\times2$ one, with eigenvalues $\lambda_\pm$ doubled, while the minimal polynomial keeps degree at most two. The singular nonzero matrices have rank two and form the null cone.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M=\mathsf{M}_4^{L}(\tilde Q)$ | the regular matrix |
| $\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2$ | the quaternionic norm |
| $P,N,H,K$ | the plain, quaternionic, Hermitian and Krein norms |
| $\lambda_\pm=Q_t\pm iB$ | the eigenvalues, each double |
| $\chi_M(t)$ | the characteristic polynomial |

## Further Reading

- [$M_4(\mathbb{C})_{\mathbb{B}}$ Representation : The Four Words and the Four Traces](m4c-representation-the-four-words-and-the-four-traces.html), for the trace normalization
- [$M_4(\mathbb{C})_{\mathbb{B}}$ Representation : Rank-One Matrices and the Determinantal Variety](m4c-representation-rank-one-matrices-and-the-determinantal-variety.html), for the null cone
- [$M_4(\mathbb{C})_{\mathbb{B}}$ Representation : $GL_2(\mathbb{C})$, $SL_2(\mathbb{C})$ and the Determinant](m4c-representation-gl2-sl2-and-the-determinant.html), for the groups
- [$M_2(\mathbb{C})$ Representation : Trace, Determinant and the Biquaternion Norm](m2c-representation-trace-determinant-and-the-biquaternion-norm.html), for the $2\times2$ version
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the norms
