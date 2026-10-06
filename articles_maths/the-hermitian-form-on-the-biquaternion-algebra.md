
# __The Hermitian Form on the Biquaternion Algebra__

## Introduction

The biquaternion algebra carries two scalar pairings of degree two, and this article treats the second of them. The **Hermitian form** is built on the Hermitian conjugation ${}^{*}={}^{\natural}\circ\bar{\cdot}$,

$$
\langle\tilde{Q},\tilde{P}\rangle_{*}=\mathrm{Sc}\!\left(\tilde{Q}\tilde{P}^{*}\right)=\sum_{\mu=0}^{3}P_{\bar\mu}Q_\mu ,
$$

with the conjugation in the second argument, so that the pairing is $\mathbb{C}$-**sesquilinear** rather than bilinear. Its diagonal is a genuine positive definite quadratic form, and it is this form, not the quaternion bilinear one, that supplies the algebra with its Euclidean and Hilbert structure.

The article owns four objects. It owns the form $\tilde{Q}\tilde{Q}^{*}$ of a single element and its scalar part, the vector part included. It owns the sesquilinear inner product, its sesquilinearity, its Hermitian symmetry and its non-degeneracy, and the Gram matrix and signature of the form. It owns the real form of signature $(8,0)$ on $\mathbb{B}\cong\mathbb{R}^{8}$ that the inner product defines, the completeness and the coefficient model $\mathbb{C}^{4}$, and the Euclidean unit sphere. And it owns the comparison of the form with the quaternion bilinear form, which is *The Four Pairings of the Biquaternion Algebra*. It assumes the four conjugations of the algebra with their fixed spaces (*The Group of Involutions*; *Biquaternions as a Vector Space over $\mathbb{C}$*) and the biquaternion norm $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\sum_\mu Q_\mu^{2}$ (*Biquaternion Norm and Invertibility*); it assumes no topology.

The readings collected here were carried by *Biquaternions as a Vector Space over $\mathbb{C}$* as §*The Hermitian Form* and §*The Inner Product*. They are forms, their home is the Topology region, and the Algebra articles keep the conjugation ${}^{*}$ itself and the Hermitian subspace $\mathbb{M}_+$ as its fixed space, those being involution-theoretic and needing no form to exist. Four deferrals are stated once and are not repeated. The topology that the form induces — the linear isometry onto $\mathbb{R}^{8}$, the sharp inequality of the normed algebra, the contractibility of the algebra, the three spherical level sets and the Riesz duality — is *The Euclidean Topology of the Biquaternion Algebra*. The compact group formed by the unitary elements is *The Unitary Group of the Biquaternion Algebra*. The form of the regular module, whose scalar part is the pairing of this article, is *The Canonical Hermitian Form on the Regular Module of the Biquaternion Algebra*. And the operator theory built on the form is *One-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint*, *Two-Sided Operators on the Biquaternion Algebra with Hermitian Adjoint* and *Mixed Inner Conjugation on the Biquaternion Algebra with Hermitian Adjoint*, the positivity of the form being *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*.

**Conventions.** Throughout, $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is the biquaternion algebra with basis $e_0,e_1,e_2,e_3$, where $e_0$ is the identity and $e_k^{2}=-e_0$ for $k=1,2,3$. A generic element is $\tilde{Q}=\sum_{\mu=0}^{3}Q_\mu e_\mu$ with $Q_\mu=q_\mu+iq'_\mu\in\mathbb{C}$, and the scalar part is written $\mathrm{Sc}$. The Hermitian conjugation is ${}^{*}={}^{\natural}\circ\bar{\cdot}$, the composite of the coefficient conjugation $\bar{\cdot}$ and the natural conjugation ${}^{\natural}$; it is conjugate-linear, and ${}^{*}{}^{*}=\mathrm{id}$.

## The Hermitian Form of an Element

**Definition (the form of an element).** The **Hermitian form** of a biquaternion is the biquaternion

$$
\tilde{Q}\tilde{Q}^{*},\qquad \tilde{Q}^{*}=\overline{\tilde{Q}^{\natural}} .
$$

**Proposition (the scalar part).** The scalar part of the form is

