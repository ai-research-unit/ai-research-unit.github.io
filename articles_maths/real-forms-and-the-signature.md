# __Real Forms and the Signature__

## Introduction

A Hermitian form over $\mathbb{C}$ is a complex object, and the classical invariant of the forms — the **signature** — is an invariant of a real object. The two are reconciled by the **real form** of the layer: the decomposition of the form of *Polarisation and the Hermitian Square* into a real symmetric part and a real alternating part,

$$
h = g + \mathrm{i}\,\omega, \qquad g = \operatorname{Re}h, \quad \omega = \operatorname{Im}h ,
$$

carries the Hermitian form to a real symmetric form $g$, and the **signature** is the invariant of $g$ under a real change of coordinates. The two readings agree: a Hermitian form over $\mathbb{C}$ is classified up to congruence by its signature $(p,q)$ exactly as a real symmetric form is over $\mathbb{R}$, by *Congruence and the Stabiliser of a Form*, and the real part $g$ doubles the inertia, its signature on the underlying real space of dimension $2n$ being $(2p,2q)$. This article states that correspondence in both directions: the descent of $h$ to a real form halves the inertia back to $(p,q)$, and the complexification doubles it.

A **real structure** on the complex space is a conjugation $c$ compatible with $h$, its fixed space is the real form, and the form descends to the real form exactly when $c$ is compatible; the descended real symmetric form has the signature of $h$, and Sylvester's law of inertia makes the signature the complete invariant over an ordered field. The transfer between the complex and the real readings, and the arithmetic of the transfer, are the Galois descent of the layer and the Weil transfer, and the corresponding algebra-level descent — the real forms of the algebra itself — is *Real Forms of a Sesqualgebra* and *Real Forms and the Descent of an Algebra*.

The inertia is *The Indefinite Case and the Signature*, the classification of the congruence classes is *Congruence and the Stabiliser of a Form*, the real and imaginary parts of the form are *Polarisation and the Hermitian Square*, and the reading of the descent on the biquaternions is *The Form on the Biquaternion Algebra as a General Plain Sesquilinear Form*. Throughout, $\mathbb{C}/\mathbb{R}$ is the base with $\varsigma$ the conjugation, $V$ is a finite-dimensional complex space with a non-degenerate Hermitian form $h$, $g = \operatorname{Re}h$ and $\omega = \operatorname{Im}h$, and $V_{\mathbb{R}}$ is the underlying real space with the complex structure $J$.

## The Real and the Imaginary Parts

**Proposition.** The real part $g$ is a symmetric $\mathbb{R}$-bilinear form on $V_{\mathbb{R}}$ and the imaginary part $\omega$ is alternating; the two are tied by $g(x,y) = \omega(Jx,y)$, and $h$ is recovered from $g$ and from the complex structure.

**Proof.** The symmetry of $g$ and the alternation of $\omega$ are *Polarisation and the Hermitian Square*; the identity $g(x,y) = \omega(Jx,y)$ is the computation $\operatorname{Re}h(x,y) = \operatorname{Im}h(\mathrm{i}x,y)$. Conversely, from $g$ and from $J$ the identity $h(x,y) = g(x,y) + \mathrm{i}g(x,Jy)$ recovers the Hermitian form.

**Corollary.** The Hermitian form is the same datum as the pair (symmetric real form, complex structure) with the compatibility $g(Jx,Jy) = g(x,y)$; the compatibility is the pullback along $J$ of the symmetry, and it is what makes the form Hermitian rather than merely real.

## Real Structures and the Descent

**Definition.** A **real structure** on $V$ is a conjugation $c$, that is, a $\varsigma$-semilinear map with $c^{2} = 1$; its fixed space $V_{0} = V^{c}$ is a real form of $V$, and $V = V_{0}\otimes_{\mathbb{R}}\mathbb{C}$. A real structure is **compatible** with $h$ when

$$
h(cx, cy) = h(y, x) \qquad \text{for all } x, y \in V .
$$

**Proposition.** The real structure $c$ is compatible with $h$ exactly when $h$ descends to a symmetric real form $g_{0}$ on $V_{0}$, that is, exactly when the restriction of $g = \operatorname{Re}h$ to $V_{0}$ is real-valued and its complexification is $h$; then $h$ is the complexification of $g_{0}$.

