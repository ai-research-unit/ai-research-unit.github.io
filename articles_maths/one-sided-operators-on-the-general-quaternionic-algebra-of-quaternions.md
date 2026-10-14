# __One-Sided Operators on the General Quaternionic Algebra of Quaternions__

## Introduction

The bracket of the block is the general quaternionic bilinear product $\tilde p \star \tilde q = \tilde p^{\natural}\tilde q$ of *Introduction to the General Quaternionic Algebra of Quaternions*, and it is built from two **plain** operations, the left and the right multiplication of the quaternion algebra:

$$
L_{\tilde a}(\tilde x) = \tilde a\tilde x , \qquad R_{\tilde b}(\tilde x) = \tilde x\tilde b .
$$

These two families are the one-sided operators of the block. They are the two copies of the algebra inside the operator algebra, the first an isomorphic copy and the second an anti-isomorphic one; they commute, and every two-sided operator is a product of one of each (*Two-Sided Operators on the General Quaternionic Algebra of Quaternions*, above this article in this category). The quaternionic product itself enters through the forms: the quaternionic bilinear form $N$ of signature $(4,0)$ supplies one adjoint and the plain form $\mathrm B$ of signature $(1,3)$ the other, and the two adjoints are the two faces of the block (*The Isotropic Structure of the General Quaternionic Algebra*, above this article in this category). This article gives the two families, their composition laws and their commutation, the two adjoints, the self-adjoint and the skew sectors for the quaternionic form, and the one-sided operators that are automorphisms of the form; the pin and spin construction that the automorphisms generate is *The Pin and Spin Groups of the General Quaternionic Algebra of Quaternions*, below this article in this category.

**A word on the two left multiplications.** The left multiplication *of the quaternionic product* is the plain left multiplication by the conjugate, $L^{(\star)}_{\tilde a} = L_{\tilde a^{\natural}}$, and its composition law and monoid are the object of *The Left Multiplications of the Quaternionic Product and the Opposite Monoid*, above this article in this category. Here the subject is the two plain families $L$ and $R$ themselves, which are the ones that carry the adjoints and the sectors.

**Conventions.** $\tilde p = \sum_\mu p_\mu e_\mu$, the conjugation ${}^{\natural}$ negates $e_1,e_2,e_3$, the quaternionic form is $N(\tilde p,\tilde q) = \mathrm{Sc}(\tilde p\tilde q^{\natural}) = \sum_\mu p_\mu q_\mu$ of signature $(4,0)$, and the plain form is $\mathrm B(\tilde p,\tilde q) = \mathrm{Sc}(\tilde p\tilde q)$ of signature $(1,3)$; the adjoints are written ${}^{N}$ and ${}^{\sim}$.

## The Two Multiplications

**Definition.** For $\tilde a,\tilde b \in \mathbb{H}$ the **left multiplication** by $\tilde a$ and the **right multiplication** by $\tilde b$ are the real-linear maps $L_{\tilde a}(\tilde x) = \tilde a\tilde x$ and $R_{\tilde b}(\tilde x) = \tilde x\tilde b$. The two families are $\mathcal L = \{L_{\tilde a}\}$ and $\mathcal R = \{R_{\tilde b}\}$.

**Theorem (linearity, the identity, injectivity).** The maps $\tilde a \mapsto L_{\tilde a}$ and $\tilde b \mapsto R_{\tilde b}$ are linear and injective, so $\mathcal L$ and $\mathcal R$ are four-dimensional subspaces of $\operatorname{End}_\mathbb{R}(\mathbb{H})$; $L_{e_0} = R_{e_0} = \mathrm{id}$; and $L_{\tilde a}$, $R_{\tilde b}$ are bijections exactly when $\tilde a$, $\tilde b$ are nonzero, with $L_{\tilde a}^{-1} = L_{\tilde a^{-1}}$ and $R_{\tilde b}^{-1} = R_{\tilde b^{-1}}$.

