# __Spectral Regularity and Degeneracy in the Quaternion Algebra__

## Introduction

The left regular representation $L_{\tilde q}(x)=\tilde q x$ is a faithful four-dimensional real representation. This article solves its eigenvalue problem: the characteristic polynomial is $((\lambda-q_t)^2+|\vec q|^2)^2$, the minimal polynomial is $(\lambda-q_t)^2+|\vec q|^2$ off the real axis and $\lambda-q_t$ on it, and the complex eigenvalues are $q_t\pm i|\vec q|$. The two eigenvalues are distinct exactly when $\vec q\ne0$. That condition is **spectral regularity**; its failure is **spectral degeneracy**, and the degenerate locus is the real axis. Every element is semisimple, so there is no defective element.

The algebra is [Quaternion Algebra](quaternion-algebra.html); the norm is [Norm and Invertibility in the Quaternion Algebra](norm-and-invertibility-in-the-quaternion-algebra.html); the eigenbasis is [Eigenvalue Decomposition and Eigenbasis of a Quaternion](eigenvalue-decomposition-and-eigenbasis-of-a-quaternion.html); the comparison with the norm is [Relations between the Quaternion Norm and Spectral Regularity and Degeneracy](relations-between-the-quaternion-norm-and-spectral-regularity-and-degeneracy.html).

**Notation.** An element is $\tilde q=q_t+\vec q=q_t e_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$, with $\vec q^2=-|\vec q|^2e_t$. The conjugate is $\tilde q^{\natural}=q_t-\vec q$, the quaternion norm is $\langle\tilde q\rangle_{\natural}=\tilde q\tilde q^{\natural}=q_t^2+|\vec q|^2$, and the modulus is $|\tilde q|=\sqrt{\langle\tilde q\rangle_{\natural}}$. The letter $s=|\vec q|$ is reserved for the length of the vector part, so $|\tilde q|^2=q_t^2+s^2$. The length $|\vec q|$ and the modulus $|\tilde q|$ are different numbers.

## Left Multiplication and the Characteristic Polynomial

**Definition.** The **left multiplication** and **right multiplication** by $\tilde q$ are the real-linear maps
$$L_{\tilde q}:\mathbb H\to\mathbb H,\quad L_{\tilde q}(x)=\tilde q x,\qquad R_{\tilde q}:\mathbb H\to\mathbb H,\quad R_{\tilde q}(x)=x\tilde q.$$

**Proposition (faithfulness).** The map $\tilde q\mapsto L_{\tilde q}$ is an injective algebra homomorphism, and $\tilde q\mapsto R_{\tilde q}$ is an injective anti-homomorphism. In particular, $L_{\tilde q}=0$ exactly when $\tilde q=0$.

*Proof.* $L_{\tilde q_1}L_{\tilde q_2}=L_{\tilde q_1\tilde q_2}$ and $L_{\tilde q_1}+L_{\tilde q_2}=L_{\tilde q_1+\tilde q_2}$; the map is injective because $L_{\tilde q}(e_t)=\tilde q$. The right case is analogous.

**Proposition (the matrix).** In the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$,
$$M_L(\tilde q)=
\begin{pmatrix}
q_t&-q_x&-q_y&-q_z\\
q_x&q_t&-q_z&q_y\\
q_y&q_z&q_t&-q_x\\
q_z&-q_y&q_x&q_t
\end{pmatrix}.$$
The matrix of $L_{\vec q}$ is this matrix with $q_t=0$, and it is skew-symmetric.

**Proposition (the square and the characteristic polynomial).** For every $\tilde q=q_t+\vec q$,
$$L_{\tilde q}=q_t\,\mathrm{id}+L_{\vec q},\qquad L_{\vec q}^{\,2}=-|\vec q|^2\,\mathrm{id},$$
and
$$p_{\tilde q}(\lambda)=\det(\lambda\,\mathrm{id}-L_{\tilde q})=\bigl((\lambda-q_t)^2+|\vec q|^2\bigr)^2.$$

*Proof.* Since $L$ is a homomorphism, $L_{\vec q}^{\,2}=L_{\vec q^2}=L_{-|\vec q|^2e_t}=-|\vec q|^2\mathrm{id}$. If $s=|\vec q|\ne0$, the operator $A=L_{\vec q}$ satisfies $A^2=-s^2\mathrm{id}$ and is not scalar, so its minimal polynomial is $\lambda^2+s^2$ and its degree-four characteristic polynomial is $(\lambda^2+s^2)^2$; translating by $q_t$ gives the quartic. If $s=0$, then $A=0$ and the quartic is $(\lambda-q_t)^4$.

## The Minimal Polynomial