$$
\mathrm{Sc}\!\left(\tilde{Q}\tilde{Q}^{*}\right)=\sum_{\mu=0}^{3}\lvert Q_\mu\rvert^{2}=\sum_{\mu=0}^{3}\left(q_\mu^{2}+q'_\mu{}^{2}\right),
$$

a real number, non-negative, and zero only at $\tilde{Q}=0$.

**Proof.** The conjugation acts on the basis by $e_0^{*}=e_0$ and $e_k^{*}=-e_k$, so that $\tilde{Q}^{*}=\sum_{\nu}\eta_\nu\bar{Q}_\nu e_\nu$ with $\eta_0=+1$ and $\eta_k=-1$; hence

$$
\tilde{Q}\tilde{Q}^{*}=\sum_{\mu,\nu}Q_\mu\bar{Q}_\nu\,\eta_\nu\,e_\mu e_\nu .
$$

Among the products $e_\mu e_\nu$ only those with $\mu=\nu$ are scalars, and there $e_0^{2}=e_0$ and $e_k^{2}=-e_0$. The scalar part is therefore $\sum_\mu Q_\mu\bar{Q}_\mu\,\eta_\mu\,(\pm1)=\sum_\mu\lvert Q_\mu\rvert^{2}$, the two signs contributed by the terms $\mu=k$ cancelling. A sum of squares of real numbers vanishes only when every $q_\mu$ and every $q'_\mu$ vanishes.

**Example (a form with a non-zero vector part).** The element $\tilde{Q}=e_0+ie_1$ is Hermitian, $\tilde{Q}^{*}=\tilde{Q}$, and

$$
\tilde{Q}\tilde{Q}^{*}=(e_0+ie_1)^{2}=e_0+2ie_1+(ie_1)^{2}=2e_0+2ie_1 ,
$$

because $(ie_1)^{2}=i^{2}e_1^{2}=e_0$. The scalar part is $2$ and the vector part is $2ie_1$. The form of an element is thus a biquaternion and not a real number, and its vector part need not vanish.

**Proposition (Hermitian character).** The form of an element is a Hermitian element, $(\tilde{Q}\tilde{Q}^{*})^{*}=\tilde{Q}\tilde{Q}^{*}$; that is, $\tilde{Q}\tilde{Q}^{*}\in\mathbb{M}_+$.

**Proof.** The conjugation reverses the product and has order two, so $(\tilde{Q}\tilde{Q}^{*})^{*}=(\tilde{Q}^{*})^{*}\tilde{Q}^{*}=\tilde{Q}\tilde{Q}^{*}$.

**Remark (the form is not multiplicative, and it is not the norm).** The assignment $\tilde{Q}\mapsto\tilde{Q}\tilde{Q}^{*}$ is not multiplicative. The element $\tilde{Q}=e_1+ie_2$ is a zero divisor, $\tilde{Q}^{2}=0$, while $\tilde{Q}\tilde{Q}^{*}=2e_0+2ie_3$ is not zero; were the assignment multiplicative, $(\tilde{Q}^{2})(\tilde{Q}^{2})^{*}$ would be $(\tilde{Q}\tilde{Q}^{*})^{2}=8e_0+8ie_3$, whereas it is $0$. The quadratic function $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\sum_\mu Q_\mu^{2}$ is a different function of the element, complex-valued and indefinite; the two are compared in *The Four Pairings of the Biquaternion Algebra*.

## The Inner Product

**Definition (the inner product).** The **inner product** of two biquaternions is the complex scalar

$$
\langle\tilde{Q},\tilde{P}\rangle_{*}=\mathrm{Sc}\!\left(\tilde{Q}\tilde{P}^{*}\right)=\sum_{\mu=0}^{3}P_{\bar\mu}Q_\mu
=\sum_{\mu=0}^{3}\left(p_\mu q_\mu+p'_\mu q'_\mu\right)+i\sum_{\mu=0}^{3}\left(p_\mu q'_\mu-p'_\mu q_\mu\right),
$$

the scalar part of the form of the pair.

**Proposition (sesquilinearity).** For every $\lambda\in\mathbb{C}$,

$$
\langle\lambda\tilde{Q},\tilde{P}\rangle_{*}=\lambda\langle\tilde{Q},\tilde{P}\rangle_{*},\qquad
\langle\tilde{Q},\lambda\tilde{P}\rangle_{*}=\bar{\lambda}\langle\tilde{Q},\tilde{P}\rangle_{*} ,
$$

so the pairing is linear in the first argument and conjugate-linear in the second.

**Proof.** The scalar part is linear over $\mathbb{C}$ and satisfies $\mathrm{Sc}(XY)=\mathrm{Sc}(YX)$. In the first slot this gives $\mathrm{Sc}((\lambda\tilde{Q})\tilde{P}^{*})=\lambda\,\mathrm{Sc}(\tilde{Q}\tilde{P}^{*})$. In the second slot, $(\lambda\tilde{P})^{*}=\bar{\lambda}\tilde{P}^{*}$ because $\lambda$ is central, and $\bar{\lambda}\,\mathrm{Sc}(\tilde{Q}\tilde{P}^{*})=\mathrm{Sc}(\tilde{Q}\,\bar{\lambda}\tilde{P}^{*})$.

**Proposition (Hermitian symmetry).** $\langle\tilde{Q},\tilde{P}\rangle_{*}^{*}=\langle\tilde{P},\tilde{Q}\rangle_{*}$.

**Proof.** The conjugate of a scalar is the scalar part of the conjugate biquaternion, $\overline{\mathrm{Sc}(X)}=\mathrm{Sc}(X^{*})$, so $\langle\tilde{Q},\tilde{P}\rangle_{*}^{*}=\mathrm{Sc}\bigl((\tilde{Q}\tilde{P}^{*})^{*}\bigr)=\mathrm{Sc}(\tilde{P}\tilde{Q}^{*})=\langle\tilde{P},\tilde{Q}\rangle_{*}$.

**Proposition (non-degeneracy).** If $\langle\tilde{Q},\tilde{P}\rangle_{*}=0$ for every $\tilde{Q}$, then $\tilde{P}=0$; if $\langle\tilde{Q},\tilde{P}\rangle_{*}=0$ for every $\tilde{P}$, then $\tilde{Q}=0$.

**Proof.** Testing the first statement at the four basis elements $\tilde{Q}=e_\mu$ gives $P_{\bar\mu}=0$ for every $\mu$, hence $\tilde{P}=0$; testing the second at $\tilde{P}=e_\mu$ gives $Q_\mu=0$ for every $\mu$, hence $\tilde{Q}=0$.

**Proposition (the Gram matrix and the signature).** In the basis $e_0,e_1,e_2,e_3$ the Gram matrix of the inner product is the identity,

$$
\langle e_\mu,e_\nu\rangle_{*}=\delta_{\mu\nu},
$$

and the form is positive definite, of signature $(8,0)$ on the real space $\mathbb{B}\cong\mathbb{R}^{8}$.

**Proof.** Since $e_0^{*}=e_0$ and $e_k^{*}=-e_k$, the diagonal values are $\langle e_0,e_0\rangle_{*}=\mathrm{Sc}(e_0^{2})=1$ and $\langle e_k,e_k\rangle_{*}=\mathrm{Sc}(-e_k^{2})=1$, while for $\mu\neq\nu$ the product $e_\mu e_\nu$ has vanishing scalar part, so the off-diagonal values are zero. On the diagonal the form is $\langle\tilde{Q},\tilde{Q}\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2}$, positive off zero by the proposition on the scalar part, so the form is positive definite; a positive definite real form on a space of real dimension eight has signature $(8,0)$.