*Proof.* Linearity in the parameter is linearity of the product in each factor. For injectivity, $L_{\tilde a} = 0$ forces $\tilde a = L_{\tilde a}(e_0) = 0$, and $R_{\tilde b} = 0$ forces $\tilde b = R_{\tilde b}(e_0) = 0$; the identity element gives $L_{e_0} = R_{e_0} = \mathrm{id}$. The inverse of a nonzero parameter is taken in the division algebra, and $L_{\tilde a}L_{\tilde a^{-1}} = L_{e_0} = \mathrm{id}$.

**Remark.** Each one-sided operator is **linear** in its parameter, unlike the two-sided operator, which is bilinear in two parameters. This is why a single one-sided operator cannot carry the form: the form appears only in the composition of two, or in the adjoint.

## Composition Laws and the Two Actions

**Theorem (the composition laws).** For all parameters,

$$
L_{\tilde a}L_{\tilde c} = L_{\tilde a\tilde c} , \qquad R_{\tilde b}R_{\tilde d} = R_{\tilde d\tilde b} , \qquad L_{\tilde a}R_{\tilde b} = R_{\tilde b}L_{\tilde a} .
$$

The left law preserves the order of the parameters and the right law reverses it, so $\mathcal L$ is a copy of the algebra and $\mathcal R$ a copy of the opposite algebra; the two families commute.

*Proof.* $L_{\tilde a}L_{\tilde c}(\tilde x) = \tilde a\tilde c\tilde x = L_{\tilde a\tilde c}(\tilde x)$; $R_{\tilde b}R_{\tilde d}(\tilde x) = \tilde x\tilde d\tilde b = R_{\tilde d\tilde b}(\tilde x)$; the commutation is the associativity of the plain product, $\tilde a(\tilde x\tilde b) = (\tilde a\tilde x)\tilde b$.

**Corollary (the intersection and the span).** $\mathcal L \cap \mathcal R = \{\lambda\,\mathrm{id} : \lambda \in \mathbb{R}\}$ is the scalar line of operators, and $\operatorname{span}_\mathbb{R}(\mathcal L \cup \mathcal R)$ has dimension $7$.

*Proof.* An operator that is both a left and a right multiplication is multiplication by a central element, that is by a real scalar, since the centre of $\mathbb{H}$ is $\mathbb{R}e_0$; the dimension is then $4 + 4 - 1 = 7$.

**Proposition (the double centraliser).** The operators commuting with every left multiplication are exactly the right multiplications, and dually; the operators commuting with both families are the scalars.

*Proof.* A right multiplication commutes with every left multiplication by the composition theorem. Conversely, if $T$ commutes with all $L_{\tilde a}$ and $\tilde b = T(e_0)$, then $T(\tilde a) = T(L_{\tilde a}e_0) = L_{\tilde a}T(e_0) = \tilde a\tilde b = R_{\tilde b}(\tilde a)$, so $T = R_{\tilde b}$; the double centraliser is the intersection of the two families, that is the scalars.

## The Adjoints and the Association

**Theorem (the plain adjoints).** With respect to the plain form $\mathrm B$,

$$
L_{\tilde a}^{\sim} = R_{\tilde a} , \qquad R_{\tilde b}^{\sim} = L_{\tilde b} .
$$

The plain adjoint therefore exchanges the two families and is the identity on their intersection.

*Proof.* $\mathrm B(L_{\tilde a}\tilde p,\tilde q) = \mathrm{Sc}(\tilde a\tilde p\tilde q) = \mathrm{Sc}(\tilde p\tilde q\tilde a) = \mathrm B(\tilde p, R_{\tilde a}\tilde q)$ by the cyclic invariance of the scalar part, which is the association of the two factors; the second identity is the mirror computation.

**Corollary (the association).** The plain adjoint is an anti-isomorphism $\mathcal L \to \mathcal R$ of operator spaces, reading the left multiplication by $\tilde a$ as the right multiplication by $\tilde a$; it is the operator-level form of the exchange of the two factors of a product, and it is the identity on the scalars. A one-sided operator is self-adjoint for $\mathrm B$ exactly when its parameter is central, that is on the scalar line of operators.

*Proof.* $L_{\tilde a}^{\sim} = R_{\tilde a}$, so self-adjointness is $L_{\tilde a} = R_{\tilde a}$, that is $\tilde a\tilde x = \tilde x\tilde a$ for all $\tilde x$, that is centrality.