**Theorem.** Let $m_{\tilde q}$ be the monic generator of $\{f\in\mathbb R[\lambda]:f(\tilde q)=0\}$. Then
$$m_{\tilde q}(\lambda)=
\begin{cases}
(\lambda-q_t)^2+|\vec q|^2,&\vec q\ne0,\\[2pt]
\lambda-q_t,&\vec q=0.
\end{cases}$$
Both polynomials are squarefree, and
$$p_{\tilde q}=m_{\tilde q}^2\ \text{ if }\vec q\ne0,\qquad p_{\tilde q}=m_{\tilde q}^4\ \text{ if }\vec q=0.$$

*Proof.* Because $L$ is faithful, $f(L_{\tilde q})=L_{f(\tilde q)}=0$ if and only if $f(\tilde q)=0$; hence $L_{\tilde q}$ and $\tilde q$ have the same minimal polynomial. For $\vec q\ne0$, $(\tilde q-q_t)^2=\vec q^2=-|\vec q|^2e_t$, so the quadratic annihilates, and a degree-one annihilator would make $\tilde q$ real; the quadratic is minimal. For $\vec q=0$, $\tilde q=q_t$ and $\lambda-q_t$ is minimal. The quadratic has the distinct roots $q_t\pm i|\vec q|$ when $\vec q\ne0$; $\lambda-q_t$ is squarefree. The relations to $p_{\tilde q}$ follow from the characteristic polynomial.

**Corollary.** For $\vec q\ne0$ the discriminant of $m_{\tilde q}$ is $-4|\vec q|^2$, and it vanishes exactly when the two roots coalesce.

## The Spectral Criterion

**Definition (eigenvalue).** Let $\mathbb H_{\mathbb C}=\mathbb H\otimes_{\mathbb R}\mathbb C$, with $L_{\tilde q}^{\mathbb C}$ the complex-linear extension. A complex $\lambda$ is an **eigenvalue** of $\tilde q$ if $L_{\tilde q}^{\mathbb C}-\lambda\,\mathrm{id}$ is not invertible, equivalently if $p_{\tilde q}(\lambda)=0$. A nonzero $x\in\mathbb H_{\mathbb C}$ is an **eigenvector** if $\tilde q x=\lambda x$. The **spectrum** $\sigma(\tilde q)$ is the set of eigenvalues. An element is **spectrally regular** if its two eigenvalues are distinct, and **spectrally degenerate** otherwise.

**Theorem (the eigenvalues).** For every $\tilde q=q_t+\vec q$,
$$\sigma(\tilde q)=\{q_t+i|\vec q|,\ q_t-i|\vec q|\}.$$
If $\vec q\ne0$ the two eigenvalues are distinct, each of algebraic multiplicity two. If $\vec q=0$ the spectrum is the singleton $\{q_t\}$, of algebraic multiplicity four.

*Proof.* The roots of $(\lambda-q_t)^2+|\vec q|^2$ are $q_t\pm i|\vec q|$; the square in $p_{\tilde q}$ doubles each algebraic multiplicity, and at $\vec q=0$ the quartic is $(\lambda-q_t)^4$.

**Theorem (the criterion).** The following are equivalent: (1) $\tilde q$ is spectrally regular; (2) $\vec q\ne0$; (3) $|\vec q|^2\ne0$; (4) the eigenvalues $q_t\pm i|\vec q|$ are distinct; (5) $\tilde q\notin\mathbb R$. The negation is spectral degeneracy, and the degenerate locus is the real axis $\mathbb R e_t$.

*Proof.* The equivalence of (2), (3) and (5) is positive definiteness: $|\vec q|^2=q_x^2+q_y^2+q_z^2$ vanishes only at $\vec q=0$, which is the condition $\tilde q=q_t\in\mathbb R$. The eigenvalues coincide exactly when $|\vec q|=0$, which is (4); the equivalence of (4) with (1) is the definition.

**Remark (no real eigenvector off the axis).** If $\vec q\ne0$ and $\lambda\in\mathbb R$, then $\tilde q-\lambda$ is a unit, so $(\tilde q-\lambda)x=0$ gives $x=0$: a non-real quaternion has no real eigenvector. Its eigenvalues are complex conjugate and its eigenvectors lie in the complexification; on the axis the eigenspace is all of $\mathbb H_{\mathbb C}$.

## The Degenerate Locus

**Theorem.** The spectrally degenerate set is
$$\mathcal S=\{\tilde q:\vec q=0\}=\mathbb R e_t,$$
a real line through the origin, closed in $\mathbb H$, of dimension one and measure zero. Its complement $\mathbb H\setminus\mathbb R$ is open, dense and of dimension four. The origin is the only non-unit in $\mathcal S$.

