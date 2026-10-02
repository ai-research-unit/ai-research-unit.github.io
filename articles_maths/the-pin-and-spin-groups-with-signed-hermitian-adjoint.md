# __The Pin and Spin Groups with Signed Hermitian Adjoint__

## Introduction

The classical construction of the covering groups of the orthogonal group uses the inverse: the Clifford group is the set of units $x$ for which $x\,v\,x^{-1}$ is again a vector, the norm $N(x)=x x^{\natural}$ cuts it down to $\mathrm{Pin}$, and the parity cuts $\mathrm{Pin}$ down to $\mathrm{Spin}$. The right factor in all of it is $x^{-1}$, and the operator carrying it is the signed inner conjugation $\mathrm{Ad}^{\alpha}_x(v)=\alpha(x)vx^{-1}$.

This article makes the same construction with the right factor replaced by the dagger, that is with the **signed Hermitian sandwich** of *Two-Sided Operators on a Hilbert Algebra with Signed Hermitian Adjoint*,

$$
\Theta^{\alpha}_x(v)=\alpha(x)\,v\,x^{\dagger},
$$

and it isolates what changes. The dagger needs an involution $\sigma$ of the base and is defined on the whole algebra; the inverse needs invertibility and nothing else. Three objects must therefore be compared rather than one. The **Clifford group** $\Gamma(V,q)$ is defined by the condition $\mathrm{Ad}^{\alpha}_x(V)\subseteq V$; the **unitary slice** $U=\{x:x^{\dagger}x=1\}$ is defined by the dagger; and the new object is the set of parameters for which the Hermitian sandwich is an *isometry* of $V$,

$$
\Gamma_{\dagger}=\{\,x\in\Gamma(V,q) : \sigma(N(x))^{2}=1\,\},
$$

the **Hermitian Clifford group**. The three are related by two facts: the Hermitian sandwich preserves $V$ exactly for $x\in\Gamma$ and is an isometry exactly for $x\in\Gamma_{\dagger}$, by the action proposition of the companion article; and on the slice $U$ the dagger is the inverse, so there $\Theta^{\alpha}_x=\mathrm{Ad}^{\alpha}_x$ and the whole inverse theory transfers verbatim.

The payoff is a single clean statement. With the trivial involution the Hermitian Clifford group **is** the pin group, $\Gamma_{\dagger}=\mathrm{Pin}$, and the hermitian reading of $\mathrm{Pin}$ is the set of elements whose Hermitian sandwich is an isometry; the odd part of it gives the reflections and the even part the rotations, and the map to $O(V,q)$ is two-to-one exactly as for the inverse member. The general involution $\sigma$ widens the scalars and the norm condition but changes no group-theoretic statement, because everything is a scalar modification of the inverse member on the slice.

The groups $\Gamma$, $\mathrm{Pin}$, $\mathrm{Spin}$, the norm and the exact sequences are *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*; the dagger and the involution of the base are *Hilbert Algebras*; the unitary slice, its compactness and the compact real form are *The Unitary Slice and the Compact Real Form with Hermitian Adjoint*; the operator and its action on $V$ are *Two-Sided Operators on a Hilbert Algebra with Signed Hermitian Adjoint*; the unsigned member and its Clifford-group identities are *The Hermitian Sandwich on a Hilbert Algebra with Hermitian Adjoint*. Nothing owned by those entries is reproved.

**Conventions.** The base $A$ is a commutative ring with involution $\sigma$, $F$ is the field of scalars of the Clifford algebra, $V$ is free of rank $n$ with a non-degenerate quadratic form $q$, $x^{\dagger}=\sigma(\alpha(x^{r}))$, $x^{\natural}=\alpha(x^{r})$ is Clifford conjugation, $N(x)=x x^{\natural}$, $\rho_u(v)=v-2g(v,u)q(u)^{-1}u$, and $\Theta^{\alpha}_x$, $\Theta_x$, $\mathrm{Ad}^{\alpha}_x$ are the three sandwiches named above.

## The Three Conditions

**Proposition (the slice is a group).** $U=\{x:x^{\dagger}x=1\}$ is a subgroup of the unit group. It contains $1$; if $x\in U$ then $x^{\dagger}=x^{-1}$ and $x^{\dagger}\in U$; and $U$ is closed under multiplication.

