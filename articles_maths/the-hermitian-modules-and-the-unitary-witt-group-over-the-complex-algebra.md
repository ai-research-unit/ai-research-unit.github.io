# __The Hermitian Modules and the Unitary Witt Group over the Complex Algebra__

## Introduction

A Hermitian module over the complex algebra is a complex vector space with a Hermitian form. Every module over a field is free, so the module is classified by its rank; the forms of the positive cone are then classified by the rank alone, since every definite form of rank $n$ is congruent to the identity matrix. Beyond the positive cone the invariant is the inertia, and the classes modulo the hyperbolic forms form the unitary Witt group, which is $\mathbb{Z}$.

The article proves the freedom, exhibits the canonical form and the unitary group, classifies the forms by inertia, computes the Witt group by the signature, and separates the isotropic forms of the plain product from the Hermitian ones, which have no isotropic vector in the positive cone. The comparison with the split case closes the account.

The field property that makes every module free is *The Specificities of the Complex Algebra*; the two forms are *The Two Forms and the Two Algebraic Norms of the Complex Space*; the cone is *The Positivity and the Ray of Squares of the Complex Space*; the general theory of the two-sided operators on a Hermitian module is *Bilinear Operators on a Hermitian Module with Hermitian Adjoint*, and the general Witt theory is *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*. The biquaternion instance is *Hermitian Forms over the Biquaternion Algebra and the Unitary Witt Group with Hermitian Adjoint*, where the module of rank one is already two-dimensional.

**Interpretation.** The algebra is $\mathbb{C}$ with the bar, and ${}^{*}=\bar{\cdot}$ is the conjugation. The free module of rank $n$ is $\mathbb{C}^{n}$ with the coordinatewise action, and its elements are $x=(x_1,\dots,x_n)$, $y=(y_1,\dots,y_n)$. A Hermitian form is written $h(x,y)=\sum_{k}x_ky_k^{*}$, and a general one is $h_{G}(x,y)=\sum_{k,l}x_kG_{kl}y_l^{*}$ with $G$ a Hermitian matrix. The inertia of $h$ is the triple $(n,m,r)$ of positive, negative and zero directions, and the signature is $\sigma=n-m$.

## The Hermitian Modules

**Definition.** A **Hermitian module** over the algebra is a module $M$ together with a map $h:M\times M\to\mathbb{C}$ that is additive in each argument, $\mathbb{C}$-linear in the first and conjugate-linear in the second, $h(x\lambda,y)=\lambda h(x,y)$ and $h(x,y\mu)=h(x,y)\bar\mu$, and Hermitian, $h(y,x)=\overline{h(x,y)}$.

**Proposition.** Every module over the algebra is free, so a Hermitian module is a complex vector space with a Hermitian form, and its underlying module is classified by its rank.

*Proof.* A module over a field is a vector space, and a vector space has a basis; the rank is the cardinal of a basis and classifies the space up to isomorphism.

**Proposition.** The Hermitian forms on the free module of rank $n$ are the Hermitian matrices: every form is $h_{G}$ for one Hermitian $G$, and the map $G\mapsto h_{G}$ is a bijection.

*Proof.* Given $h$, put $G_{kl}=h(e_k,e_l)$; the Hermitian symmetry of $h$ is the Hermitian symmetry of $G$, and sesquilinearity gives $h(x,y)=\sum_{k,l}x_kG_{kl}y_l^{*}$. Conversely each such expression is a Hermitian form.

## The Canonical Form

**Definition.** The **canonical form** on $\mathbb{C}^{n}$ is $h_{0}(x,y)=\sum_{k}x_ky_k^{*}$, of Gram matrix $I_n$.

**Proposition.** The canonical form is positive definite, and its norm is the squared Euclidean norm: $h_{0}(x,x)=\sum_{k}|x_k|^{2}$.

*Proof.* Each term $x_kx_k^{*}$ is a non-negative real, and the sum vanishes only when every coordinate does.

**Theorem.** Every positive definite Hermitian form of rank $n$ is congruent to the canonical form: there is an invertible $S$ with $S^{*}GS=I_n$.

*Proof.* A positive definite Hermitian $G$ has a positive definite square root $P$, and $G=P^{2}=P^{*}I_nP$, so $S=P$ works.

**Corollary.** The Hermitian modules of the positive cone are classified by their rank alone.

*Proof.* The module is classified by the rank, and the form of a fixed rank by the theorem.

## The Unitary Group

**Definition.** The **unitary group** is $\mathrm{U}(n)=\{U:U^{*}U=I_n\}$.