*Proof.* The line is the common zero set of the continuous functions $q_x,q_y,q_z$, hence closed; a line in $\mathbb R^4$ has measure zero, and its complement is open and dense. A nonzero real quaternion has the inverse $q_t^{-1}e_t$; the origin has none.

**Proposition.** For $\tilde q=q_t\in\mathbb R$, $L_{\tilde q}=q_t\,\mathrm{id}$, the spectrum is $\{q_t\}$, the eigenspace is all of $\mathbb H_{\mathbb C}$, and the minimal polynomial is $\lambda-q_t$; the element is semisimple.

**Remark (degeneracy is not invertibility).** The degenerate set contains every nonzero real quaternion, and every nonzero quaternion is a unit. Spectral degeneracy therefore does not imply non-invertibility; the comparison is in [Relations between the Quaternion Norm and Spectral Regularity and Degeneracy](relations-between-the-quaternion-norm-and-spectral-regularity-and-degeneracy.html).

## Semisimplicity and the Absence of Defect

**Definition.** An element is **semisimple** if $\mathbb R[\tilde q]$ is semisimple, equivalently if $L_{\tilde q}$ is diagonalisable over $\mathbb C$; it is **defective** if it is not semisimple, equivalently if its minimal polynomial has a repeated root.

**Theorem.** For every $\tilde q\in\mathbb H$, $\mathbb R[\tilde q]\cong\mathbb R$ if $\tilde q\in\mathbb R$ and $\mathbb R[\tilde q]\cong\mathbb C$ if $\tilde q\notin\mathbb R$. Both are fields, hence semisimple; therefore every element is semisimple and none is defective.

*Proof.* The real case is immediate. In the non-real case the minimal polynomial $(\lambda-q_t)^2+|\vec q|^2$ is irreducible over $\mathbb R$, because its discriminant $-4|\vec q|^2$ is negative, so $\mathbb R[\tilde q]\cong\mathbb R[\lambda]/(m_{\tilde q})\cong\mathbb C$. A field is simple, hence semisimple, and the minimal polynomial is squarefree, so $L_{\tilde q}$ is diagonalisable over $\mathbb C$.

**Corollary.** There is no defective element. The Jordan–Chevalley decomposition of every element is trivial: its semisimple part is itself and its nilpotent part is zero.

**Remark (why division is the reason).** The proof uses only that $\mathbb H$ is a finite-dimensional real division algebra: then $\mathbb R[\tilde q]$ is an integral domain, hence a field, hence $\mathbb R$ or $\mathbb C$. Defectivity requires a zero divisor, and $\mathbb H$ has none.

**Remark.** Over $\mathbb R$ the operator is not diagonalisable when $\vec q\ne0$, because it has no real eigenvector; its real canonical form is two rotation-scaling blocks. This is not defectivity: the obstruction is the absence of real eigenvalues.

## Contrast with the Split-Quaternion and Biquaternion Cones

**The common mechanism.** In each algebra, $L_{\vec q}^{\,2}=L_{\vec q^2}$ and $\vec q^2=\mu e_t$ for a scalar $\mu$, so $(L_{\tilde q}-q_t\mathrm{id})^2=\mu\,\mathrm{id}$ and the eigenvalues satisfy $(\lambda-q_t)^2=\mu$. Spectral degeneracy is exactly $\mu=0$, the isotropy of the vector part.

| algebra | vector form $\mu$ | degenerate locus | nonzero isotropic vectors | defective points there |
|---|---|---|---|---|
| $\mathbb H$ | $q_x^2+q_y^2+q_z^2$ | real axis | none | no |
| $\mathbb H_{\mathrm{s}}$ | $-q_x^2+q_y^2+q_z^2$ | scalar line plus isotropic cone | yes | yes |
| $\mathbb B$ | $Q_x^2+Q_y^2+Q_z^2$ | complex scalar line plus cone | yes | yes |

**Theorem.** In $\mathbb H$ the vector form is positive definite, so $\vec q^2=0$ forces $\vec q=0$; the degenerate locus is the real axis and no point is defective. In $\mathbb H_{\mathrm{s}}$ the form has signature $(2,1)$ and in $\mathbb B$ it is complex; in both, a nonzero isotropic vector gives $(\tilde q-q_t)^2=0$ with $\tilde q\ne q_t$, so the minimal polynomial is $(\lambda-q_t)^2$ and the element is defective.

*Proof.* In each case $(\tilde q-q_t)^2=\vec q^2$. If $\vec q^2=0$ and $\vec q\ne0$, the minimal polynomial is $(\lambda-q_t)^2$, with a repeated root; if the form is definite, $\vec q^2=0$ forces $\vec q=0$ and the minimal polynomial is $\lambda-q_t$.

