# __One-Sided Operators on the General Quaternionic Algebra__

## Introduction

The bracket of the block is the general quaternionic bilinear product $\tilde q_1 \star \tilde q_2 = \tilde q_1^{\natural}\tilde q_2$ of *Introduction to the General Quaternionic Algebra*, and it is built from two **plain** operations, the left and the right multiplication of the quaternion algebra:

$$
L_{\tilde q_3}(\tilde q) = \tilde q_3\tilde q , \qquad R_{\tilde q_4}(\tilde q) = \tilde q\tilde q_4 .
$$

These two families are the one-sided operators of the block. They are the two copies of the algebra inside the operator algebra, the first an isomorphic copy and the second an anti-isomorphic one; they commute, and every two-sided operator is a product of one of each (*Two-Sided Operators on the General Quaternionic Algebra*, above this article in this category). The quaternionic product itself enters through the forms: the quaternionic bilinear form $\langle\cdot,\cdot\rangle_{\natural}$ of signature $(4,0)$ supplies one adjoint and the plain form $\mathrm B$ of signature $(1,3)$ the other, and the two adjoints are the two faces of the block (*The Isotropic Structure of the General Quaternionic Algebra*, above this article in this category). This article gives the two families, their composition laws and their commutation, the two adjoints, the self-adjoint and the skew sectors for the quaternionic form, and the one-sided operators that are automorphisms of the form; the pin and spin construction that the automorphisms generate is *The Pin and Spin Groups of the General Quaternionic Algebra*, below this article in this category.

**A word on the two left multiplications.** The left multiplication *of the quaternionic product* is the plain left multiplication by the conjugate, $L^{(\star)}_{\tilde q_3} = L_{\tilde q_3^{\natural}}$, and its composition law and monoid are the object of *The Left Multiplications of the Quaternionic Product and the Opposite Monoid*, above this article in this category. Here the subject is the two plain families $L$ and $R$ themselves, which are the ones that carry the adjoints and the sectors.

## The Two Multiplications

**Definition.** For $\tilde q_3,\tilde q_4 \in \mathbb{H}$ the **left multiplication** by $\tilde q_3$ and the **right multiplication** by $\tilde q_4$ are the real-linear maps $L_{\tilde q_3}(\tilde q) = \tilde q_3\tilde q$ and $R_{\tilde q_4}(\tilde q) = \tilde q\tilde q_4$. The two families are $\mathcal L = \{L_{\tilde q_3}\}$ and $\mathcal R = \{R_{\tilde q_4}\}$.

**Theorem (linearity, the identity, injectivity).** The maps $\tilde q_3 \mapsto L_{\tilde q_3}$ and $\tilde q_4 \mapsto R_{\tilde q_4}$ are linear and injective, so $\mathcal L$ and $\mathcal R$ are four-dimensional subspaces of $\operatorname{End}_\mathbb{R}(\mathbb{H})$; $L_{e_t} = R_{e_t} = \mathrm{id}$; and $L_{\tilde q_3}$, $R_{\tilde q_4}$ are bijections exactly when $\tilde q_3$, $\tilde q_4$ are nonzero, with $L_{\tilde q_3}^{-1} = L_{\tilde q_3^{-1}}$ and $R_{\tilde q_4}^{-1} = R_{\tilde q_4^{-1}}$.

*Proof.* Linearity in the parameter is linearity of the product in each factor. For injectivity, $L_{\tilde q_3} = 0$ forces $\tilde q_3 = L_{\tilde q_3}(e_t) = 0$, and $R_{\tilde q_4} = 0$ forces $\tilde q_4 = R_{\tilde q_4}(e_t) = 0$; the identity element gives $L_{e_t} = R_{e_t} = \mathrm{id}$. The inverse of a nonzero parameter is taken in the division algebra, and $L_{\tilde q_3}L_{\tilde q_3^{-1}} = L_{e_t} = \mathrm{id}$.

**Remark.** Each one-sided operator is **linear** in its parameter, unlike the two-sided operator, which is bilinear in two parameters. This is why a single one-sided operator cannot carry the form: the form appears only in the composition of two, or in the adjoint.

## Composition Laws and the Two Actions

**Theorem (the composition laws).** For all parameters,

