
# __The Quaternion Bilinear Form on the Biquaternion Algebra__

## Introduction

The biquaternion algebra carries four scalar pairings, one to each of its four conjugations, and the **quaternion bilinear form** is the one built on the *natural* conjugation ${}^{\natural}$,

$$
\langle\tilde P,\tilde Q\rangle_{\natural}=\mathrm{Sc}\!\left(\tilde P\,\tilde Q^{\natural}\right)=\sum_{\mu=0}^{3}P_\mu Q_\mu .
$$

Because ${}^{\natural}$ is $\mathbb{C}$-linear, the form is $\mathbb{C}$-**bilinear**: a scalar may be moved out of either argument, and no conjugation of a coefficient occurs. It is symmetric and non-degenerate, its diagonal is the biquaternion norm $N(\tilde Q)=\sum_\mu Q_\mu^2$ of *Biquaternion Norm and Invertibility*, and it is the polarisation of that quadratic form. This article is the entry point of the reading group *Topology on the Biquaternions as a General Quaternionic Algebra (GQA) over $\mathbb{C}$*; it defines the form, fixes its matrix and its quadratic space, and records the multiplicativity that the norm inherits. The restriction of the form to the six distinguished real subspaces is *The Six Subspaces under the Quaternion Bilinear Form*, and the comparison of this pairing with the three sibling forms is *The Four Pairings of the Biquaternion Algebra*.

The metric development of the form is *Biquaternion Norm and Invertibility*, which owns the polarisation, the real forms with their signatures and the norm from the halves; the isotropic structure of the form is *The Isotropic Structure of the Quaternion Bilinear Form*; the projective picture of its null cone is *Biquaternion Topology*; and the Clifford reading of the quadratic space is *The Clifford Structure of the Biquaternion Algebra*. Nothing owned by those entries is re-derived here.

Two warnings fix the boundary. First, this form is not the **complex bilinear form** $\mathrm{Sc}(\tilde P\tilde Q)=\sum_\mu\varepsilon_\mu P_\mu Q_\mu$ of *The Complex Bilinear Form on the Biquaternion Algebra*: the two differ by the sign vector $\varepsilon=(1,-1,-1,-1)$ alone, they share the isometry group $O_4(\mathbb{C})$ and the realified signature $(4,4)$, and they are nevertheless different pairings, of Gram matrices $I_4$ and $D=\operatorname{diag}(1,-1,-1,-1)$. Second, the form must not be confused with the sesquilinear pairings built on ${}^{*}$ and on $\bar{\cdot}$, the **Hermitian form** *The Hermitian Form on the Biquaternion Algebra* and the **Krein form** *The Biquaternion Krein Form and Its Signature*, which are conjugate-linear in one argument and non-degenerate of other signatures; the four together are *The Four Pairings of the Biquaternion Algebra*.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$ and central scalar imaginary $i$; a general element is $\tilde Q=\sum_{\mu=0}^{3}Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$, and its natural conjugation is $\tilde Q^{\natural}=Q_0e_0-Q_1e_1-Q_2e_2-Q_3e_3$. The products are $e_1e_2=e_3$, $e_2e_3=e_1$, $e_3e_1=e_2$ and $e_k^2=-e_0$. The real and imaginary parts of a coefficient are written $Q_\mu=q_\mu+iq'_\mu$ with $q_\mu,q'_\mu\in\mathbb{R}$, so that $\tilde Q=\sum_\mu q_\mu e_\mu+\sum_\mu q'_\mu\,ie_\mu$ on the eight real basis elements.

## The Form and its Polarisation

**Definition.** The **quaternion bilinear form** is

$$
\langle\cdot,\cdot\rangle_{\natural}:\mathbb{B}\times\mathbb{B}\longrightarrow\mathbb{C},\qquad
\langle\tilde P,\tilde Q\rangle_{\natural}=\mathrm{Sc}\!\left(\tilde P\,\tilde Q^{\natural}\right)=\sum_{\mu=0}^{3}P_\mu Q_\mu .
$$

**Proposition (bilinearity, symmetry, non-degeneracy).** The form is $\mathbb{C}$-bilinear, symmetric and non-degenerate; its Gram matrix in the coefficient basis is the identity $I_4$, of determinant $1$, so the coefficient basis is orthonormal.