**Proof.** If $c$ is compatible then for $x, y \in V_{0}$ one has $\varsigma(h(x,y)) = h(cy,cx) = h(y,x)$, so $h$ is symmetric on $V_{0}$ and, its diagonal being real, $h$ coincides there with the symmetric form $g_{0}$; by $\mathbb{C}$-bilinearity the complexification of $g_{0}$ is $h$. Conversely, if $h$ descends to a symmetric real form on $V_{0}$, then for general $x,y$ write them in a real basis of $V_{0}$ and use the $\varsigma$-semilinearity of $c$ and the symmetry of $h$ on $V_{0}$.

**Corollary.** The real forms of $h$ are the compatible real structures, and the descended forms $g_{0}$ are the real symmetric forms of the layer; the passage from $h$ to $g_{0}$ is the **descent** of the layer, and its inverse is the complexification.

**Proposition.** The descended form $g_{0}$ has the signature $(p,q)$ of $h$ itself, and the real part $g = \operatorname{Re}h$ has the signature $(2p,2q)$ on the underlying real space of dimension $2n$; the descent preserves the inertia and the complexification doubles it.

**Proof.** For $x \in V_{0}$ the value $h(x,x)$ is fixed by $\varsigma$ and real, and it equals $g_{0}(x,x)$; a real basis of $V_{0}$ that diagonalises $g_{0}$ with $p$ positive and $q$ negative entries is therefore a basis in which $h$ has the same $p$ positive and $q$ negative entries, so the two signatures agree. Complexifying that basis adds the vectors $J e_{i}$ of the second copy, each contributing the same square again, and the inertia of $g$ on $V_{\mathbb{R}}$ is $(2p,2q)$. Conversely the inertia is the complete invariant on each side, by Sylvester's law.

## The Signature

**Definition.** For a real symmetric form $g_{0}$ on a real space of dimension $n$ the **signature** is the pair $(p,q)$ of the numbers of the positive and the negative squares in a diagonal shape; the form is **definite** when $q = 0$ or $p = 0$ and **indefinite** otherwise.

**Theorem (Sylvester).** Two real symmetric forms are congruent exactly when they have the same signature; the signature is the complete invariant.

**Proof.** The theorem is the law of inertia, proved by the simultaneous diagonalisation and the invariance of the two numbers under a change of basis; the algebraic proof and the Hermitian transfer are *The Indefinite Case and the Signature* and *Congruence and the Stabiliser of a Form*.

**Proposition.** The Hermitian form $h$ is definite exactly when the real part $g$ is definite, and then the Hermitian signature is $(n,0)$ or $(0,n)$ while $g$ has the signature $(2n,0)$ or $(0,2n)$; the indefinite case carries both signs.

**Proof.** $h(x,x) = g(x,x)$ for every $x$, so the diagonal of $h$ is the diagonal of $g$; a Hermitian form is definite when its diagonal has a constant sign, which is the definiteness of $g$, and the two numbers $p$ and $q$ of $h$, with $p+q = n$, become $2p$ and $2q$ for $g$ on the real space of dimension $2n$.

**Corollary (the descent is signature-preserving).** Inside a fixed complex congruence class — fixed by the signature $(p,q)$, by *Congruence and the Stabiliser of a Form* — every compatible real structure descends to a real symmetric form $g_{0}$ of the same signature, so the descended real forms are mutually isometric; the definite classes are the two extreme signatures $(n,0)$ and $(0,n)$ and the indefinite classes the intermediate ones.

## The Transfer Between the Two Readings

**Proposition.** The maps

$$
h \longmapsto g = \operatorname{Re}h, \qquad g \longmapsto h = g\otimes_{\mathbb{R}}\mathbb{C}
$$

are mutually inverse on the forms with a fixed real structure, and they carry the congruence over $\mathbb{R}$ to the congruence over $\mathbb{C}$; the signature is preserved by both, the descent halving the inertia and the complexification doubling it.

**Proof.** The first map is the descent and the second the complexification, and they are inverse by the previous proposition. The signature is preserved by a real change of coordinates by Sylvester's law, and it is preserved by a complex one as well, by the Hermitian reading of the same law: over $\mathbb{C}$ a Hermitian form is classified by its signature, not by its dimension, while a **complex bilinear** symmetric form is classified by its rank alone. The sign can be changed only in the bilinear reading, where the congruence uses the transpose: $C = \operatorname{diag}(1,\mathrm{i})$ sends the bilinear form $\operatorname{diag}(1,1)$ to $\operatorname{diag}(1,-1)$ because $C^{T}\operatorname{diag}(1,1)C = \operatorname{diag}(1,\mathrm{i}^{2})$, whereas the Hermitian $C^{\dagger}\operatorname{diag}(1,-1)C$ of the same $C$ is $\operatorname{diag}(1,-1)$ and no Hermitian form changes its signature along its class. The distinction is *Congruence and the Stabiliser of a Form*.