*Proof.* This is the slice proposition of *The Hermitian Sandwich on a Hilbert Algebra with Hermitian Adjoint*: $(xy)^{\dagger}(xy)=y^{\dagger}x^{\dagger}xy=y^{\dagger}y=1$.

**Proposition (the Hermitian Clifford group is a group).** $\Gamma_{\dagger}=\{x\in\Gamma(V,q):\sigma(N(x))^{2}=1\}$ is a subgroup of $\Gamma(V,q)$, and it is the set of parameters for which the Hermitian sandwiches restrict to isometries of $V$,

$$
\Theta^{\alpha}_x(V)\subseteq V\iff x\in\Gamma(V,q),
\qquad
\Theta^{\alpha}_x\bigr|_{V}\in O(V,q)\iff x\in\Gamma_{\dagger}.
$$

*Proof.* $N$ is multiplicative on $\Gamma$ and $\sigma$ is a ring homomorphism, so $\sigma(N(xy))=\sigma(N(x))\sigma(N(y))$ and the condition $\sigma(N)^{2}=1$ is closed under multiplication and inversion; it holds at $1$. The two equivalences are the action proposition of the companion article, where the operator acts on $V$ as $\varepsilon_x\sigma(N(x))\chi(x)$ with $\chi(x)\in O(V,q)$, so it is an isometry exactly when the scalar has square $1$.

**Proposition (the slice meets the Clifford group in the norm-one subgroup).** With the trivial involution, $\sigma=\mathrm{id}$, the dagger is the Clifford conjugation, $x^{\dagger}=x^{\natural}$, and on the Clifford group $x^{\natural}\,x=N(x)$. Hence

$$
U\cap\Gamma(V,q)=\{\,x\in\Gamma:N(x)=1\,\},
\qquad
\Gamma_{\dagger}=\{\,x\in\Gamma:N(x)=\pm1\,\}=\mathrm{Pin}(V,q).
$$

So the Hermitian Clifford group **is** the pin group, and the slice meets it in the norm-one subgroup, of index at most two. For a definite form in the convention of the corpus, $q$ negative definite, the value $N(x)=\prod_i(-q(v_i))$ is positive for every $x\in\Gamma$, so the two coincide, $U\cap\Gamma=\Gamma_{\dagger}=\mathrm{Pin}(V,q)$, and the slice recovers the pin group as in *The Unitary Slice and the Compact Real Form with Hermitian Adjoint*; for an indefinite form $U\cap\Gamma=\{N=1\}$ is the double cover of the identity component $SO^{+}(V,q)$.

*Proof.* For $\sigma=\mathrm{id}$ the dagger is $x^{\natural}$, so $U=\{x:x^{\natural}x=1\}$; on $\Gamma$ one has $x^{\natural}=N(x)x^{-1}$, hence $x^{\natural}x=N(x)$ and $U\cap\Gamma=\{x\in\Gamma:N(x)=1\}$, while $\Gamma_{\dagger}=\{x\in\Gamma:N(x)^{2}=1\}=\{x\in\Gamma:N(x)=\pm1\}$, which is the pin group of the inverse article. For a negative definite form the factors $-q(v_i)$ are positive, so $N$ is positive on the versors and on $\Gamma$, and $N(x)=\pm1$ is $N(x)=1$.

**Remark (the equality is the point).** The proposition says that in the trivial-involution case the three conditions — "the dagger is the inverse", "the Hermitian sandwich is an isometry", "the norm is $\pm1$" — cut $\Gamma$ down to the same group, the pin group being the isometry locus and the slice its norm-one subgroup. The Hermitian sandwich therefore needs no new group: it reconstructs $\mathrm{Pin}$ from the adjunction rather than from the inversion, and the identity $\Theta^{\alpha}_x=\mathrm{Ad}^{\alpha}_x$ on the slice is what makes the two constructions agree.