**Proposition.** $\mathrm{U}(n)$ is the automorphism group of the canonical form, it is a compact group of real dimension $n^{2}$, and it acts transitively on the level sets of $h_{0}$.

*Proof.* $h_{0}(Ux,Uy)=h_{0}(x,y)$ exactly when $U^{*}U=I_n$; the group is closed and bounded in the space of matrices; a unit vector is sent to any other by a unitary matrix.

**Remark (the strongest objection).** It may be objected that the unitary group is transitive on the forms of a fixed rank, and it is not. The orbit of the canonical form under congruence by unitary matrices is the canonical form itself, since $U^{*}I_nU=I_n$, so the transitivity fails at the first test. Two correct statements replace it. The group transitive on the positive definite forms of rank $n$ is the full linear group, by the theorem of the preceding section. The unitary group does diagonalise every Hermitian form, $G=U\Lambda U^{*}$ with $\Lambda$ real diagonal, so its orbits on the forms are the eigenvalue multisets; and the congruence classes, which forget the eigenvalues and keep only their signs, are the inertias. The unitary group is therefore the group of the canonical form's symmetries and the group that brings every form to diagonal shape, and it is not the group that moves one form to another.

## The Classification by Inertia

**Definition.** The **inertia** of a Hermitian form is the triple $(n,m,r)$ of the numbers of positive, negative and zero eigenvalues of its Gram matrix; the **rank** is $n+m$ and the **signature** is $\sigma=n-m$.