$$
\boxed{\;L_{\tilde q_3}L_{\tilde q_5} = L_{\tilde q_3\tilde q_5} , \qquad R_{\tilde q_4}R_{\tilde q_6} = R_{\tilde q_6\tilde q_4} , \qquad L_{\tilde q_3}R_{\tilde q_4} = R_{\tilde q_4}L_{\tilde q_3}\;}.
$$

The left law preserves the order of the parameters and the right law reverses it, so $\mathcal L$ is a copy of the algebra and $\mathcal R$ a copy of the opposite algebra; the two families commute.

*Proof.* $L_{\tilde q_3}L_{\tilde q_5}(\tilde q) = \tilde q_3\tilde q_5\tilde q = L_{\tilde q_3\tilde q_5}(\tilde q)$; $R_{\tilde q_4}R_{\tilde q_6}(\tilde q) = \tilde q\tilde q_6\tilde q_4 = R_{\tilde q_6\tilde q_4}(\tilde q)$; the commutation is the associativity of the plain product, $\tilde q_3(\tilde q\tilde q_4) = (\tilde q_3\tilde q)\tilde q_4$.

**Corollary (the intersection and the span).** $\mathcal L \cap \mathcal R = \{\lambda\,\mathrm{id} : \lambda \in \mathbb{R}\}$ is the scalar line of operators, and $\operatorname{span}_\mathbb{R}(\mathcal L \cup \mathcal R)$ has dimension $7$.

*Proof.* An operator that is both a left and a right multiplication is multiplication by a central element, that is by a real scalar, since the centre of $\mathbb{H}$ is $\mathbb{R}e_t$; the dimension is then $4 + 4 - 1 = 7$.

**Proposition (the double centraliser).** The operators commuting with every left multiplication are exactly the right multiplications, and dually; the operators commuting with both families are the scalars.

*Proof.* A right multiplication commutes with every left multiplication by the composition theorem. Conversely, if $T$ commutes with all $L_{\tilde q_3}$ and $\tilde q_4 = T(e_t)$, then $T(\tilde q_3) = T(L_{\tilde q_3}e_t) = L_{\tilde q_3}T(e_t) = \tilde q_3\tilde q_4 = R_{\tilde q_4}(\tilde q_3)$, so $T = R_{\tilde q_4}$; the double centraliser is the intersection of the two families, that is the scalars.

## The Adjoints and the Association

**Theorem (the plain adjoints).** With respect to the plain form $\mathrm B$,

$$
\boxed{\;L_{\tilde q_3}^{\sim} = R_{\tilde q_3} , \qquad R_{\tilde q_4}^{\sim} = L_{\tilde q_4}\;}.
$$

The plain adjoint therefore exchanges the two families and is the identity on their intersection.

*Proof.* $\langle L_{\tilde q_3}\tilde q_1,\tilde q_2\rangle = \mathrm{Sc}(\tilde q_3\tilde q_1\tilde q_2) = \mathrm{Sc}(\tilde q_1\tilde q_2\tilde q_3) = \langle\tilde q_1,R_{\tilde q_3}\tilde q_2\rangle$ by the cyclic invariance of the scalar part, which is the association of the two factors; the second identity is the mirror computation.

**Corollary (the association).** The plain adjoint is an anti-isomorphism $\mathcal L \to \mathcal R$ of operator spaces, reading the left multiplication by $\tilde q_3$ as the right multiplication by $\tilde q_3$; it is the operator-level form of the exchange of the two factors of a product, and it is the identity on the scalars. A one-sided operator is self-adjoint for $\mathrm B$ exactly when its parameter is central, that is on the scalar line of operators.

*Proof.* $L_{\tilde q_3}^{\sim} = R_{\tilde q_3}$, so self-adjointness is $L_{\tilde q_3} = R_{\tilde q_3}$, that is $\tilde q_3\tilde q = \tilde q\tilde q_3$ for all $\tilde q$, that is centrality.

## The Adjoints for the Quaternionic Form

**Theorem (the quaternionic adjoints).** With respect to the quaternionic form $\langle\cdot,\cdot\rangle_{\natural}$,

$$
\boxed{\;L_{\tilde q_3}^{N} = L_{\tilde q_3^{\natural}} , \qquad R_{\tilde q_4}^{N} = R_{\tilde q_4^{\natural}}\;}.
$$

The quaternionic adjoint therefore **keeps each family in place** and conjugates the parameter, and it is the identity on the scalars.

