# __Matrix Representations : Trace, Determinant and the Biquaternion Norm__

## Introduction

The trace of the $2\times2$ model is twice the scalar part and the trace of the $4\times4$ model is four times it. The determinant of the first is the quaternionic norm and the determinant of the second is its square. The norm itself survives in the $4\times4$ display as a quarter-trace of a word, not as the determinant.

**The subject.** This article develops the four algebraic norms as matrix invariants, the characteristic and minimal polynomials in the two sizes, and the singular set. The basic trace and determinant are *Matrix Representations : The Product, the Trace and the Determinant*; this article uses them and goes to the finer invariants.

**The one law.** Every difference between the two sizes follows from the block form $\mathsf M_4^{L}=\mathrm I_2\otimes\mathsf M_2$: the trace doubles, the determinant squares, the characteristic polynomial squares, and the minimal polynomial does not.

**Conventions.** The algebra is that of *The Biquaternion Algebra*; the displays and the change $C_{\Pi}$ are those of *Matrix Representations : The Models and the Change of Frame*. Write $\mathsf{M}_4^{L}(\tilde Q)=M$, $\langle\tilde Q\rangle_{\natural}=Q_t^2+Q_x^2+Q_y^2+Q_z^2$, $B^2=Q_x^2+Q_y^2+Q_z^2$ and $\lambda_\pm=Q_t\pm iB$.

**Boundaries.** The four forms are *Matrix Representations : The Four Words and the Four Traces*; the basic invariants are *Matrix Representations : The Product, the Trace and the Determinant*.

**Frame.** This article uses the coefficient basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$, because that is the basis in which quaternion conjugation is transposition: $\mathsf M_4^{L}(\tilde Q^{\natural})=M^{\mathsf T}$. The canonical frame of *Matrix Representations Conventions*, §*The Matrix Models*, is the Peirce frame, where $\mathsf M_4^{L}(\tilde Q)=I_2\otimes\mathsf M_2(\tilde Q)$; the two displays differ by the Peirce change $C_{\Pi}$ of *Matrix Representations : The Models and the Change of Frame*. In the canonical frame the same involution is $M\mapsto C\,M^{\mathsf T}\,C^{-1}$ with $C=-\sigma_2\otimes\sigma_2$, the signed reversal of the four Peirce coordinates.

## Common Aspects

Every difference between the two sizes follows from one identity, $\mathsf M_4^{L}=\mathrm I_2\otimes\mathsf M_2$: the trace doubles, the determinant squares, the characteristic polynomial squares, and the minimal polynomial does not. The four algebraic norms survive as quarter-traces of words, not as determinants. This section states the laws that hold in every display; the three sections below write them.

**The trace.** The trace is $4Q_t$ in the regular model and $2Q_t$ in the entry model. It kills the vector part and is blind to the two copies: each block contributes $2Q_t$, and the two blocks together $4Q_t$. It is $\mathbb{C}$-linear and invariant under conjugation by units.

**The determinant.** The determinant is the squared norm,
$$
\det M=\langle\tilde Q\rangle_{\natural}^2=(Q_t^2+B^2)^2,
$$
and the entry determinant is $\langle\tilde Q\rangle_{\natural}$. The determinant is multiplicative and invariant under conjugation. Its modulus is the squared modulus of the norm and its argument is twice the argument of the norm:
$$
\lvert\det M\rvert=\lvert\langle\tilde Q\rangle_{\natural}\rvert^2,
\qquad
\arg\det M=2\arg\langle\tilde Q\rangle_{\natural}.
$$

**Invertibility and the null cone.** The matrix is invertible exactly when the norm is nonzero, and a nonzero singular regular matrix has rank two, never rank one. The singular nonzero elements form the null cone $\{\langle\tilde Q\rangle_{\natural}=0\}$, with the zero matrix as its apex. The cone is the singular set of the regular model.

**The four norms.** The plain, quaternionic, Hermitian and Krein norms are the scalar parts of the products $\tilde Q^2$, $\tilde Q^{\natural}\tilde Q$, $\tilde Q^{*}\tilde Q$ and $\tilde Q^{\natural}\tilde Q^{*}$:

| Norm | Algebra value | Definite |
|---|---|---|
| Plain $P$ | $Q_t^2-Q_x^2-Q_y^2-Q_z^2$ | no |
| Quaternionic $N$ | $Q_t^2+Q_x^2+Q_y^2+Q_z^2$ | no |
| Hermitian $H$ | $\sum_\mu\lvert Q_\mu\rvert^2$ | yes |
| Krein $K$ | $\lvert Q_t\rvert^2-\sum_k\lvert Q_k\rvert^2$ | no |

The Hermitian norm is positive definite; the Krein norm has signature $(2,6)$ on the real algebra; the plain and quaternionic norms are complex-valued and have no sign.

**The characteristic and minimal polynomials.** The characteristic polynomial of the operator is the square of the entry characteristic polynomial. Its roots are $\lambda_\pm=Q_t\pm iB$, each of algebraic multiplicity two, and they are distinct exactly when $B^2\neq0$. The minimal polynomial is $t-Q_t$ for a scalar and $t^2-2Q_tt+\langle\tilde Q\rangle_{\natural}$ otherwise, of degree two even when the eigenvalues coincide. The regular matrix is never nonderogatory.

**The Euclidean norm.** $\lVert\tilde Q\rVert_E=\sqrt{H}$, and $\lvert\det M\rvert=\lvert N\rvert^2$, not $\lvert\tilde Q\rvert^4$. The inequality $\lvert N\rvert\le H$ is the triangle inequality for the four squares $Q_\mu^2$, with equality exactly when the four squares are non-negative real multiples of one another. Normality does not force equality: $\tilde Q=e_t+i\vec e_x$ is normal, with $N=0$ and $H=2$.

## The Coefficient Frame

**The trace and its powers.** In the coefficient frame $M=\mathsf M_4^{L}(\tilde Q)$ and $\operatorname{Tr}M=4Q_t$, so $Q_t=\tfrac14\operatorname{Tr}M$. Since $M=\mathrm I_2\otimes\mathsf M_2(\tilde Q)$,

$$
\operatorname{Tr}(M^k)=2\operatorname{Tr}\bigl(\mathsf M_2(\tilde Q)^k\bigr)
$$

for every $k\ge1$. The trace of the square is $4(Q_t^2-B^2)=4P$, and the trace of the cube is $4Q_t(Q_t^2-3B^2)$.

**The determinant and the inverse.** The determinant is $\langle\tilde Q\rangle_{\natural}^2$, and the inverse is
$$
M^{-1}=\mathsf M_4^{L}(\tilde Q^{-1})=\frac{\mathsf M_4^{L}(\tilde Q^{\natural})}{\langle\tilde Q\rangle_{\natural}}
=\frac{M^{\mathsf T}}{\langle\tilde Q\rangle_{\natural}},
$$
because the transpose is quaternion conjugation in the coefficient frame. The numerator is the transpose, not the adjugate: the adjugate of a $4\times4$ matrix is homogeneous of degree three, while $\mathsf M_4^{L}(\tilde Q^{\natural})$ is linear.

**The characteristic polynomial.** Written out,
$$
\chi_M(t)=\bigl(t^2-2Q_tt+\langle\tilde Q\rangle_{\natural}\bigr)^2
=t^4-4Q_tt^3+(4Q_t^2+2\langle\tilde Q\rangle_{\natural})t^2-4Q_t\langle\tilde Q\rangle_{\natural}t+\langle\tilde Q\rangle_{\natural}^2.
$$
Cayley–Hamilton gives $M^2-2Q_tM+\langle\tilde Q\rangle_{\natural}\mathrm I_4=0$, the block form of the entry identity; the degree-four identity is its square and carries no additional information.

**The four norms.** They are the quarter-traces of the four words:

| Norm | Matrix formula |
|---|---|
| Plain $P$ | $\tfrac14\operatorname{Tr}(M^2)$ |
| Quaternionic $N$ | $\tfrac14\operatorname{Tr}(M^{\mathsf T}M)$ |
| Hermitian $H$ | $\tfrac14\operatorname{Tr}(M^{\dagger}M)$ |
| Krein $K$ | $\tfrac14\operatorname{Tr}(M^{\mathsf T}M^{\dagger})$ |