## The Adjoints for the Quaternionic Form

**Theorem (the quaternionic adjoints).** With respect to the quaternionic form $N$,

$$
L_{\tilde a}^{N} = L_{\tilde a^{\natural}} , \qquad R_{\tilde b}^{N} = R_{\tilde b^{\natural}} .
$$

The quaternionic adjoint therefore **keeps each family in place** and conjugates the parameter, and it is the identity on the scalars.

*Proof.* $N(L_{\tilde a}\tilde p,\tilde q) = \mathrm{Sc}(\tilde a\tilde p\tilde q^{\natural}) = \mathrm{Sc}(\tilde p\,\tilde q^{\natural}\tilde a) = \mathrm{Sc}(\tilde p\,(\tilde a^{\natural}\tilde q)^{\natural}) = N(\tilde p, L_{\tilde a^{\natural}}\tilde q)$, since ${}^{\natural}$ is an anti-automorphism; the right case is the same computation with the factors in the other order.

**Corollary (the two adjoints compared).** The plain adjoint exchanges the families and does not conjugate; the quaternionic adjoint conjugates and does not exchange. The two adjoints agree exactly on the scalar parameters, where conjugation and exchange are both the identity.

*Proof.* The first adjoint sends $L_{\tilde a}$ to $R_{\tilde a}$ and the second to $L_{\tilde a^{\natural}}$; they are equal as maps of the family exactly when $R_{\tilde a} = L_{\tilde a^{\natural}}$, that is $\tilde x\tilde a = \tilde a^{\natural}\tilde x$ for all $\tilde x$, which forces $\tilde a$ central with $\tilde a = \tilde a^{\natural}$, that is $\tilde a \in \mathbb{R}e_0$.

## The Self-Adjoint and Skew Sectors

**Theorem (the sectors for the quaternionic form).** The left multiplication $L_{\tilde a}$ is $N$-self-adjoint exactly when $\tilde a$ is Hermitian, that is on the scalar line $S$; it is $N$-skew-adjoint exactly when $\tilde a$ is anti-Hermitian, that is on the vector subspace $V$. The two sectors are therefore the two eigenspaces of the conjugation, of real dimensions one and three, and the two half-sums give the splitting of the one-sided operators into their symmetric and their alternating parts.

*Proof.* By injectivity, $L_{\tilde a^{\natural}} = L_{\tilde a}$ is $\tilde a^{\natural} = \tilde a$, the fixed subspace of the conjugation, which is the scalar line; $L_{\tilde a^{\natural}} = -L_{\tilde a} = L_{-\tilde a}$ is $\tilde a^{\natural} = -\tilde a$, the negated subspace, which is the vector subspace.

**Corollary (the two readings).** With the plain form the two sectors read differently: a one-sided operator is $\mathrm B$-self-adjoint exactly for a central parameter, that is on the scalar line, and there is no $\mathrm B$-skew sector inside the one-sided families, because $R_{\tilde a} = -L_{\tilde a}$ would force $\tilde a = 0$; the alternating direction appears only in the two-sided layer. The quaternionic form is thus the form of the block that supplies both sectors one-sidedly, and the reason is its definiteness.

*Proof.* The $\mathrm B$-self-adjoint condition is centrality, as above; the skew condition is $\tilde x\tilde a = -\tilde a\tilde x$ for all $\tilde x$, which at $\tilde x = e_0$ gives $\tilde a = 0$.

## The One-Sided Automorphisms of the Form

**Definition.** A one-sided operator is an **automorphism of the form** when it is a bijection preserving it.

**Theorem (the automorphisms of the quaternionic form).** $L_{\tilde a}$ preserves $N$ exactly when $N(\tilde a) = 1$, and so does $R_{\tilde a}$; the one-sided automorphisms of the quaternionic form are the multiplications by an element of the unit shell, a three-dimensional family.

*Proof.* By multiplicativity, $N(L_{\tilde a}\tilde x) = N(\tilde a)N(\tilde x)$, so preservation for all $\tilde x$ is $N(\tilde a) = 1$; the right case is identical. The shell $N = 1$ is the unit sphere of $\mathbb{H} \cong \mathbb{R}^4$, of real dimension three.