*Proof.* $\langle L_{\tilde q_3}\tilde q_1,\tilde q_2\rangle_{\natural} = \mathrm{Sc}(\tilde q_3\tilde q_1\tilde q_2^{\natural}) = \mathrm{Sc}(\tilde q_1\,\tilde q_2^{\natural}\tilde q_3) = \mathrm{Sc}(\tilde q_1\,(\tilde q_3^{\natural}\tilde q_2)^{\natural}) = \langle\tilde q_1,L_{\tilde q_3^{\natural}}\tilde q_2\rangle_{\natural}$, since ${}^{\natural}$ is an anti-automorphism; the right case is the same computation with the factors in the other order.

**Corollary (the two adjoints compared).** The plain adjoint exchanges the families and does not conjugate; the quaternionic adjoint conjugates and does not exchange. The two adjoints agree exactly on the scalar parameters, where conjugation and exchange are both the identity.

*Proof.* The first adjoint sends $L_{\tilde q_3}$ to $R_{\tilde q_3}$ and the second to $L_{\tilde q_3^{\natural}}$; they are equal as maps of the family exactly when $R_{\tilde q_3} = L_{\tilde q_3^{\natural}}$, that is $\tilde q\tilde q_3 = \tilde q_3^{\natural}\tilde q$ for all $\tilde q$, which forces $\tilde q_3$ central with $\tilde q_3 = \tilde q_3^{\natural}$, that is $\tilde q_3 \in \mathbb{R}e_t$.

## The Self-Adjoint and Skew Sectors

**Theorem (the sectors for the quaternionic form).** The left multiplication $L_{\tilde q_3}$ is $\langle\cdot,\cdot\rangle_{\natural}$-self-adjoint exactly when $\tilde q_3$ is Hermitian, that is on the scalar line $S$; it is $N$-skew-adjoint exactly when $\tilde q_3$ is anti-Hermitian, that is on the vector subspace $V$. The two sectors are therefore the two eigenspaces of the conjugation, of real dimensions one and three, and the two half-sums give the splitting of the one-sided operators into their symmetric and their alternating parts.

*Proof.* By injectivity, $L_{\tilde q_3^{\natural}} = L_{\tilde q_3}$ is $\tilde q_3^{\natural} = \tilde q_3$, the fixed subspace of the conjugation, which is the scalar line; $L_{\tilde q_3^{\natural}} = -L_{\tilde q_3} = L_{-\tilde q_3}$ is $\tilde q_3^{\natural} = -\tilde q_3$, the negated subspace, which is the vector subspace.

**Corollary (the two readings).** With the plain form the two sectors read differently: a one-sided operator is $\mathrm B$-self-adjoint exactly for a central parameter, that is on the scalar line, and there is no $\mathrm B$-skew sector inside the one-sided families, because $R_{\tilde q_3} = -L_{\tilde q_3}$ would force $\tilde q_3 = 0$; the alternating direction appears only in the two-sided layer. The quaternionic form is thus the form of the block that supplies both sectors one-sidedly, and the reason is its definiteness.

*Proof.* The $\mathrm B$-self-adjoint condition is centrality, as above; the skew condition is $\tilde q\tilde q_3 = -\tilde q_3\tilde q$ for all $\tilde q$, which at $\tilde q = e_t$ gives $\tilde q_3 = 0$.

## The One-Sided Automorphisms of the Form

**Definition.** A one-sided operator is an **automorphism of the form** when it is a bijection preserving it.

**Theorem (the automorphisms of the quaternionic form).** $L_{\tilde q_3}$ preserves $\langle\cdot,\cdot\rangle_{\natural}$ exactly when $\langle\tilde q_3\rangle_{\natural} = 1$, and so does $R_{\tilde q_3}$; the one-sided automorphisms of the quaternionic form are the multiplications by an element of the unit shell, a three-dimensional family.

*Proof.* By multiplicativity, $\langle L_{\tilde q_3}\tilde q\rangle_{\natural} = \langle\tilde q_3\rangle_{\natural}\langle\tilde q\rangle_{\natural}$, so preservation for all $\tilde q$ is $\langle\tilde q_3\rangle_{\natural} = 1$; the right case is identical. The shell $N = 1$ is the unit sphere of $\mathbb{H} \cong \mathbb{R}^4$, of real dimension three.

**Theorem (the automorphisms of the plain form).** $L_{\tilde q_3}$ preserves $\mathrm B$ exactly when $\tilde q_3 = \pm e_t$; the one-sided automorphisms of the plain form are $\pm\mathrm{id}$ alone.