**Remark (the arithmetic reading).** For an extension of fields with an involution the two constructions are the **transfer** and the **norm** of the forms, and the arithmetic of the transfer is the subject of the theory of the Hermitian and the quadratic forms over a field with an involution; the Witt group of the layer and the transfer between the two groups are *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint* and *Witt's Theorems*.

## Examples

### The Standard Form

On $\mathbb{C}^{n}$ with the standard form $h(x,y) = \sum \bar{x}_{i}y_{i}$ the real part is the Euclidean form of $\mathbb{R}^{2n}$ of signature $(2n,0)$, and the real structure $c$ is the coordinate conjugation; the descended form is the Euclidean form of $\mathbb{R}^{n}$ of signature $(n,0)$.

### The Indefinite Form

On $\mathbb{C}^{n}$ with the form of signature $(p,q)$, $p+q = n$, the real part has signature $(2p,2q)$ on $\mathbb{R}^{2n}$; every compatible real structure descends to a real form of the same signature $(p,q)$, and the family is the set of the real forms of the complex class, all mutually isometric.

### The Biquaternion Algebra

On $\mathbb{B}$ with the form $\operatorname{Sc}(\bar{\tilde Q}\tilde Q')$ the signature over $\mathbb{R}$ is $(2,6)$ and the index is $2$; the definite companion $\operatorname{Sc}(\tilde Q\tilde Q^{\dagger})$ has signature $(8,0)$, and the two readings, together with the Lorentzian one, are *The Form on the Biquaternion Algebra as a General Plain Sesquilinear Form* and *The Low-Dimensional Spin Groups and the Exceptional Isomorphisms with Inner Conjugation*.

## Summary

- A Hermitian form over $\mathbb{C}$ decomposes as $h = g + \mathrm{i}\omega$ into a real symmetric part and a real alternating part, tied by $g(x,y) = \omega(Jx,y)$.
- A **real structure** is a conjugation $c$; it is compatible with $h$ exactly when $h$ descends to a symmetric real form on the fixed space, and then $h$ is its complexification.
- The **signature** $(p,q)$ is the complete invariant of a real symmetric form (Sylvester) and of a Hermitian form over $\mathbb{C}$, and $h$ is definite exactly when $g$ is.
- The complex congruence class is fixed by the signature $(p,q)$, and every compatible real structure inside it descends to a real form of the same signature; the two constructions between $h$ and $g$ are the descent and the complexification, the transfer and the norm in the arithmetic reading.
- The descent **halves** the inertia and the complexification **doubles** it: $g_{0}$ has signature $(p,q)$ on $V_{0}$ and $g = \operatorname{Re}h$ has signature $(2p,2q)$ on $V_{\mathbb{R}}$.
- The algebra-level descent is *Real Forms of a Sesqualgebra*; the inertia is *The Indefinite Case and the Signature*; the biquaternion signatures are *The Form on the Biquaternion Algebra as a General Plain Sesquilinear Form*.

## Summary of Notation

| symbol | meaning |
|---|---|
| $g = \operatorname{Re}h$ | the real symmetric part of the Hermitian form |
| $\omega = \operatorname{Im}h$ | the real alternating part |
| $J$ | the complex structure, with $g(x,y) = \omega(Jx,y)$ |
| $c$ | a real structure, a conjugation of the complex space |
| $V_{0} = V^{c}$ | the real form, the fixed space of $c$ |
| $g_{0}$ | the descended real symmetric form |
| $(p,q)$ | the signature of a real symmetric form |

## Further Reading

- Winfried Scharlau, *Quadratic and Hermitian Forms* (Springer, 1985), for the descent, the transfer and the classification of the forms over a field with an involution.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields*, Graduate Studies in Mathematics 67 (American Mathematical Society, 2005), for Sylvester's law, the signature and the definite and indefinite cases.
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings*, Grundlehren der mathematischen Wissenschaften 294 (Springer, 1991), for the Hermitian forms over a field with an involution and their real forms.