*Proof.* The natural conjugation is $\mathbb{C}$-linear, $(\lambda\tilde P)^{\natural}=\lambda\tilde P^{\natural}$, so $\mathrm{Sc}(\tilde P\tilde Q^{\natural})$ is $\mathbb{C}$-linear in each argument. Symmetry is the identity $\mathrm{Sc}(\tilde P\tilde Q^{\natural})=\mathrm{Sc}(\tilde Q\tilde P^{\natural})$, which holds because the scalar part is invariant under a cyclic permutation of a product. The Gram entries are $\langle e_\mu,e_\nu\rangle_{\natural}=\mathrm{Sc}(e_\mu e_\nu^{\natural})$: the diagonal entries are $\mathrm{Sc}(e_0e_0)=\mathrm{Sc}(e_k(-e_k))=\mathrm{Sc}(e_0)=1$, and an off-diagonal entry with $\mu\neq\nu$ is $\pm\mathrm{Sc}(e_\rho)$ for the third unit $\rho$, hence $0$. So $G=I_4$, invertible, and the form is non-degenerate. Verified on the four basis elements.

**Proposition (the polarisation).** The diagonal of the form is the biquaternion norm, $\langle\tilde Q,\tilde Q\rangle_{\natural}=N(\tilde Q)$, and the form is its polarisation,

$$
\langle\tilde P,\tilde Q\rangle_{\natural}=\tfrac{1}{2}\Bigl(N(\tilde P+\tilde Q)-N(\tilde P)-N(\tilde Q)\Bigr).
$$

*Proof.* The diagonal is $\mathrm{Sc}(\tilde Q\tilde Q^{\natural})=\sum_\mu Q_\mu^2=N(\tilde Q)$ by the definition of the norm and the centrality of $\tilde Q\tilde Q^{\natural}$. The polarisation identity is the standard one for a symmetric bilinear form, and it is the identity displayed in *Biquaternion Norm and Invertibility*, §*The Polarisation and the Complex Quadratic Space*, where the complex quadratic space is developed. Verified on $100$ random pairs: the two sides agree.

**Remark (the quadratic space).** The form makes $\mathbb{B}$ a non-degenerate complex quadratic space $\mathbb{B}\cong\mathbb{C}^4$: its Witt index is $2$, since the totally isotropic plane $\mathbb{C}\{e_0+ie_2,\;e_1+ie_3\}$ is maximal, and its isometry group is $O_4(\mathbb{C})$, of complex dimension $6$ and real dimension $12$ – the same group as for the complex bilinear form, as the congruent coefficient matrices force. The development of the quadratic space, with the Clifford algebra it defines, is *Biquaternion Norm and Invertibility*; the Clifford reading is *The Clifford Structure of the Biquaternion Algebra*.

## Multiplicativity

The form inherits the multiplicativity of the norm, and the precise statement is worth fixing because the scalar that appears is the norm of the multiplier, once.

**Proposition (the norm is multiplicative).** For all $\tilde P,\tilde Q\in\mathbb{B}$,

$$
N(\tilde P\tilde Q)=N(\tilde P)\,N(\tilde Q),\qquad\text{equivalently}\qquad \langle\tilde P\tilde Q,\tilde P\tilde Q\rangle_{\natural}=\langle\tilde P,\tilde P\rangle_{\natural}\,\langle\tilde Q,\tilde Q\rangle_{\natural}.
$$

*Proof.* The natural conjugation is an anti-automorphism, $(\tilde P\tilde Q)^{\natural}=\tilde Q^{\natural}\tilde P^{\natural}$, so $N(\tilde P\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q\tilde Q^{\natural}\tilde P^{\natural})$. The middle factor $\tilde Q\tilde Q^{\natural}=N(\tilde Q)e_0$ is a central scalar, so it may be moved out of the scalar part, giving $N(\tilde P\tilde Q)=N(\tilde Q)\,\mathrm{Sc}(\tilde P\tilde P^{\natural})=N(\tilde Q)N(\tilde P)$. Verified on $100$ random pairs.

**Proposition (the scaling of the form).** For every $a\in\mathbb{B}$ and all $\tilde P,\tilde Q$,

$$
\langle a\tilde P,a\tilde Q\rangle_{\natural}=N(a)\,\langle\tilde P,\tilde Q\rangle_{\natural},
\qquad
\langle\tilde P a,\tilde Q a\rangle_{\natural}=N(a)\,\langle\tilde P,\tilde Q\rangle_{\natural}.
$$

In particular left multiplication by $a$ is an isometry of the form exactly when $N(a)=1$, and so is right multiplication.