**Remark (for a general involution the three differ).** The slice $U$ and the Hermitian Clifford group $\Gamma_{\dagger}$ are different subsets of the unit group in general. The slice condition is $x^{\dagger}x=1$ and it does not involve the quadratic form; the isometry condition is $\sigma(N(x))^{2}=1$ and it does. An element can be a unit of norm $\pm1$ without being on the slice, and an element of the slice can have $\sigma(N(x))^{2}\neq1$; in the trivial-involution case the two reduce to $U\cap\Gamma=\{N=1\}$ and $\Gamma_{\dagger}=\{N=\pm1\}=\mathrm{Pin}$, which coincide for a definite form and differ by an index-two subgroup otherwise. The scalar widening by $\sigma$ is the only trace of the coefficient involution in the group theory.

## The Reflections and the Covering

**Proposition (the reflections are the odd elements).** Let $u\in V$ with $q(u)\neq0$. Then $u$ is odd, $u^{\dagger}=-\sigma(u)$, and

$$
\Theta^{\alpha}_u(v)=u\,v\,\sigma(u)=-q(u)\,\rho_u(v),\qquad v\in V .
$$

On a vector of square $-1$ the signed Hermitian sandwich **is** the reflection, $\Theta^{\alpha}_u=\rho_u$, and $\Theta^{\alpha}_u\in\Gamma_\bar{\cdot}$; the unsigned Hermitian sandwich is $-\rho_u$ there. So the odd elements of the Hermitian Clifford group realise the reflections, and the even ones realise the rotations.

*Proof.* The vector identity and the reflection statement are the propositions of the companion article; $\Theta^{\alpha}_u$ is an isometry for a unit vector by the determinant-and-scalar computation: $-q(u)$ has square $1$ when $q(u)=\pm1$. That an even element gives a rotation follows from $\Theta^{\alpha}_x=\Theta_x=\mathrm{Ad}_x$ on the slice and the parity of the determinant.

**Theorem (the double cover, in the Hermitian formulation).** Suppose that $-1$ is not a square in $F$ and that every element of $F^{\times}$ differs from $\pm1$ by a square; both hold over $\mathbb{R}$. Let the involution be trivial and the form definite in the corpus's convention, $q$ negative definite, so that every element of $\mathrm{Pin}(V,q)$ lies on the slice and $\Gamma_{\dagger}=U\cap\Gamma=\mathrm{Pin}(V,q)$. Then

$$
1\longrightarrow\{\pm1\}\longrightarrow \mathrm{Pin}(V,q)\xrightarrow{\ \Theta^{\alpha}\ } O(V,q)\longrightarrow 1,
\qquad
1\longrightarrow\{\pm1\}\longrightarrow \mathrm{Spin}(V,q)\xrightarrow{\ \Theta^{\alpha}\ } SO(V,q)\longrightarrow 1
$$

are exact, with the same two-to-one identification $x\sim-x$ as in the inverse formulation.

*Proof.* On $U$ the operator is the signed inner conjugation, $\Theta^{\alpha}_x=\mathrm{Ad}^{\alpha}_x$; the two exact sequences are therefore those of *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*, transported along the identity $U=\Gamma_{\dagger}$ of the previous section. The kernel is $\{\pm1\}$ by the slice corollary of the companion article.

**Remark (the general involution).** For a nontrivial $\sigma$ the sequence must be read with the scalars of the base: the kernel of $\Theta^{\alpha}$ on $\Gamma_{\dagger}$ is $F^{\times}\cap\Gamma_{\dagger}=\{\lambda\in F^{\times}:\sigma(\lambda^{2})^{2}=1\}$, which contains the scalars of fourth root of unity and, over a field with $-1$ not a square, still gives the two elements $\{\pm1\}$ when $\sigma$ fixes $F$. The image is $O(V,q)$ whenever the reflections can be rescaled to unit vectors, exactly as in the inverse case. So the covering statement is insensitive to $\sigma$ up to the scalars, and no new group-theoretic phenomenon appears.

## Cartan–Dieudonné and the Reflection Length

**Theorem (Cartan–Dieudonné).** Let $(V,q)$ be a non-degenerate quadratic space of dimension $n$ over a field of characteristic not two. Every isometry of $V$ is a product of at most $n$ reflections, and it lies in $SO(V,q)$ exactly when it is a product of an even number of them.

*Proof.* Quoted from *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*; the theorem is independent of which sandwich realises the reflections.