## The Hilbert Structure

The inner product is positive definite, and the structure it places on the algebra is read in four steps.

**The real inner product.** The real part of the inner product, with the two arguments in the symmetric order,

$$
(\tilde{P},\tilde{Q})_{\mathbb{R}}=\mathrm{Re}\,\langle\tilde{Q},\tilde{P}\rangle_{*}=\sum_{\mu=0}^{3}\left(p_\mu q_\mu+p'_\mu q'_\mu\right),
$$

is a positive definite real inner product on the underlying real space of dimension eight, by the Gram matrix and the diagonal of the preceding section.

**Completeness.** An inner product space of finite dimension over $\mathbb{R}$ or over $\mathbb{C}$ is complete, its unit ball being compact in the norm it defines. The algebra is therefore a complex Hilbert space of dimension four, with orthonormal basis $e_0,e_1,e_2,e_3$, and the coefficient map

$$
\tilde{Q}=\sum_{\mu=0}^{3}Q_\mu e_\mu\longmapsto (Q_0,Q_1,Q_2,Q_3)
$$

is an isomorphism of $\mathbb{B}$ onto $\mathbb{C}^{4}$ with its ordinary Hermitian inner product.

**The Euclidean norm.** The norm of the form is

$$
\lVert\tilde{Q}\rVert_E=\sqrt{\langle\tilde{Q},\tilde{Q}\rangle_{*}}=\left(\sum_{\mu=0}^{3}\lvert Q_\mu\rvert^{2}\right)^{1/2}=\sqrt{\mathrm{Sc}\!\left(\tilde{Q}\tilde{Q}^{*}\right)} ,
$$

which is positive definite, homogeneous of degree one and subadditive.

**The Euclidean unit sphere.** The level set of the norm is the Euclidean unit sphere of the underlying real space,

$$
S^{7}=\{\tilde{Q}\in\mathbb{B}:\lVert\tilde{Q}\rVert_E=1\},
$$

a sphere of dimension seven. Its topology, the fact that it is not a group and its meeting with the null cone are *The Euclidean Topology of the Biquaternion Algebra*, and the operator theory that the norm makes possible is the pair of operator articles named in the introduction.