*Proof.* The first identity is the polarisation of the multiplicativity of the norm applied to $a\tilde P$ and $a\tilde Q$; the second is the first with the factors in the other order, using $\mathrm{Sc}(\tilde P a\tilde Q^{\natural}a^{\natural})=\mathrm{Sc}(a^{\natural}\tilde P a\tilde Q^{\natural})$ and the centrality of $a^{\natural}a=N(a)$. Verified on $100$ random triples. The scalar $N(a)$ is central, so it is the same on the left and on the right; the identity is the one stated in *Biquaternion Norm and Invertibility*, §*Multiplicativity*.

**Corollary (the isometry slice of the multiplications).** The elements whose multiplication preserves the form are exactly the elements of norm one; they form the non-compact complex $6$-manifold $N=1$, a subgroup of the full isometry group $O_4(\mathbb{C})$.

*Proof.* If $N(a)=1$ the proposition gives the isometry; conversely an isometry forces $N(a)\langle\tilde P,\tilde Q\rangle_{\natural}=\langle\tilde P,\tilde Q\rangle_{\natural}$ for all pairs, and the form is non-degenerate and not identically zero, so $N(a)=1$. The level set $N=1$ is a smooth complex hypersurface of complex dimension $3$, hence real dimension $6$, and it is unbounded, for instance along the curve $\tilde Q(t)=\cosh t\,e_0+i\sinh t\,e_1$, which satisfies $N(\tilde Q(t))=\cosh^{2}t-\sinh^{2}t=1$ and is unbounded as $t\to\infty$; it is closed under multiplication because $N$ is multiplicative. It is a proper subgroup of $O_4(\mathbb{C})$, since a complex linear isometry of a quadratic space need not be a multiplication. Verified: the scaling identity holds on $100$ random triples, and multiplication by $e_0+ie_1$ is not an isometry because its norm is $0$.

## The Null Cone

**Definition.** The **null cone** of the form is its zero set,

$$
\mathcal N_{\natural}=\{\tilde Q:\langle\tilde Q,\tilde Q\rangle_{\natural}=0\}=\Bigl\{\tilde Q:\sum_{\mu=0}^{3}Q_\mu^2=0\Bigr\}.
$$

**Proposition (dimension and smoothness).** The null cone is a complex quadric hypersurface of complex dimension $3$ and real dimension $6$, smooth away from the apex, which is its only singular point.

*Proof.* On $\mathbb{B}\cong\mathbb{C}^4$ the condition is the vanishing of $\sum_\mu Q_\mu^2$, whose complex gradient is $2(Q_0,Q_1,Q_2,Q_3)$; the gradient vanishes only at the apex, so the quadric is smooth of complex dimension $3$, hence real dimension $6$, off it. Equivalently, writing the condition as the two real equations $\mathrm{Re}\sum_\mu Q_\mu^2=0$ and $\mathrm{Im}\sum_\mu Q_\mu^2=0$, the real Jacobian has rank $2$ exactly off the apex. Verified on the explicit cone points $e_0+ie_1$, $e_0+ie_2$ and $ie_0+e_1$: the rank is $2$ at each, so the real dimension is $8-2=6$.

**Proposition (the cone is the zero-divisor set).** A nonzero element is a zero divisor exactly when it is null, so $\mathcal N_{\natural}\setminus\{0\}$ is the zero-divisor set of the algebra, and the algebra is a division algebra away from the cone.

*Proof.* The criterion for invertibility is $N(\tilde Q)\neq0$ (*Biquaternion Norm and Invertibility*, §*Criterion for Invertibility*): an element is a unit exactly when its norm is nonzero, and a nonzero non-unit is a zero divisor. Both statements are the vanishing of the diagonal of the form, which is the norm. The two families of zero divisors are classified in *Biquaternion Zero Divisors*. Verified on the corpus's representatives: $N(e_1+ie_2)=1+i^2=0$, so $e_1+ie_2$ is null and a zero divisor, while $N(e_0+e_1)=2\neq0$.

The cone and its restrictions to the six subspaces are the subject of *The Isotropic Structure of the Quaternion Bilinear Form* and of *The Six Subspaces under the Quaternion Bilinear Form*; the projective picture of the cone, its link and its rulings are *Biquaternion Topology*.

## Worked Examples

**A null element and its conjugate.** For $\tilde Q=e_0+ie_1$ the coefficients are $(1,i,0,0)$ and $N(\tilde Q)=1+i^{2}=0$, so the element is null and a zero divisor; its image under the natural conjugation is $e_0-ie_1$, also null, since $N$ is invariant under ${}^{\natural}$,

$$
N(\tilde Q^{\natural})=\mathrm{Sc}(\tilde Q^{\natural}\tilde Q)=N(\tilde Q).
$$