**Corollary (the Hermitian reading).** With $\sigma=\mathrm{id}$, every element of $O(V,q)$ is a product of signed Hermitian sandwiches of unit vectors,

$$
\gamma=\Theta^{\alpha}_{u_1}\circ\cdots\circ\Theta^{\alpha}_{u_k},\qquad q(u_i)=-1,
$$

with $k$ even exactly when $\gamma\in SO(V,q)$; the word length $k$ is the reflection length of $\gamma$ and the algebraic length of the corresponding element of $\mathrm{Pin}$ in the generating set of unit vectors. The reflections are the Hermitian sandwiches of the odd elements, and the parity of the number of factors is the determinant.

*Proof.* The unit vectors are in $\mathrm{Pin}$ and $\Theta^{\alpha}_u=\rho_u$; Cartan–Dieudonné writes the isometry as a product of reflections; the parity and determinant statements are the parity proposition of the companion article.

## Low-Dimensional Cases

Over $\mathbb{R}$ with the definite negative form, $e_j^{2}=-1$ and $\sigma=\mathrm{id}$, the constructions read as follows.

- $n=1$: $\mathrm{Cl}_{0,1}\cong\mathbb{C}$, $\mathrm{Pin}=\{\pm1,\pm e_1\}$, and $\Theta^{\alpha}_{e_1}=\rho_{e_1}$ is the single nontrivial reflection; $\mathrm{Spin}=\{\pm1\}$.
- $n=2$: $\mathrm{Cl}_{0,2}\cong\mathbb{H}$, $\mathrm{Pin}$ is the group of $24$ Hurwitz units up to sign, equal to $\{\pm1,\pm e_1,\pm e_2,\pm e_3\}$ with $e_3=e_1e_2$; the even part $\mathrm{Spin}=\{\pm1,\pm e_3\}$ is the circle group of the plane, and $\Theta^{\alpha}_{e_3}$ is the rotation through $\pi$.
- $n=3$: $\mathrm{Cl}_{0,3}\cong\mathbb{H}\oplus\mathbb{H}$, $\mathrm{Pin}$ is the binary octahedral group of order $48$, $\mathrm{Spin}$ is the binary tetrahedral group of order $24$; the odd elements give the reflections and the even ones the rotations of $\mathbb{R}^{3}$, and the unit vectors $e_1,e_2,e_3$ give $\rho_{e_1},\rho_{e_2},\rho_{e_3}$.

In each case $\mathrm{Pin}$ is compact because the form is definite, the norm $N(x)=x x^{\natural}$ is a nonzero real, and the Hermitian sandwich of a unit vector is the reflection with no rescaling. The dictionary with the biquaternion algebra, where the Hermitian sandwich is the corpus sandwich $\tilde Q\,x\,\bar{\tilde{Q}}$ and the slice is the Lorentz group, is *Biquaternion Versors and the Orthogonal Group* in the physics corpus.

## The Indefinite and Degenerate Cases

**Remark (isotropic vectors).** If $q$ is indefinite, a vector with $q(u)=0$ is not invertible and not on the slice; neither Hermitian sandwich is defined for it as an isometry, and the reflection $\rho_u$ does not exist. The construction is confined to the non-isotropic vectors in both formulations, and the Hermitian one has no advantage there.

**Remark (the norm can be isotropic).** On $\mathrm{Cl}_{1,1}\cong M_2(\mathbb{R})$ the norm is the determinant of signature $(2,2)$ and vanishes on the nonzero rank-one matrices. Those elements are zero divisors and not in $\Gamma$, so $\Gamma_{\dagger}\subseteq\Gamma$ excludes them; but an element of the slice can lie outside $\Gamma$, and the two conditions are genuinely independent off the trivial-involution case, as the next remark records.

**Remark (the slice is not inside the Clifford group).** In $\mathrm{Cl}_{1,1}\cong M_2(\mathbb{R})$ the element $1-\tfrac12e_2-\tfrac12e_1e_2$ has norm $1$ and is a unit, and its signed inner conjugation does not preserve $V$, by *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*. The same element shows that a unit can satisfy a norm condition and fail the Clifford-group condition, which is why $\Gamma_{\dagger}$ is defined inside $\Gamma$ and not by a norm condition alone. In the trivial-involution case this cannot happen, because there the norm condition and the slice condition coincide with membership in $\Gamma$.