Each reduces to the scalar part of the corresponding product: $\tilde Q^{\natural}\tilde Q=Ne_t$, $\tilde Q^{*}\tilde Q=He_t$ and $\tilde Q^{\natural}\tilde Q^{*}=Ke_t$. The determinant is the square of the quaternionic norm; the norm itself is recovered by the word $M^{\mathsf T}M$, not by the determinant.

## The Entry Model

**The invariants.** In the entry model, with $X=\mathsf M_2(\tilde Q)$,

$$
\operatorname{tr}X=2Q_t,\qquad
\det X=\langle\tilde Q\rangle_{\natural},
\qquad
X^{-1}=\frac{\operatorname{adj}X}{\langle\tilde Q\rangle_{\natural}}.
$$

The inverse formula is the matrix form of $\tilde Q\tilde Q^{\natural}=\langle\tilde Q\rangle_{\natural}e_t$: the adjugate is the image of ${}^{\natural}$.

**The characteristic polynomial.** It is the biquadratic itself,
$$
\chi_X(t)=t^2-2Q_tt+\langle\tilde Q\rangle_{\natural},
$$
with roots $\lambda_\pm=Q_t\pm iB$. Its discriminant is $-4B^2$, so the roots are distinct exactly when $B^2\neq0$. The minimal polynomial is the characteristic polynomial for a non-scalar element, and $t-Q_t$ for a scalar.

**The four norms.** The entry model computes them by half-traces:

| Norm | $2\times2$ formula |
|---|---|
| Plain $P$ | $\tfrac12\operatorname{tr}(X^2)$ |
| Quaternionic $N$ | $\tfrac12\operatorname{tr}(X^{\mathsf T}X)$ |
| Hermitian $H$ | $\tfrac12\operatorname{tr}(X^{\dagger}X)$ |
| Krein $K$ | $\tfrac12\operatorname{tr}(X^{\mathsf T}X^{\dagger})$ |

The values are the same as in the regular model. The factor is $\tfrac12$ rather than $\tfrac14$ because the identity has trace $2$ rather than $4$.

## The Peirce Frame

**The block invariants.** In the Peirce frame $M=\operatorname{diag}(B,B)$ with $B=\mathsf M_2(\tilde Q)$. The trace is $2\operatorname{tr}B=4Q_t$, the determinant is $\det(B)^2=\langle\tilde Q\rangle_{\natural}^2$, and the inverse is $\operatorname{diag}(B^{-1},B^{-1})$. Every invariant is the entry invariant read twice, with the trace doubled and the determinant squared.

**The spectrum.** The block matrix has the spectrum of $B$, each eigenvalue twice. The characteristic polynomial is $\chi_B(t)^2$, with roots $\lambda_\pm$ of multiplicity two. The minimal polynomial is $\chi_B(t)$ itself, of degree two, because the two blocks are equal: the operator is never nonderogatory.

**The four norms.** The quarter-traces of the block words are the half-traces of the entry words, because $\operatorname{Tr}(\mathrm I_2\otimes W)=2\operatorname{tr}W$. The four norms are therefore the same numbers, computed at twice the size with half the normalization:

$$
\tfrac14\operatorname{Tr}(M^2)=\tfrac12\operatorname{tr}(B^2),
$$

and likewise for $M^{\mathsf T}M$, $M^{\dagger}M$ and $M^{\mathsf T}M^{\dagger}$.

**The singular set.** The singular nonzero matrices are exactly the block matrices with $\det B=0$ and $B\neq0$, of rank two. The null cone is the set $\{\langle\tilde Q\rangle_{\natural}=0\}$, and the block display shows its cause: the two identical blocks vanish together, so the rank drops from four to two and never to one or three.

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

- [Matrix Representations : The Four Words and the Four Traces](matrix-representations-the-four-words-and-the-four-traces.html), for the trace normalization
- [Matrix Representations : The Product, the Trace and the Determinant](matrix-representations-the-product-the-trace-and-the-determinant.html), for the basic invariants
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the norms