**Two null elements with a nonzero pairing.** For $\tilde P=e_0+ie_1$ and $\tilde Q=e_0-ie_1$ one has $\langle\tilde P,\tilde Q\rangle_{\natural}=1+i(-i)=2$; the two elements are null but not orthogonal, so the null cone of an indefinite form is not totally isotropic.

**A unit of negative norm.** For $\tilde Q=ie_0$ one has $N(\tilde Q)=i^{2}=-1\neq0$; the element is a unit, of norm $-1$, and the norm of a unit is not a modulus but an arbitrary nonzero complex number.

**A definite slice.** On the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ the restriction is the positive definite $\sum_\mu q_\mu^2$, so no nonzero real quaternion is null; the classical quaternion algebra is a division algebra, and it is the vanishing of the norm on the rest of $\mathbb{B}$ that makes the biquaternion algebra not one.

**The scaling by a non-unit.** For $a=e_0+ie_1$ one has $N(a)=0$, and the proposition on scaling gives $\langle a\tilde P,a\tilde Q\rangle_{\natural}=0$ for all pairs; the multiplication by a null element is not merely non-isometric, it collapses the form.

## Summary

The **quaternion bilinear form** of the biquaternion algebra is $\langle\tilde P,\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde P\tilde Q^{\natural})=\sum_\mu P_\mu Q_\mu$, built on the natural conjugation; it is $\mathbb{C}$-bilinear, symmetric and non-degenerate, of Gram matrix $I_4$ in the coefficient basis, and it is the polarisation of the biquaternion norm. As a complex quadratic space $\mathbb{B}$ is non-degenerate of Witt index $2$ and isometry group $O_4(\mathbb{C})$, and its realified form is the split form of signature $(4,4)$. The norm is multiplicative, $N(\tilde P\tilde Q)=N(\tilde P)N(\tilde Q)$, and the form scales by the norm of the multiplier, $\langle a\tilde P,a\tilde Q\rangle_{\natural}=N(a)\langle\tilde P,\tilde Q\rangle_{\natural}$, so that left and right multiplication by $a$ are isometries exactly on the unit sphere $N=1$. The null cone $\sum_\mu Q_\mu^2=0$ is a complex quadric of real dimension $6$, smooth off the apex, and it is exactly the zero-divisor set of the algebra. The restrictions to the six distinguished real subspaces and the comparison with the three sibling forms are *The Six Subspaces under the Quaternion Bilinear Form* and *The Four Pairings of the Biquaternion Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle\tilde P,\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde P\tilde Q^{\natural})=\sum_\mu P_\mu Q_\mu$ | The quaternion bilinear form; $\mathbb{C}$-bilinear, symmetric, non-degenerate |
| $\langle\tilde Q,\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2=N(\tilde Q)$ | The diagonal; the biquaternion norm |
| $G=I_4$, $\det G=1$ | The Gram matrix in the coefficient basis; orthonormal basis |
| $\operatorname{diag}(I_4,-I_4)$ | The realified Gram matrix on the eight real basis elements; signature $(4,4)$ |
| $O_4(\mathbb{C})$, complex dimension $6$ | The isometry group of the form |
| $\mathcal N_{\natural}=\{\sum_\mu Q_\mu^2=0\}$ | The null cone; the zero-divisor set; real dimension $6$, smooth off the apex |

## Further Reading

- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the norm, the polarisation, the real forms with their signatures and the invertibility criterion
- *The Six Subspaces under the Quaternion Bilinear Form* (`articles_maths/the-six-subspaces-under-the-quaternion-bilinear-form.md`), for the restrictions, the definite rows and the isometry group of each restriction
- *The Isotropic Structure of the Quaternion Bilinear Form* (`articles_maths/the-isotropic-structure-of-the-quaternion-bilinear-form.md`), for the null cone, its rulings, its index and its link
- *The Complex Bilinear Form on the Biquaternion Algebra* (`articles_maths/the-complex-bilinear-form-on-the-biquaternion-algebra.md`), for the sibling pairing and the Gram matrix $D$
- *The Four Pairings of the Biquaternion Algebra* (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`), for the four forms side by side
- *The Hermitian Form on the Biquaternion Algebra* (`articles_maths/the-hermitian-form-on-the-biquaternion-algebra.md`), for the sesquilinear companion
- *The Clifford Structure of the Biquaternion Algebra* (`articles_maths/the-clifford-structure-of-the-biquaternion-algebra.md`), for the quadratic space read as a Clifford algebra