**Remark (the degenerate case).** If $q$ is degenerate the Clifford group need not act on $V$ by invertible maps, the map to $O(V,q)$ need not be onto, and the covering statement fails in both formulations; the Hermitian sandwich does not repair it. The degenerate theory belongs to *Degenerate Clifford Algebras and the Radical*.

## Summary

The Hermitian formulation of the covering groups replaces the inverse by the dagger and therefore compares three conditions. The **Clifford group** $\Gamma$ is where the Hermitian sandwich preserves the vector space, and the **Hermitian Clifford group**

$$
\Gamma_{\dagger}=\{\,x\in\Gamma:\sigma(N(x))^{2}=1\,\}
$$

is where it is an isometry; it is a subgroup of $\Gamma$ because $N$ is multiplicative and $\sigma$ is a homomorphism. The **unitary slice** $U=\{x:x^{\dagger}x=1\}$ is a group, and it is where the dagger is the inverse, so that on $U$ the Hermitian sandwich is the signed inner conjugation and the entire inverse theory transfers verbatim. With the **trivial involution** the two conditions reduce to

$$
\sigma=\mathrm{id}\ \Longrightarrow\ U\cap\Gamma=\{\,x\in\Gamma:N(x)=1\,\},\quad \Gamma_{\dagger}=\{\,x\in\Gamma:N(x)=\pm1\,\}=\mathrm{Pin}(V,q),
$$

and the two coincide for a definite form in the corpus's convention, so that the Hermitian sandwich reconstructs the pin group from the adjunction and needs no new group: the odd elements give the reflections through $\Theta^{\alpha}_u(v)=u\,v\,\sigma(u)=-q(u)\rho_u(v)$, which for a unit vector is $\rho_u$ exactly, and the even ones give the rotations; the map to $O(V,q)$ is two-to-one, with kernel $\{\pm1\}$ on the slice, and the sequences $1\to\{\pm1\}\to\mathrm{Pin}\to O\to1$ and $1\to\{\pm1\}\to\mathrm{Spin}\to SO\to1$ are exact over $\mathbb{R}$ and a definite form. Cartan–Dieudonné then writes every isometry as a product of signed Hermitian sandwiches of unit vectors, with the parity of the number of factors equal to the determinant. For a general involution the three conditions differ, the scalars widen, and the covering statement is unchanged up to those scalars; the indefinite and degenerate cases fail in the same way as for the inverse member, and the Hermitian form brings no repair.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Gamma(V,q)$ | Clifford group, $\Theta^{\alpha}_x(V)\subseteq V$ |
| $\Gamma_{\dagger}=\{x\in\Gamma:\sigma(N(x))^{2}=1\}$ | Hermitian Clifford group, the isometry locus |
| $U=\{x:x^{\dagger}x=1\}$ | Unitary slice, a group, dagger = inverse |
| $\Theta^{\alpha}_x=\mathrm{Ad}^{\alpha}_x$ on $U$ | The two theories agree on the slice |
| $\sigma=\mathrm{id}\Rightarrow\Gamma_{\dagger}=\mathrm{Pin}$, $U\cap\Gamma=\{N=1\}$ | Hermitian reconstruction of the pin group; slice is its norm-one subgroup |
| $\Theta^{\alpha}_u=\rho_u$ for $q(u)=-1$ | Odd elements give reflections |
| $1\to\{\pm1\}\to\mathrm{Pin}\xrightarrow{\Theta^{\alpha}}O\to1$ | Double cover, $\sigma=\mathrm{id}$, definite form |
| $1\to\{\pm1\}\to\mathrm{Spin}\xrightarrow{\Theta^{\alpha}}SO\to1$ | Spin double cover, $\sigma=\mathrm{id}$, definite form |

## Further Reading

- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the Clifford group, the twisted adjoint and the covering groups.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the low-dimensional pin and spin groups and the Hurwitz units.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for the unitary group of an algebra with involution and the Hermitian Clifford group.
- Jean Dieudonné, *La géométrie des groupes classiques* (Springer, 3rd ed. 1971), for the generation of the orthogonal group by reflections and the spinor norm.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the covering groups in the Hermitian and the indefinite settings.