**Theorem (Sylvester's law).** Two Hermitian forms over the algebra are congruent exactly when they have the same inertia. Every form is congruent to $\mathrm{diag}(1_{n},-1_{m},0_{r})$.

*Proof.* Diagonalise $G$ by a unitary change of coordinates and scale the non-zero diagonal entries by the positive square roots of their moduli; the congruences preserve the signs by the inertia theorem for Hermitian matrices, and the normal form is attained.

**Proposition (the realification).** The real form $\operatorname{Re}h$ on $\mathbb{R}^{2n}$ has signature $(2n,2m)$ and rank $2(n+m)$.

*Proof.* A complex line on which $h$ is positive is a real plane on which $\operatorname{Re}h$ is positive definite, since $h(x,x)=|x|^{2}h(u,u)$ for a unit $u$ on the line; a line on which $h$ is negative contributes a negative plane; and a null line contributes a null plane.

**Remark (the doubling).** The complex inertia is read on the realification as an even signature in each entry. That is the sense in which the classification of the Hermitian forms over the algebra is the classification of the real symmetric forms of even signature, and it is why the complex case has no phenomenon the real case lacks: the invariants are the same two, and one of them is doubled.

## The Unitary Witt Group

**Definition.** Two non-degenerate Hermitian forms are **Witt equivalent** when they become congruent after the addition of hyperbolic planes $H=\mathrm{diag}(1,-1)$ to each. The classes form the **unitary Witt group** $W(\mathbb{C},{}^{*})$ under the orthogonal sum, the inverse of a class being the class of the negated form.

**Theorem.** $W(\mathbb{C},{}^{*})\cong\mathbb{Z}$, generated by the canonical form and computed by the signature.

*Proof.* The signature is additive under the orthogonal sum, vanishes on $H$, and changes sign under the negation of the form, so it descends to a homomorphism $W\to\mathbb{Z}$. It is injective: a form of signature zero has $n=m$, hence is congruent to $\mathrm{diag}(1_{n},-1_{n},0_{r})$, hence is the sum of $n$ hyperbolic planes and $r$ zero entries, hence is the zero class. It is surjective: the canonical form of rank $n$ has signature $n$, and its negative has signature $-n$.

**Remark (why $\mathbb{Z}$ and not $\mathbb{Z}/2$).** The group is the integers because the fixed field of the involution is $\mathbb{R}$, where negative directions exist and the forms $\mathrm{diag}(1_{n},-1_{m})$ are pairwise non-congruent. A theory in which the only admissible forms were the definite ones would have no negative direction, the hyperbolic plane would be excluded, and the signature would be a positive integer with no group behind it. The whole of the Witt theory is the bookkeeping of the signs.

## The Isotropic Forms of the Plain Product

**Definition.** The **plain form** on $\mathbb{C}^{n}$ is $P(x,y)=\sum_{k}x_ky_k$, of Gram matrix $I_n$ and without conjugation.

**Proposition.** For $n\ge2$ the plain form is isotropic: $P(x,x)=0$ for the non-zero vector $x=(1,i,0,\dots,0)$.

*Proof.* $P(x,x)=1^{2}+i^{2}=0$.

**Proposition.** On $\mathbb{C}^{2}$ the isotropic vectors of the plain form are the two complex lines spanned by $(1,i)$ and by $(1,-i)$.

*Proof.* $x_1^{2}+x_2^{2}=(x_1+ix_2)(x_1-ix_2)$, and the algebra has no zero divisor, so one of the two factors vanishes.

**Remark (the plain form on the realification).** As a complex symmetric form the plain form is non-degenerate of rank $n$, and over $\mathbb{C}$ all non-degenerate symmetric forms of a fixed rank are isometric, so it is indistinguishable from the canonical form in its own class. Its realification is another matter: $\operatorname{Re}P$ has signature $(n,n)$, so the plain form is indefinite on the real space and its isotropy is real isotropy.

**Remark (the absence of a Hermitian counterpart in the positive cone).** No Hermitian form of the positive cone is isotropic, because $h(x,x)=0$ forces $x=0$ there. Indefinite Hermitian forms do exist and are isotropic: $\mathrm{diag}(1,-1)$ has the isotropic vector $(1,1)$. Such a form lies outside the positive cone, in the same way the plain form lies outside the Hermitian class. The isotropy is therefore confined twice over: to the forms of mixed inertia, and, on the plain side, to every form of rank at least two.

## The Comparison with the Split Case

In the split-complex algebra the form of the cone is $\sum_{k}x_k\bar y_k$ with the bar the swap of the two components, and that form is indefinite from the start: its value at $x$ is $\sum_{k}(a_k^{2}-b_k^{2})$, which vanishes on the non-zero elements with $a_k=\pm b_k$ for every $k$. The positive theory of this article has no split analogue for the same reason: the cone of the split algebra is not a cone of definite forms, so the words *positive definite* and *isotropic* do not divide the forms the way they divide them here. On the complex side the division is clean: definite and free of isotropy on one side, indefinite and isotropic on the other.

## Summary

A Hermitian module over the complex algebra is a complex vector space with a Hermitian form. Every module is free, so the module is classified by its rank; the forms of the positive cone are classified by the rank too, by congruence to the identity matrix, and the canonical form has the unitary group $\mathrm{U}(n)$ for its automorphism group, of real dimension $n^{2}$ and transitive on the level sets and not on the forms. Beyond the cone the invariant is the inertia $(n,m,r)$, read on the realification as the even signature $(2n,2m)$, and the non-degenerate forms modulo the hyperbolic planes form the unitary Witt group $\mathbb{Z}$, generated by the canonical form and computed by the signature. The plain form is isotropic for every rank at least two, on the two lines spanned by $(1,i)$ and $(1,-i)$ in rank two, and no form of the positive cone is isotropic; in the split case the form of the cone is indefinite and the isotropic vectors exist.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $h(x,y)=\sum_{k}x_ky_k^{*}$ | the canonical Hermitian form on $\mathbb{C}^{n}$ |
| $h_{G}(x,y)=\sum_{k,l}x_kG_{kl}y_l^{*}$ | the Hermitian form of the Hermitian matrix $G$ |
| $(n,m,r)$, $\sigma=n-m$ | the inertia and the signature of a Hermitian form |
| $\mathrm{U}(n)$ | the unitary group, the automorphism group of the canonical form |
| $H=\mathrm{diag}(1,-1)$ | the hyperbolic plane, of signature zero and of Witt class zero |
| $W(\mathbb{C},{}^{*})\cong\mathbb{Z}$ | the unitary Witt group, computed by the signature |
| $P(x,y)=\sum_{k}x_ky_k$ | the plain form, symmetric, isotropic in rank two and above |

## Further Reading

- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for Hermitian forms over an algebra with involution, their congruence classification and the unitary Witt group.
- Tsit-Yuen Lam, *Introduction to Quadratic Forms over Fields*, Graduate Studies in Mathematics 67 (American Mathematical Society, 2005), for Sylvester's law, inertia, hyperbolic planes and the Witt group of a field.
- Igor R. Shafarevich and Alexei O. Remizov, *Linear Algebra and Geometry* (Springer, 2013), for the classification of Hermitian forms, the unitary group and its transitivity properties.
- Winfried Scharlau, *Quadratic and Hermitian Forms*, Grundlehren der mathematischen Wissenschaften 270 (Springer, 1985), for the Witt group of Hermitian forms, its functoriality and its computation for the classical fields.