**Examples (units that are defective).** In $\mathbb H_{\mathrm{s}}$ the element $1+\vec e_x+\vec e_y$ has $\vec q^2=0$, norm $1+1-1=1$, and $(\tilde q-1)^2=0$. In $\mathbb B$ the element $e_t+\vec e_x+i\vec e_y$ has $B^2=1+i^2=0$, norm $1+0=1$, and $(\tilde Q-e_t)^2=0$. Both are units, spectrally degenerate and defective; in $\mathbb H$ no such example exists.

**Corollary.** Among the three, $\mathbb H$ is the only division algebra, the only one with a definite vector form, and the only one with no defective element; its degenerate locus is the smallest possible nonempty one, a line.

**Remark.** In $\mathbb B$ the spectral cone $B^2=0$ is distinct from the null cone of the norm, $Q_t^2+B^2=0$; the first is where the eigenvalues coalesce, the second where the element is a zero divisor. See [Relations between Quaternionic Norm and Spectral Regularity and Degeneracy](relations-between-quaternionic-norm-and-spectral-regularity-and-degeneracy.html).

## Summary

The characteristic polynomial is $((\lambda-q_t)^2+|\vec q|^2)^2$; the minimal polynomial is $(\lambda-q_t)^2+|\vec q|^2$ off the axis and $\lambda-q_t$ on it. The complex eigenvalues are $q_t\pm i|\vec q|$, each of multiplicity two off the axis and coalesced at $q_t$ on it. The element is spectrally regular exactly when $\vec q\ne0$; the degenerate locus is the real axis, a closed line.

Every element is semisimple, because $\mathbb R[\tilde q]$ is $\mathbb R$ or $\mathbb C$ and the minimal polynomial is squarefree; there is no defective element. In the split-quaternion and biquaternion algebras the vector form is indefinite or complex, the degenerate locus is a cone, and its nonzero points are defective; $1+\vec e_x+\vec e_y$ and $e_t+\vec e_x+i\vec e_y$ witness it. In $\mathbb H$ the definite form forbids this: the absence of defect is the spectral face of the division property.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb H$ | the quaternion algebra |
| $\tilde q=q_t+\vec q$ | a general quaternion, scalar part $q_t$, vector part $\vec q$ |
| $\vec q=q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$ | the vector part |
| $|\vec q|=\sqrt{q_x^2+q_y^2+q_z^2}$ | the length of the vector part, with $\vec q^2=-|\vec q|^2e_t$ |
| $\tilde q^{\natural}=q_t-\vec q$ | the quaternion conjugate |
| $\langle\tilde q\rangle_{\natural}=\tilde q\tilde q^{\natural}=q_t^2+|\vec q|^2$ | the quaternion norm |
| $|\tilde q|=\sqrt{\langle\tilde q\rangle_{\natural}}$ | the modulus |
| $L_{\tilde q}(x)=\tilde q x$, $R_{\tilde q}(x)=x\tilde q$ | left and right multiplication |
| $p_{\tilde q}(\lambda)=\det(\lambda\mathrm{id}-L_{\tilde q})$ | the characteristic polynomial |
| $m_{\tilde q}(\lambda)$ | the minimal polynomial |
| $\sigma(\tilde q)=\{q_t\pm i|\vec q|\}$ | the complex spectrum |
| $\lambda_\pm=q_t\pm i|\vec q|$ | the two eigenvalues |
| $\mathcal S=\mathbb R e_t$ | the spectrally degenerate locus |

## Further Reading

- [Quaternion Algebra](quaternion-algebra.html), for the multiplication table, the conjugation and the scalar–vector decomposition.
- [Norm and Invertibility in the Quaternion Algebra](norm-and-invertibility-in-the-quaternion-algebra.html), for the quaternion norm and the division property.
- [Eigenvalue Decomposition and Eigenbasis of a Quaternion](eigenvalue-decomposition-and-eigenbasis-of-a-quaternion.html), for the centraliser, the eigenlines and the eigenbasis.
- [Relations between the Quaternion Norm and Spectral Regularity and Degeneracy](relations-between-the-quaternion-norm-and-spectral-regularity-and-degeneracy.html), for the comparison of the two quadratic conditions.
- [The Three Sectors of the Quaternion Algebra](the-three-sectors-of-the-quaternion-algebra.html), for the three nonempty sectors and the empty fourth.
- [Spectral Regularity and Degeneracy in the Biquaternion Algebra](spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the biquaternion cone and its strata.
- [Split-Quaternion Algebra](split-quaternion-algebra.html), for the split-quaternion multiplication and the element $1+\vec e_x+\vec e_y$.