**Theorem (the automorphisms of the plain form).** $L_{\tilde a}$ preserves $\mathrm B$ exactly when $\tilde a = \pm e_0$; the one-sided automorphisms of the plain form are $\pm\mathrm{id}$ alone.

*Proof.* The preservation condition is $L_{\tilde a}^{\sim}L_{\tilde a} = \mathrm{id}$, that is $R_{\tilde a}L_{\tilde a} = \mathrm{id}$, that is $\tilde a\tilde x\tilde a = \tilde x$ for all $\tilde x$. At $\tilde x = e_0$ this gives $\tilde a^2 = e_0$; substituting back gives $\tilde a\tilde x = \tilde x\tilde a$ for all $\tilde x$, so $\tilde a$ is central, and a central element with square $e_0$ is $\pm e_0$.

**Corollary (the two families of automorphisms).** The one-sided automorphisms of the quaternionic form are the unit shell, of real dimension three, and they are the pin group of the block (*The Pin and Spin Groups of the General Quaternionic Algebra of Quaternions*, below this article in this category); the one-sided automorphisms of the plain form are only $\pm\mathrm{id}$. The definiteness of the quaternionic form is again the reason: its automorphisms are read off the norm, while the plain form detects only its own square roots of the identity.

## Summary

The one-sided operators of the block are the plain left and right multiplications $L_{\tilde a}(\tilde x) = \tilde a\tilde x$ and $R_{\tilde b}(\tilde x) = \tilde x\tilde b$: linear and injective in the parameter, invertible exactly for a nonzero one; with the composition laws $L_{\tilde a}L_{\tilde c} = L_{\tilde a\tilde c}$, $R_{\tilde b}R_{\tilde d} = R_{\tilde d\tilde b}$ and the commutation $L_{\tilde a}R_{\tilde b} = R_{\tilde b}L_{\tilde a}$; the two families intersect in the scalars and span a seven-dimensional space, and the double centraliser is the scalars. The plain form's adjoint exchanges the two families, $L_{\tilde a}^{\sim} = R_{\tilde a}$ and $R_{\tilde b}^{\sim} = L_{\tilde b}$; the quaternionic form's adjoint conjugates the parameter and keeps the family, $L_{\tilde a}^{N} = L_{\tilde a^{\natural}}$ and $R_{\tilde b}^{N} = R_{\tilde b^{\natural}}$. For the quaternionic form the self-adjoint sector is the scalar line and the skew sector the vector subspace, the two eigenspaces of the conjugation; for the plain form there is no skew sector one-sidedly. A one-sided operator preserves the quaternionic form exactly when its parameter lies on the unit shell, a three-dimensional family, and preserves the plain form only for the two scalar parameters $\pm e_0$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $L_{\tilde a}(\tilde x) = \tilde a\tilde x$, $R_{\tilde b}(\tilde x) = \tilde x\tilde b$ | the one-sided operators of the block |
| $\mathcal L$, $\mathcal R$ | the two four-dimensional families, $\mathcal L \cong \mathbb{H}$, $\mathcal R \cong \mathbb{H}^{\mathrm{opp}}$ |
| $L_{\tilde a}L_{\tilde c} = L_{\tilde a\tilde c}$, $R_{\tilde b}R_{\tilde d} = R_{\tilde d\tilde b}$ | the composition laws, direct on the left and reversed on the right |
| $L_{\tilde a}^{\sim} = R_{\tilde a}$, $R_{\tilde b}^{\sim} = L_{\tilde b}$ | the adjoints for the plain form $\mathrm B$ |
| $L_{\tilde a}^{N} = L_{\tilde a^{\natural}}$, $R_{\tilde b}^{N} = R_{\tilde b^{\natural}}$ | the adjoints for the quaternionic form $N$ |
| $S$, $V$ | the self-adjoint and the skew parameter sectors for $N$ |
| $N(\tilde a) = 1$ | the one-sided automorphisms of the quaternionic form |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the left and right multiplications, the double centraliser and the inner derivations of an algebra.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for the unit group and the derivations of a division ring.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the adjoint attached to a form with an involution and the sectors it produces.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the left and right multiplications of the quaternions and the unit shell.