*Proof.* The preservation condition is $L_{\tilde q_3}^{\sim}L_{\tilde q_3} = \mathrm{id}$, that is $R_{\tilde q_3}L_{\tilde q_3} = \mathrm{id}$, that is $\tilde q_3\tilde q\tilde q_3 = \tilde q$ for all $\tilde q$. At $\tilde q = e_t$ this gives $\tilde q_3^2 = e_t$; substituting back gives $\tilde q_3\tilde q = \tilde q\tilde q_3$ for all $\tilde q$, so $\tilde q_3$ is central, and a central element with square $e_t$ is $\pm e_t$.

**Corollary (the two families of automorphisms).** The one-sided automorphisms of the quaternionic form are the unit shell, of real dimension three, and they are the pin group of the block (*The Pin and Spin Groups of the General Quaternionic Algebra*, below this article in this category); the one-sided automorphisms of the plain form are only $\pm\mathrm{id}$. The definiteness of the quaternionic form is again the reason: its automorphisms are read off the norm, while the plain form detects only its own square roots of the identity.

## Summary

The one-sided operators of the block are the plain left and right multiplications $L_{\tilde q_3}(\tilde q) = \tilde q_3\tilde q$ and $R_{\tilde q_4}(\tilde q) = \tilde q\tilde q_4$: linear and injective in the parameter, invertible exactly for a nonzero one; with the composition laws $L_{\tilde q_3}L_{\tilde q_5} = L_{\tilde q_3\tilde q_5}$, $R_{\tilde q_4}R_{\tilde q_6} = R_{\tilde q_6\tilde q_4}$ and the commutation $L_{\tilde q_3}R_{\tilde q_4} = R_{\tilde q_4}L_{\tilde q_3}$; the two families intersect in the scalars and span a seven-dimensional space, and the double centraliser is the scalars. The plain form's adjoint exchanges the two families, $L_{\tilde q_3}^{\sim} = R_{\tilde q_3}$ and $R_{\tilde q_4}^{\sim} = L_{\tilde q_4}$; the quaternionic form's adjoint conjugates the parameter and keeps the family, $L_{\tilde q_3}^{N} = L_{\tilde q_3^{\natural}}$ and $R_{\tilde q_4}^{N} = R_{\tilde q_4^{\natural}}$. For the quaternionic form the self-adjoint sector is the scalar line and the skew sector the vector subspace, the two eigenspaces of the conjugation; for the plain form there is no skew sector one-sidedly. A one-sided operator preserves the quaternionic form exactly when its parameter lies on the unit shell, a three-dimensional family, and preserves the plain form only for the two scalar parameters $\pm e_t$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $L_{\tilde q_3}(\tilde q) = \tilde q_3\tilde q$, $R_{\tilde q_4}(\tilde q) = \tilde q\tilde q_4$ | the one-sided operators of the block |
| $\mathcal L$, $\mathcal R$ | the two four-dimensional families, $\mathcal L \cong \mathbb{H}$, $\mathcal R \cong \mathbb{H}^{\mathrm{opp}}$ |
| $L_{\tilde q_3}L_{\tilde q_5} = L_{\tilde q_3\tilde q_5}$, $R_{\tilde q_4}R_{\tilde q_6} = R_{\tilde q_6\tilde q_4}$ | the composition laws, direct on the left and reversed on the right |
| $L_{\tilde q_3}^{\sim} = R_{\tilde q_3}$, $R_{\tilde q_4}^{\sim} = L_{\tilde q_4}$ | the adjoints for the plain form $\mathrm B$ |
| $L_{\tilde q_3}^{N} = L_{\tilde q_3^{\natural}}$, $R_{\tilde q_4}^{N} = R_{\tilde q_4^{\natural}}$ | the adjoints for the quaternionic form $\langle\cdot,\cdot\rangle_{\natural}$ |
| $S$, $V$ | the self-adjoint and the skew parameter sectors for $\langle\cdot,\cdot\rangle_{\natural}$ |
| $\langle\tilde q_3\rangle_{\natural} = 1$ | the one-sided automorphisms of the quaternionic form |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the left and right multiplications, the double centraliser and the inner derivations of an algebra.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for the unit group and the derivations of a division ring.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the adjoint attached to a form with an involution and the sectors it produces.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the left and right multiplications of the quaternions and the unit shell.