**Remark (the norm is not multiplicative).** The norm of the form is not multiplicative with respect to the biquaternion product, the witness being the zero divisor of the preceding section: $\tilde{Q}=e_1+ie_2$ has $\lVert\tilde{Q}\rVert_E^{2}=2$ and $\tilde{Q}^{2}=0$, so the multiplicative inequality fails. The sharp inequality that does hold, and the constant in it, are *The Euclidean Topology of the Biquaternion Algebra*.

## Summary

The second scalar pairing of the biquaternion algebra is the Hermitian form $\langle\tilde{Q},\tilde{P}\rangle_{*}=\mathrm{Sc}(\tilde{Q}\tilde{P}^{*})=\sum_\mu P_{\bar\mu}Q_\mu$, built on the conjugate-linear Hermitian conjugation ${}^{*}$ and therefore sesquilinear, linear in the first argument and conjugate-linear in the second. Its diagonal is the positive definite real form $\sum_\mu\lvert Q_\mu\rvert^{2}$ of signature $(8,0)$ on $\mathbb{B}\cong\mathbb{R}^{8}$, and its Gram matrix in the basis $e_\mu$ is the identity; it is Hermitian by symmetry and non-degenerate. The form of a single element $\tilde{Q}\tilde{Q}^{*}$ is a Hermitian biquaternion, its scalar part being the diagonal of the pairing and its vector part not in general vanishing, as the example $(e_0+ie_1)^{2}=2e_0+2ie_1$ shows; the assignment is not multiplicative. The real part of the pairing is a positive definite real inner product, so the algebra is a complete complex Hilbert space of dimension four with orthonormal basis $e_0,e_1,e_2,e_3$, and the level set of its norm is the Euclidean unit sphere $S^{7}$. The reading of this form on the six distinguished subspaces, next to the three sibling forms, is *The Six Subspaces and the Four Forms* and *The Four Pairings of the Biquaternion Algebra*. The topology that the form induces is *The Euclidean Topology of the Biquaternion Algebra*, the compact group it singles out is *The Unitary Group of the Biquaternion Algebra*, and the module-level origin of the scalar form is *The Canonical Hermitian Form on the Regular Module of the Biquaternion Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| ${}^{*}={}^{\natural}\circ\bar{\cdot}$ | The Hermitian conjugation; conjugate-linear, of order two |
| $\tilde{Q}\tilde{Q}^{*}$ | The Hermitian form of an element; a Hermitian biquaternion |
| $\mathrm{Sc}(\tilde{Q}\tilde{Q}^{*})=\sum_\mu\lvert Q_\mu\rvert^{2}$ | Its scalar part; positive definite, zero only at $\tilde{Q}=0$ |
| $\langle\tilde{Q},\tilde{P}\rangle_{*}=\mathrm{Sc}(\tilde{Q}\tilde{P}^{*})=\sum_\mu P_{\bar\mu}Q_\mu$ | The inner product; sesquilinear and Hermitian |
| $\langle\lambda\tilde{Q},\tilde{P}\rangle_{*}=\lambda\langle\tilde{Q},\tilde{P}\rangle_{*}$, $\langle\tilde{Q},\lambda\tilde{P}\rangle_{*}=\bar{\lambda}\langle\tilde{Q},\tilde{P}\rangle_{*}$ | Sesquilinearity of the inner product |
| $\langle\tilde{Q},\tilde{P}\rangle_{*}^{*}=\langle\tilde{P},\tilde{Q}\rangle_{*}$ | Hermitian symmetry |
| $\langle e_\mu,e_\nu\rangle_{*}=\delta_{\mu\nu}$ | Gram matrix; signature $(8,0)$, positive definite |
| $(\tilde{P},\tilde{Q})_{\mathbb{R}}=\mathrm{Re}\,\langle\tilde{Q},\tilde{P}\rangle_{*}$ | The real inner product of the underlying real space |
| $\lVert\tilde{Q}\rVert_E=\sqrt{\sum_\mu\lvert Q_\mu\rvert^{2}}$ | The Euclidean norm of the form |
| $S^{7}=\{\lVert\tilde{Q}\rVert_E=1\}$ | The Euclidean unit sphere |
| $\langle\tilde{Q},\tilde{P}\rangle_{\natural}=\mathrm{Sc}(\tilde{Q}\tilde{P}^{\natural})=\sum_\mu Q_\mu P_\mu$ | The quaternion bilinear form, the companion pairing |

## Further Reading

- Paul R. Halmos, *A Hilbert Space Problem Book*, 2nd edition (Springer, 1982), for the reading of a finite-dimensional inner product space as a Hilbert space.
- John B. Conway, *A Course in Functional Analysis*, 2nd edition (Springer, 1990), for completeness, the orthonormal basis and the finite-dimensional Hilbert-space facts used here.
- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for sesquilinear and Hermitian forms over a ring with an involution.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the Hermitian forms attached to the involutions of an algebra.
